from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets

iris_data = datasets.load_iris()
print("Iris Data set loaded...")

x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.1)
# random_state=0

for i in range(len(iris_data.target_names)):
    print("Label", i, "-", str(iris_data.target_names[i]))

knn_classifier = KNeighborsClassifier(n_neighbors=2)
knn_classifier.fit(x_train, y_train)
y_pred = knn_classifier.predict(x_test)

print("Results of Classification using K-nn with K=1 ")

for r in range(0, len(x_test)):
    print(" Sample:", str(x_test[r]), " Actual-label:", str(y_test[r]), " Predicted-label:", str(y_pred[r]))

print("Classification Accuracy :", knn_classifier.score(x_test, y_test))
