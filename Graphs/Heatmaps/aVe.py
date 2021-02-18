from fickleXAI import *
from matplotlib import pyplot as plt
import numpy as np
import sys

folderName = ""#sys.argv[1]

theTruth = "12345" #list(string.ascii_lowercase)
timeArray = []
loops0 = 10
for k in range(loops0+1):
    loops1=10
    innerArray = []
    for l in range(loops1+1):
        timeArrayAvg = []
        environmentReliability = 0.9+l*0.1/loops1
        subloops = 10
        for j in range(subloops):
            agentArray = genAgents(50, 0.9+l*0.1/loops0)
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
        innerArray.append(sum(timeArrayAvg)/subloops)
    timeArray.append(innerArray)
    # for i in agentArray:
    #     print(i)#
plt.imshow(timeArray, cmap='YlOrRd', origin='lower', extent=[0.9,1,0.9,1],aspect='auto')
plt.colorbar()
plt.ylabel("Agent Reliability")
plt.xlabel("Environment Reliability")
plt.title("Heatmap comparing Environment and Agent Reliability.")
plt.savefig(folderName+"aVe_Heatmap.png")
#plt.show()
