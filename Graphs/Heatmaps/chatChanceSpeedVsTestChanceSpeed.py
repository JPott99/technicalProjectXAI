from fickleXAI import *
from matplotlib import pyplot as plt
import numpy as np
import sys

folderName = ""#sys.argv[1]

startPint = 0.15
stepPint = 0.3


theTruth = "12345" #list(string.ascii_lowercase)
environmentReliability = 0.99
timeArray = []
loops0 = 25
for k in range(loops0):
    loops1=25
    innerArray = []
    for l in range(loops1):
        timeArrayAvg = []
        subloops = 10
        for j in range(subloops):
            agentArray = genAgents(50,0.99)
            counter  = 0
            continueLooping = True
            guessAccuracies = []
            while continueLooping == True:
                guessAccuracy = 0
                for i in range(len(agentArray)):
                    agentArray[i] = agentAction(agentArray[i], environmentReliability, agentArray, theTruth, startPint+(1+k)*stepPint/loops0, startPint+(1+l)*stepPint/loops1)
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
plt.imshow(timeArray, cmap='YlOrRd', origin='lower', extent=[startPint,startPint+stepPint,startPint,startPint+stepPint],aspect='auto')
plt.colorbar()
plt.ylabel("Agent Sharing Rate")
plt.xlabel("Environment Sharing Rate")
plt.title("Heatmap comparing Agent and Environment sharing rates.")
plt.savefig(folderName+"heatMapChatVTestEMZI.png")
#plt.show()
