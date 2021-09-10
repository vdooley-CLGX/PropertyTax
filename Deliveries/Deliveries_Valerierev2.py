# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:57:06 2021

@author: krbishop
"""

import archook
archook.get_arcpy()
import arcpy


arcpy.env.workspace = "C:\Deliveries"
arcpy.env.overwriteOutput = True
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries", out_name="DVD")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries", out_name="FTP")


arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="PGE")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\PGE", out_name="Utility_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\PGE\Utility_2021_04", out_name="Data")


arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="Black Hills")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills", out_name="County_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills\County_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills", out_name="Municipal_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills\Municipal_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills", out_name="SalesUseTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills\SalesUseTax_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills", out_name="SpecialTaxDistrict_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills\SpecialTaxDistrict_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills", out_name="Township_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Black Hills\Township_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\County_2021_04\Data\County_2021_04.shp", "County_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("County_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Arkansas' , 'Colorado' , 'Iowa' , 'Kansas' , 'Montana' , 'Nebraska' , 'South Dakota' , 'Wyoming' ) ''')
arcpy.CopyFeatures_management("County_2021_04_lyr", "c:\Deliveries\DVD\Black Hills\County_2021_04\Data\County_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_04\Data\Municipal_2021_04.shp", "Municipal_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("Municipal_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Arkansas' , 'Colorado' , 'Iowa' , 'Kansas' , 'Montana' , 'Nebraska' , 'South Dakota' , 'Wyoming' ) ''')
arcpy.CopyFeatures_management("Municipal_2021_04_lyr", "c:\Deliveries\DVD\Black Hills\Municipal_2021_04\Data\Municipal_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SalesUseTax_2021_04\Data\SalesUseTax_2021_04.shp", "SalesUseTax_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("SalesUseTax_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Arkansas' , 'Colorado' , 'Iowa' , 'Kansas' , 'Montana' , 'Nebraska' , 'South Dakota' , 'Wyoming' ) ''')
arcpy.CopyFeatures_management("SalesUseTax_2021_04_lyr", "c:\Deliveries\DVD\Black Hills\SalesUseTax_2021_04\Data\SalesUseTax_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04.shp", "SpecialTaxDistrict_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("SpecialTaxDistrict_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'CO' , 'KS' , 'MT' , 'NE' , 'SD' , 'WY' ) ''')
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_04_lyr", "c:\Deliveries\DVD\Black Hills\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_04\Data\Township_2021_04.shp", "Township_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("Township_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Arkansas' , 'Colorado' , 'Iowa' , 'Kansas' , 'Montana' , 'Nebraska' , 'South Dakota' , 'Wyoming' ) ''')
arcpy.CopyFeatures_management("Township_2021_04_lyr", "c:\Deliveries\DVD\Black Hills\Township_2021_04\Data\Township_2021_04")



arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="FM Global")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\FM Global", out_name="County_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\FM Global\County_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\FM Global", out_name="PremiumTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\FM Global\PremiumTax_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\County_2021_04\Data\County_2021_04.shp", "County_2021_04_lyr")
arcpy.CopyFeatures_management("County_2021_04_lyr", "c:\Deliveries\FTP\FM Global\County_2021_04\Data\County_2021_04")
arcpy.CopyFeatures_management("PremiumTax_2021_04_lyr", "c:\Deliveries\FTP\FM Global\PremiumTax_2021_04\Data\PremiumTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="FM Global")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\FM Global", out_name="County_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\FM Global\County_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\FM Global", out_name="PremiumTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\FM Global\PremiumTax_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\County_2021_04\Data\County_2021_04.shp", "County_2021_04_lyr")
arcpy.CopyFeatures_management("County_2021_04_lyr", "c:\Deliveries\DVD\FM Global\County_2021_04\Data\County_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\PremiumTax_2021_04\Data\PremiumTax_2021_04.shp", "PremiumTax_2021_04_lyr")
arcpy.CopyFeatures_management("PremiumTax_2021_04_lyr", "c:\Deliveries\DVD\FM Global\PremiumTax_2021_04\Data\PremiumTax_2021_04")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="Verizon")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Verizon", out_name="County_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Verizon\County_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Verizon", out_name="Municipal_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Verizon\Municipal_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Verizon", out_name="Township_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Verizon\Township_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\County_2021_04\Data\County_2021_04.shp", "County_2021_04_lyr")
arcpy.CopyFeatures_management("County_2021_04_lyr", "c:\Deliveries\FTP\Verizon\County_2021_04\Data\County_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_04\Data\Municipal_2021_04.shp", "Municipal_2021_04_lyr")
arcpy.CopyFeatures_management("Municipal_2021_04_lyr", "c:\Deliveries\FTP\Verizon\Municipal_2021_04\Data\Municipal_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_04\Data\Township_2021_04.shp", "Township_2021_04_lyr")
arcpy.CopyFeatures_management("Township_2021_04_lyr", "c:\Deliveries\FTP\Verizon\Township_2021_04\Data\Township_2021_04")



arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="Ameren")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Ameren", out_name="Municipal_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Ameren\Municipal_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Ameren", out_name="Township_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Ameren\Township_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_04\Data\Municipal_2021_04.shp", "Municipal_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("Municipal_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Missouri' , 'Illinois') ''')
arcpy.CopyFeatures_management("Municipal_2021_04_lyr", "c:\Deliveries\FTP\Ameren\Municipal_2021_04\Data\Municipal_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_04\Data\Township_2021_04.shp", "Township_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("Township_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Missouri' , 'Illinois') ''')
arcpy.CopyFeatures_management("Township_2021_04_lyr", "c:\Deliveries\FTP\Ameren\Township_2021_04\Data\Township_2021_04")



arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="Entergy")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Entergy", out_name="Municipal_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Entergy\Municipal_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Entergy", out_name="Township_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Entergy\Township_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Entergy", out_name="SchoolDistrict_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Entergy\SchoolDistrict_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_04\Data\Municipal_2021_04.shp", "Municipal_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("Municipal_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Arkansas' , 'Louisiana' , 'Mississippi' , 'Missouri' , 'Tennessee', 'Texas') ''')
arcpy.CopyFeatures_management("Municipal_2021_04_lyr", "C:\Deliveries\DVD\Entergy\Municipal_2021_04\Data\Municipal_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_04\Data\Township_2021_04.shp", "Township_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("Township_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Arkansas' , 'Louisiana' , 'Mississippi' , 'Missouri' , 'Tennessee', 'Texas') ''')
arcpy.CopyFeatures_management("Township_2021_04_lyr", "C:\Deliveries\DVD\Entergy\Township_2021_04\Data\Township_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SchoolDistrict_2021_04\Data\SchoolDistrict_2021_04.shp", "SchoolDistrict_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("SchoolDistrict_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Arkansas' , 'Louisiana' , 'Mississippi' , 'Missouri' , 'Tennessee' , 'Texas') ''')
arcpy.CopyFeatures_management("SchoolDistrict_2021_04_lyr", "c:\Deliveries\DVD\Entergy\SchoolDistrict_2021_04\Data\SchoolDistrict_2021_04")



arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="MSB")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\MSB", out_name="Municipal_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\MSB\Municipal_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\MSB", out_name="PremiumTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\MSB\PremiumTax_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="MSB")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\MSB", out_name="Municipal_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\MSB\Municipal_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\MSB", out_name="PremiumTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\MSB\PremiumTax_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_04\Data\Municipal_2021_04.shp", "Municipal_2021_04_lyr")
arcpy.CopyFeatures_management("Municipal_2021_04_lyr", "c:\Deliveries\DVD\MSB\Municipal_2021_04\Data\Municipal_2021_04")
arcpy.CopyFeatures_management("Municipal_2021_04_lyr", "c:\Deliveries\FTP\MSB\Municipal_2021_04\Data\Municipal_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\PremiumTax_2021_04\Data\PremiumTax_2021_04.shp", "PremiumTax_2021_04_lyr")
arcpy.CopyFeatures_management("PremiumTax_2021_04_lyr", "c:\Deliveries\DVD\MSB\PremiumTax_2021_04\Data\PremiumTax_2021_04")
arcpy.CopyFeatures_management("PremiumTax_2021_04_lyr", "c:\Deliveries\FTP\MSB\PremiumTax_2021_04\Data\PremiumTax_2021_04")



arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="Oncor")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Oncor", out_name="Municipal_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Oncor\Municipal_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_04\Data\Municipal_2021_04.shp", "Municipal_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("Municipal_2021_04_lyr", "NEW_SELECTION",'''"State" = 'Texas' ''')
arcpy.CopyFeatures_management("Municipal_2021_04_lyr", "c:\Deliveries\FTP\Oncor\Municipal_2021_04\Data\Municipal_2021_04")



arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="TDS")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\TDS", out_name="Municipal_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\TDS\Municipal_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\TDS", out_name="Township_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\TDS\Township_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_04\Data\Municipal_2021_04.shp", "Municipal_2021_04_lyr")
arcpy.CopyFeatures_management("Municipal_2021_04_lyr", "c:\Deliveries\DVD\TDS\Municipal_2021_04\Data\Municipal_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_04\Data\Township_2021_04.shp", "Township_2021_04_lyr")
arcpy.CopyFeatures_management("Township_2021_04_lyr", "c:\Deliveries\DVD\TDS\Township_2021_04\Data\Township_2021_04")



arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="National Grid")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\National Grid", out_name="Municipal_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\National Grid\Municipal_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\National Grid", out_name="Township_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\National Grid\Township_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_04\Data\Municipal_2021_04.shp", "Municipal_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("Municipal_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Massachusetts' , 'New Hampshire' , 'New York' , 'Rhode Island') ''')
arcpy.CopyFeatures_management("Municipal_2021_04_lyr", "c:\Deliveries\DVD\National Grid\Municipal_2021_04\Data\Municipal_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_04\Data\Township_2021_04.shp", "Township_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("Township_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Massachusetts' , 'New Hampshire' , 'New York' , 'Rhode Island') ''')
arcpy.CopyFeatures_management("Township_2021_04_lyr", "c:\Deliveries\DVD\National Grid\Township_2021_04\Data\Township_2021_04")





arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="AMIC")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\AMIC", out_name="PremiumTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\AMIC\PremiumTax_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\PremiumTax_2021_04\Data\PremiumTax_2021_04.shp", "PremiumTax_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("PremiumTax_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Alabama' , 'California' , 'Delaware' , 'Florida', 'Georgia' , 'Illinois' , 'Kentucky', 'Louisiana' , 'Maryland' , 'Minnesota', 'Mississippi' , 'New Jersey' , 'New York', 'South Carolina' , 'North Dakota' ) ''')
arcpy.CopyFeatures_management("PremiumTax_2021_04_lyr", "c:\Deliveries\DVD\AMIC\PremiumTax_2021_04\Data\PremiumTax_2021_04")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="Eagle Technology Management")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Eagle Technology Management", out_name="PremiumTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Eagle Technology Management\PremiumTax_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\PremiumTax_2021_04\Data\PremiumTax_2021_04.shp", "PremiumTax_2021_04_lyr")
arcpy.CopyFeatures_management("PremiumTax_2021_04_lyr", "c:\Deliveries\FTP\Eagle Technology Management\PremiumTax_2021_04\Data\PremiumTax_2021_04")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="State Farm")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\State Farm", out_name="Municipal_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\State Farm\Municipal_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\State Farm", out_name="Township_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\State Farm\Township_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_04\Data\Municipal_2021_04.shp", "Municipal_2021_04_lyr")
arcpy.CopyFeatures_management("Municipal_2021_04_lyr", "c:\Deliveries\FTP\State Farm\Municipal_2021_04\Data\Municipal_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_04\Data\Township_2021_04.shp", "Township_2021_04_lyr")
arcpy.CopyFeatures_management("Township_2021_04_lyr", "c:\Deliveries\FTP\State Farm\Township_2021_04\Data\Township_2021_04")





arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="Nationwide")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Nationwide", out_name="County_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Nationwide\County_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Nationwide", out_name="PremiumTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Nationwide\PremiumTax_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\County_2021_04\Data\County_2021_04.shp", "County_2021_04_lyr")
arcpy.CopyFeatures_management("County_2021_04_lyr", "c:\Deliveries\DVD\Nationwide\County_2021_04\Data\County_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\PremiumTax_2021_04\Data\PremiumTax_2021_04.shp", "PremiumTax_2021_04_lyr")
arcpy.CopyFeatures_management("PremiumTax_2021_04_lyr", "c:\Deliveries\DVD\Nationwide\PremiumTax_2021_04\Data\PremiumTax_2021_04")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="Nationwide Mutual Insurance Company")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Nationwide Mutual Insurance Company", out_name="PremiumTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Nationwide Mutual Insurance Company\PremiumTax_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\PremiumTax_2021_04\Data\PremiumTax_2021_04.shp", "PremiumTax_2021_04_lyr")
arcpy.CopyFeatures_management("PremiumTax_2021_04_lyr", "c:\Deliveries\FTP\Nationwide Mutual Insurance Company\PremiumTax_2021_04\Data\PremiumTax_2021_04")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="Metlife")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Metlife", out_name="PremiumTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Metlife\PremiumTax_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\PremiumTax_2021_04\Data\PremiumTax_2021_04.shp", "PremiumTax_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("PremiumTax_2021_04_lyr", "NEW_SELECTION",'''"State" = 'Florida' ''')
arcpy.CopyFeatures_management("PremiumTax_2021_04_lyr", "c:\Deliveries\FTP\Metlife\PremiumTax_2021_04\Data\PremiumTax_2021_04")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="Vallen Distribution")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Vallen Distribution", out_name="SalesUseTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Vallen Distribution\SalesUseTax_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Vallen Distribution", out_name="SpecialTaxDistrict_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Vallen Distribution\SpecialTaxDistrict_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SalesUseTax_2021_04\Data\SalesUseTax_2021_04.shp", "SalesUseTax_2021_04_lyr")
arcpy.CopyFeatures_management("SalesUseTax_2021_04_lyr", "c:\Deliveries\DVD\Vallen Distribution\SalesUseTax_2021_04\Data\SalesUseTax_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04.shp", "SpecialTaxDistrict_2021_04_lyr")
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_04_lyr", "c:\Deliveries\DVD\Vallen Distribution\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="American Electric Power Rusling")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Rusling", out_name="SalesUseTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Rusling\SalesUseTax_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Rusling", out_name="SpecialTaxDistrict_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Rusling\SpecialTaxDistrict_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SalesUseTax_2021_04\Data\SalesUseTax_2021_04.shp", "SalesUseTax_2021_04_lyr")
arcpy.CopyFeatures_management("SalesUseTax_2021_04_lyr", "c:\Deliveries\DVD\American Electric Power Rusling\SalesUseTax_2021_04\Data\SalesUseTax_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04.shp", "SpecialTaxDistrict_2021_04_lyr")
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_04_lyr", "c:\Deliveries\DVD\American Electric Power Rusling\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="American Electric Power Gentry")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Gentry", out_name="SchoolDistrict_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Gentry\SchoolDistrict_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Gentry", out_name="Township_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\American Electric Power Gentry\Township_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SchoolDistrict_2021_04\Data\SchoolDistrict_2021_04.shp", "SchoolDistrict_2021_04_lyr")
arcpy.CopyFeatures_management("SchoolDistrict_2021_04_lyr", "C:\Deliveries\DVD\American Electric Power Gentry\SchoolDistrict_2021_04\Data\SchoolDistrict_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_04\Data\Township_2021_04.shp", "Township_2021_04_lyr")
arcpy.CopyFeatures_management("Township_2021_04_lyr", "c:\Deliveries\DVD\American Electric Power Gentry\Township_2021_04\Data\Township_2021_04")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="Southwest Gas Corporation")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Southwest Gas Corporation", out_name="SalesUseTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Southwest Gas Corporation\SalesUseTax_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Southwest Gas Corporation", out_name="SpecialTaxDistrict_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Southwest Gas Corporation\SpecialTaxDistrict_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SalesUseTax_2021_04\Data\SalesUseTax_2021_04.shp", "SalesUseTax_2021_04_lyr")
arcpy.CopyFeatures_management("SalesUseTax_2021_04_lyr", "c:\Deliveries\DVD\Southwest Gas Corporation\SalesUseTax_2021_04\Data\SalesUseTax_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04.shp", "SpecialTaxDistrict_2021_04_lyr")
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_04_lyr", "c:\Deliveries\DVD\Southwest Gas Corporation\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="ProTax Systems")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems", out_name="Twelve States")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Twelve States", out_name="SalesUseTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Twelve States\SalesUseTax_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Twelve States", out_name="SpecialTaxDistrict_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Twelve States\SpecialTaxDistrict_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Twelve States", out_name="TelcoTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Twelve States\TelcoTax_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Twelve States", out_name="UtilityTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Twelve States\UtilityTax_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Twelve States", out_name="Municipal_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Twelve States\Municipal_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Twelve States", out_name="County_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Twelve States\County_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SalesUseTax_2021_04\Data\SalesUseTax_2021_04.shp", "SalesUseTax_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("SalesUseTax_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Alabama' , 'Alaska' , 'Hawaii' , 'Kansas', 'Nevada' , 'Illinois' , 'Louisiana' , 'New York' , 'Oklahoma', 'Texas' , 'Vermont' , 'South Carolina' ) ''')
arcpy.CopyFeatures_management("SalesUseTax_2021_04_lyr", "C:\Deliveries\FTP\ProTax Systems\Twelve States\SalesUseTax_2021_04\Data\SalesUseTax_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04.shp", "SpecialTaxDistrict_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("SpecialTaxDistrict_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'AK' , 'AL' , 'HI' ,  'KS' , 'NV' , 'IL' , 'LA' , 'NY' , 'OK' , 'TX' , 'VT' , 'SC' ) ''')
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_04_lyr", "C:\Deliveries\FTP\ProTax Systems\Twelve States\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\TelcoTax_2021_04\Data\TelcoTax_2021_04.shp", "TelcoTax_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("TelcoTax_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Alabama' , 'Alaska' , 'Hawaii' , 'Kansas', 'Nevada' , 'Illinois' , 'Louisiana' , 'New York' , 'Oklahoma', 'Texas' , 'Vermont' , 'South Carolina' ) ''')
arcpy.CopyFeatures_management("TelcoTax_2021_04_lyr", "c:\Deliveries\FTP\ProTax Systems\Twelve States\TelcoTax_2021_04\Data\TelcoTax_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\UtilityTax_2021_04\Data\UtilityTax_2021_04.shp", "UtilityTax_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("UtilityTax_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Alabama' , 'Alaska' , 'Hawaii' , 'Kansas', 'Nevada' , 'Illinois' , 'Louisiana' , 'New York' , 'Oklahoma', 'Texas' , 'Vermont' , 'South Carolina' ) ''')
arcpy.CopyFeatures_management("UtilityTax_2021_04_lyr", "C:\Deliveries\FTP\ProTax Systems\Twelve States\UtilityTax_2021_04\Data\UtilityTax_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_04\Data\Municipal_2021_04.shp", "Municipal_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("Municipal_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Alabama' , 'Alaska' , 'Hawaii' , 'Kansas', 'Nevada' , 'Illinois' , 'Louisiana' , 'New York' , 'Oklahoma', 'Texas' , 'Vermont' , 'South Carolina' ) ''')
arcpy.CopyFeatures_management("Municipal_2021_04_lyr", "C:\Deliveries\FTP\ProTax Systems\Twelve States\Municipal_2021_04\Data\Municipal_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\County_2021_04\Data\County_2021_04.shp", "County_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("County_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Alabama' , 'Alaska' , 'Hawaii' , 'Kansas', 'Nevada' , 'Illinois' , 'Louisiana' , 'New York' , 'Oklahoma', 'Texas' , 'Vermont' , 'South Carolina' ) ''')
arcpy.CopyFeatures_management("County_2021_04_lyr", "C:\Deliveries\FTP\ProTax Systems\Twelve States\County_2021_04\Data\County_2021_04")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems", out_name="Three States")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Three States", out_name="SpecialTaxDistrict_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Three States\SpecialTaxDistrict_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Three States", out_name="TelcoTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Three States\TelcoTax_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Three States", out_name="UtilityTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\ProTax Systems\Three States\UtilityTax_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04.shp", "SpecialTaxDistrict_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("SpecialTaxDistrict_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'CA' , 'MO' , 'WA' ) ''')
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_04_lyr", "C:\Deliveries\FTP\ProTax Systems\Three States\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\TelcoTax_2021_04\Data\TelcoTax_2021_04.shp", "TelcoTax_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("TelcoTax_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'California' , 'Missouri' , 'Washington' ) ''')
arcpy.CopyFeatures_management("TelcoTax_2021_04_lyr", "C:\Deliveries\FTP\ProTax Systems\Three States\TelcoTax_2021_04\Data\TelcoTax_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\UtilityTax_2021_04\Data\UtilityTax_2021_04.shp", "UtilityTax_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("UtilityTax_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'California' , 'Missouri' , 'Washington' ) ''')
arcpy.CopyFeatures_management("UtilityTax_2021_04_lyr", "C:\Deliveries\FTP\ProTax Systems\Three States\UtilityTax_2021_04\Data\UtilityTax_2021_04")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="Duke Energy Johnson")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Johnson", out_name="SalesUseTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Johnson\SalesUseTax_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Johnson", out_name="SpecialTaxDistrict_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Johnson\SpecialTaxDistrict_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SalesUseTax_2021_04\Data\SalesUseTax_2021_04.shp", "SalesUseTax_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("SalesUseTax_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Florida' , 'Indiana' , 'Kentucky', 'North Carolina' , 'Ohio' , 'South Carolina' ) ''')
arcpy.CopyFeatures_management("SalesUseTax_2021_04_lyr", "C:\Deliveries\DVD\Duke Energy Johnson\SalesUseTax_2021_04\Data\SalesUseTax_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04.shp", "SpecialTaxDistrict_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("SpecialTaxDistrict_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'FL' , 'KY' , 'NC' , 'OH', 'SC' ) ''')
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_04_lyr", "C:\Deliveries\DVD\Duke Energy Johnson\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04")





arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="Duke Energy Wright")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Wright", out_name="SalesUseTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Wright\SalesUseTax_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Wright", out_name="SpecialTaxDistrict_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Wright\SpecialTaxDistrict_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SalesUseTax_2021_04\Data\SalesUseTax_2021_04.shp", "SalesUseTax_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("SalesUseTax_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'Florida' , 'Indiana' , 'Kentucky', 'North Carolina' , 'Ohio' , 'South Carolina' ) ''')
arcpy.CopyFeatures_management("SalesUseTax_2021_04_lyr", "C:\Deliveries\DVD\Duke Energy Wright\SalesUseTax_2021_04\Data\SalesUseTax_2021_04")
arcpy.SelectLayerByAttribute_management("SpecialTaxDistrict_2021_04_lyr", "NEW_SELECTION",'''STATE IN( 'FL' , 'KY' , 'NC' , 'OH', 'SC' ) ''')
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_04_lyr", "C:\Deliveries\DVD\Duke Energy Wright\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD", out_name="Duke Energy Shepherd")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Shepherd", out_name="SchoolDistrict_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\DVD\Duke Energy Shepherd\SchoolDistrict_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SchoolDistrict_2021_04\Data\SchoolDistrict_2021_04.shp", "SchoolDistrict_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("SchoolDistrict_2021_04_lyr", "NEW_SELECTION",'''"State" = 'Kentucky' ''')
arcpy.CopyFeatures_management("SchoolDistrict_2021_04_lyr", "c:\Deliveries\DVD\Duke Energy Shepherd\SchoolDistrict_2021_04\Data\SchoolDistrict_2021_04")






arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="Qwest Century Link")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Qwest Century Link", out_name="SpecialTaxDistrict_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Qwest Century Link\SpecialTaxDistrict_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Qwest Century Link", out_name="TelcoTax_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Qwest Century Link\TelcoTax_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04.shp", "SpecialTaxDistrict_2021_04_lyr")
arcpy.CopyFeatures_management("SpecialTaxDistrict_2021_04_lyr", "c:\Deliveries\FTP\Qwest Century Link\SpecialTaxDistrict_2021_04\Data\SpecialTaxDistrict_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\TelcoTax_2021_04\Data\TelcoTax_2021_04.shp", "TelcoTax_2021_04_lyr")
arcpy.CopyFeatures_management("TelcoTax_2021_04_lyr", "c:\Deliveries\FTP\Qwest Century Link\TelcoTax_2021_04\Data\TelcoTax_2021_04")




arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP", out_name="Northeastern Utilities")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Northeastern Utilities", out_name="Municipal_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Northeastern Utilities\Municipal_2021_04", out_name="Data")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Northeastern Utilities", out_name="Township_2021_04")
arcpy.CreateFolder_management(out_folder_path="C:\Deliveries\FTP\Northeastern Utilities\Township_2021_04", out_name="Data")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Municipal_2021_04\Data\Municipal_2021_04.shp", "Municipal_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("Municipal_2021_04_lyr", "NEW_SELECTION",'''"STATE" IN('Maine' , 'Vermont' , 'New Hampshire') AND "COUNTY" IN ( 'Fairfield' , 'Hartford' , 'Litchfield' , 'Middlesex' , 'New Haven' , 'New London' , 'Tolland'  , 'York' , 'Barnstable' , 'Berkshire' , 'Bristol' , 'Dukes' , 'Hampden' , 'Hampshire' , 'Middlesex' , 'Norfolk' , 'Plymouth' , 'Suffolk' , 'Worcester' , 'Belknap', 'Carroll', 'Cheshire' , 'Coos' , 'Grafton' , 'Hillsborough' , 'Merrimack' , 'Rockingham' , 'Strafford' , 'Sullivan' , 'Caledonia' , 'Essex' ) OR STATE = 'Connecticut' AND "COUNTY" IN ( 'Fairfield' , 'Hartford' , 'Litchfield' , 'Middlesex' , 'New Haven' , 'New London' , 'Tolland' ,'Windham', 'York' , 'Barnstable' , 'Berkshire' , 'Bristol' , 'Dukes' ,  'Hampden' , 'Hampshire' , 'Middlesex' , 'Norfolk' , 'Plymouth' , 'Suffolk' , 'Worcester' , 'Belknap', 'Carroll', 'Cheshire' , 'Coos' , 'Grafton' , 'Hillsborough' , 'Merrimack' , 'Rockingham' , 'Strafford' , 'Sullivan' , 'Caledonia' , 'Essex' ) OR STATE = 'Massachusetts' AND "COUNTY" IN ( 'Fairfield' , 'Hartford' , 'Litchfield' , 'Middlesex' , 'New Haven' , 'New London' , 'Tolland' ,'Windham', 'York' , 'Barnstable' , 'Berkshire' , 'Bristol' , 'Dukes' , 'Franklin' , 'Hampden' , 'Hampshire' , 'Middlesex' , 'Norfolk' , 'Plymouth' , 'Suffolk' , 'Worcester' , 'Belknap', 'Carroll', 'Cheshire' , 'Coos' , 'Grafton' , 'Hillsborough' , 'Merrimack' , 'Rockingham' , 'Strafford' , 'Sullivan' , 'Caledonia' , 'Essex' ) ''')
arcpy.CopyFeatures_management("Municipal_2021_04_lyr", "c:\Deliveries\FTP\Northeastern Utilities\Municipal_2021_04\Data\Municipal_2021_04")
arcpy.MakeFeatureLayer_management("C:\Deliveries\Township_2021_04\Data\Township_2021_04.shp", "Township_2021_04_lyr")
arcpy.SelectLayerByAttribute_management("Township_2021_04_lyr", "NEW_SELECTION",'''"STATE" IN('Maine' , 'Vermont' , 'New Hampshire') AND "COUNTY" IN ( 'Fairfield' , 'Hartford' , 'Litchfield' , 'Middlesex' , 'New Haven' , 'New London' , 'Tolland'  , 'York' , 'Barnstable' , 'Berkshire' , 'Bristol' , 'Dukes' , 'Hampden' , 'Hampshire' , 'Middlesex' , 'Norfolk' , 'Plymouth' , 'Suffolk' , 'Worcester' , 'Belknap', 'Carroll', 'Cheshire' , 'Coos' , 'Grafton' , 'Hillsborough' , 'Merrimack' , 'Rockingham' , 'Strafford' , 'Sullivan' , 'Caledonia' , 'Essex' ) OR STATE = 'Connecticut' AND "COUNTY" IN ( 'Fairfield' , 'Hartford' , 'Litchfield' , 'Middlesex' , 'New Haven' , 'New London' , 'Tolland' ,'Windham', 'York' , 'Barnstable' , 'Berkshire' , 'Bristol' , 'Dukes' ,  'Hampden' , 'Hampshire' , 'Middlesex' , 'Norfolk' , 'Plymouth' , 'Suffolk' , 'Worcester' , 'Belknap', 'Carroll', 'Cheshire' , 'Coos' , 'Grafton' , 'Hillsborough' , 'Merrimack' , 'Rockingham' , 'Strafford' , 'Sullivan' , 'Caledonia' , 'Essex' ) OR STATE = 'Massachusetts' AND "COUNTY" IN ( 'Fairfield' , 'Hartford' , 'Litchfield' , 'Middlesex' , 'New Haven' , 'New London' , 'Tolland' ,'Windham', 'York' , 'Barnstable' , 'Berkshire' , 'Bristol' , 'Dukes' , 'Franklin' , 'Hampden' , 'Hampshire' , 'Middlesex' , 'Norfolk' , 'Plymouth' , 'Suffolk' , 'Worcester' , 'Belknap', 'Carroll', 'Cheshire' , 'Coos' , 'Grafton' , 'Hillsborough' , 'Merrimack' , 'Rockingham' , 'Strafford' , 'Sullivan' , 'Caledonia' , 'Essex' ) ''')
arcpy.CopyFeatures_management("Township_2021_04_lyr", "c:\Deliveries\FTP\Northeastern Utilities\Township_2021_04\Data\Township_2021_04")



