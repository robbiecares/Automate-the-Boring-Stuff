#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4, logging, datetime

# logging.basicConfig(filename='downloadXkcdLog.txt', level=logging.DEBUG, format=f'{asctime} - {levelname} - {message}')


url = 'https://xkcd.com'               # starting url
os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd
while not url.endswith('#'):

    # Download the page.
    print(f'Downloading page {url}...')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')

     # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
        with open('downloadXkcdLog.txt', 'a+') as log:
            log.write(f'{datetime.datetime.now()}; {url}; could not find image')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # logging.DEBUG(f'comic url: {comicUrl}')

        # confirm if the image has already been saved
        imageFile_path = os.path.join('xkcd', os.path.basename(comicUrl))
        if not os.path.isfile(imageFile_path):
            # Download the image.
            print(f'Downloading image {comicUrl}')
            try:
                res = requests.get(comicUrl)
            except requests.exceptions.InvalidURL:
                with open('downloadXkcdLog.txt', 'a+') as log:
                    log.write(f'{datetime.datetime.now()}; {comicUrl}; invalid url')

                # Get the Prev button's url.
                prevLink = soup.select('a[rel="prev"]')[0]
                url = 'https://xkcd.com' + prevLink.get('href')
                continue

        # Save the image to ./xkcd.
        imageFile = open(imageFile_path, 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')


    print('Done.')