# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:15:13 2019

@author: fcalgiano
"""
#Before running this script, be sure to add all of your inputs into your working environment folder for the script. 
#Also be sure to rename your inputs to a more general name, (i.e. County_2020_04.shp should be renamed to County.shp and PropretyTaxGenUpdates_2020_07 should be renamed to PropretyTaxGenUpdates).


import arcpy


#create workspace environment
arcpy.env.workspace = r"C:/Taxes/PropertyPayrollUpdate/Property/2021_07/Test_Delete/PropertyTaxRegUpdates.dbf"

#overwrite old working shapefiles
arcpy.env.overwriteOutput = True 

#Script arguments / inputs
PropertyTaxGeomUnion=r'C:/Taxes/PropertyPayrollUpdate/Property/2021_07/Test_Delete/PropertyTaxGeomUnion.shp'
PropertyTaxRegUpdates=r'C:/Taxes/PropertyPayrollUpdate/Property/2021_07/Test_Delete/PropertyTaxRegUpdates.dbf'
Workspace=r'C:/Taxes/PropertyPayrollUpdate/Property/2021_07/Test_Delete'

#Local Variables

PropertyTaxGeomOutput=Workspace +"\\"+"PropertyTaxGeomOutput.shp"
PropertyTaxRegOutput=Workspace +"\\"+"PropertyTaxRegOutput.shp"


#Start by importing all necesssary shapefiles and DBFs:
#import current quarter's Property Tax Geometry shapefile that includes the Property Tax fields
arcpy.management.MakeFeatureLayer(PropertyTaxGeomUnion, "PropertyTaxGeomUnion")

#import Proprety Tax Gen Updates DBF for the current quarter
arcpy.management.MakeTableView(PropertyTaxRegUpdates, "PropertyTaxRegUpdates")

#Run repair geometry on PropertyTaxGeomUnion shapefile.
#arcpy.management.RepairGeometry ("PropertyTaxGeomUnion")

#Copy PropertyTaxGeomUnion for PropertyTaxGenOutput
arcpy.management.Copy(r"C:/Taxes/PropertyPayrollUpdate/Property/2021_07/Test_Delete/PropertyTaxGeomUnion.shp", r"C:/Taxes/PropertyPayrollUpdate/Property/2021_07/Test_Delete/PropertyTaxRegOutput.shp")

#import PropertyTaxGenOutput       
arcpy.management.MakeFeatureLayer(PropertyTaxRegOutput, "PropertyTaxRegOutput")

#Join PropertyTaxRegOutput to PropertyTaxRegUpdates on "join" field (Join = [FIPSSTCO] + [PL_FIPS] + [TWN_FIPS] + [SD_ID] + [SD_NAME]) and calculate tax fields
arcpy.management.AddJoin("PropertyTaxRegOutput", "join", "PropertyTaxRegUpdates", "join", "KEEP_ALL")

#Select where PropertyTaxRegOutput joins with PropertyTaxRegUpdates. Skipping this step throws an error because of NULL values.
arcpy.management.SelectLayerByAttribute(in_layer_or_view="PropertyTaxRegOutput", selection_type="NEW_SELECTION", where_clause='"PropertyTaxRegUpdates.join" IS NOT NULL')

#Calculate TA_NAME, TA_FIPS, ST_FILING and SPD_TAX from PropertyTaxRegUpdates to PropertyTaxRegOutput
arcpy.management.CalculateField(in_table="PropertyTaxRegOutput", field="PropertyTaxRegOutput.TPP_TA_NM", expression="!PropertyTaxRegUpdates.TPP_TA_NM!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="PropertyTaxRegOutput", field="PropertyTaxRegOutput.TPP_TA_FIP", expression="!PropertyTaxRegUpdates.TPP_TA_FIP!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="PropertyTaxRegOutput", field="PropertyTaxRegOutput.RENDTN_NAM", expression="!PropertyTaxRegUpdates.RENDTN_NAM!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="PropertyTaxRegOutput", field="PropertyTaxRegOutput.RENDTN_FIP", expression="!PropertyTaxRegUpdates.RENDTN_FIP!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="PropertyTaxRegOutput", field="PropertyTaxRegOutput.INTANGIBLE", expression="!PropertyTaxRegUpdates.INTANGIBLE!", expression_type="PYTHON_9.3", code_block="")

#Remove Join from PropertyTaxRegOutput
arcpy.management.RemoveJoin("PropertyTaxRegOutput", "PropertyTaxRegUpdates")

#Clear Selection from PropertyTaxRegOutput
arcpy.management.SelectLayerByAttribute("PropertyTaxRegOutput", "CLEAR_SELECTION")

#PropertyTaxGenOutput layer is now complete. Now begins manual updates of new records that did not join.
