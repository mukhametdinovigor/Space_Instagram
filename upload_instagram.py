import os
from instabot import Bot
from PIL import Image
import dotenv


def thumbnail_pictures(end_folder, size, start_folder):
    images = os.listdir(start_folder)
    for image in images:
        start_file_path = os.path.join(os.getcwd(), start_folder)
        photo = Image.open(os.path.join(start_file_path, image))
        photo.thumbnail(size)
        rgb_photo = photo.convert('RGB')
        end_file_path = os.path.join(os.getcwd(), end_folder, image)
        rgb_photo.save(f'{end_file_path}', format='JPEG')


def upload_images_to_instagram(end_folder, login, password):
    bot = Bot()
    bot.login(username=login, password=password)
    images_for_instagram = os.listdir(end_folder)
    for pic in images_for_instagram:
        bot.upload_photo(os.path.join(os.getcwd(), end_folder, pic))


def main():
    dotenv.load_dotenv()
    instagram_login = os.getenv('INSTAGRAM_LOGIN')
    instagram_password = os.getenv('INSTAGRAM_PASSWORD')
    download_folder = 'images'
    upload_folder = 'images_for_instagram'
    image_size = (1080, 1080)
    os.makedirs(upload_folder, exist_ok=True)
    thumbnail_pictures(upload_folder, image_size, download_folder)
    upload_images_to_instagram(upload_folder, instagram_login, instagram_password)


if __name__ == '__main__':
    main()
