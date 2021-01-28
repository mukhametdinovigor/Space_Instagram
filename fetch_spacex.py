import requests
import os


def image_download(image_url, filename):
    response = requests.get(image_url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(images_url):
    file_path = 'images\\spacex'
    file_extension = '.jpg'
    spacex_response = requests.get(images_url)
    spacex_response.raise_for_status()
    images_links = spacex_response.json()['links']['flickr_images']
    for image_number, image_link in enumerate(images_links):
        image_download(image_link, f'{file_path}{image_number + 1}{file_extension}')


def main():
    spacex_url = 'https://api.spacexdata.com/v3/launches/67'
    os.makedirs('images', exist_ok=True)
    fetch_spacex_last_launch(spacex_url)


if __name__ == '__main__':
    main()
