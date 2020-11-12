from frameworkXAI import *
from matplotlib import pyplot as plt

theTruth = "1234567" #list(string.ascii_lowercase)
environmentReliability = 0.99
agentArray = genAgents(50)
counter  = 0
continueLooping = True
guessAccuracies = []
while continueLooping == True:
    guessAccuracy = 0
    for i in range(len(agentArray)):
        agentArray[i] = agentAction(agentArray[i], environmentReliability, agentArray, theTruth, 0.5, 0.1)
        guessAccuracy += checkAgentGuessAccuracy(agentArray[i][4],theTruth)/len(agentArray)
    guessAccuracies.append(guessAccuracy)
    counter+=1
    if guessAccuracy>0.75:
        continueLooping = False
        print(guessAccuracy)
        print(counter-1)
    if counter >10000:
        print("TIME OUT!")
        continueLooping = False
        print(guessAccuracy)
# for i in agentArray:
#     print(i)
plt.plot(guessAccuracies)
plt.show()
