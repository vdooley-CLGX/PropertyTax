# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:15:13 2019

@author: fcalgiano
"""
#Before running this script, be sure to add all of your inputs into your working environment folder for the script. Also be sure to rename your inputs to a more general name, (i.e. County_2020_04.shp should be renamed to County.shp and PropretyTaxGenUpdates_2020_07 should be renamed to PropretyTaxGenUpdates).

import archook
archook.get_arcpy()
import arcpy

#create workspace environment
arcpy.env.workspace = "C:\Franny\Taxes\PropertyTaxBuild"

#overwrite old working shapefiles
arcpy.env.overwriteOutput = True 

#Start by importing all necesssary shapefiles and DBFs:
#import current quarter's Property Tax Reg Geometry shapefile 
arcpy.MakeFeatureLayer_management("C:\Franny\Taxes\PropertyTaxBuild\PropertyTaxReg_wrk.shp", "PropertyTaxReg_wrk")

#import Proprety Tax Reg Updates DBF for the current quarter
arcpy.MakeTableView_management("C:\Franny\Taxes\PropertyTaxBuild\PropertyTaxRegUpdates.dbf", "PropertyTaxRegUpdates")

#Run repair geometry on PropertyTaxReg_wrk shapefile.
arcpy.RepairGeometry_management ("PropertyTaxReg_wrk")

#Copy PropertyTaxReg_wrk for PropertyTaxRegOutput
arcpy.Copy_management("PropertyTaxReg_wrk.shp", "C:\Franny\Taxes\PropertyTaxBuild\PropertyTaxRegOutput.shp")

#import PropertyTaxGenOutput       
arcpy.MakeFeatureLayer_management("C:\Franny\Taxes\PropertyTaxBuild\PropertyTaxRegOutput.shp", "PropertyTaxRegOutput")

#Join PropertyTaxGenOutput to PropertyTaxGenUpdates on "join" field (Join = [FIPSSTCO] + [PL_FIPS] + [TWN_FIPS] + [SD_ID] + [SD_NAME]) and calculate tax fields
arcpy.AddJoin_management("PropertyTaxRegOutput", "join", "PropertyTaxRegUpdates", "join", "KEEP_ALL")

#Select where PropertyTaxGenOutput joins with PropertyTaxGenUpdates. Skipping this step throws an error because of NULL values.
arcpy.SelectLayerByAttribute_management(in_layer_or_view="PropertyTaxRegOutput", selection_type="NEW_SELECTION", where_clause='"PropertyTaxRegUpdates.join" IS NOT NULL')

#Calculate TA_NAME, TA_FIPS, ST_FILING and SPD_TAX from PropertyTaxGenUpdates to PropertyTaxGenOutput
arcpy.CalculateField_management(in_table="PropertyTaxRegOutput", field="PropertyTaxRegOutput.TPP_TA_NM", expression="!PropertyTaxRegUpdates.TPP_TA_NM!", expression_type="PYTHON_9.3", code_block="")

arcpy.CalculateField_management(in_table="PropertyTaxRegOutput", field="PropertyTaxRegOutput.TPP_TA_FIP", expression="!PropertyTaxRegUpdates.TPP_TA_FIP!", expression_type="PYTHON_9.3", code_block="")

arcpy.CalculateField_management(in_table="PropertyTaxRegOutput", field="PropertyTaxRegOutput.RENDTN_NAM", expression="!PropertyTaxRegUpdates.RENDTN_NAM!", expression_type="PYTHON_9.3", code_block="")

arcpy.CalculateField_management(in_table="PropertyTaxRegOutput", field="PropertyTaxRegOutput.RENDTN_FIP", expression="!PropertyTaxRegUpdates.RENDTN_FIP!", expression_type="PYTHON_9.3", code_block="")

arcpy.CalculateField_management(in_table="PropertyTaxRegOutput", field="PropertyTaxRegOutput.INTANGIBLE", expression="!PropertyTaxRegUpdates.INTANGIBLE!", expression_type="PYTHON_9.3", code_block="")

#Remove Join from SalesUseTaxOutput
arcpy.RemoveJoin_management("PropertyTaxRegOutput", "PropertyTaxRegUpdates")

#Clear Selection from SalesUseTaxOutput
arcpy.SelectLayerByAttribute_management("PropertyTaxRegOutput", "CLEAR_SELECTION")

#PropertyTaxGenOutput layer is now complete. Now begins manual updates of new records that did not join.
