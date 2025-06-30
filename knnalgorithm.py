import csv
from math import sqrt
from collections import Counter
dataset = []
with open('diabetes.csv', 'r') as file:
    f = csv.reader(file)
    next(f) 
    for row in f:
        dataset.append([float(value) for value in row])
split = int(0.7 * len(dataset))
traindata = dataset[:split]
testdata = dataset[split:]
def euclidean(p1, p2):
    dis = 0.0
    for i in range(len(p1) - 1):
        dis += (p1[i] - p2[i]) ** 2
    return sqrt(dis)
def getneighbors(traindata, testpoint, k):
    distances = []
    for trainpoint in traindata:
        dist = euclidean(testpoint, trainpoint)
        distances.append((trainpoint, dist))
    distances.sort(key=lambda x: x[1])
    neighbors = [distances[i][0] for i in range(k)]
    return neighbors
def outcome(traindata, testpoint, k):
    neighbors = getneighbors(traindata, testpoint, k)
    outcomes = [neighbor[-1] for neighbor in neighbors]
    prediction = Counter(outcomes).most_common(1)[0][0]
    return prediction
def calcaccuracy(traindata, testdata, k):
    correctpredictions = 0
    for testpoint in testdata:
        actualoutcome = testpoint[-1]
        predicted = outcome(traindata, testpoint, k)
        if predicted == actualoutcome:
            correctpredictions += 1
    accuracy = correctpredictions / len(testdata) * 100
    return accuracy
k=14

accuracy = calcaccuracy(traindata, testdata, k)
print("k=",k)
print(f"The accuracy of the algorithm is: {accuracy:.2f}%")
