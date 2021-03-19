from frameworkXAI import *
from matplotlib import pyplot as plt
import numpy as np
import explainerTools
import sys

folderName = ""#sys.argv[1]

theTruth = "12345" #list(string.ascii_lowercase)
environmentReliability = 0.99
timeArray = []
loops0 = 50
for k in range(loops0):
    print(k)
    loops1=50
    innerArray = []
    for l in range(loops1):
        timeArrayAvg = []
        subloops = 30
        for j in range(subloops):
            agentArray = genAgents(50,0.5+0.5*k/loops0)
            counter  = 0
            continueLooping = True
            guessAccuracies = []
            while continueLooping == True:
                guessAccuracy = 0
                for i in range(len(agentArray)):
                    agentArray[i] = agentAction(agentArray[i], environmentReliability, agentArray, theTruth,-1+l/loops1*2, 0.35,0.35)
                    guessAccuracy += checkAgentGuessAccuracy(agentArray[i][4],theTruth)/len(agentArray)
                guessAccuracies.append(guessAccuracy)
                counter+=1
                # if guessAccuracy>0.75:
                #     continueLooping = False
                #     timeArrayAvg.append(counter)
                if counter >100:
                    # timeArrayAvg.append(counter)
                    continueLooping = False
            timeArrayAvg.append(explainerTools.findAvgChainLength(agentArray))
        innerArray.append(sum(timeArrayAvg)/subloops)
    timeArray.append(innerArray)
    # for i in agentArray:
    #     print(i)#
plt.imshow(timeArray, cmap='YlOrRd', origin='lower', extent=[-1,1,0.5,1],aspect='auto')
plt.colorbar()
plt.ylabel(r"Agent Reliability, $A$")
plt.xlabel(r"Flexibility, $\alpha$")
plt.title(r"Heatmap comparing $A$ and $\alpha$.")
plt.savefig(folderName+"heatMapCahinE"+str(int(environmentReliability*100))+".png")
#plt.show()
