import numpy as np
import matplotlib.pyplot as plt

def local_regression(x_target, features, labels, bandwidth):
    x_target = [1, x_target] 
    features_expanded = [[1, i] for i in features]
    features_expanded = np.asarray(features_expanded)
    x_weights = (features_expanded.T) * np.exp(np.sum((features_expanded - x_target) ** 2, axis=1) / (-2 * bandwidth))
    regression_coefficients = np.linalg.pinv(x_weights @ features_expanded) @ x_weights @ labels @ x_target # @ symbol used for matrix multiplication
    return regression_coefficients 

def plot_local_regression(bandwidth):
    predictions = [local_regression(x_target, features, labels, bandwidth) for x_target in data_domain]
    plt.plot(features, labels, 'o', color='black')
    plt.plot(data_domain, predictions, color='red')
    plt.show()

features = np.linspace(-3, 3, num=1000)
data_domain = features
labels = np.log(np.abs(features ** 2 - 1) + .5)

plot_local_regression(10)
plot_local_regression(0.1)
