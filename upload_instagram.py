import os
from instabot import Bot
from PIL import Image
import dotenv

dotenv.load_dotenv()
INSTAGRAM_LOGIN = os.getenv('INSTAGRAM_LOGIN')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')


def thumbnail_pic():
    images = os.listdir('images')
    for image in images:
        photo = Image.open(f'images//{image}')
        photo.thumbnail((1080, 1080))
        rgb_photo = photo.convert('RGB')
        rgb_photo.save(f'images_for_instagram//{image}', format='JPEG')


def upload_instagram():
    bot = Bot()
    bot.login(username=INSTAGRAM_LOGIN, password=INSTAGRAM_PASSWORD)
    images_for_instagram = os.listdir('images_for_instagram')
    for pic in images_for_instagram:
        bot.upload_photo(f'images_for_instagram//{pic}')


def main():
    os.makedirs('images_for_instagram', exist_ok=False)
    thumbnail_pic()
    upload_instagram()


if __name__ == '__main__':
    main()
