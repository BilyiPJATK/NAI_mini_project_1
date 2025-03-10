import math


def calculateDistances(training_vectors, test_vectors):
    value = 0;
    for i in range(len(training_vectors)):
        value += (training_vectors[i] - test_vectors[i])**2
    return math.sqrt(value)

with open('files\\iris.data', 'r') as file:
    irisData = file.readlines()

with open('files\\iris.test.data', 'r') as file:
    irisTestData = file.readlines()

print(irisData)
print(irisTestData)