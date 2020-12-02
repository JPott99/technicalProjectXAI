from frameworkXAI import *
from matplotlib import pyplot as plt
import string
import numpy as np
import sys

folderName = sys.argv[1]

theTruth = "0123456789"
timeArray = []
environmentReliability = 0.99
loops0 = len(theTruth)-1
for k in range(3,loops0):
    myTruth = theTruth[0:k]
    loops1=25
    innerArray = []
    for l in range(2,loops1+1):
        timeArrayAvg = []
        subloops = 5
        for j in range(subloops):
            agentArray = genAgents(l*2,1)
            counter  = 0
            continueLooping = True
            guessAccuracies = []
            while continueLooping == True:
                guessAccuracy = 0
                for i in range(len(agentArray)):
                    agentArray[i] = agentAction(agentArray[i], environmentReliability, agentArray, myTruth, 0.5, 0.1)
                    guessAccuracy += checkAgentGuessAccuracy(agentArray[i][4],myTruth)/len(agentArray)
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
    # for i in agentArray:
    #     print(i)#
plt.imshow(timeArray, cmap='YlOrRd', origin='lower', extent=[2,50,3,8],aspect='auto')
plt.colorbar()
plt.ylabel("Length of Truth")
plt.xlabel("Number of Agents")
plt.title("Heatmap comparing Length of Truth to Number of Agents.")
plt.savefig("Graphs/"+folderName+"/heatMapTruthLenVAgentCount.png")
#plt.show()
