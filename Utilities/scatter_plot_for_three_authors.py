import matplotlib.pyplot as plt

import scipy.io as io
import numpy as np
from sklearn.manifold import TSNE
vectors = io.loadmat('vectors_three_authors.mat')
vector=vectors['paper_vectors']



model = TSNE(n_components=2, random_state=0)
np.set_printoptions(suppress=True)
X=[]

for i in range(3):
    X.append(model.fit_transform(vector[0][i]))
X=np.concatenate((X[0],X[1],X[2]))


a=([1]*(len(vector[0][0])))
b=([4]*(len(vector[0][1])))
c=([6]*(len(vector[0][2])))
Y=a+b+c

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)
plt.xlabel('Dimension_1')
plt.ylabel('Dimension_2')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())


plt.show()

