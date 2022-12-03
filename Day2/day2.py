from enum import Enum

#P1 = player 1
#P2 = player 2

class moveShapes:
    def __init__(self, win, lose, draw, value):
         self.win = win
         self.lose = lose
         self.draw = draw
         self.value = value

    def outcome(self, P1): #For part 1
        if P1 == self.draw:
            return 3
        elif P1 == self.win:
            return 6
        elif P1 == self.lose:
            return 0
        else:
            print("Invalid move")
            return False

    def expectedMove(self, expectedOutcome): #For part 2
        if expectedOutcome == 'X':
            return self.win, 0
        elif expectedOutcome == 'Y':
            return self.draw, 3
        elif expectedOutcome == 'Z':
            return self.lose, 6
        else:
            print("Invalid outcome")
            return False

R = moveShapes("S", "P", "R", 1) #win, lose, draw
P = moveShapes("R", "S", "P", 2)
S = moveShapes("P", "R", "S", 3)

def returnShape(shape): #Converts string to moveShapes
    if shape == 'R':
        return R
    elif shape == 'P':
        return P
    elif shape == 'S':
        return S

def scoreCalc(P2, outcome):
    score = P2 + outcome 
    return score

def decodeMove(moveList):
    for index, moves in enumerate(moveList):
        if moves == 'A' or moves == 'X':
            moveList[index] = R
        elif moves == 'B' or moves == 'Y':
            moveList[index] = P
        elif moves == 'C' or moves == 'Z':
            moveList[index] = S
        else:
            print("Invalid move")
            return False
    return moveList

def parseTxt():
    f = open('Day2/day2.txt', encoding='utf8',mode = 'r')
    opponentMoves = []
    yourMoves = []
    outcomeList = []
    allMoves = f.read().split('\n')
    for round in allMoves:
        sets = round.split()

        opponentMoves.append(sets[0])
        yourMoves.append(sets[1])
        outcomeList.append(sets[1])
    opponentMoves = decodeMove(opponentMoves)
    yourMoves = decodeMove(yourMoves)
    f.close()
    return opponentMoves, yourMoves, outcomeList


P1set, P2set, expectedOutcome = parseTxt()
outcomeList = []
scoreList = []

#Part 1
for index, moves in enumerate(P2set):
    outcomeList.append(moves.outcome(P1set[index].draw))
for index, moves in enumerate(P2set):
    scoreList.append(scoreCalc(moves.value, outcomeList[index]))
print(sum(scoreList))

P2set = []
scoreList = []
outcomeList = []

#Part 2
for index, moves in enumerate(P1set):
    P2temp, outcomeScoreTemp = moves.expectedMove(expectedOutcome[index])
    P2set.append(P2temp)
    outcomeList.append(outcomeScoreTemp)
    scoreList.append(scoreCalc(returnShape(P2set[index]).value, outcomeList[index]))

print(sum(scoreList))