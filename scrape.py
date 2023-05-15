from bs4 import BeautifulSoup
import requests
import os


def download_images(images, path):
    print(f'Found {len(images)} images')
    for i, image in enumerate(images):
        num = f'0{i+1}' if i + 1 < 10 else f'{i+1}'
        try:
            image_link = image['src'] # change this between data-src and src depending on the site
            r = requests.get(image_link).content
        except:
            print(f'image{num} failed link: {image}')
            continue
        f = open(f'{path}\\images{num}.jpg', "wb")
        f.write(r)

    print('download done')


def delete_images(path):
    for filename in os.listdir(path):
        os.remove(f'{path}\\{filename}')

                
def main(url, path):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.findAll('img')
    download_images(images, path)


if __name__ == '__main__':
    import sys
    sys.path.insert(0, '') # Full path to MangaScroller folder

    url = input('input url:')
    path = 'MangaScroller\\Images' # Full path to Images folder

    delete_images(path)
    main(url, path)