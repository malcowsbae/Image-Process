# Using Pillow 
from PIL import Image,ImageOps
import PIL
import os

#Going through all the files ins the current DIR
path = os.getcwd()+'/Grey Scale Img'
try:
    os.mkdir(path)
except FileExistsError:
    print('Output folder from a previous session still exists !')
    print('Please Delete or rename the Grey Scale Folder to proceed ')
    input()
    exit()
for fileName in os.listdir(os.getcwd()):
    #Igoring the script
    if(fileName != 'convert_to_grayscale.py'):
        try:
            og_image = Image.open(str(fileName))
            print('Converting : ',end='')
            print(fileName[0:len(fileName)-4])
        except PIL.UnidentifiedImageError:
            continue
        except PermissionError:
            continue
        # applying grayscale method
        gray_image = ImageOps.grayscale(og_image)
        gray_image.save('.\\Grey Scale Img\\'+fileName[0:len(fileName)-4]+'_GreyScale'+'.png')
#gray_image.show()
