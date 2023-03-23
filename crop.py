import os
from PIL import Image

save_path = "C:/Users/Owner/Code/py/datasets/runway/no_fod_cropped/"

path = "C:/Users/Owner/Code/py/datasets/runway/no_fod/"
for filename in os.listdir(path):
    
    im = Image.open(path + filename)

    h, w = im.size

    if h == 829 and w == 729:
        im.save(save_path + filename,"PNG")
        # print("NOT CROPPING, SAVING " + filename)
        continue


    left = 495.5
    top = 0
    right = 1324.5
    bottom = 729
    
    # Cropped image of above dimension
    # (It will not change original image)
    # print("CROPPING, SAVING " + filename)
    im1 = im.crop((left, top, right, bottom))
    im1.save(save_path + filename,"PNG")

    