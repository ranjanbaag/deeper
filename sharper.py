import os
import sys
from PIL import Image
from PIL import ImageFilter
from skimage.filters import laplace
from skimage.io import imread
#from skimage import data

#from skimage.color import rgb2gray
import numpy as np
from matplotlib import pylab
#from pylab import *
#from matplotlib.pyplot import *
#import matplotlib
#import matplotlib.pyplot as plt
# Open an already existing image
src_img = sys.argv[1]


def plot_image (image , title) :
    pylab.imshow(image), pylab.title(title,size=20), pylab.axis('off')
def rgb2gray (im) :
    return np.clip(0.2989 * im[...,0] + 0.5870 * im[...,1] + 0.1140 * im[...,2], 0, 1)

def ski_sharp ():
    im = rgb2gray(imread(src_img))
    im1 = np.clip(laplace(im) + im, 0, 1)
    pylab.figure(figsize=(20,30))
    pylab.subplot(211), plot_image(im, 'original image')
    pylab.subplot(212), plot_image(im1, 'sharpened image')
    pylab.tight_layout()
    pylab.show()


imageObject = Image.open(src_img);
imageObject.show();

# Apply sharp filter
sharpened1 = imageObject.filter(ImageFilter.SHARPEN);
sharpened2 = sharpened1.filter(ImageFilter.SHARPEN);

# Show the sharpened images
sharpened1.show();
sharpened2.show();




