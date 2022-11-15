import requests
from PIL import Image

x = requests.get('https://www.google.com.ua/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png').content
with open('google_image.jpg', 'wb') as handler:
    handler.write(x)
print('image downloaded')
img = Image.open('google_image.jpg')
img.show()
