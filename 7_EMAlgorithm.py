import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics as metrics
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture

target_names = [0, 1, 2]

def map_labels(label_list):
    unique_labels = []
    for label in label_list:
        if label not in unique_labels:
            unique_labels.append(label)
    for i in range(len(label_list)):
        pos = unique_labels.index(label_list[i])
        label_list[i] = target_names[pos]
    return label_list

def plot_graph(layout, title, scatter_type, target_labels):
    plt.subplot(layout[0], layout[1], layout[2])
    if scatter_type == 1:
        plt.scatter(X.Sepal_Length, X.Sepal_Width, c=colormap[target_labels], s=40)
    else:
        plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[target_labels], s=40)
    plt.title(title)

def train_and_plot(model):
    model_instance = model(3)
    model_instance.fit(X)
    plt.figure()
    colormap = np.array(['red', 'lime', 'black'])
    plot_graph([1, 2, 1], 'Real Classification', 0, y.Targets)
    model_name = 'KMeans' if model == KMeans else 'GaussianMixture'
    predicted_labels = model_instance.predict(X)
    plot_graph([1, 2, 2], model_name, 0, predicted_labels)
    plt.show()
    mapped_labels = map_labels(predicted_labels)
    print("\nPredicted Labels: \n", mapped_labels)
    print("Accuracy ", metrics.accuracy_score(y, mapped_labels))
    print("Confusion Matrix ", metrics.confusion_matrix(y, mapped_labels))

iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
y = pd.DataFrame(iris.target, columns=['Targets'])

plt.figure()
colormap = np.array(['red', 'lime', 'black'])
train_and_plot(KMeans)
train_and_plot(GaussianMixture)
