import math
import numpy as np
import cv2

def check_image(image, kernel):
    """
    Check if the image is colour or grayscale.
    Pass the image to the convolution function.
    Return the convoluted image.
    """
    if len(image.shape) == 3:
    #operate separately on each channel if image is a colour image
        b,g,r = cv2.split(image)
        blue = convolution(b, kernel)
        green = convolution(g, kernel)        
        red = convolution(r, kernel)
        new_im = cv2.merge((blue, green, red))
    elif len(image.shape) == 0:
        new_im = convolution(image, kernel)
    return new_im

def convolution(image, kernel):  
    """
    Convolute image.
    Take image and kernel as arguments to convolute.
    Return convoluted image.
    """
    kh = kernel.shape[0]        #kernel height
    kw = kernel.shape[1]        #kernel width
    khm = math.floor(kh/2)      #half of kernel height
    kwm = math.floor(kw/2)      #half of kernel width
    ih = image.shape[0]         #image height
    iw = image.shape[1]         #image width
    #make an image frameless
    im_temp = np.zeros((ih+kh, iw+kw))
    im_temp[khm:ih+khm, kwm:iw+kwm] = image
    im_temp[0:khm, kwm:iw+kwm] = image[0:khm, :]
    im_temp[ih+khm:ih+2*khm, kwm:iw+kwm] = image[ih-khm:ih, :]
    im_temp[khm:ih+khm:, 0:kwm] = image[:, 0:kwm]
    im_temp[khm:ih+khm, iw+kwm:iw+2*kwm] = image[:, iw-kwm:iw]
    #create a new image to store the convoluted image
    convoluted = np.zeros((ih, iw))
    #convolute an image with a flipped kernel
    for i in range(ih):
        for j in range(iw):
            weights = 0
            for k in range(kh):
                for l in range(kw):
                    kk = kh - 1 - k
                    ll = kw - 1 - l
                    weights = weights + im_temp[i+k, j+l] * kernel[kk,ll] 
            convoluted[i,j] = weights
    return convoluted