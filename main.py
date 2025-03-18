import math
from collections import Counter

def calculate_distance(vector1, vector2):
    value = 0
    vector1 = vector1.strip().split(",")
    vector2 = vector2.strip().split(",")

    for i in range(len(vector1)-1):
        value += (float(vector1[i]) - float(vector2[i]))**2
    return math.sqrt(value), vector1[-1], vector2[-1]

def knn(test_vector, data_set, k):
    if k <= 0:
        raise ValueError(f"k must be a positive integer. Received k={k}")

    list_of_distances = []
    for each_data in data_set:
        list_of_distances.append(calculate_distance(each_data, test_vector))
    list_of_distances.sort()
    most_common_label = Counter([each_k_data[1] for each_k_data in list_of_distances[:k]]).most_common()
    if len(most_common_label) > 1:
        most_common_label = most_common_label[0]
    return most_common_label[0][0]

def evaluate_accuracy(test_set, train_set, k):
    correct = 0
    for test_vector in test_set:
        predicted_label = knn(test_vector, train_set, k)
        true_label = test_vector.strip().split(",")[-1]
        if predicted_label == true_label:
            correct += 1
    accuracy = correct / len(test_set)
    return accuracy

with open('files\\iris.data', 'r') as file:
    irisData = file.readlines()
with open('files\\iris.test.data', 'r') as file:
    irisTestData = file.readlines()

# for k in range(1, 25):
#     accuracy = evaluate_accuracy(irisTestData, irisData, k)
#     print(f"Accuracy for k={k}: {accuracy:.2%}")


with open('files\\wdbc.data', 'r') as file:
    wdbc_data = file.readlines()
with open('files\\wdbc.test.data', 'r') as file:
    wdbc_test_data = file.readlines()


# for k in range(1, 25):
#     accuracy = evaluate_accuracy(wdbc_test_data, wdbc_data, k)
#     print(f"Accuracy for k={k}: {accuracy:.2%}")


accuracy = evaluate_accuracy(wdbc_test_data, wdbc_data, 3)
print(f"Accuracy for k={3}: {accuracy:.2%}")