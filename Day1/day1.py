class Elf:
    def __init__(self, snacksList):
        self.totalcalc = 0
        self.totalCal(snacksList)

    def totalCal(self, snacksList):
        for item in snacksList:
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
    for item in snackList:
        tempElf = Elf(item)
        elfList.append(tempElf)

    elfList.sort(reverse=True, key=sortLogic)
    
    topNumber = 3
    sumOfCalcTop = 0
    for num in range(topNumber):
        sumOfCalcTop += elfList[num].totalcalc

# PART 1
    print("Elf with most snacks has calories = " + str(elfList[0].totalcalc))
# PART 2    
    print("Total calc on top " + str(topNumber) + " elf = " + str(sumOfCalcTop))

if __name__ == "__main__":
    main()