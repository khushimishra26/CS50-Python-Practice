#Blurring an image
from PIL import Image, ImageFilter

before = Image.open("stars.jpg")
after = before.filter(ImageFilter.BoxBlur(5))
after.save("output.jpg")
