import os
from instabot import Bot
from PIL import Image
import dotenv


def thumbnail_pictures(end_folder):
    start_folder = 'images'
    images = os.listdir(start_folder)
    for image in images:
        start_file_path = os.path.join(os.getcwd(), start_folder)
        photo = Image.open(os.path.join(start_file_path, image))
        photo.thumbnail((1080, 1080))
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
    INSTAGRAM_LOGIN = os.getenv('INSTAGRAM_LOGIN')
    INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
    upload_folder = 'images_for_instagram'
    os.makedirs(upload_folder, exist_ok=True)
    thumbnail_pictures(upload_folder)
    upload_images_to_instagram(upload_folder, INSTAGRAM_LOGIN, INSTAGRAM_PASSWORD)


if __name__ == '__main__':
    main()
