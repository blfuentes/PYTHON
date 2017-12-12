import string
import random

charList = list(string.ascii_lowercase)
charList.append(' ')
targetString = "methinks it is like a weasel"
#targetString = "abcd"
stringLength = len(targetString)

def generateString(length):
    result = ""
    for idx in range(0,length):
        result += random.choice(charList)
    return result

def compareString(origin, target, length):
    score = 0
    for idx in range(0, length):
        if origin[idx] == target[idx]:
            score +=1
    return 100 * score / length

def runCheck(inputString):
    bestString = ""
    bestScore = 0
    counter = 0
    while True:
        originString = generateString(len(inputString))
        lastScore = compareString(originString, targetString, len(stringLength))
        if lastScore > bestScore:
            bestScore = lastScore
            bestString = originString
        print("Generated string: %s"%originString)
        print("Target string   : %s"%targetString)
        print("Score: %.2f"%lastScore)
        counter += 1
        if counter == 1000:
            print("Best score: %.2f - best string: %s"%(bestScore, bestString))
            counter = 0
        if lastScore >= 50:
            break
        print("")

def hillClimbing(inputString):
    inputStringLength = len(inputString)
    bestScore = 0
    counter = 0
    bestString = generateString(inputStringLength)
    while True:
        #compare
        lastScore = compareString(bestString, targetString, inputStringLength)
        if lastScore >= bestScore:
            bestScore = lastScore

        #output   
        print("Generated string: %s"%bestString)
        print("Target string   : %s"%targetString)
        print("Score: %.2f%%"%lastScore)
        counter += 1
        if counter % 200 == 0:
            print("Best score: %.2f%% - best string: %s"%(bestScore, bestString))
        if bestScore == 100:
            break

        #change one character
        hasNewChar = False
        newString = ""
        if bestScore != 0:
            for idx in range(0, inputStringLength):
                if bestString[idx] != targetString[idx] and not hasNewChar:
                    newChar = random.choice(charList)
                    print("New char %s"%newChar)
                    newString += newChar
                    hasNewChar = True
                else:
                    newString += bestString[idx]
            print("Next try: %s"%newString)
            bestString = newString
        else:
            bestString = generateString(inputStringLength)
            
        print("")

    print("Number of attempts: %d"%counter)

    return counter
    
#runCheck(targetString)
myResults = list()
for idx in range(5):
    myResults.append(hillClimbing(targetString))

print ("All results:")
print (myResults)
