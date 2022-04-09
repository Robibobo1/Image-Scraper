import os
import json 
import requests # to sent GET requests
from bs4 import BeautifulSoup # to parse HTML

PATH = "C:\\Users\\Robin\\Desktop\\Code Projet\\Image-Scraper"
ADRESS = "https://www.scan-vf.net/my-hero-academia/chapitre-347/1"
GOOGLE_IMAGE = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

usr_agent = {'User-agent': 'Mozilla/5.0'}

SAVE_FOLDER = 'images'


SAVE_FOLDER = 'images'

def main():
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)
    download_images()
    
def download_images():
    # ask for user input
    data = input('What are you looking for? ')
    n_images = int(input('How many images do you want? '))

    print('Start searching...')
    
    # get url query string
    searchurl = PATH
    print(searchurl)

    # request url, without usr_agent the permission gets denied
    response = requests.get(searchurl, headers=usr_agent)
    html = response.text
    print(html)
    
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.findAll('div', {'class': 'img-responsive scan-page'}, limit=n_images)
    
    # extract the link from the div tag
    imagelinks= []
    for re in results:
        text = re.text # this is a valid json string
        text_dict= json.loads(text) # deserialize json to a Python dict
        link = text_dict['ou']
        # image_type = text_dict['ity']
        imagelinks.append(link)

    print(f'found {len(imagelinks)} images')
    print('Start downloading...')

    for i, imagelink in enumerate(imagelinks):
        # open image link and save as file§
        response = requests.get(imagelink)
        
        imagename = SAVE_FOLDER + '/' + data + str(i+1) + '.png'
        with open(imagename, 'wb') as file:
            file.write(response.content)

    print('Done')


if __name__ == '__main__':
    main()