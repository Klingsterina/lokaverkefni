import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Hledur fashion mnist gagnasettid
#hafid path sem toma strenginn ef skrain er i somu moppu og tid erud ad vinna i
def load_f_mnist(path, kind="train"):
    import os
    import gzip
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path, "%s-labels-idx1-ubyte.gz" % kind)
    images_path = os.path.join(path, "%s-images-idx3-ubyte.gz" % kind)
    with gzip.open(labels_path, "rb") as lbpath:
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8, offset=8)
    with gzip.open(images_path, "rb") as imgpath:
        images = np.frombuffer(imgpath.read(), dtype=np.uint8, offset=16).reshape(len(labels), 784)
    return images, labels

    #Hledur mnist gagnasettid
    #hafid path sem toma strenginn ef skrain er i somu moppu og tid erud ad vinna i
def load_mnist(path, kind="train"):
    import os
    import gzip
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path, "mnist_%s-labels-idx1-ubyte.gz" % kind)
    images_path = os.path.join(path, "mnist_%s-images-idx3-ubyte.gz" % kind)
    with gzip.open(labels_path, "rb") as lbpath:
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8, offset=8)
    with gzip.open(images_path, "rb") as imgpath:
        images = np.frombuffer(imgpath.read(), dtype=np.uint8, offset=16).reshape(len(labels), 784)
    return images, labels

X, labels = load_mnist("lokaverk") #mnist
X_f, labels_f = load_f_mnist("lokaverk") #fashion mnsist

def plot_one(X,i):
    one = X[1].reshape(28, 28)
    fig = plt.figure
    plt.imshow(one, cmap="gray")
    plt.show()

plot_one(X,10)
plot_one(X_f,101)

def run_kmeans(data, k, max_iter=100):
    return

def assign(data, centroids):
    return

def update(data,assignments, centroids):
    return

# her erum vid ad keyra kmeans a fashion mnist gagnasettid
assignments = run_kmeans(X_f,10)
assignments_orig = run_kmeans(X,10)

def plot_result(X,clust, output):
    plt.figure(figsize=(20, 20))
    for i in range(1, 101):
        plt.subplot(10, 10, i)
        plt.imshow(X[np.where(output == clust)][i].reshape(28, 28), cmap=plt.cm.binary)
        plt.show()


#her eru fyrstu 100 stokin sem vid reikniritið mitt flokkaði i flokk 2.
# sjaum að þetta er líklegast kjóla flokkurinn en eitthvað af bolum og buxum␣hafa dottið með. Smá óhjákvæmilegt.
plot_result(X_f,2,assignments)

#her eru fyrstu 100 stokin sem vid reikniritið mitt flokkaði i flokk 3 i␣upprunalega mnist (tölurnar þeas).
# sjaum að þetta er talan 6. Hinsvegar hafa laumast inn einn tvistur og nokkrir␣fjarkar og slíkt. Samt nokkuð gott.
plot_result(X,3,assignments_orig)

#ef assignments eru lokagiskid okkar og labels eru retta svarid sem vid faum␣tegar vid tokum inn gognin
#og cat er einhver flokkur
#tetta fall tetta fall okkur besta gisk a hvada flokkur tetta er i labels.
def get_real_category(assignment,labels,cat):
    a = labels[np.where(assignment==cat)]
    unique, counts = np.unique(a, return_counts=True)
    return dict(zip(unique, counts))

#get_real_category(assignments_orig,labels,1)
d = get_real_category(assignments_orig,labels,1)
print(d)

#Sjaum ad ofan ad okkar flokkur 1 er i raunveruleikanum flokkur 8.
#sem tydir ad vid flokkum í flokk 1 með um 72% nákvæmni
d[8]/sum(d.values())

plot_result(X,1,assignments_orig)
