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
        mean = k/loops0*0.6;
        stdDev = (l/loops1)*0.35;
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
                    agentArray[i] = agentAction(agentArray[i], environmentReliability, agentArray, theTruth,0, randFlex[i],0.35)
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
plt.imshow(timeArray, cmap='YlOrRd', origin='lower', extent=[0,0.6,0,0.35],aspect='auto')
plt.colorbar()
plt.ylabel("Agent Learning Rate Variance")
plt.xlabel("Agent Learning Rate Mean")
plt.title("Heatmap showing mixed Agent Learning Rate performance.")
plt.savefig(folderName+"mixedAgentALearnHeatmapE"+str(int(eRel*100))+"A"+str(int(aRel*100))+".png")
#plt.show()
