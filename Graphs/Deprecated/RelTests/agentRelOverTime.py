import zealousXAI
import fickleXAI
import testerXAI
import lessTesterXAI
import zealousTesterXAI
import superFickleXAI
import sys
from matplotlib import pyplot as plt
import numpy as np
theTruth = "12345" #list(string.ascii_lowercase)
timeArrayZ = []
timeArrayZError = []
timeArrayF = []
timeArrayFError = []
# timeArrayT = []
timeArraySF = []
timeArraySFError = []
loops = 20
reliability = float(sys.argv[1])
for k in range(loops):
    agentReliability = 0.5+(k+1)/loops*0.5
    print(k, agentReliability)
    environmentReliability = reliability
    timeArrayAvgZ = []
    timeArrayAvgF = []
    # timeArrayAvgT = []
    timeArrayAvgSF = []
    subloops = 10
    for j in range(subloops):
        agentArrayZ = zealousXAI.genAgents(50,agentReliability)
        agentArrayF = fickleXAI.genAgents(50,agentReliability)
        # agentArrayT = testerXAI.genAgents(50,agentReliability)
        agentArraySF = superFickleXAI.genAgents(50,agentReliability)
        counter  = 0
        continueLooping = True
        while continueLooping == True:
            guessAccuracyZ = 0
            guessAccuracyF = 0
            # guessAccuracyT = 0
            guessAccuracySF = 0
            for i in range(len(agentArrayZ)):
                agentArrayZ[i] = zealousXAI.agentAction(agentArrayZ[i], environmentReliability, agentArrayZ, theTruth, 0.5, 0.1)
                guessAccuracyZ += zealousXAI.checkAgentGuessAccuracy(agentArrayZ[i][4],theTruth)/len(agentArrayZ)
                agentArrayF[i] = fickleXAI.agentAction(agentArrayF[i], environmentReliability, agentArrayF, theTruth, 0.5, 0.1)
                guessAccuracyF += fickleXAI.checkAgentGuessAccuracy(agentArrayF[i][4],theTruth)/len(agentArrayF)
                # agentArrayT[i] = testerXAI.agentAction(agentArrayT[i], environmentReliability, agentArrayT, theTruth, 0.5, 0.1)
                # guessAccuracyT += testerXAI.checkAgentGuessAccuracy(agentArrayT[i][4],theTruth)/len(agentArrayT)
                agentArraySF[i] = superFickleXAI.agentAction(agentArraySF[i], environmentReliability, agentArraySF, theTruth, 0.5, 0.1)
                guessAccuracySF += superFickleXAI.checkAgentGuessAccuracy(agentArraySF[i][4],theTruth)/len(agentArraySF)
            counter+=1
            if guessAccuracyZ>0.75 and len(timeArrayAvgZ)==j:
                timeArrayAvgZ.append(counter)
            if guessAccuracyF>0.75 and len(timeArrayAvgF)==j:
                timeArrayAvgF.append(counter)
            # if guessAccuracyT>0.75 and len(timeArrayAvgT)==j:
            #     timeArrayAvgT.append(counter)
            if guessAccuracySF>0.75 and len(timeArrayAvgSF)==j:
                timeArrayAvgSF.append(counter)
            if len(timeArrayAvgZ+timeArrayAvgF+timeArrayAvgSF) == 3*(j+1):
                continueLooping = False
            if counter >1000:
                if len(timeArrayAvgZ)==j:
                    timeArrayAvgZ.append(counter)
                if len(timeArrayAvgF)==j:
                    timeArrayAvgF.append(counter)
                # if len(timeArrayAvgT)==j:
                #     timeArrayAvgT.append(counter)
                if len(timeArrayAvgSF)==j:
                    timeArrayAvgSF.append(counter)
                continueLooping = False
    timeArrayZ.append(sum(timeArrayAvgZ)/subloops)
    timeArrayZError.append(np.std(np.array(timeArrayAvgZ)))
    timeArrayF.append(sum(timeArrayAvgF)/subloops)
    timeArrayFError.append(np.std(np.array(timeArrayAvgF)))
    #timeArrayT.append(sum(timeArrayAvgT)/subloops)
    timeArraySF.append(sum(timeArrayAvgSF)/subloops)
    timeArraySFError.append(np.std(np.array(timeArrayAvgSF)))
    # for i in agentArray:
    #     print(i)
firstNo = 1/loops*0.5+0.5
x = np.linspace(firstNo,1,loops)
plt.plot(x,timeArrayZ)
plt.fill_between(x,np.array(timeArrayZ)-np.array(timeArrayZError),np.array(timeArrayZ)+np.array(timeArrayZError), alpha = 0.5)
plt.plot(x,timeArrayF)
plt.fill_between(x,np.array(timeArrayF)-np.array(timeArrayFError),np.array(timeArrayF)+np.array(timeArrayFError), alpha = 0.5)
#plt.plot(np.linspace(firstNumber,1,loops),timeArrayT)
plt.plot(x,timeArraySF)
plt.fill_between(x,np.array(timeArraySF)-np.array(timeArraySFError),np.array(timeArraySF)+np.array(timeArraySFError), alpha = 0.5)
plt.legend(["Zealous","Flexible", "Fickle"])
plt.xlabel("Agent Reliability")
plt.ylabel("Number of Iterations to 75% accuracy")
plt.title("Performance of Agent Flexibility against $\it{A}$")
plt.savefig("agentRelFlexTestER"+str(int(100*reliability))+".png")
# plt.show()
