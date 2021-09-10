# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:15:13 2019

@author: fcalgiano
"""
#Before running this script, be sure to add all of your inputs into your working environment folder for the script. Also be sure to rename your inputs to a more general name, (i.e. County_2020_04.shp should be renamed to County.shp and PropretyTaxGenUpdates_2020_07 should be renamed to PropretyTaxGenUpdates).

import arcpy

#create workspace environment
arcpy.env.workspace = "C:\Taxes\PropertyPayrollUpdate\Property\2021_07\Test_Delete"

#overwrite old working shapefiles
arcpy.env.overwriteOutput = True 

#Script arguments / inputs
PropertyTaxGeomUnion=r'C:/Taxes/PropertyPayrollUpdate/Property/2021_07/Test_Delete/PropertyTaxGeomUnion.shp'
PropertyTaxGenUpdates=r'C:/Taxes/PropertyPayrollUpdate/Property/2021_07/Test_Delete/PropertyTaxGenUpdates.dbf'
Workspace=r'C:/Taxes/PropertyPayrollUpdate/Property/2021_07/Test_Delete'

#Local Variables

PropertyTaxGeomOutput=Workspace +"\\"+"PropertyTaxGeomOutput.shp"
PropertyTaxGenOutput=Workspace +"\\"+"PropertyTaxGenOutput.shp"


#Start by importing all necesssary shapefiles and DBFs:
#import current quarter's Property Tax Geometry shapefile that includes the Property Tax fields
arcpy.management.MakeFeatureLayer(PropertyTaxGeomUnion, "PropertyTaxGeomUnion")

#import Proprety Tax Gen Updates DBF for the current quarter
arcpy.management.MakeTableView(PropertyTaxGenUpdates, "PropertyTaxGenUpdates")

#Run repair geometry on PropertyTaxGeomUnion shapefile.
#arcpy.management.RepairGeometry ("PropertyTaxGeomUnion")

#Copy PropertyTaxGeomUnion for PropertyTaxGenOutput
arcpy.Copy_management(r"C:/Taxes/PropertyPayrollUpdate/Property/2021_07/Test_Delete/PropertyTaxGeomUnion.shp", r"C:/Taxes/PropertyPayrollUpdate/Property/2021_07/Test_Delete/PropertyTaxGenOutput.shp" )
#arcpy.management.Copy("PropertyTaxGeomUnion.shp", PropertyTaxGenOutput)

#import PropertyTaxGenOutput       
arcpy.management.MakeFeatureLayer(PropertyTaxGenOutput, "PropertyTaxGenOutput")

#Join PropertyTaxGenOutput to PropertyTaxGenUpdates on "join" field (Join = [FIPSSTCO] + [PL_FIPS] + [TWN_FIPS] + [SD_ID] + [SD_NAME]) and calculate tax fields
arcpy.management.AddJoin("PropertyTaxGenOutput", "join", "PropertyTaxGenUpdates", "join", "KEEP_ALL")

#Select where PropertyTaxGenOutput joins with PropertyTaxGenUpdates. Skipping this step throws an error because of NULL values.
arcpy.management.SelectLayerByAttribute(in_layer_or_view="PropertyTaxGenOutput", selection_type="NEW_SELECTION", where_clause='"PropertyTaxGenUpdates.join" IS NOT NULL')

#Calculate TA_NAME, TA_FIPS, ST_FILING and SPD_TAX from PropertyTaxGenUpdates to PropertyTaxGenOutput
arcpy.management.CalculateField(in_table="PropertyTaxGenOutput", field="PropertyTaxGenOutput.TPP_TA_NM", expression="!PropertyTaxGenUpdates.TPP_TA_NM!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="PropertyTaxGenOutput", field="PropertyTaxGenOutput.TPP_TA_FIP", expression="!PropertyTaxGenUpdates.TPP_TA_FIP!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="PropertyTaxGenOutput", field="PropertyTaxGenOutput.RENDTN_NAM", expression="!PropertyTaxGenUpdates.RENDTN_NAM!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="PropertyTaxGenOutput", field="PropertyTaxGenOutput.RENDTN_FIP", expression="!PropertyTaxGenUpdates.RENDTN_FIP!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="PropertyTaxGenOutput", field="PropertyTaxGenOutput.INTANGIBLE", expression="!PropertyTaxGenUpdates.INTANGIBLE!", expression_type="PYTHON_9.3", code_block="")

#Remove Join from SalesUseTaxOutput
arcpy.management.RemoveJoin("PropertyTaxGenOutput", "PropertyTaxGenUpdates")

#Clear Selection from SalesUseTaxOutput
arcpy.management.SelectLayerByAttribute("PropertyTaxGenOutput", "CLEAR_SELECTION")

#PropertyTaxGenOutput layer is now complete. Now begins manual updates of new records that did not join.
