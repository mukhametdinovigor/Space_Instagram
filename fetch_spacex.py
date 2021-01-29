import requests
import os


def image_download(image_url, filename):
    response = requests.get(image_url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_launch(images_url, folder):
    file_path = os.path.join(os.getcwd(), folder, 'spacex')
    file_extension = '.jpg'
    spacex_response = requests.get(images_url)
    spacex_response.raise_for_status()
    images_links = spacex_response.json()['links']['flickr_images']
    for image_number, image_link in enumerate(images_links):
        image_download(image_link, f'{file_path}{image_number + 1}{file_extension}')


def main():
    folder = 'images'
    spacex_url = 'https://api.spacexdata.com/v3/launches/67'
    os.makedirs(folder, exist_ok=True)
    fetch_spacex_launch(spacex_url, folder)


if __name__ == '__main__':
    main()
