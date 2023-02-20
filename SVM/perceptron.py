#!/usr/bin/env python
import numpy as np


def perceptron_learning_algorithm(X, y):
    # can also be initialized at zero.
    w = np.random.rand(3)
    misclassified_examples = predict(hypothesis, X, y, w)
    while misclassified_examples.any():
        x, expected_y = pick_one_from(misclassified_examples, X, y)
        # update rule
        w = update_rule(expected_y, w, x)
        misclassified_examples = predict(hypothesis, X, y, w)
    return w


def update_rule(expected_y, w, x):
    w = w + x * expected_y
    return w


def hypothesis(x, w):
    return np.sign(np.dot(w, x))


# Make predictions on all data points
# and return the ones that are misclassified.
def predict(hypothesis_function, X, y, w):
    predictions = np.apply_along_axis(hypothesis_function, 1, X, w)
    misclassified = X[y != predictions]
    return misclassified


# Pick one misclassified example randomly
# and return it with its expected label.
def pick_one_from(misclassified_examples, X, y):
    np.random.shuffle(misclassified_examples)
    x = misclassified_examples[0]
    index = np.where(np.all(X == x, axis=1))
    return x, y[index]


from succinctly.datasets import get_dataset, linearly_separable as ls

np.random.seed(88)

X, y = get_dataset(ls.get_training_examples)
print(X.shape)
print(y.shape)

# transform X into an array of augmented vectors.
X_augmented = np.c_[np.ones(X.shape[0]), X]
print(X_augmented.shape)

w = perceptron_learning_algorithm(X_augmented, y)

# [-44.35244895 1.50714969 5.52834138]
print(w)

x = np.array([1, 2, 7])

expected_y = -1

w = np.array([4, 5, 3])

print(hypothesis(w, x))  # The predicted y is 1.

w = update_rule(expected_y, w, x)  # we apply the update rule.

# The predicted y is -1.
print(hypothesis(w, x))
