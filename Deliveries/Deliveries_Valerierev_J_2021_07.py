# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:57:06 2021

@author: vmajor
"""

import archook
archook.get_arcpy()
import arcpy
import os
import shutil
import glob2
import custom_class

qa = custom_class.do_stuff()


arcpy.env.workspace = "C:\Deliveries"
arcpy.env.overwriteOutput = True
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries", out_name="DVD")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries", out_name="FTP")


arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="PGE")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\PGE", out_name="UtilityTax_2021_07")


#change these file paths every quarter to reflect new date
shutil.copytree(r'C:\Taxes\Working_Tax_Boundaries_Update\PGE\2021_07\_Delivery\Data', r'C:\Deliveries\DVD\PGE\UtilityTax_2021_07\Data')
shutil.copytree(r'C:\Taxes\Working_Tax_Boundaries_Update\PGE\2021_07\_Delivery\Support', r'C:\Deliveries\DVD\PGE\UtilityTax_2021_07\Support')

arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="Black Hills")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills", out_name="County_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills\County_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills", out_name="Municipal_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills\Municipal_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills", out_name="SalesUseTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills\SalesUseTax_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills", out_name="SpecialTaxDistrict_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills\SpecialTaxDistrict_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills", out_name="Township_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills\Township_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\County_2021_07\Data\County_2021_07.shp", "County_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("County_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Arkansas' , 'Colorado' , 'Iowa' , 'Kansas' , 'Montana' , 'Nebraska' , 'South Dakota' , 'Wyoming' ) ''')
arcpy.CopyFeatures_management("County_2021_07_lyr", "c:\Deliveries\DVD\Black Hills\County_2021_07\Data\County_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_07\Data\Municipal_2021_07.shp", "Municipal_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("Municipal_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Arkansas' , 'Colorado' , 'Iowa' , 'Kansas' , 'Montana' , 'Nebraska' , 'South Dakota' , 'Wyoming' ) ''')
arcpy.CopyFeatures_management("Municipal_2021_07_lyr", "c:\Deliveries\DVD\Black Hills\Municipal_2021_07\Data\Municipal_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SalesUseTax_2021_07\Data\SalesUseTax_2021_07.shp", "SalesUseTax_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("SalesUseTax_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Arkansas' , 'Colorado' , 'Iowa' , 'Kansas' , 'Montana' , 'Nebraska' , 'South Dakota' , 'Wyoming' ) ''')
arcpy.CopyFeatures_management("SalesUseTax_2021_07_lyr", "c:\Deliveries\DVD\Black Hills\SalesUseTax_2021_07\Data\SalesUseTax_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SpecialTaxDistrict_2021_07\Data\SpecialTaxDistrict_2021_07.shp", "SpecialTaxDistrict_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("SpecialTaxDistrict_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'CO' , 'KS' , 'MT' , 'NE' , 'SD' , 'WY' ) ''')
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_07_lyr", "c:\Deliveries\DVD\Black Hills\SpecialTaxDistrict_2021_07\Data\SpecialTaxDistrict_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_07\Data\Township_2021_07.shp", "Township_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("Township_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Arkansas' , 'Colorado' , 'Iowa' , 'Kansas' , 'Montana' , 'Nebraska' , 'South Dakota' , 'Wyoming' ) ''')
arcpy.CopyFeatures_management("Township_2021_07_lyr", "c:\Deliveries\DVD\Black Hills\Township_2021_07\Data\Township_2021_07")



arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="FM Global")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\FM Global", out_name="County_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\FM Global\County_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\FM Global", out_name="PremiumTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\FM Global\PremiumTax_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\County_2021_07\Data\County_2021_07.shp", "County_2021_07_lyr")
arcpy.CopyFeatures_management("County_2021_07_lyr", "c:\Deliveries\FTP\FM Global\County_2021_07\Data\County_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\PremiumTax_2021_07\Data\PremiumTax_2021_07.shp", "PremiumTax_2021_07_lyr")
arcpy.CopyFeatures_management("PremiumTax_2021_07_lyr", "c:\Deliveries\FTP\FM Global\PremiumTax_2021_07\Data\PremiumTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="FM Global")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\FM Global", out_name="County_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\FM Global\County_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\FM Global", out_name="PremiumTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\FM Global\PremiumTax_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\County_2021_07\Data\County_2021_07.shp", "County_2021_07_lyr")
arcpy.CopyFeatures_management("County_2021_07_lyr", "c:\Deliveries\DVD\FM Global\County_2021_07\Data\County_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\PremiumTax_2021_07\Data\PremiumTax_2021_07.shp", "PremiumTax_2021_07_lyr")
arcpy.CopyFeatures_management("PremiumTax_2021_07_lyr", "c:\Deliveries\DVD\FM Global\PremiumTax_2021_07\Data\PremiumTax_2021_07")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="Verizon")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Verizon", out_name="County_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Verizon\County_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Verizon", out_name="Municipal_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Verizon\Municipal_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Verizon", out_name="Township_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Verizon\Township_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\County_2021_07\Data\County_2021_07.shp", "County_2021_07_lyr")
arcpy.CopyFeatures_management("County_2021_07_lyr", "c:\Deliveries\FTP\Verizon\County_2021_07\Data\County_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_07\Data\Municipal_2021_07.shp", "Municipal_2021_07_lyr")
arcpy.CopyFeatures_management("Municipal_2021_07_lyr", "c:\Deliveries\FTP\Verizon\Municipal_2021_07\Data\Municipal_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_07\Data\Township_2021_07.shp", "Township_2021_07_lyr")
arcpy.CopyFeatures_management("Township_2021_07_lyr", "c:\Deliveries\FTP\Verizon\Township_2021_07\Data\Township_2021_07")



arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="Ameren")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Ameren", out_name="Municipal_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Ameren\Municipal_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Ameren", out_name="Township_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Ameren\Township_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_07\Data\Municipal_2021_07.shp", "Municipal_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("Municipal_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Missouri' , 'Illinois') ''')
arcpy.CopyFeatures_management("Municipal_2021_07_lyr", "c:\Deliveries\FTP\Ameren\Municipal_2021_07\Data\Municipal_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_07\Data\Township_2021_07.shp", "Township_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("Township_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Missouri' , 'Illinois') ''')
arcpy.CopyFeatures_management("Township_2021_07_lyr", "c:\Deliveries\FTP\Ameren\Township_2021_07\Data\Township_2021_07")



arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="Entergy")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Entergy", out_name="Municipal_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Entergy\Municipal_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Entergy", out_name="Township_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Entergy\Township_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Entergy", out_name="SchoolDistrict_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Entergy\SchoolDistrict_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_07\Data\Municipal_2021_07.shp", "Municipal_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("Municipal_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Arkansas' , 'Louisiana' , 'Mississippi' , 'Missouri' , 'Tennessee', 'Texas') ''')
arcpy.CopyFeatures_management("Municipal_2021_07_lyr", "C:\Deliveries\DVD\Entergy\Municipal_2021_07\Data\Municipal_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_07\Data\Township_2021_07.shp", "Township_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("Township_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Arkansas' , 'Louisiana' , 'Mississippi' , 'Missouri' , 'Tennessee', 'Texas') ''')
arcpy.CopyFeatures_management("Township_2021_07_lyr", "C:\Deliveries\DVD\Entergy\Township_2021_07\Data\Township_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SchoolDistrict_2021_07\Data\SchoolDistrict_2021_07.shp", "SchoolDistrict_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("SchoolDistrict_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Arkansas' , 'Louisiana' , 'Mississippi' , 'Missouri' , 'Tennessee' , 'Texas') ''')
arcpy.CopyFeatures_management("SchoolDistrict_2021_07_lyr", "c:\Deliveries\DVD\Entergy\SchoolDistrict_2021_07\Data\SchoolDistrict_2021_07")



arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="MSB")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\MSB", out_name="Municipal_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\MSB\Municipal_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\MSB", out_name="PremiumTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\MSB\PremiumTax_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="MSB")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\MSB", out_name="Municipal_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\MSB\Municipal_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\MSB", out_name="PremiumTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\MSB\PremiumTax_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_07\Data\Municipal_2021_07.shp", "Municipal_2021_07_lyr")
arcpy.CopyFeatures_management("Municipal_2021_07_lyr", "c:\Deliveries\DVD\MSB\Municipal_2021_07\Data\Municipal_2021_07")
arcpy.CopyFeatures_management("Municipal_2021_07_lyr", "c:\Deliveries\FTP\MSB\Municipal_2021_07\Data\Municipal_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\PremiumTax_2021_07\Data\PremiumTax_2021_07.shp", "PremiumTax_2021_07_lyr")
arcpy.CopyFeatures_management("PremiumTax_2021_07_lyr", "c:\Deliveries\DVD\MSB\PremiumTax_2021_07\Data\PremiumTax_2021_07")
arcpy.CopyFeatures_management("PremiumTax_2021_07_lyr", "c:\Deliveries\FTP\MSB\PremiumTax_2021_07\Data\PremiumTax_2021_07")



arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="Oncor")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Oncor", out_name="Municipal_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Oncor\Municipal_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_07\Data\Municipal_2021_07.shp", "Municipal_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("Municipal_2021_07_lyr", "NEW_SELECTION",'''"State" = 'Texas' ''')
arcpy.CopyFeatures_management("Municipal_2021_07_lyr", "c:\Deliveries\FTP\Oncor\Municipal_2021_07\Data\Municipal_2021_07")



arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="TDS")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\TDS", out_name="Municipal_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\TDS\Municipal_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\TDS", out_name="Township_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\TDS\Township_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_07\Data\Municipal_2021_07.shp", "Municipal_2021_07_lyr")
arcpy.CopyFeatures_management("Municipal_2021_07_lyr", "c:\Deliveries\DVD\TDS\Municipal_2021_07\Data\Municipal_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_07\Data\Township_2021_07.shp", "Township_2021_07_lyr")
arcpy.CopyFeatures_management("Township_2021_07_lyr", "c:\Deliveries\DVD\TDS\Township_2021_07\Data\Township_2021_07")



arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="National Grid")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\National Grid", out_name="Municipal_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\National Grid\Municipal_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\National Grid", out_name="Township_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\National Grid\Township_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_07\Data\Municipal_2021_07.shp", "Municipal_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("Municipal_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Massachusetts' , 'New Hampshire' , 'New York' , 'Rhode Island') ''')
arcpy.CopyFeatures_management("Municipal_2021_07_lyr", "c:\Deliveries\DVD\National Grid\Municipal_2021_07\Data\Municipal_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_07\Data\Township_2021_07.shp", "Township_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("Township_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Massachusetts' , 'New Hampshire' , 'New York' , 'Rhode Island') ''')
arcpy.CopyFeatures_management("Township_2021_07_lyr", "c:\Deliveries\DVD\National Grid\Township_2021_07\Data\Township_2021_07")





arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="AMIC")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\AMIC", out_name="PremiumTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\AMIC\PremiumTax_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\PremiumTax_2021_07\Data\PremiumTax_2021_07.shp", "PremiumTax_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("PremiumTax_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Alabama' , 'California' , 'Delaware' , 'Florida', 'Georgia' , 'Illinois' , 'Kentucky', 'Louisiana' , 'Maryland' , 'Minnesota', 'Mississippi' , 'New Jersey' , 'New York', 'South Carolina' , 'North Dakota' ) ''')
arcpy.CopyFeatures_management("PremiumTax_2021_07_lyr", "c:\Deliveries\DVD\AMIC\PremiumTax_2021_07\Data\PremiumTax_2021_07")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="Eagle Technology Management")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Eagle Technology Management", out_name="PremiumTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Eagle Technology Management\PremiumTax_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\PremiumTax_2021_07\Data\PremiumTax_2021_07.shp", "PremiumTax_2021_07_lyr")
arcpy.CopyFeatures_management("PremiumTax_2021_07_lyr", "c:\Deliveries\FTP\Eagle Technology Management\PremiumTax_2021_07\Data\PremiumTax_2021_07")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="State Farm")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\State Farm", out_name="Municipal_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\State Farm\Municipal_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\State Farm", out_name="Township_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\State Farm\Township_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_07\Data\Municipal_2021_07.shp", "Municipal_2021_07_lyr")
arcpy.CopyFeatures_management("Municipal_2021_07_lyr", "c:\Deliveries\FTP\State Farm\Municipal_2021_07\Data\Municipal_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_07\Data\Township_2021_07.shp", "Township_2021_07_lyr")
arcpy.CopyFeatures_management("Township_2021_07_lyr", "c:\Deliveries\FTP\State Farm\Township_2021_07\Data\Township_2021_07")





arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="Nationwide")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Nationwide", out_name="County_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Nationwide\County_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Nationwide", out_name="PremiumTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Nationwide\PremiumTax_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\County_2021_07\Data\County_2021_07.shp", "County_2021_07_lyr")
arcpy.CopyFeatures_management("County_2021_07_lyr", "c:\Deliveries\DVD\Nationwide\County_2021_07\Data\County_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\PremiumTax_2021_07\Data\PremiumTax_2021_07.shp", "PremiumTax_2021_07_lyr")
arcpy.CopyFeatures_management("PremiumTax_2021_07_lyr", "c:\Deliveries\DVD\Nationwide\PremiumTax_2021_07\Data\PremiumTax_2021_07")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="Nationwide Mutual Insurance Company")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Nationwide Mutual Insurance Company", out_name="PremiumTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Nationwide Mutual Insurance Company\PremiumTax_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\PremiumTax_2021_07\Data\PremiumTax_2021_07.shp", "PremiumTax_2021_07_lyr")
arcpy.CopyFeatures_management("PremiumTax_2021_07_lyr", "c:\Deliveries\FTP\Nationwide Mutual Insurance Company\PremiumTax_2021_07\Data\PremiumTax_2021_07")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="American Electric Power Rusling")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Rusling", out_name="SalesUseTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Rusling\SalesUseTax_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Rusling", out_name="SpecialTaxDistrict_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Rusling\SpecialTaxDistrict_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SalesUseTax_2021_07\Data\SalesUseTax_2021_07.shp", "SalesUseTax_2021_07_lyr")
arcpy.CopyFeatures_management("SalesUseTax_2021_07_lyr", "c:\Deliveries\DVD\American Electric Power Rusling\SalesUseTax_2021_07\Data\SalesUseTax_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SpecialTaxDistrict_2021_07\Data\SpecialTaxDistrict_2021_07.shp", "SpecialTaxDistrict_2021_07_lyr")
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_07_lyr", "c:\Deliveries\DVD\American Electric Power Rusling\SpecialTaxDistrict_2021_07\Data\SpecialTaxDistrict_2021_07")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="American Electric Power Gentry")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Gentry", out_name="SchoolDistrict_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Gentry\SchoolDistrict_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Gentry", out_name="Township_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Gentry\Township_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SchoolDistrict_2021_07\Data\SchoolDistrict_2021_07.shp", "SchoolDistrict_2021_07_lyr")
arcpy.CopyFeatures_management("SchoolDistrict_2021_07_lyr", "C:\Deliveries\DVD\American Electric Power Gentry\SchoolDistrict_2021_07\Data\SchoolDistrict_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_07\Data\Township_2021_07.shp", "Township_2021_07_lyr")
arcpy.CopyFeatures_management("Township_2021_07_lyr", "c:\Deliveries\DVD\American Electric Power Gentry\Township_2021_07\Data\Township_2021_07")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="Southwest Gas Corporation")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Southwest Gas Corporation", out_name="SalesUseTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Southwest Gas Corporation\SalesUseTax_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Southwest Gas Corporation", out_name="SpecialTaxDistrict_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Southwest Gas Corporation\SpecialTaxDistrict_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SalesUseTax_2021_07\Data\SalesUseTax_2021_07.shp", "SalesUseTax_2021_07_lyr")
arcpy.CopyFeatures_management("SalesUseTax_2021_07_lyr", "c:\Deliveries\DVD\Southwest Gas Corporation\SalesUseTax_2021_07\Data\SalesUseTax_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SpecialTaxDistrict_2021_07\Data\SpecialTaxDistrict_2021_07.shp", "SpecialTaxDistrict_2021_07_lyr")
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_07_lyr", "c:\Deliveries\DVD\Southwest Gas Corporation\SpecialTaxDistrict_2021_07\Data\SpecialTaxDistrict_2021_07")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="ProTax Systems")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems", out_name="Six Layers")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Six Layers", out_name="SalesUseTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Six Layers\SalesUseTax_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Six Layers", out_name="SpecialTaxDistrict_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Six Layers\SpecialTaxDistrict_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Six Layers", out_name="TelcoTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Six Layers\TelcoTax_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Six Layers", out_name="UtilityTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Six Layers\UtilityTax_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Six Layers", out_name="Municipal_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Six Layers\Municipal_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Six Layers", out_name="County_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Six Layers\County_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SalesUseTax_2021_07\Data\SalesUseTax_2021_07.shp", "SalesUseTax_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("SalesUseTax_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Alabama' , 'Alaska' , 'Colorado' , 'Hawaii' , 'Kansas', 'Missouri' , 'Nevada' , 'Illinois' , 'Louisiana' , 'New York' , 'Oklahoma', 'Texas' , 'Vermont' , 'South Carolina' ) ''')
arcpy.CopyFeatures_management("SalesUseTax_2021_07_lyr", "C:\Deliveries\FTP\ProTax Systems\Six Layers\SalesUseTax_2021_07\Data\SalesUseTax_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SpecialTaxDistrict_2021_07\Data\SpecialTaxDistrict_2021_07.shp", "SpecialTaxDistrict_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("SpecialTaxDistrict_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'AL' , 'CO', 'KS' , 'MO', 'NV' , 'IL' , 'LA' , 'NY' , 'OK' , 'TX' , 'SC' ) ''')
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_07_lyr", "C:\Deliveries\FTP\ProTax Systems\Six Layers\SpecialTaxDistrict_2021_07\Data\SpecialTaxDistrict_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\TelcoTax_2021_07\Data\TelcoTax_2021_07.shp", "TelcoTax_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("TelcoTax_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Alabama' , 'Alaska' , 'California' , 'Colorado' , 'Hawaii' , 'Kansas', 'Missouri' , 'Nevada' , 'Illinois' , 'Louisiana' , 'New York' , 'Oklahoma', 'Texas' , 'Vermont' , 'South Carolina' , ' Washington' ) ''')
arcpy.CopyFeatures_management("TelcoTax_2021_07_lyr", "c:\Deliveries\FTP\ProTax Systems\Six Layers\TelcoTax_2021_07\Data\TelcoTax_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\UtilityTax_2021_07\Data\UtilityTax_2021_07.shp", "UtilityTax_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("UtilityTax_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Alabama' , 'Alaska' , 'California' , 'Colorado' , 'Hawaii' , 'Kansas', 'Missouri' , 'Nevada' , 'Illinois' , 'Louisiana' , 'New York' , 'Oklahoma', 'Texas' , 'Vermont' , 'South Carolina' , ' Washington' ) ''')
arcpy.CopyFeatures_management("UtilityTax_2021_07_lyr", "C:\Deliveries\FTP\ProTax Systems\Six Layers\UtilityTax_2021_07\Data\UtilityTax_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_07\Data\Municipal_2021_07.shp", "Municipal_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("Municipal_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Alabama' , 'Alaska' , 'Colorado' , 'Hawaii' , 'Kansas' , 'Missouri' , 'Nevada' , 'Illinois' , 'Louisiana' , 'New York' , 'Oklahoma', 'Texas' , 'Vermont' , 'South Carolina' ) ''')
arcpy.CopyFeatures_management("Municipal_2021_07_lyr", "C:\Deliveries\FTP\ProTax Systems\Six Layers\Municipal_2021_07\Data\Municipal_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\County_2021_07\Data\County_2021_07.shp", "County_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("County_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Alabama' , 'Alaska' , 'Colorado' , 'Hawaii' , 'Kansas' , 'Missouri' , 'Nevada' , 'Illinois' , 'Louisiana' , 'New York' , 'Oklahoma', 'Texas' , 'Vermont' , 'South Carolina' ) ''')
arcpy.CopyFeatures_management("County_2021_07_lyr", "C:\Deliveries\FTP\ProTax Systems\Six Layers\County_2021_07\Data\County_2021_07")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems", out_name="Three Layers")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Three Layers", out_name="SpecialTaxDistrict_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Three Layers\SpecialTaxDistrict_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Three Layers", out_name="TelcoTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Three Layers\TelcoTax_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Three Layers", out_name="UtilityTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Three Layers\UtilityTax_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SpecialTaxDistrict_2021_07\Data\SpecialTaxDistrict_2021_07.shp", "SpecialTaxDistrict_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("SpecialTaxDistrict_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'CA' , 'MO' , 'WA' ) ''')
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_07_lyr", "C:\Deliveries\FTP\ProTax Systems\Three Layers\SpecialTaxDistrict_2021_07\Data\SpecialTaxDistrict_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\TelcoTax_2021_07\Data\TelcoTax_2021_07.shp", "TelcoTax_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("TelcoTax_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'California' , 'Missouri' , 'Washington' ) ''')
arcpy.CopyFeatures_management("TelcoTax_2021_07_lyr", "C:\Deliveries\FTP\ProTax Systems\Three Layers\TelcoTax_2021_07\Data\TelcoTax_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\UtilityTax_2021_07\Data\UtilityTax_2021_07.shp", "UtilityTax_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("UtilityTax_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'California' , 'Missouri' , 'Washington' ) ''')
arcpy.CopyFeatures_management("UtilityTax_2021_07_lyr", "C:\Deliveries\FTP\ProTax Systems\Three Layers\UtilityTax_2021_07\Data\UtilityTax_2021_07")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="Duke Energy Johnson")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Johnson", out_name="SalesUseTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Johnson\SalesUseTax_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Johnson", out_name="SpecialTaxDistrict_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Johnson\SpecialTaxDistrict_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SalesUseTax_2021_07\Data\SalesUseTax_2021_07.shp", "SalesUseTax_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("SalesUseTax_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Florida' , 'Indiana' , 'Kentucky', 'North Carolina' , 'Ohio' , 'South Carolina' ) ''')
arcpy.CopyFeatures_management("SalesUseTax_2021_07_lyr", "C:\Deliveries\DVD\Duke Energy Johnson\SalesUseTax_2021_07\Data\SalesUseTax_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SpecialTaxDistrict_2021_07\Data\SpecialTaxDistrict_2021_07.shp", "SpecialTaxDistrict_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("SpecialTaxDistrict_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'FL' , 'KY' , 'NC' , 'OH', 'SC' ) ''')
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_07_lyr", "C:\Deliveries\DVD\Duke Energy Johnson\SpecialTaxDistrict_2021_07\Data\SpecialTaxDistrict_2021_07")





arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="Duke Energy Wright")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Wright", out_name="SalesUseTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Wright\SalesUseTax_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Wright", out_name="SpecialTaxDistrict_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Wright\SpecialTaxDistrict_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SalesUseTax_2021_07\Data\SalesUseTax_2021_07.shp", "SalesUseTax_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("SalesUseTax_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'Florida' , 'Indiana' , 'Kentucky', 'North Carolina' , 'Ohio' , 'South Carolina' ) ''')
arcpy.CopyFeatures_management("SalesUseTax_2021_07_lyr", "C:\Deliveries\DVD\Duke Energy Wright\SalesUseTax_2021_07\Data\SalesUseTax_2021_07")
arcpy.SelectLayerByAttribute_management("SpecialTaxDistrict_2021_07_lyr", "NEW_SELECTION",'''STATE IN( 'FL' , 'KY' , 'NC' , 'OH', 'SC' ) ''')
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_07_lyr", "C:\Deliveries\DVD\Duke Energy Wright\SpecialTaxDistrict_2021_07\Data\SpecialTaxDistrict_2021_07")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="Duke Energy Shepherd")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Shepherd", out_name="SchoolDistrict_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Shepherd\SchoolDistrict_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SchoolDistrict_2021_07\Data\SchoolDistrict_2021_07.shp", "SchoolDistrict_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("SchoolDistrict_2021_07_lyr", "NEW_SELECTION",'''"State" = 'Kentucky' ''')
arcpy.CopyFeatures_management("SchoolDistrict_2021_07_lyr", "c:\Deliveries\DVD\Duke Energy Shepherd\SchoolDistrict_2021_07\Data\SchoolDistrict_2021_07")






arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="Qwest Century Link")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Qwest Century Link", out_name="SpecialTaxDistrict_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Qwest Century Link\SpecialTaxDistrict_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Qwest Century Link", out_name="TelcoTax_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Qwest Century Link\TelcoTax_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SpecialTaxDistrict_2021_07\Data\SpecialTaxDistrict_2021_07.shp", "SpecialTaxDistrict_2021_07_lyr")
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_07_lyr", "c:\Deliveries\FTP\Qwest Century Link\SpecialTaxDistrict_2021_07\Data\SpecialTaxDistrict_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\TelcoTax_2021_07\Data\TelcoTax_2021_07.shp", "TelcoTax_2021_07_lyr")
arcpy.CopyFeatures_management("TelcoTax_2021_07_lyr", "c:\Deliveries\FTP\Qwest Century Link\TelcoTax_2021_07\Data\TelcoTax_2021_07")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="Northeastern Utilities")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Northeastern Utilities", out_name="Municipal_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Northeastern Utilities\Municipal_2021_07", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Northeastern Utilities", out_name="Township_2021_07")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Northeastern Utilities\Township_2021_07", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_07\Data\Municipal_2021_07.shp", "Municipal_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("Municipal_2021_07_lyr", "NEW_SELECTION",'''"STATE" IN('Maine' , 'Vermont' , 'New Hampshire') AND "COUNTY" IN ( 'Fairfield' , 'Hartford' , 'Litchfield' , 'Middlesex' , 'New Haven' , 'New London' , 'Tolland'  , 'York' , 'Barnstable' , 'Berkshire' , 'Bristol' , 'Dukes' , 'Hampden' , 'Hampshire' , 'Middlesex' , 'Norfolk' , 'Plymouth' , 'Suffolk' , 'Worcester' , 'Belknap', 'Carroll', 'Cheshire' , 'Coos' , 'Grafton' , 'Hillsborough' , 'Merrimack' , 'Rockingham' , 'Strafford' , 'Sullivan' , 'Caledonia' , 'Essex' ) OR STATE = 'Connecticut' AND "COUNTY" IN ( 'Fairfield' , 'Hartford' , 'Litchfield' , 'Middlesex' , 'New Haven' , 'New London' , 'Tolland' ,'Windham', 'York' , 'Barnstable' , 'Berkshire' , 'Bristol' , 'Dukes' ,  'Hampden' , 'Hampshire' , 'Middlesex' , 'Norfolk' , 'Plymouth' , 'Suffolk' , 'Worcester' , 'Belknap', 'Carroll', 'Cheshire' , 'Coos' , 'Grafton' , 'Hillsborough' , 'Merrimack' , 'Rockingham' , 'Strafford' , 'Sullivan' , 'Caledonia' , 'Essex' ) OR STATE = 'Massachusetts' AND "COUNTY" IN ( 'Fairfield' , 'Hartford' , 'Litchfield' , 'Middlesex' , 'New Haven' , 'New London' , 'Tolland' ,'Windham', 'York' , 'Barnstable' , 'Berkshire' , 'Bristol' , 'Dukes' , 'Franklin' , 'Hampden' , 'Hampshire' , 'Middlesex' , 'Norfolk' , 'Plymouth' , 'Suffolk' , 'Worcester' , 'Belknap', 'Carroll', 'Cheshire' , 'Coos' , 'Grafton' , 'Hillsborough' , 'Merrimack' , 'Rockingham' , 'Strafford' , 'Sullivan' , 'Caledonia' , 'Essex' ) ''')
arcpy.CopyFeatures_management("Municipal_2021_07_lyr", "c:\Deliveries\FTP\Northeastern Utilities\Municipal_2021_07\Data\Municipal_2021_07")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_07\Data\Township_2021_07.shp", "Township_2021_07_lyr")
arcpy.SelectLayerByAttribute_management("Township_2021_07_lyr", "NEW_SELECTION",'''"STATE" IN('Maine' , 'Vermont' , 'New Hampshire') AND "COUNTY" IN ( 'Fairfield' , 'Hartford' , 'Litchfield' , 'Middlesex' , 'New Haven' , 'New London' , 'Tolland'  , 'York' , 'Barnstable' , 'Berkshire' , 'Bristol' , 'Dukes' , 'Hampden' , 'Hampshire' , 'Middlesex' , 'Norfolk' , 'Plymouth' , 'Suffolk' , 'Worcester' , 'Belknap', 'Carroll', 'Cheshire' , 'Coos' , 'Grafton' , 'Hillsborough' , 'Merrimack' , 'Rockingham' , 'Strafford' , 'Sullivan' , 'Caledonia' , 'Essex' ) OR STATE = 'Connecticut' AND "COUNTY" IN ( 'Fairfield' , 'Hartford' , 'Litchfield' , 'Middlesex' , 'New Haven' , 'New London' , 'Tolland' ,'Windham', 'York' , 'Barnstable' , 'Berkshire' , 'Bristol' , 'Dukes' ,  'Hampden' , 'Hampshire' , 'Middlesex' , 'Norfolk' , 'Plymouth' , 'Suffolk' , 'Worcester' , 'Belknap', 'Carroll', 'Cheshire' , 'Coos' , 'Grafton' , 'Hillsborough' , 'Merrimack' , 'Rockingham' , 'Strafford' , 'Sullivan' , 'Caledonia' , 'Essex' ) OR STATE = 'Massachusetts' AND "COUNTY" IN ( 'Fairfield' , 'Hartford' , 'Litchfield' , 'Middlesex' , 'New Haven' , 'New London' , 'Tolland' ,'Windham', 'York' , 'Barnstable' , 'Berkshire' , 'Bristol' , 'Dukes' , 'Franklin' , 'Hampden' , 'Hampshire' , 'Middlesex' , 'Norfolk' , 'Plymouth' , 'Suffolk' , 'Worcester' , 'Belknap', 'Carroll', 'Cheshire' , 'Coos' , 'Grafton' , 'Hillsborough' , 'Merrimack' , 'Rockingham' , 'Strafford' , 'Sullivan' , 'Caledonia' , 'Essex' ) ''')
arcpy.CopyFeatures_management("Township_2021_07_lyr", "c:\Deliveries\FTP\Northeastern Utilities\Township_2021_07\Data\Township_2021_07")





#Create RTX Script #5 Create PxPoint Index
os.system('cmd /k "cd C:\Python27 & buildrtx.exe C:\Deliveries\DVD --force & buildrtx.exe C:\Deliveries\FTP --force"')





#QAQC Script #6 Fianlize Layer
DVD_data_folders = glob2.glob('C:\Deliveries\DVD\**\*Data')
FTP_data_folders = glob2.glob('C:\Deliveries\FTP\**\*Data')
combine_data_folders = DVD_data_folders + FTP_data_folders

for data_folder in combine_data_folders:
    qa.run_qa(data_folder)





#DVD Release Letters 
#Be sure to update PDF's before running


shutil.copyfile(r'C:\Deliveries\_Release_Letters\ReleaseLetter_AEP_SchoolDist_Township.pdf', r'C:\Deliveries\DVD\American Electric Power Gentry\ReleaseLetter_AEP_SchoolDist_Township.pdf')
shutil.copyfile(r'C:\Deliveries\_Release_Letters\ReleaseLetter_AEP_SpTD_SalesUse.pdf', r'C:\Deliveries\DVD\American Electric Power Rusling\ReleaseLetter_AEP_SpTD_SalesUse.pdf')
shutil.copyfile(r'C:\Deliveries\_Release_Letters\ReleaseLetter_American Modern.pdf', r'C:\Deliveries\DVD\AMIC\ReleaseLetter_American Modern.pdf')
shutil.copyfile(r'C:\Deliveries\_Release_Letters\ReleaseLetter_Black_Hills.pdf', r'C:\Deliveries\DVD\Black Hills\ReleaseLetter_Black_Hills.pdf')
shutil.copyfile(r'C:\Deliveries\_Release_Letters\ReleaseLetter_Duke-MJohnson.pdf', r'C:\Deliveries\DVD\Duke Energy Johnson\ReleaseLetter_Duke-MJohnson.pdf')
shutil.copyfile(r'C:\Deliveries\_Release_Letters\ReleaseLetter_Duke-CShepherd.pdf', r'C:\Deliveries\DVD\Duke Energy Shepherd\ReleaseLetter_Duke-CShepherd.pdf')
shutil.copyfile(r'C:\Deliveries\_Release_Letters\ReleaseLetter_Duke-AWright.pdf', r'C:\Deliveries\DVD\Duke Energy Wright\ReleaseLetter_Duke-AWright.pdf')
shutil.copyfile(r'C:\Deliveries\_Release_Letters\ReleaseLetter_Entergy.pdf', r'C:\Deliveries\DVD\Entergy\ReleaseLetter_Entergy.pdf')
shutil.copyfile(r'C:\Deliveries\_Release_Letters\ReleaseLetter_FMGlobal.pdf', r'C:\Deliveries\DVD\FM Global\ReleaseLetter_FMGlobal.pdf')
shutil.copyfile(r'C:\Deliveries\_Release_Letters\ReleaseLetter_MSB_Premium_Muni.pdf', r'C:\Deliveries\DVD\MSB\ReleaseLetter_MSB_Premium_Muni.pdf')
shutil.copyfile(r'C:\Deliveries\_Release_Letters\ReleaseLetter_NationalGrid.pdf', r'C:\Deliveries\DVD\National Grid\ReleaseLetter_NationalGrid.pdf')
shutil.copyfile(r'C:\Deliveries\_Release_Letters\ReleaseLetter_Nationwide.pdf', r'C:\Deliveries\DVD\Nationwide\ReleaseLetter_Nationwide.pdf')
shutil.copyfile(r'C:\Deliveries\_Release_Letters\ReleaseLetter_PGE.pdf', r'C:\Deliveries\DVD\PGE\ReleaseLetter_PGE.pdf')
shutil.copyfile(r'C:\Deliveries\_Release_Letters\ReleaseLetter_SouthwestGas.pdf', r'C:\Deliveries\DVD\Southwest Gas Corporation\ReleaseLetter_SouthwestGas.pdf')
shutil.copyfile(r'C:\Deliveries\_Release_Letters\ReleaseLetter_TDS.pdf', r'C:\Deliveries\DVD\TDS\ReleaseLetter_SouthwestGas.pdf')




#DVD Folder Documentation


shutil.copytree(r'C:\Deliveries\SchoolDistrict_2021_07\Support', r'C:\Deliveries\DVD\American Electric Power Gentry\SchoolDistrict_2021_07\Support')
shutil.copytree(r'C:\Deliveries\Township_2021_07\Support', r'C:\Deliveries\DVD\American Electric Power Gentry\Township_2021_07\Support')

shutil.copytree(r'C:\Deliveries\SalesUseTax_2021_07\Support', r'C:\Deliveries\DVD\American Electric Power Rusling\SalesUseTax_2021_07\Support')
shutil.copytree(r'C:\Deliveries\SpecialTaxDistrict_2021_07\Support', r'C:\Deliveries\DVD\American Electric Power Rusling\SpecialTaxDistrict_2021_07\Support')


shutil.copytree(r'C:\Deliveries\PremiumTax_2021_07\Support', r'C:\Deliveries\DVD\AMIC\PremiumTax_2021_07\Support')


shutil.copytree(r'C:\Deliveries\County_2021_07\Support', r'C:\Deliveries\DVD\Black Hills\County_2021_07\Support')
shutil.copytree(r'C:\Deliveries\Municipal_2021_07\Support', r'C:\Deliveries\DVD\Black Hills\Municipal_2021_07\Support')
shutil.copytree(r'C:\Deliveries\SalesUseTax_2021_07\Support', r'C:\Deliveries\DVD\Black Hills\SalesUseTax_2021_07\Support')
shutil.copytree(r'C:\Deliveries\SpecialTaxDistrict_2021_07\Support', r'C:\Deliveries\DVD\Black Hills\SpecialTaxDistrict_2021_07\Support')
shutil.copytree(r'C:\Deliveries\Township_2021_07\Support', r'C:\Deliveries\DVD\Black Hills\Township_2021_07\Support')


shutil.copytree(r'C:\Deliveries\SalesUseTax_2021_07\Support', r'C:\Deliveries\DVD\Duke Energy Johnson\SalesUseTax_2021_07\Support')
shutil.copytree(r'C:\Deliveries\SpecialTaxDistrict_2021_07\Support', r'C:\Deliveries\DVD\Duke Energy Johnson\SpecialTaxDistrict_2021_07\Support')

shutil.copytree(r'C:\Deliveries\SchoolDistrict_2021_07\Support', r'C:\Deliveries\DVD\Duke Energy Shepherd\SchoolDistrict_2021_07\Support')

shutil.copytree(r'C:\Deliveries\SalesUseTax_2021_07\Support', r'C:\Deliveries\DVD\Duke Energy Wright\SalesUseTax_2021_07\Support')
shutil.copytree(r'C:\Deliveries\SpecialTaxDistrict_2021_07\Support', r'C:\Deliveries\DVD\Duke Energy Wright\SpecialTaxDistrict_2021_07\Support')



shutil.copytree(r'C:\Deliveries\Municipal_2021_07\Support', r'C:\Deliveries\DVD\Entergy\Municipal_2021_07\Support')
shutil.copytree(r'C:\Deliveries\SchoolDistrict_2021_07\Support', r'C:\Deliveries\DVD\Entergy\SchoolDistrict_2021_07\Support')
shutil.copytree(r'C:\Deliveries\Township_2021_07\Support', r'C:\Deliveries\DVD\Entergy\Township_2021_07\Support')


shutil.copytree(r'C:\Deliveries\PremiumTax_2021_07\Support', r'C:\Deliveries\DVD\FM Global\County_2021_07\Support')
shutil.copytree(r'C:\Deliveries\County_2021_07\Support', r'C:\Deliveries\DVD\FM Global\PremiumTax_2021_07\Support')


shutil.copytree(r'C:\Deliveries\Municipal_2021_07\Support', r'C:\Deliveries\DVD\MSB\Municipal_2021_07\Support')
shutil.copytree(r'C:\Deliveries\PremiumTax_2021_07\Support', r'C:\Deliveries\DVD\MSB\PremiumTax_2021_07\Support')


shutil.copytree(r'C:\Deliveries\Municipal_2021_07\Support', r'C:\Deliveries\DVD\National Grid\Municipal_2021_07\Support')
shutil.copytree(r'C:\Deliveries\Township_2021_07\Support', r'C:\Deliveries\DVD\National Grid\Township_2021_07\Support')


shutil.copytree(r'C:\Deliveries\County_2021_07\Support', r'C:\Deliveries\DVD\Nationwide\County_2021_07\Support')
shutil.copytree(r'C:\Deliveries\PremiumTax_2021_07\Support', r'C:\Deliveries\DVD\Nationwide\PremiumTax_2021_07\Support')



shutil.copytree(r'C:\Deliveries\SalesUseTax_2021_07\Support', r'C:\Deliveries\DVD\Southwest Gas Corporation\SalesUseTax_2021_07\Support')
shutil.copytree(r'C:\Deliveries\SpecialTaxDistrict_2021_07\Support', r'C:\Deliveries\DVD\Southwest Gas Corporation\SpecialTaxDistrict_2021_07\Support')


shutil.copytree(r'C:\Deliveries\Municipal_2021_07\Support', r'C:\Deliveries\DVD\TDS\Municipal_2021_07\Support')
shutil.copytree(r'C:\Deliveries\Township_2021_07\Support', r'C:\Deliveries\DVD\TDS\Township_2021_07\Support')



#FTP Folder Documentation


shutil.copytree(r'C:\Deliveries\Municipal_2021_07\Support', 'C:\Deliveries\FTP\Ameren\Municipal_2021_07\Support')
shutil.copytree(r'C:\Deliveries\Township_2021_07\Support', 'C:\Deliveries\FTP\Ameren\Township_2021_07\Support')


shutil.copytree(r'C:\Deliveries\PremiumTax_2021_07\Support', r'C:\Deliveries\FTP\Eagle Technology Management\PremiumTax_2021_07\Support')


shutil.copytree(r'C:\Deliveries\County_2021_07\Support', r'C:\Deliveries\FTP\FM Global\County_2021_07\Support')
shutil.copytree(r'C:\Deliveries\PremiumTax_2021_07\Support', r'C:\Deliveries\FTP\FM Global\PremiumTax_2021_07\Support')



shutil.copytree(r'C:\Deliveries\Municipal_2021_07\Support', 'C:\Deliveries\FTP\MSB\Municipal_2021_07\Support')
shutil.copytree(r'C:\Deliveries\PremiumTax_2021_07\Support', r'C:\Deliveries\FTP\MSB\PremiumTax_2021_07\Support')


shutil.copytree(r'C:\Deliveries\PremiumTax_2021_07\Support', r'C:\Deliveries\FTP\Nationwide Mutual Insurance Company\PremiumTax_2021_07\Support')


shutil.copytree(r'C:\Deliveries\Municipal_2021_07\Support', r'C:\Deliveries\FTP\Northeastern Utilities\Municipal_2021_07\Support')
shutil.copytree(r'C:\Deliveries\Township_2021_07\Support', r'C:\Deliveries\FTP\Northeastern Utilities\Township_2021_07\Support')


shutil.copytree(r'C:\Deliveries\Municipal_2021_07\Support', 'C:\Deliveries\FTP\Oncor\Municipal_2021_07\Support')


shutil.copytree(r'C:\Deliveries\SpecialTaxDistrict_2021_07\Support', r'C:\Deliveries\FTP\ProTax Systems\Three Layers\SpecialTaxDistrict_2021_07\Support')
shutil.copytree(r'C:\Deliveries\TelcoTax_2021_07\Support', r'C:\Deliveries\FTP\ProTax Systems\Three Layers\TelcoTax_2021_07\Support')
shutil.copytree(r'C:\Deliveries\UtilityTax_2021_07\Support', r'C:\Deliveries\FTP\ProTax Systems\Three Layers\UtilityTax_2021_07\Support')

shutil.copytree(r'C:\Deliveries\County_2021_07\Support', r'C:\Deliveries\FTP\ProTax Systems\Six Layers\County_2021_07\Support')
shutil.copytree(r'C:\Deliveries\Municipal_2021_07\Support', 'C:\Deliveries\FTP\ProTax Systems\Six Layers\Municipal_2021_07\Support')
shutil.copytree(r'C:\Deliveries\SalesUseTax_2021_07\Support', r'C:\Deliveries\FTP\ProTax Systems\Six Layers\SalesUseTax_2021_07\Support')
shutil.copytree(r'C:\Deliveries\SpecialTaxDistrict_2021_07\Support', r'C:\Deliveries\FTP\ProTax Systems\Six Layers\SpecialTaxDistrict_2021_07\Support')
shutil.copytree(r'C:\Deliveries\TelcoTax_2021_07\Support', r'C:\Deliveries\FTP\ProTax Systems\Six Layers\TelcoTax_2021_07\Support')
shutil.copytree(r'C:\Deliveries\UtilityTax_2021_07\Support', r'C:\Deliveries\FTP\ProTax Systems\Six Layers\UtilityTax_2021_07\Support')


shutil.copytree(r'C:\Deliveries\SpecialTaxDistrict_2021_07\Support', r'C:\Deliveries\FTP\Qwest Century Link\SpecialTaxDistrict_2021_07\Support')
shutil.copytree(r'C:\Deliveries\TelcoTax_2021_07\Support', r'C:\Deliveries\FTP\Qwest Century Link\TelcoTax_2021_07\Support')


shutil.copytree(r'C:\Deliveries\Municipal_2021_07\Support', 'C:\Deliveries\FTP\State Farm\Municipal_2021_07\Support')
shutil.copytree(r'C:\Deliveries\Township_2021_07\Support', r'C:\Deliveries\FTP\State Farm\Township_2021_07\Support')


shutil.copytree(r'C:\Deliveries\County_2021_07\Support', r'C:\Deliveries\FTP\Verizon\County_2021_07\Support')
shutil.copytree(r'C:\Deliveries\Municipal_2021_07\Support', 'C:\Deliveries\FTP\Verizon\Municipal_2021_07\Support')
shutil.copytree(r'C:\Deliveries\Township_2021_07\Support', r'C:\Deliveries\FTP\Verizon\Township_2021_07\Support')



