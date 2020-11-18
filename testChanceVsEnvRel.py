from frameworkXAI import *
from matplotlib import pyplot as plt
import numpy as np

theTruth = "12345" #list(string.ascii_lowercase)
timeArray = []
loops0 = 50
for k in range(loops0):
    loops1=50
    innerArray = []
    for l in range(loops1+1):
        timeArrayAvg = []
        subloops = 10
        for j in range(subloops):
            environmentReliability = l/loops1
            agentArray = genAgents(50,l/loops1)
            counter  = 0
            continueLooping = True
            guessAccuracies = []
            while continueLooping == True:
                guessAccuracy = 0
                for i in range(len(agentArray)):
                    agentArray[i] = agentAction(agentArray[i], environmentReliability, agentArray, theTruth, 0.5, (k+1)*0.49/loops0)
                    guessAccuracy += checkAgentGuessAccuracy(agentArray[i][4],theTruth)/len(agentArray)
                guessAccuracies.append(guessAccuracy)
                counter+=1
                if guessAccuracy>0.7:
                    continueLooping = False
                    timeArrayAvg.append(counter)
                if counter >1000:
                    timeArrayAvg.append(counter)
                    continueLooping = False
        innerArray.append(sum(timeArrayAvg)/subloops)
    timeArray.append(innerArray)
    print(k)
    # for i in agentArray:
    #     print(i)#
plt.imshow(timeArray, cmap='YlOrRd', origin='lower', extent=[0,1,0.49/loops0,0.49],aspect='auto')
plt.colorbar()
plt.ylabel("Chance to Ask Environment")
plt.xlabel("Chance of Environment sharing correct info")
plt.title("Heatmap comparing Test Chance and Agent Reliability.")
plt.savefig("Graphs/v1 Zealous/heatMapTestVEnvRel.png")
plt.show()
