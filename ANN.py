import numpy as np

# Input data
inputs = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
outputs = np.array(([92], [86], [89]), dtype=float)

# Normalize input data
inputs = inputs / np.amax(inputs)

# Normalize output data
outputs = outputs / 100

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Training parameters
epochs = 5000
learning_rate = 0.1

# Initialize weights and biases
hidden_layer_weights = np.random.uniform(size=(2, 3))
hidden_layer_biases = np.random.uniform(size=(1, 3))
output_layer_weights = np.random.uniform(size=(3, 1))
output_layer_biases = np.random.uniform(size=(1, 1))

# Training loop
for epoch in range(epochs):
    # Forward propagation
    hidden_layer_input = np.dot(inputs, hidden_layer_weights) + hidden_layer_biases
    hidden_layer_activation = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_activation, output_layer_weights) + output_layer_biases
    predicted_output = sigmoid(output_layer_input)

    # Compute gradients
    hidden_layer_gradient = sigmoid_derivative(hidden_layer_activation)
    output_layer_gradient = sigmoid_derivative(predicted_output)

    # Backpropagation
    output_error = outputs - predicted_output
    output_delta = output_error * output_layer_gradient

    hidden_layer_error = output_delta.dot(output_layer_weights.T)
    hidden_layer_delta = hidden_layer_error * hidden_layer_gradient

    # Update weights and biases
    output_layer_weights += hidden_layer_activation.T.dot(output_delta) * learning_rate
    output_layer_biases += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
    hidden_layer_weights += inputs.T.dot(hidden_layer_delta) * learning_rate
    hidden_layer_biases += np.sum(hidden_layer_delta, axis=0, keepdims=True) * learning_rate

# Display results
print("Input: \n" + str(inputs))
print("Actual Output: \n" + str(outputs))
print("Predicted Output: \n", predicted_output)
