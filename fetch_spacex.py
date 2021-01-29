import requests
import os
from utils import download_image


def fetch_spacex_launch(images_url, folder):
    file_path = os.path.join(os.getcwd(), folder, 'spacex')
    file_extension = '.jpg'
    spacex_response = requests.get(images_url)
    spacex_response.raise_for_status()
    images_links = spacex_response.json()['links']['flickr_images']
    for image_number, image_link in enumerate(images_links, start=1):
        download_image(image_link, f'{file_path}{image_number}{file_extension}')


def main():
    folder = 'images'
    spacex_url = 'https://api.spacexdata.com/v3/launches/67'
    os.makedirs(folder, exist_ok=True)
    fetch_spacex_launch(spacex_url, folder)


if __name__ == '__main__':
    main()
