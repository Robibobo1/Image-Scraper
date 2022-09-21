## Importing Necessary Modules
from urllib import request
import requests # to get image from the web
import shutil # to save it locally
import os
from os.path import basename

#siteUrl = "https://www.scan-vf.net/uploads/manga/my-hero-academia/chapters/chapitre-"
#destinationUrl = "C:/Users/robin/Desktop/Images"
#chMin = 99
#chMax = 101

hasFound = True

def imgScraper(siteUrl,destinationUrl,chMin,chMax, suffixList, folderName = "CH"):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    if not os.path.exists(destinationUrl):
            os.makedirs(destinationUrl)

    for chapterNbr in range(chMin,chMax + 1):

        if not os.path.exists(destinationUrl + "/" + folderName + f"{chapterNbr:03}"):
            os.makedirs(destinationUrl + "/" + folderName + f"{chapterNbr:03}")

        for pageNbr in range(1,300):

            hasFound = False

            for suffix in suffixList:

                #image_url = siteUrl + str(chapterNbr) + "/" + f"{pageNbr:02}" + suffix
                image_url = siteUrl + str(chapterNbr) + "/" + str(pageNbr) + suffix
                filename = destinationUrl + "/" + folderName + f"{chapterNbr:03}"  + "/" + f"{pageNbr:02}" + suffix
                print(image_url)

                if not os.path.exists(filename):

                    with open(filename, 'wb') as handle:
                        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                        response = requests.get(siteUrl, stream=True, headers=headers)

                        if not response.ok:
                            print(response)

                        for block in response.iter_content(1024):
                            if not block:
                                break

                            handle.write(block)
                        hasFound = True

                    #else:
                        #print("img not found !")
                else:
                    print("ch" + f"{chapterNbr:03}" + "p" + f"{pageNbr:02}" + " already downloaded")
                    hasFound = True
                    break

            if not hasFound:
                break