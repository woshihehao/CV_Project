import gaussian
import convolution
import numpy as np
import cv2

def main():
    """The main function of the program."""
    #get images and kernels for convolution
    img1, img2, kernel1, kernel2 = gaussian.choose_pair() 
    #create a low-pass filter of the first image
    low_pass = convolution.check_image(img1, kernel1)
    #create a low-pass filter of the second image
    low_pass_temp = convolution.check_image(img2, kernel2)
    #create a high-pass filter of the second image
    high_pass = cv2.subtract(img2, low_pass_temp)
    #add low-pass and high-pass filter to make a hybrid image
    hybrid = cv2.add(low_pass, high_pass)
    visualise(hybrid)
   
def visualise(hybrid):
    """Visualise hybrid image in 4 different scales."""
    h = hybrid.shape[0]
    w = hybrid.shape[1]
    #set space between images
    space = int(w/30)
    #set a new image with white background to put 4 scaled images onto
    output = np.zeros((h, int(2*w), 3)) + 255
    y = 0
    for i in range(4):
        image = cv2.resize(hybrid, (w, h), interpolation = cv2.INTER_CUBIC)
        h, w, d = image.shape
        output[0:h, y:y+w] = image
        y = y + w + space
        w = int(w/2)
        h = int(h/2)
    cv2.imwrite('hybrid.png', output)
    
if __name__ == "__main__":
    main()