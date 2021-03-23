from frameworkXAI import *
from matplotlib import pyplot as plt
import numpy as np
import sys

folderName = ""#sys.argv[1]

theTruth = "12345" #list(string.ascii_lowercase)
aRel = float(sys.argv[1])
eRel = float(sys.argv[2])
environmentReliability = eRel
timeArray = []
loops0 = 30
for k in range(loops0):

    loops1=30
    innerArray = []
    for l in range(loops1):
        timeArrayAvg = []
        subloops = 10
        mean1 = 0.9
        stdDev1 = 0.1*(l/loops1);
        mean2 = 0
        stdDev2 = 1*(k/loops1);

        for j in range(subloops):
            randP1 = mean1 + np.random.randn(50)*stdDev1**2
            randP2 = mean2 + np.random.randn(50)*stdDev2**2
            agentArray = genAgents(50,randP1)
            # print(randFlex)
            counter  = 0
            continueLooping = True
            guessAccuracies = []
            while continueLooping == True:
                guessAccuracy = 0
                for i in range(len(agentArray)):
                    agentArray[i] = agentAction(agentArray[i], environmentReliability, agentArray, theTruth,randP2[i], 0.35,0.35)
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
        # print(innerArray[-1])
    timeArray.append(innerArray)

    # for i in agentArray:
    #     print(i)#
plt.imshow(timeArray, cmap='YlOrRd', origin='lower', extent=[0,1,0,0.1],aspect='auto')
plt.colorbar()
plt.ylabel(r"$A$ Variance")
plt.xlabel(r"Flexibility Variance")
plt.title(r"Heatmap showing mixed $A$ and $\alpha$ performance.")
plt.savefig(folderName+"mixedAgentARelFlexHeatmapE"+str(int(eRel*100))+".png")
#plt.show()
