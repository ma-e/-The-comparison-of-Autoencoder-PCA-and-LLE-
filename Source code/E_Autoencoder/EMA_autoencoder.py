#Name:E MA
# CS535 NLP
#05-03-2018

# using keras for my autoencoder project
from keras.layers import Input, Dense
from keras.models import Model
#using matplotlib to plot all the images
import matplotlib.pyplot as plt
#using sklearn to split data to test + train
from sklearn.model_selection import train_test_split


# this is the size of our encoded representations
encoding_dim = 8  # 32 floats -> compression of factor 24.5, assuming the input is 784 floats

# this is our input placeholder
input_img = Input(shape=(16384,))

# "encoded" is the encoded representation of the input
encoded = Dense(encoding_dim, activation='relu')(input_img)
# "decoded" is the lossy reconstruction of the input
decoded = Dense(16384, activation='sigmoid')(encoded)

# this model maps an input to its reconstruction
autoencoder = Model(input_img, decoded)

# this model maps an input to its encoded representation
encoder = Model(input_img, encoded)

# create a placeholder for an encoded (32-dimensional) input
encoded_input = Input(shape=(encoding_dim,))
# retrieve the last layer of the autoencoder model
decoder_layer = autoencoder.layers[-1]
# create the decoder model
decoder = Model(encoded_input, decoder_layer(encoded_input))

autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')


#using numpy
import numpy as np
#from sklearn.model_selection import KFold

#load our 88*784 data in
X = np.loadtxt("EMA_100_16384_feature_matrix.txt",delimiter = ' ')
print(X.shape)
#x_train,x_test=train_test_split(X,test_size=0.5,random_state=42)
#end with use slice to slice training data and test data.
#first 5 slice of image is our training set
x_train = X[:5]
print (x_train.shape)
#other 6 slice is our testing set
x_test = X[:10]
print(x_test.shape)

# if the vaulue is between 0-2 we dont need use astype to nomlize the data.
#x_train = x_train.astype('float32') / 255.
#x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape(((len(x_train)), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

print (x_train.shape)
print (x_test.shape)

# fit it to autoencoder
autoencoder.fit(x_train,x_train,
                epochs=5000,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test, x_test))


 # encode and decode some digits
# note that we take them from the *test* set
encoded_imgs = encoder.predict(x_test)
decoded_imgs = decoder.predict(encoded_imgs)

print (decoded_imgs.shape)

n = 5 # how many digits we will display
plt.figure(figsize=(20, 4))


m = 2 #how many rows do you want be in your plot
for i in range(n):
    # display original image
    ax = plt.subplot(m, int(n), i + 1)
    plt.imshow(x_test[i].reshape(128,128))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    #title for the plot
    if i == 2:
        ax.set_title('Autoencoder Original Face Images')
    
    # display the reconstructed image
    ax = plt.subplot(m, int(n), i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(128, 128))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    #set up title for my plot
    if i == 2:
        ax.set_title('Autoencoder Reconstructed Face Images')
plt.show()

