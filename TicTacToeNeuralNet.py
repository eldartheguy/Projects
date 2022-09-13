import math
import random
NNArr = []
popSize = 20
resultsArr = [0]*popSize       
emptyBoard = [0,0,0,0,0,0,0,0,0]
genAmount = 10000
winBonus = 0
roundsAmount = 1000

def flipBoard(board):
    tempBoard = []
    for square in board:
        tempBoard.append(-1*square)
    return tempBoard

def think(board , neuralNet):
    tempArr = []
    for i in range(9):
        tempSum = 0
        for j in range(18):
            tempSum += board[j] *neuralNet[i][j]
        tempSum += neuralNet[i][18]
        tempArr.append(tempSum)
    maxArr = [index for index in range(9) if tempArr[index] == max(tempArr)]
    return maxArr[0]

def checkWin(board):
    if board[0]==board[1] and board[1]==board[2] and board[0] != 0:
        return True
    if board[3]==board[4] and board[4]==board[5] and board[3] != 0:
        return True
    if board[6]==board[7] and board[7]==board[8] and board[6] != 0:
        return True
    if board[0]==board[4] and board[4]==board[8] and board[0] != 0:
        return True
    if board[2]==board[4] and board[4]==board[6] and board[2] != 0:
        return True
    if board[0]==board[3] and board[3]==board[6] and board[0] != 0:
        return True
    if board[1]==board[4] and board[4]==board[7] and board[1] != 0:
        return True
    if board[2]==board[5] and board[5]==board[8] and board[2] != 0:
        return True
    return False




def showBoard(board):
    tempArr = []
    for square in board:
        if square == 1:
            tempArr.append('X')
        elif square == -1:
            tempArr.append('O')
        else:
            tempArr.append(' ')
    print(tempArr[0] + '|' + tempArr[1] + '|' + tempArr[2])
    print('-----')
    print(tempArr[3] + '|' + tempArr[4] + '|' + tempArr[5])
    print('-----')
    print(tempArr[6] + '|' + tempArr[7] + '|' + tempArr[8])

def convertToNeural(board):
    outputBoard = []
    for i in board:
        if i == 1:
            outputBoard.append(1)
        else:
            outputBoard.append(0)
    for j in board:
        if j == -1:
            outputBoard.append(1)
        else:
            outputBoard.append(0)
    return outputBoard

def game(indexplayer1, show):
    board = emptyBoard.copy()
    player1 = NNArr[indexplayer1]
    turn = 0
    gameOver = False
    while turn < 9 and not gameOver:
        if show:
            showBoard(board)
            print('\n')
        if turn%2 == 0:
            pickedIndex = think(convertToNeural(board), player1)
            if board[pickedIndex] != 0:
                resultsArr[indexplayer1] -= 1
                if show:
                    print('Whoops Thats Taken Fam')
                potentialArr = [i for i in range(9) if board[i] == 0]
                random.shuffle(potentialArr)
                pickedIndex = potentialArr[0]
            board[pickedIndex] = 1
            if checkWin(board):
                resultsArr[indexplayer1] += winBonus
                gameOver = True
        if turn%2 == 1:
            if show:
                print('Whoops Thats Taken Fam')
            potentialArr = [i for i in range(9) if board[i] == 0]
            random.shuffle(potentialArr)
            pickedIndex = potentialArr[0]
            board[pickedIndex] = -1
            if checkWin(board):
                #resultsArr[indexplayer2] += 3
                gameOver = True
        turn += 1
        
    if not gameOver:
        pass
        #resultsArr[indexplayer1] += 1
        #resultsArr[indexplayer2] += 1

def mutatePlayer(playerNN, mutationFactor):
    outputArr = []
    for weightArr in playerNN:
        tempArr =[]
        for weight in weightArr:
            if random.random() <= mutationFactor:
                tempArr.append(random.randrange(-10000,10000)/1000)
            else:
                tempArr.append(weight)
        outputArr.append(tempArr)
    return outputArr

def createPop():
    for i in range(popSize):
        tempArr = [[],[],[],[],[],[],[],[],[]]
        for weightArr in tempArr:
            for i in range(19):
                weightArr.append(random.randrange(-10000,10000)/1000)
        NNArr.append(tempArr)

def gen():
    for i in range(popSize):
        for j in range(roundsAmount):
            game(i,False)
    print(resultsArr)
    maxFitForGen = max(resultsArr)
    done = False
    tempArr = resultsArr.copy()
    for i in range(popSize):
        if resultsArr[i] == maxFitForGen and not done:
            tempArr.pop(i)
            print('\n')
            print('best player index: ' + str(i))
            personalMutationFactor = 0
            NNArr[0] = mutatePlayer(NNArr[i],0)
            NNArr[1] = mutatePlayer(NNArr[i],0.01)
            NNArr[2] = mutatePlayer(NNArr[i],0.015)
            NNArr[3] = mutatePlayer(NNArr[i],0.02)
            NNArr[4] = mutatePlayer(NNArr[i],0.03)
            NNArr[5] = mutatePlayer(NNArr[i],0.035)
            NNArr[6] = mutatePlayer(NNArr[i],0.04)
            NNArr[7] = mutatePlayer(NNArr[i],0.045)
            NNArr[8] = mutatePlayer(NNArr[i],0.05)
            NNArr[9] = mutatePlayer(NNArr[i],0.055)
            done = True
    secondMaxFitForGen = max(tempArr)
    done = False
    for i in range(popSize - 1):
        if resultsArr[i] == secondMaxFitForGen and not done:
            tempArr.pop(i)
            personalMutationFactor = 0
            NNArr[10] = mutatePlayer(NNArr[i],0)
            NNArr[11] = mutatePlayer(NNArr[i],0.01)
            NNArr[12] = mutatePlayer(NNArr[i],0.015)
            NNArr[13] = mutatePlayer(NNArr[i],0.02)
            NNArr[14] = mutatePlayer(NNArr[i],0.025)
            NNArr[15] = mutatePlayer(NNArr[i],0.03)
            NNArr[16] = mutatePlayer(NNArr[i],0.035)
            NNArr[17] = mutatePlayer(NNArr[i],0.04)
            NNArr[18] = mutatePlayer(NNArr[i],0.045)
            NNArr[19] = mutatePlayer(NNArr[i],0.05)
            done = True

createPop()    
for k in range(genAmount):
    gen()
    print("\n")
    print("gen: " + str(k) +'/' + str(genAmount))
    print("\n")
    print("max fittness: " + str(max(resultsArr)))
    print("\n")
    if max(resultsArr) == 0:
        winBonus = 0.01
    resultsArr = [0]*popSize

    









    
    
    
