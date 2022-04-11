## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally
import os

siteUrl = "https://www.scan-vf.net/uploads/manga/my-hero-academia/chapters/"
chapterString = "chapitre-"
chapterMax = 4
suffix = ".jpg"

if not os.path.exists("images"):
        os.makedirs("images")

for chapterNbr in range(1,chapterMax):
    if not os.path.exists("images/CH" + f"{chapterNbr:03}"):
        os.makedirs("images/CH" + f"{chapterNbr:03}")

    for pageNbr in range(1,100):

        ## Set up the image URL and filename
        image_url = siteUrl + chapterString + str(chapterNbr) + "/" + f"{pageNbr:02}" + suffix
        filename = "images/CH" + f"{chapterNbr:03}"  + "/" + f"{pageNbr:02}" + suffix

        print(image_url)

        if not os.path.exists(filename):
            # Open the url image, set stream to True, this will return the stream content.
            r = requests.get(image_url, stream = True)

            # Check if the image was retrieved successfully
            if r.status_code == 200:
                # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
                r.raw.decode_content = True
                
                # Open a local file with wb ( write binary ) permission.
                with open(filename,'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                    
                print('Image sucessfully Downloaded: ',filename)
            else:
                print('Image Couldn\'t be retreived')
                break
        else:
            print("Image already downloaded")