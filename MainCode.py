## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally
import os
from os.path import basename

siteUrl = "https://www.scan-vf.net/uploads/manga/my-hero-academia/chapters/"
chapterString = "chapitre-"
chapterMin = 99
chapterMax = 101

hasFound = True


if not os.path.exists("images"):
        os.makedirs("images")

for chapterNbr in range(chapterMin,chapterMax + 1):
    if not os.path.exists("images/CH" + f"{chapterNbr:03}"):
        os.makedirs("images/CH" + f"{chapterNbr:03}")

    for pageNbr in range(1,100):

        suffixList = [".jpg",".png"]
        hasFound = False

        for suffix in suffixList:

            image_url = siteUrl + chapterString + str(chapterNbr) + "/" + f"{pageNbr:02}" + suffix
            filename = "images/CH" + f"{chapterNbr:03}"  + "/" + f"{pageNbr:02}" + suffix

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
                print("Image already downloaded")
                hasFound = True

        if not hasFound:
            break

shutil.make_archive("images", 'zip', "images")
#shutil. rmtree("images")