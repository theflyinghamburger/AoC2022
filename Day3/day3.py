def findPriority(item):
    priority = 0
    if ord(item) >= 96:
        priority += ord(item) - 96
    elif ord(item) <= 90:
        priority += ord(item) - 38
    return priority


class ruckSack:
    def __init__(self, all):
        self.all = all
        self.comp1, self.comp2 = self.compSplit()
        self.intersection = self.compInsection()
        self.priority = findPriority(self.intersection[0])
    
    def compSplit(self):
        length = len(self.all)//2
        comp1 = self.all[0:length]
        comp2 = self.all[length:]
        return comp1, comp2

    def compInsection(self):
        set1 = set(self.comp1)
        set2 = set(self.comp2)
        intersection = list(set1 & set2)
        return intersection


def parseTxt():
    f = open('Day3/day3.txt', encoding='utf8',mode = 'r')
    allRucksacks = []
    allRucksacksList = f.read().split('\n')
    for rucksack in allRucksacksList:
        temp = ruckSack(rucksack)
        allRucksacks.append(temp)
    f.close()
    return allRucksacks


inventoryList = parseTxt()
priList = []
for item in inventoryList:
    #print(item.all)
    #print(item.intersection)
    priList.append(item.priority)

print(sum(priList))

badgeList = []

teamPriority = 0

for index in range(0,len(inventoryList), 3):
    badge = list(set(inventoryList[index].all) & set(inventoryList[index+1].all) & set(inventoryList[index+2].all))
    #badgeList.append(badge)
    teamPriority += findPriority(badge[0])

print(teamPriority)