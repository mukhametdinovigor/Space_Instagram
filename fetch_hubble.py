import requests
import os
from utils import download_image


def get_best_image_url(url, image_id):
    hubble_response = requests.get(f'{url}{image_id}')
    hubble_response.raise_for_status()
    return f"http:{hubble_response.json()['image_files'][-1].get('file_url')}"


def get_images_ids(collection_name):
    image_ids = set()
    payload = {'page': 'all', 'collection_name': collection_name}
    response = requests.get('http://hubblesite.org/api/v3/images', params=payload)
    response.raise_for_status()
    for attribute in response.json():
        image_ids.add(attribute['id'])
    return image_ids


def fetch_hubble_images(image_url, collection_name, folder):
    for image_id in get_images_ids(collection_name):
        user_url = get_best_image_url(image_url, image_id)
        filename = os.path.join(os.getcwd(), folder, f'{image_id}{os.path.splitext(user_url)[-1]}')
        download_image(user_url, filename)
        print(f'File {image_id} downloaded')


def main():
    folder = 'images'
    collection = 'printshop'
    hubble_url = 'http://hubblesite.org/api/v3/image/'
    os.makedirs(folder, exist_ok=True)
    fetch_hubble_images(hubble_url, collection, folder)


if __name__ == '__main__':
    main()
