import requests

with open('pic1.jpg', 'wb') as handle:
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get("https://www.scan-vf.net/uploads/manga/my-hero-academia/chapters/chapitre-366/14.jpg", stream=True, headers=headers)

    if not response.ok:
        print(response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)