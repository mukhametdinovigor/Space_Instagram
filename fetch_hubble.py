import requests
import os


def get_best_image_url(url, image_id):
    hubble_image_urls = []
    hubble_response = requests.get(f'{url}{image_id}')
    hubble_response.raise_for_status()
    for image_attributes in hubble_response.json()['image_files']:
        hubble_image_urls.append(f"http:{image_attributes['file_url']}")
    return hubble_image_urls[-1]


def get_best_image_name(url, image_id):
    best_image_extension = f".{get_best_image_url(url, image_id).split('.')[-1]}"
    file_path = os.path.join(os.getcwd(), 'images', str(image_id))
    best_image_name = f'{file_path}{best_image_extension}'
    return best_image_name


def get_images_ids(collect_name):
    image_ids = set()
    payload = {'page': 'all', 'collection_name': collect_name}
    response = requests.get('http://hubblesite.org/api/v3/images', params=payload)
    response.raise_for_status()
    for attribute in response.json():
        image_ids.add(attribute['id'])
    return image_ids


def fetch_hubble_images(image_url, collection_name):
    for image_id in get_images_ids(collection_name):
        user_url = get_best_image_url(image_url, image_id)
        filename = get_best_image_name(image_url, image_id)
        response = requests.get(user_url, verify=False)
        response.raise_for_status()
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f'File {image_id} downloaded')


def main():
    collection = 'printshop'
    hubble_url = 'http://hubblesite.org/api/v3/image/'
    os.makedirs('images', exist_ok=True)
    fetch_hubble_images(hubble_url, collection)


if __name__ == '__main__':
    main()
