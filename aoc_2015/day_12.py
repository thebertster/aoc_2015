import json

f = open("input12.txt", "r")

j = json.load(f)

processList = [ j ]

intSum = 0

while len(processList) > 0:
    objToProcess = processList.pop()
    if type(objToProcess) is dict:
        for obj in objToProcess.values():
            if (type(obj) is dict and "red" in obj.values()):
                pass
            else:
                processList.append(obj)
    elif type(objToProcess) is list:
        for obj in objToProcess:
            if (type(obj) is dict and "red" in obj.values()):
                pass
            else:
                processList.append(obj)
    elif type(objToProcess) is int:
        intSum += objToProcess

print(intSum)