from zealousXAI import *
from matplotlib import pyplot as plt
import numpy as np
import sys

# folderName = sys.argv[1]

theTruth = "12345" #list(string.ascii_lowercase)
timeArray = []
loops0 = 10
for k in range(loops0+1):
    loops1=10
    innerArray = []
    for l in range(loops1+1):
        timeArrayAvg = []
        environmentReliability = 0.99+l*0.01/loops1
        print(k,l)
        subloops = 1
        for j in range(subloops):
            agentArray = genAgents(50, 0.5+l*0.5/loops0)
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
                if counter >500:
                    timeArrayAvg.append(counter)
                    continueLooping = False
        innerArray.append(sum(timeArrayAvg)/subloops)
    timeArray.append(innerArray)
    # for i in agentArray:
    #     print(i)#
plt.imshow(timeArray, cmap='YlOrRd', origin='lower', extent=[0.5,1,0.99,1],aspect='auto')
plt.colorbar()
plt.xlabel("Agent Reliability")
plt.ylabel("Environmental Reliability")
plt.title("Heatmap showing iterations to 75% Accuracy.")
# plt.savefig("Graphs/"+folderName+"/
plt.savefig("heatMapAgentRelVEnvRel.png")
#plt.show()
