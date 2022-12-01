class Elf:
    def __init__(self, snacksList, name):
        self.totalcalc = 0
        self.snacks = snacksList
        self.name = name
        self.totalCal()

    def totalCal(self):
        for item in self.snacks:
            self.totalcalc += int(item)
        return self.totalcalc

def parseTxt():
    f = open('day1.txt', encoding='utf8',mode = 'r')
    parsedSnacks = []
    allSnacks = f.read()
    allSnacks = allSnacks.split('\n\n')
    for snacks in allSnacks:
        snacks = snacks.split('\n')
        parsedSnacks.append(snacks)
    f.close()
    return parsedSnacks

def sortLogic(elf):
    return elf.totalcalc

def main():
    elfList = []
    snackList = parseTxt()
    for index, item in enumerate(snackList):
        tempElf = Elf(item, index)
        elfList.append(tempElf)

    elfList.sort(reverse=True, key=sortLogic)
    
    topNumber = 3
    sumOfCalcTop = 0
    for num in range(topNumber):
        sumOfCalcTop += elfList[num].totalcalc

# PART 1
    for i in range(3):
        print("Elf named " + str(elfList[i].name) + " has " + str(i) + " most calories = " + str(elfList[i].totalcalc))
# PART 2    
    print("Total calc on top 3 elf = " + str(sumOfCalcTop))

if __name__ == "__main__":
    main()