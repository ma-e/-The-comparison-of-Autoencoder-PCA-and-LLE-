#Author Name: E MA
#New Mexico Highlands University Computer Science department
#CS535 NLP Spring 2018 Final Project
#Professor: Dr.Gil Gallegos

#This project use a random image to generate 100 images with size 28*28.
#100 images = 25*scaled images + 25*translation images + 25*noise images + 25*rotated image
#Then flatten the image into a 100*784 matrix

#Let's start with import python libraries.
import numpy as np
from PIL import Image

#Genetate all the vraiables we need
size = (128,128)
value_start = 0
Noisy_value_end = 125
Noisy_step = 5
Rotated_degree_end = 365
Rotated_step = 15
translation_LR_value_start = -4
translation_UD_value_start = -5
translation_LR_value_end = 8
translation_UD_value_end = 8
translation_step = 1
scale_value_start = -0.45
scale_value_end = 0.175
scale_step = 0.025

Image_list = []

#Import a random image in, I am going to use my face image in this project.
Original_IMG = Image.open('EMA_original.png')

#Convert image to grey.
Grey_IMG = Original_IMG.convert("L")

#resize image to 28*28 pixels.
IMG= Grey_IMG.resize(size)
#New_IMG.save("EMA_New_28*28.png")

########################################################################################
#Get 25 noisy pictures with 25 diffrent noisy values from 0 to 125,step 5.
for values in range(value_start,Noisy_value_end,Noisy_step):
    New_IMG_array = np.asarray(IMG)
    Noisy_array = np.random.randint(-values,values+1,size)
    New_Noisy_IMG_array = np.add(Noisy_array,New_IMG_array)
    New_Noisy_IMG_array = Image.fromarray(np.uint8(New_Noisy_IMG_array))
    Noisy_image_list = "EMA_Noisy_Image_" + str(values) + ".png"
    New_Noisy_IMG_array.save(Noisy_image_list)
    Image_list.append(Noisy_image_list)

########################################################################################
#Get 25 rotated images with 25 diffrent degree values, values from 0 to 365 clockwise rotation, step 15.
for degrees in range(value_start,Rotated_degree_end,Rotated_step):
    Rotated_IMG = IMG.rotate(degrees)
    Rotated_image_list = "EMA_Rotated_Image_" + str(degrees) + ".png"
    Rotated_IMG.save(Rotated_image_list)
    Image_list.append(Rotated_image_list)

########################################################################################
#Get 25 translation images with 25 diffrent values. 12 left and right, 13 up and down
for LR_values in range(translation_LR_value_start,translation_LR_value_end,translation_step):
    IMG_LR = IMG.transform(IMG.size,Image.AFFINE,(1,0,LR_values,0,1,0))
    LR_translation_image_list = "EMA_Translation_Image_left_right_" + str(LR_values) + ".png"
    IMG_LR.save(LR_translation_image_list)
    Image_list.append(LR_translation_image_list)


########################################################################################
for UD_values in range(translation_UD_value_start,translation_UD_value_end,translation_step):
    IMG_UD = IMG.transform(IMG.size,Image.AFFINE,(1,0,0,0,1,UD_values))
    UD_translation_image_list = "EMA_Translation_Image_up_down_" + str(UD_values) + ".png"
    IMG_UD.save(UD_translation_image_list)
    Image_list.append(UD_translation_image_list)


########################################################################################
#Get 25 Scaled images with 25 diffrent decimal values.
def frange(start,stop,step):
    i = start
    while i < stop:
        yield i
        i += step
for Values in frange(scale_value_start,scale_value_end,scale_step):
    Scale_IMG = IMG.transform(IMG.size,Image.AFFINE,(1,Values,1,0,1,1))
    scaled_image_list = "EMA_Scaled_Image_" + str(Values) + ".png"
    Scale_IMG.save(scaled_image_list)
    Image_list.append(scaled_image_list)

########################################################################################
#This function flatten all the image to a 1D array
def flatten_image(pictures):
    IMG = Image.open(pictures)
    IMG = list(IMG.getdata())
    IMG_array = np.asarray(IMG)
    IMG_array = IMG_array.astype(np.float)/255
    flatten_IMG_array = IMG_array.flatten('F') #call flatten function in here
    return (flatten_IMG_array)

########################################################################################
#get feature matrix
Feature_matrix = []
for image in Image_list:
    matrix = flatten_image(image)
    Feature_matrix.append(matrix)
    Final_Feature_matrix = np.array(Feature_matrix)


########################################################################################
#save matrix to a file
if Final_Feature_matrix.shape == (100,784):
    np.savetxt("EMA_100_784_feature_matrix.txt",Final_Feature_matrix)
else:
    np.savetxt("EMA_100*16384_feature_matrix.txt",Final_Feature_matrix)





