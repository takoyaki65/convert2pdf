import os
from PIL import Image

images = []

if __name__ == '__main__':
    gif_fileName = 'output.gif'
    img_folder = './png/'
    extension = 'png'

    img_list = os.listdir(img_folder)
    img_list.sort()
    images = [Image.open(img_folder + j)
              for j in img_list if j.endswith(extension)]
    images[0].save(gif_fileName, save_all=True, append_images=images[1::5],
                   optimize=True, duration=20, loop=0)
