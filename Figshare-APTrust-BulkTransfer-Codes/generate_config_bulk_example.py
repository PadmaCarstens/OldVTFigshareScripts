import configparser

import os

import platform 
#print("platform is ",platform.system)

"""
Created on Wed Oct  6 12:39:04 2021

@author: padma carstens
"""

"""
Curator fills in the following parameters/paths: 

FigshareArticleID: This is the number found towards the end of the DOI link, click the red "Cite" button on the item under review/to be published 
PubVerNum: Publication Version Number to be downloaded, found at the end of "Cite"
VTDRToken: VTDR token created under applications
CurName: Name of the curator, this shows up in ArchivalReadme Package created in the publication folder
CurationDir: Curation directory where Ingest/Publication folder/README file will be created
NonDissContentDir: Directory where Non disseminated content will be stored, non disseminated content includes provenance log, email correspondence and archival readme package created in the publication folder
VTCurSerFoldPath: Local Folder Path where files for the VTCurationServicesActions are stored(emails, provenance logs etc.)
---------------------------------------------------------------------------------------------------
Following is copy pasted from https://aptrust.github.io/userguide/partner_tools/

APTRUST_AWS_KEY	Access Key ID to access S3. Required only for S3 operations. Works with any S3-compatible service.
APTRUST_AWS_SECRET	Secret access key to access S3. Required only for S3 operations. Works with any S3-compatible service.
APTRUST_REGISTRY_URL	URL of the APTrust registry you want to access. Production is https://repo.aptrust.org. Demo is https://demo.aptrust.org. Required only for registry operations.
APTRUST_REGISTRY_API_VERSION	Version of the current registry API. For now, this should be v3. Required only for registry operations.
APTRUST_REGISTRY_EMAIL	The email address associated with your APTrust registry account. Required only for registry operations.
APTRUST_REGISTRY_API_KEY	The API key associated with your APTrust registry account. Required only for registry operations. Go to the name icon on repo.aptrust.org, click “GET API KEY”, generate your key
------------------------------------------------------------------------------------------------------
SanDiskPath: Path to the sandisk
LocalBagPath: Path where DART bags are stored, this path is also found on Dart app->ApplicationSettings, listed under "Value"
"""
def configurations(FigshareArticleID,PubVerNum):
  print("STARTING CONFIGURATIONS IN GENERATE CONFIG")
  VTDRToken=""
  CurName="Padma Carstens"
  GetPlatform=platform.system()#platform is Darwin for Mac, Windows for windows
  print('PLATFORM name is ',GetPlatform)

  if GetPlatform=="Darwin": #Mac
    CurationDir="/Users/padma/opt/anaconda3/envs/curation"
    NonDissContentDir="/Volumes/GoogleDrive/Shared drives/CurationServicesGoogleDriveArchive/BAGS/NonDisseminatedContent"
    DartExePath="/Applications/DART.app/Contents/MacOS/DART"
    ReadmeDir="/Users/padma/opt/anaconda3/envs/curation/README_FILES"
    platformExt="./"
    SanDiskPath="D:Bags/"
    LocalBagPath='C:/Users/padma/Documents/DART'
    VTCurSerFoldPath="/Users/padma/opt/anaconda3/envs/curation/test"

  if GetPlatform=="Windows":
    CurationDir="C:/Users/padma/anaconda3/envs/curation"
    NonDissContentDir="G:/Shared drives/CurationServicesGoogleDriveArchive/NonDisseminatedContent/"
    DartExePath="C:/Users/padma/AppData/Local/Programs/DART/DART.exe"
    ReadmeDir="C:/Users/padma/anaconda3/envs/curation/README_FILES"
    platformExt=""
    SanDiskPath="E:/Bags"
    LocalBagPath='C:/Users/padma/Documents/DART'
    VTCurSerFoldPath="C:/Users/padma/anaconda3/envs/curation/test"
  
  spreadsheetName="20230721_VTDR_PublishedDatasets_Log_V8"
  APTRUST_REGISTRY_URL = 'https://repo.aptrust.org'
  APTRUST_REGISTRY_API_VERSION='v3'
  APTRUST_REGISTRY_EMAIL=''
  APTRUST_REGISTRY_API_KEY=""
  APTRUST_AWS_KEY=''
  APTRUST_AWS_SECRET=''

#------------------------------------------------------


# ADD SECTION for figshare settings
# CREATE OBJECTS
  config_file = configparser.ConfigParser()
  config_file.add_section("FigshareSettings")
  config_file.set("FigshareSettings", "FigshareArticleID", FigshareArticleID)
  config_file.set("FigshareSettings", "PublishedVersionNumber", PubVerNum)
  config_file.set("FigshareSettings", "IngestVersionNumber", "01")
  config_file.set("FigshareSettings", "token",VTDRToken)
  config_file.set("FigshareSettings", "CuratorName",CurName)

#---------------------------------------------------------
# ADD SECTION for spreadsheet settings
  config_file.add_section("SpreadsheetSettings")
  config_file.set("SpreadsheetSettings","SpreadsheetName",spreadsheetName)
#------------------------------------------------------------------------
# ADD SECTION for AutomatedREADME settings:
  config_file.add_section("AutomatedREADMEPathSettings")
  config_file.set("AutomatedREADMEPathSettings","README_Dir", ReadmeDir)

#-------------------------------------------------------------

# ADD SECTION for AutomatedArchivalPackageREADME settings:
  config_file.add_section("ArchivalREADMEPathSettings")
  config_file.set("ArchivalREADMEPathSettings","ArchivalREADME_RootDir", CurationDir)

#-------------------------------------------------------------
# ADD SECTION for directory path where emails/provlogs are saved to be copied to VTCurationServicesActions folder:
  config_file.add_section("VTCurationServicesActionsFolder")
  config_file.set("VTCurationServicesActionsFolder","VTCurationServicesActionsFolderPath", VTCurSerFoldPath)

#-------------------------------------------------------------

#ADD SECTION for IngestBag_Download_TransferAPTrust script
  config_file.add_section("IngestBag_PathSettings")
  config_file.set("IngestBag_PathSettings","SanDiskDirPath",SanDiskPath)
  config_file.set("IngestBag_PathSettings","IngFolderPath",CurationDir)
  config_file.set("IngestBag_PathSettings","metadatajsonpath",CurationDir)
  config_file.set("IngestBag_PathSettings","LocalPathBag",LocalBagPath)
#----------------------------------------------------------------

#ADD SECTION for PubFolder_Download script
  config_file.add_section("PubFolder_PathSettings")
  config_file.set("PubFolder_PathSettings","PubFolderPath",CurationDir)
  config_file.set("PubFolder_PathSettings","SanDiskDirPath",SanDiskPath)
  config_file.set("PubFolder_PathSettings","LocalPathBag",LocalBagPath)
#----------------------------------------------------------------

#ADD SECTION for PubBagDART_TransferAPTrust script
  config_file.add_section("PubBagDartAptrust_PathSettings")
  config_file.set("PubBagDartAptrust_PathSettings","LargeBagsPath","F:/VTechbags")
  config_file.set("PubBagDartAptrust_PathSettings","NonDisseminatedContentPath",NonDissContentDir)

#-----------------------------------------------------------------

#ADD SECTION for job.py script
  config_file.add_section("dart_PathSettings")
  config_file.set("dart_PathSettings","dart_exe_path",DartExePath)

#---------------------------------------------------------------
# ADD SECTION for AWS settings
# CREATE OBJECTS
#config_file = configparser.ConfigParser(interpolation=None)
  config_file.add_section("APTrustSettings")
#config_file.set("APTrustSettings","aptCmdPath",aptPartnerToolPath )
  config_file.set("APTrustSettings", "registryURL", APTRUST_REGISTRY_URL)
  config_file.set("APTrustSettings", "registryAPIversion",APTRUST_REGISTRY_API_VERSION )
  config_file.set("APTrustSettings", "registryEmail", APTRUST_REGISTRY_EMAIL )
  config_file.set("APTrustSettings", "registryKey", APTRUST_REGISTRY_API_KEY)
  config_file.set("APTrustSettings", "AWSkey", APTRUST_AWS_KEY)
  config_file.set("APTrustSettings", "AWSsecret", APTRUST_AWS_SECRET)
  config_file.set("APTrustSettings", "platformExtn", platformExt)
#-----------------------------------------
  with open(r"configurations-bulk.ini", 'w') as configfileObj:
      config_file.write(configfileObj)
      configfileObj.flush()
      configfileObj.close()

  print("Config file 'configurations-bulk.ini' created")

# PRINT FILE CONTENT
  read_file = open("configurations-bulk.ini", "r")
  content = read_file.read()
  print("Content of the config file are:\n")
  count=1

  with open('configurations-bulk.ini') as infile:
       for line in infile:
          line = line.strip()
          if count == 5 :
              #print("HERE SKIPPING ",count)
              count += 1
              continue
          #if count > 30 : break
          if count > 7 : break
          print(line)
          count += 1
  read_file.flush()
  read_file.close()

#test:
#x=configurations("24328498","01")
#print(x)