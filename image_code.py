import cv2
import numpy as np
import sys
import os
import fnmatch

def sharpen(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    new_image= cv2.filter2D(image, -1, kernel)
    cv2.imshow('Sharpened', new_image)
    cv2.waitKey(0)
    return new_image

def blur(image):
    kernels = [3, 5, 9, 13]
    for indx, k in enumerate(kernels):
        image_bl = cv2.blur(image,ksize= (k,k))
        cv2.imshow(str(k),image_bl)
        cv2.waitKey(0)
    return 

def resize(fname,width, height):
    image = cv2.imread(fname)
    cv2.imshow('Original image',image)
    cv2.waitKey(0)
    org_height, org_width = image.shape[0:2]
    print("Width: ",org_width)
    print("height: ",org_height)
    if org_width>=org_height:
        new_image = cv2.resize(image,(width,height))
    else:
        new_image = cv2.resize(image,(height,width))
    return fname, new_image

listOfFiles = os.listdir('.')
pattern = "*.jpg"
n =len(sys.argv)
if n==3:
    width = int (sys.argv[1])
    height = int(sys.argv[2])
else:
    width = 1280
    height = 960

#new folder if it does not exist
if not os.path.exists('new_folder'):
    os.makedirs('new_folder')

for filename in listOfFiles:
    if fnmatch.fnmatch(filename,pattern):
        filename, new_image = resize(filename,width, height)
        cv2.imwrite("new_folder\\"+ filename, new_image)


filename, new_image = resize('bird.jpg',1280, 960)

#cv2.imshow('resized image', new_image)
#cv2.waitKey(0)

#blur(new_image)

#image = sharpen(new_image)


#resize('bird.jpg',1280, 960)
