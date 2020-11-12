from frameworkXAI import *
from matplotlib import pyplot as plt
import numpy as np
theTruth = "12345" #list(string.ascii_lowercase)
environmentReliability = 1
timeArray = []
loops = 100
for i in range(loops):
    timeArrayAvg = []
    subloops = 10
    for j in range(subloops):
        agentArray = genAgents(loops)
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
                timeArrayAvg.append(counter)
            if counter >1000:
                timeArrayAvg.append(counter)
                continueLooping = False
    timeArray.append(sum(timeArrayAvg)/subloops)
    # for i in agentArray:
    #     print(i)
plt.plot(timeArray)
plt.show()
