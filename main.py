import math
import sys
import matplotlib.pyplot as plt


def readfile(filename:str)->dict:
    testset = {}
    file = open(filename)
    for line in file.readlines():
        splited = line.split(',')
        values = []
        for i in range(len(splited)-1):
            values.append(float(splited[i]))
        testset[tuple(values)] = splited[len(splited)-1]
    return testset

def getlen(point1:tuple, point2:tuple) -> float:
    x = 0
    for i in range(len(point1)):
        x += math.pow(point1[i]-point2[i],2)
    return math.sqrt(x)


def getClosestPoints(example:tuple, testset:dict, k:int)->list:
    lendict = {}
    for i in testset.keys():
        lendict[i] = getlen(i, example)
    sortedDict = {}
    sortedvalues = sorted(lendict.values())
    for l in sortedvalues:
        for m in lendict.keys():
            if lendict[m] == l:
                sortedDict[m] = lendict[m]
                break
    points = []
    for j in range(k):
        keys = list(sortedDict.keys())
        points.append(testset[keys[j]])
    return points


def getMostOccuring(points: list)->str:
    champ = points[0]
    for j in points:
        if points.count(j) > points.count(champ):
            champ = j
    return champ


def predict(example:tuple, trainset:dict, k:int)->str:
    points = getClosestPoints(example, trainset, k)
    guess = getMostOccuring(points)
    return guess

def getTrainAccuracy(testset:dict, trainset:dict, k)->float:
    accuracy = 0
    for i in testset.keys():
        prediction = predict(i, trainset,k)
        if prediction == testset.get(i):
            accuracy+=1
    return (accuracy / len(testset.keys()))*100

def main():
    args = sys.argv
    k = int(args[1])
    trainset = readfile(args[2])
    testset = readfile(args[3])
    print("accuracy on testset: " + str(getTrainAccuracy(testset,trainset,k)) + "%")
    accuracyForK = []
    for i in range(1,len(testset.keys())):
        accuracyForK.append(getTrainAccuracy(testset,trainset,i))
    plt.plot(accuracyForK, [j for j in range(1,len(testset.keys()))])
    plt.ylabel('k')
    plt.xlabel('accuracy')
    plt.show()
    
    x = input("input new example: ").split(" ")
    while(len(x)>1):
        y = [float(j) for j in x[:len(list(testset.keys())[0])]]
        print(predict(tuple(y),trainset,k))
        x = input("input new example: ").split(" ")
    
    return 0





if __name__ == "__main__":
    main()