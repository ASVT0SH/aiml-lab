import csv
import random
import math

def load_csv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset

def split_dataset(dataset, split_ratio):
    train_size = int(len(dataset) * split_ratio)
    train_set = dataset[:train_size]
    test_set = dataset[train_size:]
    return [train_set, test_set]

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_stdev(numbers):
    avg = calculate_mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / (len(numbers) - 1)
    return math.sqrt(variance)

def summarize_by_class(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        class_label = vector[-1]
        if class_label not in separated:
            separated[class_label] = []
        separated[class_label].append(vector)
    
    summaries = {}
    for class_value, instances in separated.items():
        summaries[class_value] = [(calculate_mean(attribute), calculate_stdev(attribute)) for attribute in zip(*instances)][:-1]
    
    return summaries

def calculate_probability(x, mean, stdev):
    exponent = math.exp((-(x - mean) ** 2) / (2 * (stdev ** 2)))
    return (1 / ((2 * math.pi) ** (1 / 2) * stdev)) * exponent

def predict_class(summaries, input_vector):
    probabilities = {}
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = 1
        for i in range(len(class_summaries)):
            mean, stdev = class_summaries[i]
            x = input_vector[i]
            probabilities[class_value] *= calculate_probability(x, mean, stdev)
    
    best_label, best_probability = None, -1
    for class_value, probability in probabilities.items():
        if best_label is None or probability > best_probability:
            best_probability = probability
            best_label = class_value
    
    return best_label

def get_predictions(summaries, test_set):
    predictions = []
    for i in range(len(test_set)):
        result = predict_class(summaries, test_set[i])
        predictions.append(result)
    
    return predictions

def calculate_accuracy(test_set, predictions):
    correct = sum(1 for i in range(len(test_set)) if test_set[i][-1] == predictions[i])
    return (correct / len(test_set)) * 100.0

filename = 'pima-indians-diabetes.csv'
split_ratio = 0.67
dataset = load_csv(filename)
training_set, test_set = split_dataset(dataset, split_ratio)
summaries = summarize_by_class(training_set)
predictions = get_predictions(summaries, test_set)
print("\nPredictions:\n", predictions)
accuracy = calculate_accuracy(test_set, predictions)
print('Accuracy ', accuracy)
