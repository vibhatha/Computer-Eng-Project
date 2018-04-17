import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.misc


inputImage2read = np.loadtxt("input.txt", delimiter=',')


inputImage2read[inputImage2read==0] =-1

scipy.misc.imsave('input.jpg', inputImage2read)