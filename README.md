# Space Instagram

These are three scripts:
- `fetch_spacex.py` download images from [SpaceX api](https://api.spacexdata.com/v3/launches)
- `fetch_hubble.py` download images from [Hubble api](http://hubblesite.org/api/v3/images?page=all)
- `upload_instagram.py` prepare downloaded images and upload they to instagram

### How to install


Images downloading does not require any keys. To upload images you need instagram login and password. Put them into
`.env` file, and assign login to the `INSTAGRAM_LOGIN` variable, assign password to the `INSTAGRAM_PASSWORD` variable.
It should look like this:

```
INSTAGRAM_LOGIN='Your_Login'
INSTAGRAM_PASSWORD='Your_Password'
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).