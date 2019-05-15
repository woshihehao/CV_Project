import math
import cv2
import numpy as np
import parameters


def choose_pair():
    """
    Give user a choice of pair of images and set the best parameters for each pair,
    for low-pass and high-pass filters: height, width and sigma. 
    Pass images to the Gaussian filter function and return 2 images and 2 kernels.
    """
    print('This program is creating hybrid images from a given pair of images.\n'\
          'Choose a pair of images you would like to make a hybrid image from:\n'\
          '1. bicycle + motorcycle\n'\
          '2. dog + cat\n'\
          '3. Marylin Monroe + Albert Einstein\n'\
          '4. bird + plane\n'\
          '5. fish + submarine\n'\
          '6. eye + snail\n'\
          '7. kitten + moon')
    path = '/Users/frank/PycharmProjects/hybrid-images'
    path = path + '/' + 'pictures'
    choice = int(input('Enter a number from 1 to 7: \n'))
    while choice not in range(1,8):
        choice = int(input('The value you entered is invalid, try again: /n'))    
    if choice == 1:  
        img1 = cv2.imread(path + '/' + 'motorcycle.bmp')
        img2 = cv2.imread(path + '/' + 'bicycle.bmp')
        h1 = w1 = h2 = w2 = 11
        s1 = s2 = 2
    elif choice == 2: 
        img1 = cv2.imread(path + '/' + 'dog.bmp')
        img2 = cv2.imread(path + '/' + 'cat.bmp')
        h1 = w1 = h2 = w2 = 21
        s1 = s2 = 7
    elif choice == 3:
        img1 = cv2.imread(path + '/' + 'marilyn.bmp')
        img2 = cv2.imread(path + '/' + 'einstein.bmp')
        h1 = w1 = 23
        h2 = w2 = 11
        s1 = 4
        s2 = 2
    elif choice == 4:
        img1 = cv2.imread(path + '/' + 'bird.bmp')
        img2 = cv2.imread(path + '/' + 'plane.bmp')
        h1 = w1 = 6
        h2 = w2 = 21
        s1 = 2
        s2 = 8
    elif choice == 5:
        img1 = cv2.imread(path + '/' + 'submarine.bmp')
        img2 = cv2.imread(path + '/' + 'fish.bmp')
        h1 = w1 = 29
        h2 = w2 = 17
        s1 = 5
        s2 = 3
    elif choice == 6:
        img1 = cv2.imread(path + '/' + 'snail.png')
        img2 = cv2.imread(path + '/' + 'eye.png')
        h1 = w1 = 16
        h2 = w2 = 25
        s1 = 4
        s2 = 10
    elif choice == 7:
        img1 = cv2.imread(path + '/' + 'moon.png')
        img2 = cv2.imread(path + '/' + 'kitten.png')
        h1 = w1 = 5
        h2 = w2 = 21
        s1 = 1
        s2 = 5
    #convert the images into floating points data type    
    img1 = img1.astype('float64')
    img2 = img2.astype('float64')
    param = [h1,w1,s1,h2,w2,s2]
    #change parameters to user chosen if such were declared in parameters module   
    for i in range(len(param)):
        if parameters.values[i] != 0:
            param[i] = parameters.values[i]
    #create Gaussian filters for each image
    kernel1 = create_gaussian_filter((param[0], param[1]), param[2])
    kernel2 = create_gaussian_filter((param[3], param[4]), param[5])  
    return img1, img2, kernel1, kernel2

def create_gaussian_filter(size, sigma):
    """
    Create Gaussian filter kernel.
    Take template's (kernel's) size and sigma as arguments.
    Return the kernel.
    """
    h = size[0]             #height of the template
    w = size[1]             #width of the template 
    if h % 2 == 0: h += 1   #add 1 if dimensions are even
    if w % 2 == 0: w += 1
    x = math.floor(h/2)
    y = math.floor(w/2)    
    sum = 0
    #create our template
    template = np.zeros((h,w))
    #fill the template in with the numbers from Gaussian distribution
    for i in range(h):
        for j in range(w):
            template[i,j] = math.exp(-((((j-x)**2)+((i-y)**2))/(2*(sigma**2))))
            sum = sum + template[i,j]
    #normalise the numbers
    gaussian_filter = template/sum
    return gaussian_filter