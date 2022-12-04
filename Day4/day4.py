class pairOfElves:
    def __init__(self, assigned1, assigned2):
        elf1 = set(self.expand(assigned1))
        elf2 = set(self.expand(assigned2))
        self.subset, self.anyoverlap = self.subSet(elf1, elf2)

    def expand(self, assigned):
        range_ = assigned.split("-")
        expandedAssign = []
        for i in range(int(range_[0]), int(range_[1])+1):
            expandedAssign.append(i)
        return expandedAssign
    
    def subSet(self, elf1, elf2):
        a = elf1 & elf2
        subset = False 
        anyoverlap = False
        if len(a) == len(elf1) or len(a) == len(elf2):
            subset = True
        if len(a) > 0:
            anyoverlap = True
        return subset, anyoverlap

def parseTxt():
    f = open('Day4/day4.txt', encoding='utf8',mode = 'r')
   # f = open('Day4/test.txt', encoding='utf8',mode = 'r')
    allpairOfElvesList = []
    allElfPairs = f.read().split('\n')
    for elfPair in allElfPairs:
        temp = elfPair.split(",")
        temp1 = pairOfElves(temp[0], temp[1])
        allpairOfElvesList.append(temp1)
    f.close()
    return allpairOfElvesList

count = 0
count1 = 0

elfTeamList = parseTxt()
for team in elfTeamList:
    #Part 1
    if team.subset == True:
        count+=1
    #Part 2
    if team.anyoverlap == True:
        count1+=1
print("Answer 1 = " + str(count))
print("Answer 2 = " + str(count1))

