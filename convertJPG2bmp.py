from PIL import Image

if __name__ == '__main__':
    img = Image.open("night_beach.jpg")
    img.save("night_beach.bmp", "bmp")
