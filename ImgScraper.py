## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally
import os
from os.path import basename

#siteUrl = "https://www.scan-vf.net/uploads/manga/my-hero-academia/chapters/chapitre-"
#destinationUrl = "C:/Users/robin/Desktop/Images"
#chMin = 99
#chMax = 101

hasFound = True

def imgScraper(siteUrl,destinationUrl,chMin,chMax):

    if not os.path.exists(destinationUrl):
            os.makedirs(destinationUrl)

    for chapterNbr in range(chMin,chMax + 1):
        if not os.path.exists(destinationUrl + "/CH" + f"{chapterNbr:03}"):
            os.makedirs(destinationUrl + "/CH" + f"{chapterNbr:03}")

        for pageNbr in range(1,100):

            suffixList = [".png",".jpg"]
            hasFound = False

            for suffix in suffixList:

                image_url = siteUrl + str(chapterNbr) + "/" + f"{pageNbr:02}" + suffix
                filename = destinationUrl + "/CH" + f"{chapterNbr:03}"  + "/" + f"{pageNbr:02}" + suffix
                print(image_url)
                if not os.path.exists(filename):

                    r = requests.get(image_url, stream = True)

                    if r.status_code == 200:
                    
                        r.raw.decode_content = True
                        
                        with open(filename,'wb') as f:
                            shutil.copyfileobj(r.raw, f)
                            
                        print(suffix + ' sucessfully Downloaded: ',filename)
                        hasFound = True
                        break
                else:
                    print("ch" + f"{chapterNbr:03}" + "p" + f"{pageNbr:02}" + " already downloaded")
                    hasFound = True
                    break

            if not hasFound:
                break