Spring 2018 CS535 Final Project: The comparison of Autoencoder, PCA and LLE 

New Mexico Highlands University, Computer Science 

# Experiments 

## Sources
A face picture. 

## Steps
#### step 1 Convert it to gray 
#### step 2 Resize it to ```28*28``` and ```128*128```
#### step 3 Generate 100 different images for each image of step 2, 
###### a. 25 different noisy values 
###### b. 25 different rotating degrees
###### c. 25 different translation degrees
###### d. 25 different scale degrees
#### step 4 Flatten all images into a 2D array, which are ```100*784``` and ```100*16834```
#### step 5 Applied each of them to Autoencoder, PCA and LLE
#### step 6 Plot the original images and reconstructed images

 

# Results 

### Autoencoder 

#### 5000 epochs, 8 dimensions, image size '''28*28''', Error: 0.27079198806833412 

![alt text][logo]
[logo]: https://github.com/ma-e/The-comparison-of-Autoencoder-PCA-and-LLE/blob/master/img/Autoencoder%2028*28.png 

#### 5000 epochs, 8 dimensions, image size '''128*128''', Error: 0.4015 

![alt text][logo]
[logo]: https://github.com/ma-e/The-comparison-of-Autoencoder-PCA-and-LLE/blob/master/img/Autoencoder%20128*128.png

### PCA (Principal Components Analysis) 

#### Images size 28 * 28, dimension 8, Error: 0.5296762000485804 

![alt text][original]
[original]: https://github.com/ma-e/The-comparison-of-Autoencoder-PCA-and-LLE/blob/master/img/PCA%20original.png

![alt text][recontructed]
[recontructed]: https://github.com/ma-e/The-comparison-of-Autoencoder-PCA-and-LLE/blob/master/img/PCA%20reconstructed.png 

#### Image size 128*128, dimension 8, Error: 0.063106548868753401 

 ![alt text][128o]
[128o]: https://github.com/ma-e/The-comparison-of-Autoencoder-PCA-and-LLE/blob/master/img/PCA%20128*128%20Original.png 

 ![alt text][128r]
[128r]: https://github.com/ma-e/The-comparison-of-Autoencoder-PCA-and-LLE/blob/master/img/PCA%20128*128.png 
### LLE (Locally Linear Embedding) 

#### 100 * 784 (left) , Reconstruction error: 0.0479929 

 ![alt text][p2]
[p2]: https://github.com/ma-e/The-comparison-of-Autoencoder-PCA-and-LLE/blob/master/img/LLE%2028*28.png 


#### 100*16384(right), Reconstruction error: 1.93334e-06 

 ![alt text][p1]
[p1]: https://github.com/ma-e/The-comparison-of-Autoencoder-PCA-and-LLE/blob/master/img/LLE%20128*128.png 
  

# Question answers 

### Why do LLE and AE work well on nonlinear datasets? 

A data set is neither linear non nonlinear. AE are a family of neural networks for which the input is the same as the output. They work by compressing the input into a latent-space representation, and then reconstructing the output from this representation.LLE was presented at approximately the same time as Isomap. It has several advantages over Isomap, including faster optimization when implemented to take advantage of sparse matrix algorithms, and better results with many problems.LLE and AE are more complex, but they can preserve the structure and relationships in a high dimensional space when data are mapped into a low-dimensional space. 

 

### Discuss what a data manifold is? 

A manifold is a topological space that locally resembles Euclidean space near each point. More precisely, each point of an n-dimensional manifold has a neighbourhood that is homeomorphic to the Euclidean space of dimension n. In this more precise terminology, a manifold is referred to as an n-manifold.A manifold is an object of dimensionality d that is embedded in some higher dimensional space. Imagine a set of points on a sheet of paper. If we crinkle up the paper, the points are now in 3 dimensions. Many manifold learning algorithms seek to "unwrinkle" the sheet of paper to put the data back into 2 dimensions. Even if we aren't concerned with overfitting our model, a non-linear manifold learner can produce a space that makes classification and regression problems easier. 

  

### Discuss how an AE and LLE are able to reduce the dimensionality of the MD. 

AE is a family of neural networks for which the input is the same as the output*. They work by compressing the input into a latent-space representation, and then reconstructing the output from this representation.LLE it works by first measuring how each training instance linearly relates to its 

Closest neighbors(c.n.),and then looking for a low-dimensional representation of the training set where these local relationships are best preserved(more details shortly).This makes it particularly good at Unrolling twisted manifolds,especiallywhenthereisnottoomuchnoise. 

  

### Why might face data be reduced to such low dimensionality D from the original D? 

* The pixels on the image borders are almost always white, so you could completely drop these pixels from the training set without losing much information. 

* A lot of the pixels are utterly unimportant for the classification tasks. 

* Moreover, two neighboring pixels are often highly correlated, so we can  merge them into a single pixel (e.g., by taking the mean of the two pixel intensities), we will not lose much information. 

  

### How might you determine whether a dataset is linear or nonlinear? 

There are many ways to do this.In our case, we applied data to Autoencoder and PCA, get the reconstruction error results. After this, compare the errors between them. If the errors are very similar, then it is linear data set. On the contrary, if the errors are quite different, then the data set is non-linear. 

  

### Does the enlarging of the images from 28*28 to 128*128 improve your overall reconstruction? Why? Why not? 

Yes, it does.Comparing the root-mean-square error (RMSE) of AE,PCA and LLE, we can see LLE and AE both of them works better at reconstruction than the PCA.Specialty AE did very good job on denoisy as you can see.  

# References 

[1] https://en.wikipedia.org/wiki/Manifold 

[2]https://en.wikipedia.org/wiki/Nonlinear_dimensionality_reduction#Locally-linear_embedding 

[3]https://en.wikipedia.org/wiki/Autoencoder 

[4]https://en.wikipedia.org/wiki/Principal_component_analysis 

 

 
