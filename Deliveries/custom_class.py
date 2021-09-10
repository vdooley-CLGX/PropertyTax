# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 19:21:13 2021

@author: vmajor
"""
import glob2
import os
from datetime import datetime
import time
class do_stuff:
    
    def run_qa(self, folder):
        
        # local variables 
        FPATH = folder
        
        try:
#            # Report step message 1
#            arcpy.AddMessage("PROCESSING:")
#            arcpy.AddMessage(" ")
#            arcpy.AddMessage("1 of 3 - Creating ESRI Spatial Index (.shx)...")
        
            # Create ESRI Spatial Index
            #arcpy.AddSpatialIndex_management(InFeature) 
        
            # Report step message 2
            #arcpy.AddMessage("2 of 3 - Deleting extra files (.cpg & .xml)...")
        
            for file in os.listdir(FPATH):
                if file.endswith(".cpg"):
                    os.remove(os.path.join(FPATH, file))
                elif file.endswith(".xml"):
                    os.remove(os.path.join(FPATH, file))
                elif file.endswith(".lock"):
                    os.remove(os.path.join(FPATH, file))
                elif file.endswith(".rtx"):
                    rtxModDate = int(os.path.getmtime(os.path.join(FPATH, file)))
                    sRtxModDate = time.ctime(rtxModDate)
                elif file.endswith(".shp"):
                    shpModDate = int(os.path.getmtime(os.path.join(FPATH, file)))
                    sShpModDate = time.ctime(shpModDate)
                elif file.endswith(".dbf"):
                    dbfModDate = int(os.path.getmtime(os.path.join(FPATH, file)))
                    sDbfModDate = time.ctime(dbfModDate)
                else:
                    pass
        
            # Report step message 3
            #arcpy.AddMessage("3 of 3 - Checking that the .rtx file has the same or newer date stamp...")
            with open('test.txt', 'a') as writer:
                
                if (rtxModDate >= shpModDate):
                    writer.write(folder +"shpModDate passed\n")
    #                arcpy.AddMessage("   PASSED - the .rtx file is in sync ( >= .shp and/or .dbf)")
    #                arcpy.AddMessage("          last modified date for .rtx file: " + sRtxModDate)
    #                arcpy.AddMessage("          last modified date for .shp file: " + sShpModDate)
    #                arcpy.AddMessage("          last modified date for .dbf file: " + sDbfModDate)
                else:
                    writer.write(folder +"shpModDate failed\n")
    #                arcpy.AddMessage("   FAILED - the .rtx file is not in sync ( <= .shp and/or .dbf)")
    #                arcpy.AddMessage("          last modified date for .rtx file: " + sRtxModDate)
    #                arcpy.AddMessage("          last modified date for .shp file: " + sShpModDate)
    #                arcpy.AddMessage("          last modified date for .dbf file: " + sDbfModDate)
                    
                if (rtxModDate >= dbfModDate):
                    writer.write(folder +"dbfModDate passed\n")
                else:
                    writer.write(folder +"dbfModDate failed\n")
        except UnboundLocalError as e:
        
            print '\n\n', e,FPATH, '\n\n'
            
#            # Report an error message
#            arcpy.AddError("Could not complete layer finalization.")
#        
#            # Report any error messages that the tools might have generated
#            arcpy.AddMessage(arcpy.GetMessages())
                
                

if __name__ == '__main__':
    obj = do_stuff()
    
    DVD_data_folders = glob2.glob('C:\Deliveries\DVD\**\*Data')
    FTP_data_folders = glob2.glob('C:\Deliveries\FTP\**\*Data')
    combine_data_folders = DVD_data_folders + FTP_data_folders
    
    for folder in combine_data_folders:
        obj.run_qa(folder)
