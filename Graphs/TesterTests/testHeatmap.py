from testerXAI import *
from matplotlib import pyplot as plt
import numpy as np
import sys

folderName = ""#sys.argv[1]

theTruth = "12345" #list(string.ascii_lowercase)
environmentReliability = 0.90
timeArray = []
loops0 = 50
for k in range(loops0):
    print(k)
    loops1=50
    innerArray = []
    for l in range(loops1):
        timeArrayAvg = []
        subloops = 10
        for j in range(subloops):
            agentArray = genAgents(50,0.5+l/loops1*0.5)
            counter  = 0
            continueLooping = True
            guessAccuracies = []
            while continueLooping == True:
                guessAccuracy = 0
                for i in range(len(agentArray)):
                    agentArray[i] = agentAction(agentArray[i], environmentReliability, agentArray, theTruth,0, 0.35,0.35, k/loops0)
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
plt.imshow(timeArray, cmap='YlOrRd', origin='lower', extent=[0.5,1,0,1],aspect='auto')
plt.colorbar()
plt.ylabel("Testing Rate")
plt.xlabel("Agent Reliability, $\it{A}$")
plt.title("Heatmap comparing Testing Rate and Agent Reliability.")
plt.savefig(folderName+"heatMapTestA90E.png")
#plt.show()
