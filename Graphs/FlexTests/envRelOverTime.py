from frameworkXAI import *
from matplotlib import pyplot as plt
import numpy as np
import sys
theTruth = "12345" #list(string.ascii_lowercase)
reliability = float(sys.argv[1])
timeArrayZ = []
timeArrayZError = []
timeArrayF = []
timeArrayFError = []
timeArrayFu = []
timeArrayFuError = []
# timeArrayT = []
timeArraySF = []
timeArraySFError = []
loops = int(sys.argv[2])
for k in range(loops):
    environmentReliability = 0.7+(k)/loops*0.3
    timeArrayAvgZ = []
    timeArrayAvgF = []
    timeArrayAvgFu = []
    # timeArrayAvgT = []
    timeArrayAvgSF = []
    subloops = int(sys.argv[3])
    for j in range(subloops):
        agentRel = reliability
        agentArrayZ = genAgents(50,agentRel)
        agentArrayF = genAgents(50,agentRel)
        agentArrayFu = genAgents(50,agentRel)
        agentArraySF = genAgents(50,agentRel)
        counter  = 0
        continueLooping = True
        while continueLooping == True:
            guessAccuracyZ = 0
            guessAccuracyF = 0
            guessAccuracyFu = 0
            # guessAccuracyT = 0
            guessAccuracySF = 0
            for i in range(len(agentArrayZ)):
                agentArrayZ[i] = agentAction(agentArrayZ[i], environmentReliability, agentArrayZ, theTruth,0.001, 0.35, 0.35)
                guessAccuracyZ += checkAgentGuessAccuracy(agentArrayZ[i][4],theTruth)/len(agentArrayZ)
                agentArrayF[i] = agentAction(agentArrayF[i], environmentReliability, agentArrayF, theTruth,0, 0.35, 0.35)
                guessAccuracyF += checkAgentGuessAccuracy(agentArrayF[i][4],theTruth)/len(agentArrayF)
                agentArrayFu[i] = agentAction(agentArrayFu[i], environmentReliability, agentArrayFu, theTruth,1, 0.35, 0.35)
                guessAccuracyFu += checkAgentGuessAccuracy(agentArrayFu[i][4],theTruth)/len(agentArrayFu)
                # agentArrayT[i] = testerXAI.agentAction(agentArrayT[i], environmentReliability, agentArrayT, theTruth, 0.5, 0.1)
                # guessAccuracyT += testerXAI.checkAgentGuessAccuracy(agentArrayT[i][4],theTruth)/len(agentArrayT)
                agentArraySF[i] = agentAction(agentArraySF[i], environmentReliability, agentArraySF, theTruth,-1, 0.35, 0.35)
                guessAccuracySF += checkAgentGuessAccuracy(agentArraySF[i][4],theTruth)/len(agentArraySF)
            counter+=1
            if guessAccuracyZ>0.75 and len(timeArrayAvgZ)==j:
                timeArrayAvgZ.append(counter)
            if guessAccuracyF>0.75 and len(timeArrayAvgF)==j:
                timeArrayAvgF.append(counter)
            if guessAccuracyFu>0.75 and len(timeArrayAvgFu)==j:
                timeArrayAvgFu.append(counter)
            # if guessAccuracyT>0.75 and len(timeArrayAvgT)==j:
            # timeArrayAvgT.append(counter)
            if guessAccuracySF>0.75 and len(timeArrayAvgSF)==j:
                timeArrayAvgSF.append(counter)
            if len(timeArrayAvgZ+timeArrayAvgF+timeArrayAvgFu+timeArrayAvgSF) == 4*(j+1):
                continueLooping = False
            if counter >1000:
                if len(timeArrayAvgZ)==j:
                    timeArrayAvgZ.append(counter)
                if len(timeArrayAvgF)==j:
                    timeArrayAvgF.append(counter)
                if len(timeArrayAvgFu)==j:
                    timeArrayAvgFu.append(counter)
                # if len(timeArrayAvgT)==j:
                    # timeArrayAvgT.append(counter)
                if len(timeArrayAvgSF)==j:
                    timeArrayAvgSF.append(counter)
                continueLooping = False
    timeArrayZ.append(sum(timeArrayAvgZ)/subloops)
    timeArrayZError.append(np.std(np.array(timeArrayAvgZ)))
    timeArrayF.append(sum(timeArrayAvgF)/subloops)
    timeArrayFError.append(np.std(np.array(timeArrayAvgF)))
    timeArrayFu.append(sum(timeArrayAvgFu)/subloops)
    timeArrayFuError.append(np.std(np.array(timeArrayAvgFu)))
    #timeArrayT.append(sum(timeArrayAvgT)/subloops)
    timeArraySF.append(sum(timeArrayAvgSF)/subloops)
    timeArraySFError.append(np.std(np.array(timeArrayAvgSF)))
        # for i in agentArray:
        #     print(i)
firstNo = 0.7
x = np.linspace(firstNo,1,loops)
plt.plot(x,timeArrayZ)
plt.fill_between(x,np.array(timeArrayZ)-np.array(timeArrayZError),np.array(timeArrayZ)+np.array(timeArrayZError), alpha = 0.5)
plt.plot(x,timeArrayF)
plt.fill_between(x,np.array(timeArrayF)-np.array(timeArrayFError),np.array(timeArrayF)+np.array(timeArrayFError), alpha = 0.5)
plt.plot(x,timeArrayFu)
plt.fill_between(x,np.array(timeArrayFu)-np.array(timeArrayFuError),np.array(timeArrayFu)+np.array(timeArrayFuError), alpha = 0.5)
plt.plot(x,timeArraySF)
plt.fill_between(x,np.array(timeArraySF)-np.array(timeArraySFError),np.array(timeArraySF)+np.array(timeArraySFError), alpha = 0.5)
plt.legend([r"Zealous ($\alpha = 0.001$)",r"Flexible ($\alpha = 0$)", r"Fundamentalist ($\alpha = 1$)", r"Fickle ($\alpha = -1$)"])
plt.xlabel("Environmental Reliability")
plt.ylabel("Number of Iterations to Convergence")
plt.title("Performance of Agent flexibility against $\it{E}$")
plt.savefig("Graphs/FlexTests/envRelFlexTestAR"+str(int(100*reliability))+".png")
# plt.show()
