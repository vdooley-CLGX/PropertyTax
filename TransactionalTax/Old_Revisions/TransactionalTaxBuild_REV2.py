# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:15:13 2019

@author: fcalgiano
"""

import arcpy
    
#create workspace environment
arcpy.env.workspace = r"C:\Taxes\TransTaxTemp"

#overwrite old working shapefiles
arcpy.env.overwriteOutput = True 

#Before running this script, be sure to rename your inputs to a more general name, (i.e. County_2020_04.shp should be renamed to County.shp and UtilityTaxUpdates_2020_07 should be renamed to UtilityTaxUpdates).
#Start by importing all necesssary shapefiles and DBFs:
#import current quarter's County shapefile

#Script arguments / inputs
County=r'C:\Taxes\TransTaxTemp\County.shp'
Muni=r'C:\Taxes\TransTaxTemp\Municipal.shp'
SalesUse=r'C:\Taxes\TransTaxTemp\SalesUseTaxUpdates.dbf'
Rental=r'C:\Taxes\TransTaxTemp\RentalTaxUpdates.dbf'
Telco=r'C:\Taxes\TransTaxTemp\TelcoTaxUpdates.dbf'
Utility=r'C:\Taxes\TransTaxTemp\UtilityTaxUpdates.dbf'

Workspace=r'C:\Taxes\TransTaxTemp'

#Local Variables
uniMuniCnty=Workspace+"\\"+"uniMuniCnty.shp"
SalesUseTaxOutput=Workspace+"\\"+"SalesUseTaxOutput.shp"
RentalTaxOutput=Workspace+"\\"+"RentalTaxOutput.shp"
TelcoTaxOutput=Workspace+"\\"+"TelcoTaxOutput.shp"


#import current quarter's County shapefile 
arcpy.management.MakeFeatureLayer(County,"County")

#import current quarter's Muni shapefile        
arcpy.management.MakeFeatureLayer(Muni,"Muni")

#import Sales and Use Tax Updates DBF for the current quarter
arcpy.management.MakeTableView(SalesUse, "SalesUseTaxUpdates")

#import Rental Tax Updates DBF for the current quarter
arcpy.management.MakeTableView(Rental, "RentalTaxUpdates")

#import Telco Tax Updates DBF for the current quarter
arcpy.management.MakeTableView(Telco, "TelcoTaxUpdates")

#import Utility Tax Updates DBF for the current quarter
arcpy.management.MakeTableView(Utility, "UtilityTaxUpdates")

#select and delete US territories from County shapefile
arcpy.management.SelectLayerByAttribute("County", "NEW_SELECTION", 
                                            "STATE = 'American Samoa'OR STATE = 'Guam' OR STATE = 'Marshall Islands' OR STATE = 'Northern Mariana Islands' OR STATE = 'Palau' OR STATE = 'Puerto Rico' OR STATE = 'Virgin Islands'")
if int(arcpy.management.GetCount("County").getOutput(0)) > 0:
        arcpy.management.DeleteFeatures("County")
        
#select and delete US territories from Muni shapefile
arcpy.management.SelectLayerByAttribute("Muni", "NEW_SELECTION", 
                                            "STATE = 'American Samoa'OR STATE = 'Guam' OR STATE = 'Marshall Islands' OR STATE = 'Northern Mariana Islands' OR STATE = 'Palau' OR STATE = 'Puerto Rico' OR STATE = 'Virgin Islands'")
if int(arcpy.management.GetCount("Muni").getOutput(0)) > 0:
        arcpy.management.DeleteFeatures("Muni")  
        
#Clear Selection from County
arcpy.management.SelectLayerByAttribute("County", "CLEAR_SELECTION")

#Clear Selection from Muni
arcpy.management.SelectLayerByAttribute("Muni", "CLEAR_SELECTION")
        
#union Muni and County shapefiles        
arcpy.analysis.Union(["Muni", "County"], uniMuniCnty)

#import uniMuniCnty        
arcpy.management.MakeFeatureLayer(uniMuniCnty, "uniMuniCnty")

#Run repair geometry on uniMuniCnty
#arcpy.management.RepairGeometry ("uniMuniCnty")

#Copy County attributes over from County to Muni
arcpy.management.SelectLayerByAttribute("uniMuniCnty", "NEW_SELECTION", 
                                            "CITY_NAME = ''")
if int(arcpy.management.GetCount("uniMuniCnty").getOutput(0)) > 0:
    arcpy.management.CalculateField("uniMuniCnty", "FIPSSTCO", "!FIPSSTCO_1!", "PYTHON_9.3","")
    arcpy.management.CalculateField("uniMuniCnty", "STATE", "!STATE_1!", "PYTHON_9.3","")
    arcpy.management.CalculateField("uniMuniCnty", "COUNTY", "!COUNTY_1!", "PYTHON_9.3","")
    arcpy.management.CalculateField("uniMuniCnty", "ST_PL_FIPS", "!ST_PL_FI_1!", "PYTHON_9.3","")
    arcpy.management.CalculateField("uniMuniCnty", "PL_FIPS", "!PL_FIPS_1!", "PYTHON_9.3","")
    arcpy.management.CalculateField("uniMuniCnty", "CLASS_CODE", "!CLASS_CO_1!", "PYTHON_9.3","")
    arcpy.management.CalculateField("uniMuniCnty", "INC_FLAG", "!INC_FLAG_1!", "PYTHON_9.3","")
    arcpy.management.CalculateField("uniMuniCnty", "ST_PL_FIPS", "!ST_PL_FI_1!", "PYTHON_9.3","")
    arcpy.management.CalculateField("uniMuniCnty", "DT_ANX", "!DT_ANX_1!", "PYTHON_9.3","")
    arcpy.management.CalculateField("uniMuniCnty", "DT_UPD", "!DT_UPD_1!", "PYTHON_9.3","")
    arcpy.management.CalculateField("uniMuniCnty", "DT_VRF", "!DT_VRF_1!", "PYTHON_9.3","")
    arcpy.management.CalculateField("uniMuniCnty", "GNIS_CODE", "!CO_GNIS!", "PYTHON_9.3","")

#Clear Selection from uniMuniCnty
arcpy.management.SelectLayerByAttribute("uniMuniCnty", "CLEAR_SELECTION")

#Add TA_NAME to uniMuniCnty
arcpy.management.AddField("uniMuniCnty", "TA_NAME", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

#Add TA_FIPS to uniMuniCnty
arcpy.management.AddField("uniMuniCnty", "TA_FIPS", "TEXT", "", "", "10", "", "NULLABLE", "NON_REQUIRED", "")

#Add ST_FILING to uniMuniCnty
arcpy.management.AddField("uniMuniCnty", "ST_FILING", "TEXT", "", "", "15", "", "NULLABLE", "NON_REQUIRED", "")

#Add SPD_TAX to uniMuniCnty
arcpy.management.AddField("uniMuniCnty", "SPD_TAX", "TEXT", "", "", "5", "", "NULLABLE", "NON_REQUIRED", "")

#Add FIPSSTCOPL to uniMuniCnty
arcpy.management.AddField("uniMuniCnty", "FIPSSTCOPL", "TEXT", "", "", "10", "", "NULLABLE", "NON_REQUIRED", "")

#Calculate FIPSSTCOPL in uniMuniCnty
arcpy.management.CalculateField("uniMuniCnty", "FIPSSTCOPL", "!FIPSSTCO! + !PL_FIPS!", "PYTHON_9.3","")

#Delete unneeded fields from uniMuniCnty
arcpy.management.DeleteField("uniMuniCnty", ["FID_Munici", "OBJECTID","CHANGE","PRIORITY","SOURCE","NOTES","PARCEL_ALN","Shape_Leng","Shape_Le_1","Shape_Area","FID_County","OBJECTID_1","FIPSSTCO_1","STATE_1","COUNTY_1","CITY_NAM_1","CITY_TYP_1","ST_PL_FI_1","PL_FIPS_1","CLASS_CO_1","INC_FLAG_1","DT_ANX_1","DT_UPD_1","DT_VRF_1","CO_GNIS","PARCEL_A_1","Shape_Le_2","Shape_Ar_1"])

#Copy uniMuniCnty for Sales and Use Tax
arcpy.management.Copy("uniMuniCnty.shp", SalesUseTaxOutput)

#import SalesUseTaxOutput       
arcpy.management.MakeFeatureLayer(SalesUseTaxOutput, "SalesUseTaxOutput")

#Join SalesUseTaxOutput to SalesUseTaxUpdates on FIPPSTCOPL and calculate tax fields
arcpy.management.AddJoin("SalesUseTaxOutput", "FIPSSTCOPL", "SalesUseTaxUpdates", "FIPSSTCOPL", "KEEP_ALL")

#Select where SalesUseTaxOutput joins with SalesUseTaxUpdates. Skipping this step throws an error because of NULL values.
arcpy.management.SelectLayerByAttribute(in_layer_or_view="SalesUseTaxOutput", selection_type="NEW_SELECTION", where_clause='"SalesUseTaxUpdates.FIPSSTCOPL" IS NOT NULL')

#Calculate TA_NAME, TA_FIPS, ST_FILING and SPD_TAX from SalesUseTaxUpdates to SalesUseTaxOutput
arcpy.management.CalculateField(in_table="SalesUseTaxOutput", field="SalesUseTaxOutput.TA_NAME", expression="!SalesUseTaxUpdates.TA_NAME!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="SalesUseTaxOutput", field="SalesUseTaxOutput.TA_FIPS", expression="!SalesUseTaxUpdates.TA_FIPS!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="SalesUseTaxOutput", field="SalesUseTaxOutput.ST_FILING", expression="!SalesUseTaxUpdates.ST_FILING!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="SalesUseTaxOutput", field="SalesUseTaxOutput.SPD_TAX", expression="!SalesUseTaxUpdates.SPD_TAX!", expression_type="PYTHON_9.3", code_block="")

#Remove Join from SalesUseTaxOutput
arcpy.management.RemoveJoin("SalesUseTaxOutput", "SalesUseTaxUpdates")

#Clear Selection from SalesUseTaxOutput
arcpy.management.SelectLayerByAttribute("SalesUseTaxOutput", "CLEAR_SELECTION")

#SalesUseTax layer is now complete. Now begins the build for the RentalTax layer.

#Copy uniMuniCnty for Rental Tax
arcpy.management.Copy("uniMuniCnty.shp", RentalTaxOutput)

#import RentalTaxOutput       
arcpy.management.MakeFeatureLayer(RentalTaxOutput, "RentalTaxOutput")

#Add ST_LEASING to RentalTaxOutput
arcpy.management.AddField("RentalTaxOutput", "ST_LEASING", "TEXT", "", "", "5", "", "NULLABLE", "NON_REQUIRED", "")

#Add ST_RENTAL to RentalTaxOutput
arcpy.management.AddField("RentalTaxOutput", "ST_RENTAL", "TEXT", "", "", "5", "", "NULLABLE", "NON_REQUIRED", "")

#Add LR_SPEC_TX to RentalTaxOutput
arcpy.management.AddField("RentalTaxOutput", "LR_SPEC_TX", "TEXT", "", "", "5", "", "NULLABLE", "NON_REQUIRED", "")

#Add LR_TA_NAME to RentalTaxOutput
arcpy.management.AddField("RentalTaxOutput", "LR_TA_NAME", "TEXT", "", "", "35", "", "NULLABLE", "NON_REQUIRED", "")

#Add LR_TA_FIPS to RentalTaxOutput
arcpy.management.AddField("RentalTaxOutput", "LR_TA_FIPS", "TEXT", "", "", "10", "", "NULLABLE", "NON_REQUIRED", "")

#Add LR_SPD_TAX to RentalTaxOutput
arcpy.management.AddField("RentalTaxOutput", "LR_SPD_TAX", "TEXT", "", "", "5", "", "NULLABLE", "NON_REQUIRED", "")

#Add LR_REMIT to RentalTaxOutput
arcpy.management.AddField("RentalTaxOutput", "LR_REMIT", "TEXT", "", "", "10", "", "NULLABLE", "NON_REQUIRED", "")

#Add SP_TX_AUTO to RentalTaxOutput
arcpy.management.AddField("RentalTaxOutput", "SP_TX_AUTO", "TEXT", "", "", "30", "", "NULLABLE", "NON_REQUIRED", "")

#Join RentalTaxOutput to RentalTaxUpdates on FIPPSTCOPL and calculate tax fields
arcpy.management.AddJoin("RentalTaxOutput", "FIPSSTCOPL", "RentalTaxUpdates", "FIPSSTCOPL", "KEEP_ALL")

#Select where RentalTaxOutput joins with RentalTaxUpdates. Skipping this step throws an error because of NULL values.
arcpy.management.SelectLayerByAttribute(in_layer_or_view="RentalTaxOutput", selection_type="NEW_SELECTION", where_clause='"RentalTaxUpdates.FIPSSTCOPL" IS NOT NULL')

#Calculate TA_NAME, TA_FIPS, ST_FILING and SPD_TAX from RentalTaxUpdates to RentalTaxOutput
arcpy.management.CalculateField(in_table="RentalTaxOutput", field="RentalTaxOutput.TA_NAME", expression="!RentalTaxUpdates.TA_NAME!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="RentalTaxOutput", field="RentalTaxOutput.TA_FIPS", expression="!RentalTaxUpdates.TA_FIPS!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="RentalTaxOutput", field="RentalTaxOutput.ST_FILING", expression="!RentalTaxUpdates.ST_FILING!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="RentalTaxOutput", field="RentalTaxOutput.SPD_TAX", expression="!RentalTaxUpdates.SPD_TAX!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="RentalTaxOutput", field="RentalTaxOutput.ST_LEASING", expression="!RentalTaxUpdates.ST_LEASING!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="RentalTaxOutput", field="RentalTaxOutput.ST_RENTAL", expression="!RentalTaxUpdates.ST_RENTAL!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="RentalTaxOutput", field="RentalTaxOutput.LR_SPEC_TX", expression="!RentalTaxUpdates.LR_SPEC_TX!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="RentalTaxOutput", field="RentalTaxOutput.LR_TA_NAME", expression="!RentalTaxUpdates.LR_TA_NAME!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="RentalTaxOutput", field="RentalTaxOutput.LR_TA_FIPS", expression="!RentalTaxUpdates.LR_TA_FIPS!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="RentalTaxOutput", field="RentalTaxOutput.LR_SPD_TAX", expression="!RentalTaxUpdates.LR_SPD_TAX!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="RentalTaxOutput", field="RentalTaxOutput.LR_REMIT", expression="!RentalTaxUpdates.LR_REMIT!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="RentalTaxOutput", field="RentalTaxOutput.SP_TX_AUTO", expression="!RentalTaxUpdates.SP_TX_AUTO!", expression_type="PYTHON_9.3", code_block="")

#Remove Join from RentalTaxOutput
arcpy.management.RemoveJoin("RentalTaxOutput", "RentalTaxUpdates")

#Clear Selection from RentalTaxOutput
arcpy.management.SelectLayerByAttribute("RentalTaxOutput", "CLEAR_SELECTION")

#Rental Tax layer is now complete. Now begins the build for the TelcoTax layer.

#Copy uniMuniCnty for Telco Tax
arcpy.management.Copy("uniMuniCnty.shp", r"C:\Taxes\TransTaxTemp\TelcoTaxOutput.shp")

#import TelcoTaxOutput       
arcpy.management.MakeFeatureLayer(r"C:\Taxes\TransTaxTemp\TelcoTaxOutput.shp", "TelcoTaxOutput")

#Add ST_TEL_SER to TelcoTaxOutput
arcpy.management.AddField("TelcoTaxOutput", "ST_TEL_SER", "TEXT", "", "", "5", "", "NULLABLE", "NON_REQUIRED", "")

#Add TEL_SP_TAX to TelcoTaxOutput
arcpy.management.AddField("TelcoTaxOutput", "TEL_SP_TAX", "TEXT", "", "", "5", "", "NULLABLE", "NON_REQUIRED", "")

#Add TEL_TA_NAM to TelcoTaxOutput
arcpy.management.AddField("TelcoTaxOutput", "TEL_TA_NAM", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

#Add TEL_TA_FIP to TelcoTaxOutput
arcpy.management.AddField("TelcoTaxOutput", "TEL_TA_FIP", "TEXT", "", "", "10", "", "NULLABLE", "NON_REQUIRED", "")

#Add TEL_FILING to TelcoTaxOutput
arcpy.management.AddField("TelcoTaxOutput", "TEL_FILING", "TEXT", "", "", "15", "", "NULLABLE", "NON_REQUIRED", "")

#Add TEL_SPD_TX to TelcoTaxOutput
arcpy.management.AddField("TelcoTaxOutput", "TEL_SPD_TX", "TEXT", "", "", "5", "", "NULLABLE", "NON_REQUIRED", "")

#Join TelcoTaxOutput to TelcoTaxUpdates on FIPPSTCOPL and calculate tax fields
arcpy.management.AddJoin("TelcoTaxOutput", "FIPSSTCOPL", "TelcoTaxUpdates", "FIPSSTCOPL", "KEEP_ALL")

#Select where TelcoTaxOutput joins with TelcoTaxUpdates. Skipping this step throws an error because of NULL values.
arcpy.management.SelectLayerByAttribute(in_layer_or_view="TelcoTaxOutput", selection_type="NEW_SELECTION", where_clause='"TelcoTaxUpdates.FIPSSTCOPL" IS NOT NULL')

#Calculate TA_NAME, TA_FIPS, ST_FILING and SPD_TAX from TelcoTaxUpdates to TelcoTaxOutput
arcpy.management.CalculateField(in_table="TelcoTaxOutput", field="TelcoTaxOutput.TA_NAME", expression="!TelcoTaxUpdates.TA_NAME!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="TelcoTaxOutput", field="TelcoTaxOutput.TA_FIPS", expression="!TelcoTaxUpdates.TA_FIPS!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="TelcoTaxOutput", field="TelcoTaxOutput.ST_FILING", expression="!TelcoTaxUpdates.ST_FILING!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="TelcoTaxOutput", field="TelcoTaxOutput.SPD_TAX", expression="!TelcoTaxUpdates.SPD_TAX!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="TelcoTaxOutput", field="TelcoTaxOutput.ST_TEL_SER", expression="!TelcoTaxUpdates.ST_TEL_SER!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="TelcoTaxOutput", field="TelcoTaxOutput.TEL_SP_TAX", expression="!TelcoTaxUpdates.TEL_SP_TAX!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="TelcoTaxOutput", field="TelcoTaxOutput.TEL_TA_NAM", expression="!TelcoTaxUpdates.TEL_TA_NAM!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="TelcoTaxOutput", field="TelcoTaxOutput.TEL_TA_FIP", expression="!TelcoTaxUpdates.TEL_TA_FIP!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="TelcoTaxOutput", field="TelcoTaxOutput.TEL_FILING", expression="!TelcoTaxUpdates.TEL_FILING!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="TelcoTaxOutput", field="TelcoTaxOutput.TEL_SPD_TX", expression="!TelcoTaxUpdates.TEL_SPD_TX!", expression_type="PYTHON_9.3", code_block="")

#Remove Join from TelcoTaxOutput
arcpy.management.RemoveJoin("TelcoTaxOutput", "TelcoTaxUpdates")

#Clear Selection from TelcoTaxOutput
arcpy.management.SelectLayerByAttribute("TelcoTaxOutput", "CLEAR_SELECTION")

#Telco Tax layer is now complete. Now begins the build for the UtilityTax layer.

#Copy uniMuniCnty for Utility Tax
arcpy.management.Copy("uniMuniCnty.shp", TelcoTaxOutput)

#import UtilityTaxOutput       
arcpy.management.MakeFeatureLayer(TelcoTaxOutput, "UtilityTaxOutput")

#Add ST_UTL_SER to UtilityTaxOutput
arcpy.management.AddField("UtilityTaxOutput", "ST_UTL_SER", "TEXT", "", "", "5", "", "NULLABLE", "NON_REQUIRED", "")

#Add UTL_SP_TAX to UtilityTaxOutput
arcpy.management.AddField("UtilityTaxOutput", "UTL_SP_TAX", "TEXT", "", "", "5", "", "NULLABLE", "NON_REQUIRED", "")

#Add UTL_TA_NAM to UtilityTaxOutput
arcpy.management.AddField("UtilityTaxOutput", "UTL_TA_NAM", "TEXT", "", "", "50", "", "NULLABLE", "NON_REQUIRED", "")

#Add UTL_TA_FIP to UtilityTaxOutput
arcpy.management.AddField("UtilityTaxOutput", "UTL_TA_FIP", "TEXT", "", "", "10", "", "NULLABLE", "NON_REQUIRED", "")

#Add UTL_FILING to UtilityTaxOutput
arcpy.management.AddField("UtilityTaxOutput", "UTL_FILING", "TEXT", "", "", "15", "", "NULLABLE", "NON_REQUIRED", "")

#Add UTL_SPD_TX to UtilityTaxOutput
arcpy.management.AddField("UtilityTaxOutput", "UTL_SPD_TX", "TEXT", "", "", "5", "", "NULLABLE", "NON_REQUIRED", "")

#Join UtilityTaxOutput to UtilityTaxUpdates on FIPPSTCOPL and calculate tax fields
arcpy.management.AddJoin("UtilityTaxOutput", "FIPSSTCOPL", "UtilityTaxUpdates", "FIPSSTCOPL", "KEEP_ALL")

#Select where UtilityTaxOutput joins with UtilityTaxUpdates. Skipping this step throws an error because of NULL values.
arcpy.management.SelectLayerByAttribute(in_layer_or_view="UtilityTaxOutput", selection_type="NEW_SELECTION", where_clause='"UtilityTaxUpdates.FIPSSTCOPL" IS NOT NULL')

#Calculate TA_NAME, TA_FIPS, ST_FILING and SPD_TAX from UtilityTaxUpdates to UtilityTaxOutput
arcpy.management.CalculateField(in_table="UtilityTaxOutput", field="UtilityTaxOutput.TA_NAME", expression="!UtilityTaxUpdates.TA_NAME!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="UtilityTaxOutput", field="UtilityTaxOutput.TA_FIPS", expression="!UtilityTaxUpdates.TA_FIPS!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="UtilityTaxOutput", field="UtilityTaxOutput.ST_FILING", expression="!UtilityTaxUpdates.ST_FILING!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="UtilityTaxOutput", field="UtilityTaxOutput.SPD_TAX", expression="!UtilityTaxUpdates.SPD_TAX!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="UtilityTaxOutput", field="UtilityTaxOutput.ST_UTL_SER", expression="!UtilityTaxUpdates.ST_UTL_SER!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="UtilityTaxOutput", field="UtilityTaxOutput.UTL_SP_TAX", expression="!UtilityTaxUpdates.UTL_SP_TAX!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="UtilityTaxOutput", field="UtilityTaxOutput.UTL_TA_NAM", expression="!UtilityTaxUpdates.UTL_TA_NAM!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="UtilityTaxOutput", field="UtilityTaxOutput.UTL_TA_FIP", expression="!UtilityTaxUpdates.UTL_TA_FIP!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="UtilityTaxOutput", field="UtilityTaxOutput.UTL_FILING", expression="!UtilityTaxUpdates.UTL_FILING!", expression_type="PYTHON_9.3", code_block="")

arcpy.management.CalculateField(in_table="UtilityTaxOutput", field="UtilityTaxOutput.UTL_SPD_TX", expression="!UtilityTaxUpdates.UTL_SPD_TX!", expression_type="PYTHON_9.3", code_block="")

#Remove Join from UtilityTaxOutput
arcpy.management.RemoveJoin("UtilityTaxOutput", "UtilityTaxUpdates")

#Clear Selection from UtilityTaxOutput
arcpy.management.SelectLayerByAttribute("UtilityTaxOutput", "CLEAR_SELECTION")

#Utility Tax Layer is now complete.


