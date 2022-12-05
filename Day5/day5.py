from queue import deque
from copy import deepcopy

def listToString(s):
    str1 = ""
    return (str1.join(s))

class instructions:
    def __init__(self, containerNo, startStack, endStack):
        self.containerNo = containerNo
        self.startStack = startStack-1
        self.endStack = endStack-1

class boxStacks:
    def __init__(self, listOfStacks):
        self.listOfStacks = listOfStacks
    
    def peakTop(self):
        topStr = []
        for i in self.listOfStacks:
            topStr.append(i[0])
        return topStr
    
    #Part 1
    def moveInstruct(self, containerNo, startStack, endStack):
        for i in range(containerNo):
            self.listOfStacks[endStack].appendleft(self.listOfStacks[startStack].popleft())

    #Part 2
    def moveInstruct2(self, containerNo, startStack, endStack):
        tempD = deque()
        for i in range(containerNo):
            tempD.appendleft(self.listOfStacks[startStack].popleft())
        for i in range(containerNo):
            self.listOfStacks[endStack].appendleft(tempD.popleft())   
           

def parseTxt():
    f = open('Day5/day5.txt', encoding='utf8',mode = 'r')
    #f = open('Day5/test.txt',encoding='utf8',mode = 'r')
    allStacks = []
    allInstructs = []
    allStrings = f.read().split('\n\n')
    temp = allStrings[0].split('\n') #stacks, all number will be stack numbers
    for i in temp[-1].split():
        tempStack = deque()
        allStacks.append(tempStack)
    for i in temp[-1].split():
        stackCount = 0
        spaceCount = 0
        for j in temp[int(i)-1]:
            if j == " ":
                spaceCount+=1
                if spaceCount == 4:
                    stackCount+=1
                    spaceCount = 0
            elif j not in "[]\n":
                allStacks[stackCount].append(j)
                stackCount+=1
                spaceCount = 0

    temp1 = allStrings[1].split('\n') #instructions format: move 1 from 2 to 1
    for instruct in temp1:
        temp = instruct.split()
        temp = instructions(int(temp[1]), int(temp[3]), int(temp[5]))
        allInstructs.append(temp)
    f.close()
    
    return allStacks, allInstructs

def main():
        
    allStacks, allInstructs = parseTxt()
    boxstacks = boxStacks(deepcopy(allStacks))

    #Part 1
    for instruct in allInstructs:
        boxstacks.moveInstruct(instruct.containerNo, instruct.startStack, instruct.endStack)
    print(listToString(boxstacks.peakTop()))

    boxstacks.listOfStacks = deepcopy(allStacks)
    #Part 2
    for instruct in allInstructs:
        boxstacks.moveInstruct2(instruct.containerNo, instruct.startStack, instruct.endStack)
    print(listToString(boxstacks.peakTop()))

main()