from frameworkXAI import *
from matplotlib import pyplot as plt
import numpy as np



theTruth = "12345" #list(string.ascii_lowercase)
environmentReliability = 0.99
timeArray = []
loops0 = 50
for k in range(loops0):
    loops1=50-2
    innerArray = []
    for l in range(loops1):
        timeArrayAvg = []
        subloops = 10
        for j in range(subloops):
            agentArray = genAgents(l+2,1)
            counter  = 0
            continueLooping = True
            guessAccuracies = []
            while continueLooping == True:
                guessAccuracy = 0
                for i in range(len(agentArray)):
                    agentArray[i] = agentAction(agentArray[i], environmentReliability, agentArray, theTruth, k*0.8/loops0, 0.1)
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
plt.imshow(timeArray, cmap='YlOrRd', origin='lower', extent=[2,loops1+2,0,0.8],aspect='auto')
plt.colorbar()
plt.ylabel("Chance to Ask another Agent")
plt.xlabel("Number of Agents")
plt.title("Heatmap comparing Chat Chance and Agent count.")
plt.savefig("Graphs/v1 Zealous/heatMapChatVAgent.png")
plt.show()
