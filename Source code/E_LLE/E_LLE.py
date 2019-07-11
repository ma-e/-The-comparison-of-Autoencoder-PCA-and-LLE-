import numpy as np
from sklearn.manifold import LocallyLinearEmbedding
import matplotlib.pyplot as plt

X = np.array(np.loadtxt("EMA_100_16384_feature_matrix.txt")  )

def get_LLE_image(data):
    LLE = LocallyLinearEmbedding(n_components=2,n_neighbors=10)
    X_LLE = LLE.fit_transform(data)
    return X_LLE

X_ = get_LLE_image(X)

plt.scatter(X_[:, 0], X_[:, 1],c = "r")
if X.shape == (100,784):
    plt.xlabel('28 * 28 matrix', fontsize=14, color='r')
    plt.show()
else:
    plt.xlabel('128 * 128 matrix', fontsize=14, color='r')
    plt.show()
