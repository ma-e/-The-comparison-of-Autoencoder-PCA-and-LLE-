# Author: E MA
# 05-02-2018
# PCA code = original + reconstruted

# import all the licbraries in here
#use numpy
import numpy as np

size = 128,128

import matplotlib.pyplot as plt
#use Sklearn
import sklearn.decomposition
# use sklran PCA
from sklearn.decomposition import PCA
# Apply PCA
pca = sklearn.decomposition.PCA()


#This function plot our data, I did not use it
def plot_image(image,n,m):
    plot.imshow(image.reshape(n,m), cmap = "Greys", interpolation = 'nearest')
    plot.axis("off")
    plot.show()

#load our original data in, out data shape is 88*784
X = np.loadtxt("EMA_100*16384_feature_matrix.txt",delimiter = ' ')

#Centerd the data
X_center = X - X.mean()

#Fit the centerd data to pca
pca.fit(X_center)

# Transform labels to normalized encoding.
x = pca.transform(X_center)
# Transform labels back to original encoding.
X_new = pca.inverse_transform(x)


#This is the first way to Find the right dimension, from book Chapter 8
def find_dimensions_1(): #294
    pca = PCA()
    pca.fit(X_center)
    cumsum = np.cumsum(pca.explained_variance_ratio_)
    d1 = np.argmax(cumsum >= 0.95) + 1
    return d1
d1 = find_dimensions_1()
print (d1) #d = 8

#This is the second way to find right dimension, from book Cgapter 8
def find_dimensions_2():
    pca = PCA(n_components = 0.95)
    x_reduced = pca.fit_transform(X_center)
    d2 = (len(pca.components_))
    return d2
d2 = find_dimensions_2()
print (d2)


#This function is to get error betweent original data and reconstructed data
def get_error():
    #use original - reconstructed
    error = X_center - X_new
    print ("The error between orignal and PCA shape is {}".format(error.shape))
    #save error to a file
    save_error = np.savetxt('error.txt', error, fmt = '%.g')
    return error
error = get_error()

#This function is to get the explained cariance ratio
def get_explained_variance_ratio():
    pca = PCA(n_components = 3)
    x2d = pca.fit_transform(X_center)
    return (pca.explained_variance_ratio_)
ratio = get_explained_variance_ratio()
print (ratio)
print ("The sum of the expalined variance ratio is {}".format(sum(ratio)))



n = 10 # how many digits we will display
plt.figure(figsize=(20, 4))
m = 10
for i in range(n):
    # display original image
    ax = plt.subplot(m, int(n), i + 1)
    plt.imshow(X[i].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    if (i ==  5):
        ax.set_title('PCA Original Face Images of E')

    
    ax = plt.subplot(m, int(n), i + 1 + n)
    plt.imshow(X[i+10].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    ax = plt.subplot(m, int(n), i + 1 + 2*n)
    plt.imshow(X[i+20].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    ax = plt.subplot(m, int(n), i + 1 + 3*n)
    plt.imshow(X[i+30].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    ax = plt.subplot(m, int(n), i + 1 + 4*n)
    plt.imshow(X[i+40].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    ax = plt.subplot(m, int(n), i + 1 + 5*n)
    plt.imshow(X[i+50].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    ax = plt.subplot(m, int(n), i + 1 + 6*n)
    plt.imshow(X[i+60].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    ax = plt.subplot(m, int(n), i + 1 + 7*n)
    plt.imshow(X[i+70].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax = plt.subplot(m, int(n), i + 1 + 8*n)
    plt.imshow(X[i+80].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax = plt.subplot(m, int(n), i + 1 + 9*n)
    plt.imshow(X[i+90].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

plt.show()

for j in range(n):
    #plot reconstruted image
    ax = plt.subplot(m, n, j + 1)
    plt.imshow(X_new[j].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    if (j == 5):
        ax.set_title('PCA Reconstructed Face Images of E')
    
    ax = plt.subplot(m, int(n), j + 1 + n)
    plt.imshow(X_new[j+10].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    ax = plt.subplot(m, int(n), j + 1 + 2*n)
    plt.imshow(X_new[j+20].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    ax = plt.subplot(m, int(n), j + 1 + 3*n)
    plt.imshow(X_new[j+30].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    ax = plt.subplot(m, int(n), j + 1 + 4*n)
    plt.imshow(X_new[j+40].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    ax = plt.subplot(m, int(n), j + 1 + 5*n)
    plt.imshow(X_new[j+50].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    ax = plt.subplot(m, int(n), j + 1 + 6*n)
    plt.imshow(X_new[j+60].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    ax = plt.subplot(m, int(n), j + 1 + 7*n)
    plt.imshow(X_new[j+70].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax = plt.subplot(m, int(n), j + 1 + 8*n)
    plt.imshow(X_new[j+80].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax = plt.subplot(m, int(n), j + 1 + 9*n)
    plt.imshow(X_new[j+90].reshape(size))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

plt.show()




