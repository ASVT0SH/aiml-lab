from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split

iris_data = load_iris()

# Display the iris dataset
print("\n IRIS FEATURES \ TARGET NAMES: \n ", iris_data.target_names)
for i in range(len(iris_data.target_names)):
    print("\n[{0}]:[{1}]".format(i, iris_data.target_names[i]))

print("\n IRIS DATA :\n", iris_data["data"])

# Split the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(iris_data["data"], iris_data["target"], random_state=0)
print("\n Target :\n", iris_data["target"])
print("\n X TRAIN \n", X_train)
print("\n X TEST \n", X_test)
print("\n Y TRAIN \n", y_train)
print("\n Y TEST \n", y_test)

# Train and fit the model
k_neighbors_classifier = KNeighborsClassifier(n_neighbors=5)
k_neighbors_classifier.fit(X_train, y_train)

# Predicting from the model
new_sample = np.array([[5, 2.9, 1, 0.2]])
print("\n XNEW \n", new_sample)
prediction = k_neighbors_classifier.predict(new_sample)
print("\n Predicted target value: {}\n".format(prediction))
print("\n Predicted feature name: {}\n".format(iris_data["target_names"][prediction]))

# Display predictions for each test example
for i in range(len(X_test)):
    test_sample = X_test[i]
    new_test_sample = np.array([test_sample])
    prediction = k_neighbors_classifier.predict(new_test_sample)
    print("\n Actual : {0} {1}, Predicted :{2}{3}".format(
        y_test[i],
        iris_data["target_names"][y_test[i]],
        prediction,
        iris_data["target_names"][prediction]
    ))

print("\n TEST SCORE[ACCURACY]: {:.2f}\n".format(k_neighbors_classifier.score(X_test, y_test)))
