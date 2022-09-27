import requests # to get image from the web
import shutil # to save it locally
import os
from os.path import basename
import logging
import sys

folderName = "CH"
suffixList = [".png",".jpg",".webp"]
pageFormat = 2

def chapterDownloader(mangaUrl,filePath,chNumber,idFilter = None):
    
    if not os.path.exists(filePath):
        os.makedirs(filePath)

    folderPath = filePath + '/' + folderName + str(chNumber).zfill(3)

    if os.path.exists(folderPath):
        logging.info("CH" + str(chNumber) + " already exist")
        return 
    os.makedirs(folderPath)
    logging.info("Downloading chapter " + str(chNumber))

    for pageNumber in range(1,500):
        suffixFound = False
        for suffix in suffixList:
            webUrl = mangaUrl + str(chNumber) + "/" + str(pageNumber).zfill(2) + suffix
            htmlCode = imageRequest(webUrl,folderPath + "/" + str(pageNumber).zfill(2) + suffix)
            if htmlCode == 200:
                suffixFound = True
                logging.debug(webUrl)
                break
        if htmlCode == 404:
            logging.info("Chapter " + str(chNumber) + " downloaded" )
            break
    

def multiChaptersDownloader(mangaUrl,filePath,chMin,chMax):
    for chapter in range(chMin,chMax + 1):
        chapterDownloader(mangaUrl,filePath,chapter)


def volumeDownloader(mangaUrl,filePath,volumeList,volumeNumber):
    volumePath = filePath + "/Volume" + str(volumeNumber).zfill(2)
    if os.path.exists(volumePath):
        logging.info("Volume" + str(volumeNumber) + " already exist")
        return 
    os.makedirs(volumePath)
    firstChapter = volumeList[volumeNumber - 1]
    lastChapter = volumeList[volumeNumber] - 1
    multiChaptersDownloader(mangaUrl,filePath,firstChapter,lastChapter)

    try:
        for chapter in range(firstChapter,lastChapter + 1):
            shutil.move(os.path.join(filePath,folderName + str(chapter).zfill(3)), volumePath)
        logging.info("Volume " + str(volumeNumber) + " downloaded succesfully")
    except:
        logging.error("Chapter to volume failed")


def multiVolumesDownloader(mangaUrl,filePath,volumeList,volumeMin,volumeMax):
    for volume in range(volumeMin,volumeMax + 1):
        volumeDownloader(mangaUrl,filePath,volumeList,volume)


def imageRequest(webUrl,fileDestination,headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}):
    r = requests.get(webUrl, stream = True,headers=headers)
    
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(fileDestination,'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return r.status_code

def EmptyVolume(volumeList,destinationUrl):
    for volumeNbr in range(1,len(volumeList)):
        try:
            source_dir = destinationUrl + "/Volume" + f"{volumeNbr:02}"
            target_dir = destinationUrl
            file_names = os.listdir(source_dir)
            for file_name in file_names:
                shutil.move(os.path.join(source_dir, file_name), target_dir)
        except:
                print(":(")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

volumeList = [1,8,18,27,36,45,54,63,72,81,90,100,109,119,129,138,148,158,168,178,189,201,213,225,236,247,259,268,277,286,296,307,319,329,351]

multiVolumesDownloader("https://www.scan-vf.net/uploads/manga/my-hero-academia/chapters/chapitre-","Test",volumeList,1,10)