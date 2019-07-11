Spring 2018 CS535 Final Project: The comparison of Autoencoder, PCA and LLE 

New Mexico Highlands University, Computer Science 

# Experiments 

In this project, i took my face picture and convert it to gray, resize it into size 28*28 and 128*128. After this, i created 100 images based on each of them, which including 25 different noisy values, 25 different rotating degrees, 25 translation degrees, and 25 scale degrees. Finally i flatten those 200 images into a 2D array, which are 100*784 and 100*16834. Then i applied each of them to Autoencoder, PCA and LLE, plot the original images and reconstructed images,  therefore, the visualize images will help us to find out the different between  each of them. 

 

# Results 

Autoencoder 

5000 epochs, 8 dimensions, image size 28*28, Error: 0.27079198806833412 

 

5000 epochs, 8 dimensions, image size 128*128, Error: 0.4015 

 

PCA (Principal Components Analysis) 

Images size 28 * 28, dimension 8, Error: 0.5296762000485804 

 

 

 

Image size 128*128, dimension 8, Error: 0.063106548868753401 

 

LLE (Locally Linear Embedding) 

100 * 784 (left) , Reconstruction error: 0.0479929 

100*16384(right), Reconstruction error: 1.93334e-06 

  

# Question answers 

1.Why do LLE and AE work well on nonlinear datasets? 

A data set is neither linear non nonlinear. AE are a family of neural networks for which the input is the same as the output. They work by compressing the input into a latent-space representation, and then reconstructing the output from this representation.LLE was presented at approximately the same time as Isomap. It has several advantages over Isomap, including faster optimization when implemented to take advantage of sparse matrix algorithms, and better results with many problems.LLE and AE are more complex, but they can preserve the structure and relationships in a high dimensional space when data are mapped into a low-dimensional space. 

 

2.Discuss what a data manifold is? 

A manifold is a topological space that locally resembles Euclidean space near each point. More precisely, each point of an n-dimensional manifold has a neighbourhood that is homeomorphic to the Euclidean space of dimension n. In this more precise terminology, a manifold is referred to as an n-manifold.A manifold is an object of dimensionality d that is embedded in some higher dimensional space. Imagine a set of points on a sheet of paper. If we crinkle up the paper, the points are now in 3 dimensions. Many manifold learning algorithms seek to "unwrinkle" the sheet of paper to put the data back into 2 dimensions. Even if we aren't concerned with overfitting our model, a non-linear manifold learner can produce a space that makes classification and regression problems easier. 

  

3.Discuss how an AE and LLE are able to reduce the dimensionality of the MD. 

AE is a family of neural networks for which the input is the same as the output*. They work by compressing the input into a latent-space representation, and then reconstructing the output from this representation.LLE it works by first measuring how each training instance linearly relates to its 

Closest neighbors(c.n.),and then looking for a low-dimensional representation of the training set where these local relationships are best preserved(more details shortly).This makes it particularly good at Unrolling twisted manifolds,especiallywhenthereisnottoomuchnoise. 

  

4.Why might face data be reduced to such low dimensionality d from the original D? 

(1)The pixels on the image borders are almost always white, so you could completely drop these pixels from the training set without losing much information. 

(2)A lot of the pixels are utterly unimportant for the classification tasks. 

(3) Moreover, two neighboring pixels are often highly correlated, so we can  merge them into a single pixel (e.g., by taking the mean of the two pixel intensities), we will not lose much information. 

  

5.How might you determine whether a dataset is linear or nonlinear? 

There are many ways to do this.In our case, we applied data to Autoencoder and PCA, get the reconstruction error results. After this, compare the errors between them. If the errors are very similar, then it is linear data set. On the contrary, if the errors are quite different, then the data set is non-linear. 

  

6.Does the enlarging of the images from 28*28 to 128*128 improve your overall reconstruction? Why? Why not? 

Yes, it does.Comparing the root-mean-square error (RMSE) of AE,PCA and LLE, we can see LLE and AE both of them works better at reconstruction than the PCA.Specialty AE did very good job on denoisy as you can see.  

References 

[1] https://en.wikipedia.org/wiki/Manifold 

[2]https://en.wikipedia.org/wiki/Nonlinear_dimensionality_reduction#Locally-linear_embedding 

[3]https://en.wikipedia.org/wiki/Autoencoder 

[4]https://en.wikipedia.org/wiki/Principal_component_analysis 

 

 
