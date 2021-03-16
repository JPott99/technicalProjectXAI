from frameworkXAI import *
from matplotlib import pyplot as plt
import numpy as np
import sys

folderName = ""#sys.argv[1]

theTruth = "12345" #list(string.ascii_lowercase)
aRel = sys.argv[1]
eRel = sys.argv[2]
environmentReliability = eRel
timeArray = []
loops0 = 50
for k in range(loops0):
    loops1=50
    innerArray = []
    for l in range(loops1):
        timeArrayAvg = []
        subloops = 30
        mean = k/loops0;
        stdDev = (l/loops1);
        for j in range(subloops):
            agentArray = genAgents(50,aRel)
            randFlex = mean + np.random.randn(50)*stdDev**2
            # print(randFlex)
            counter  = 0
            continueLooping = True
            guessAccuracies = []
            while continueLooping == True:
                guessAccuracy = 0
                for i in range(len(agentArray)):
                    agentArray[i] = agentAction(agentArray[i], environmentReliability, agentArray, theTruth,0, 0.35,0.35,randFlex[i])
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
plt.imshow(timeArray, cmap='YlOrRd', origin='lower', extent=[0,1,0,1],aspect='auto')
plt.colorbar()
plt.ylabel("Testing Rate Variance")
plt.xlabel("Testing Rate Mean")
plt.title(r"Heatmap comparing Testing Rate normal distribution parameters.")
plt.savefig(folderName+"mixedAgentTestHeatmapE"+str(int(eRel*100)))+"A"+str(int(aRel*100)))+").png")
#plt.show()
