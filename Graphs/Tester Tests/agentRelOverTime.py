# import zealousXAI
import fickleXAI
import testerXAI
import lessTesterXAI
import zealousTesterXAI
# import superFickleXAI
import sys
from matplotlib import pyplot as plt
import numpy as np
theTruth = "12345" #list(string.ascii_lowercase)
timeArrayZ = []
timeArrayF = []
timeArrayT = []
timeArraySF = []
loops = 20
reliability = float(sys.argv[1])
for k in range(loops):
    agentReliability = 0.5+(k+1)/loops*0.5
    print(k, agentReliability)
    environmentReliability = reliability
    timeArrayAvgZ = []
    timeArrayAvgF = []
    timeArrayAvgT = []
    timeArrayAvgSF = []
    subloops = 10
    for j in range(subloops):
        agentArrayZ = fickleXAI.genAgents(50,agentReliability)
        agentArrayF = testerXAI.genAgents(50,agentReliability)
        agentArrayT = lessTesterXAI.genAgents(50,agentReliability)
        agentArraySF = zealousTesterXAI.genAgents(50,agentReliability)
        counter  = 0
        continueLooping = True
        while continueLooping == True:
            guessAccuracyZ = 0
            guessAccuracyF = 0
            guessAccuracyT = 0
            guessAccuracySF = 0
            for i in range(len(agentArrayZ)):
                agentArrayZ[i] = fickleXAI.agentAction(agentArrayZ[i], environmentReliability, agentArrayZ, theTruth, 0.5, 0.1)
                guessAccuracyZ += fickleXAI.checkAgentGuessAccuracy(agentArrayZ[i][4],theTruth)/len(agentArrayZ)
                agentArrayF[i] = testerXAI.agentAction(agentArrayF[i], environmentReliability, agentArrayF, theTruth, 0.5, 0.1)
                guessAccuracyF += testerXAI.checkAgentGuessAccuracy(agentArrayF[i][4],theTruth)/len(agentArrayF)
                agentArrayT[i] = lessTesterXAI.agentAction(agentArrayT[i], environmentReliability, agentArrayT, theTruth, 0.5, 0.1)
                guessAccuracyT += lessTesterXAI.checkAgentGuessAccuracy(agentArrayT[i][4],theTruth)/len(agentArrayT)
                agentArraySF[i] = zealousTesterXAI.agentAction(agentArraySF[i], environmentReliability, agentArraySF, theTruth, 0.5, 0.1)
                guessAccuracySF += zealousTesterXAI.checkAgentGuessAccuracy(agentArraySF[i][4],theTruth)/len(agentArraySF)
            counter+=1
            if guessAccuracyZ>0.75 and len(timeArrayAvgZ)==j:
                timeArrayAvgZ.append(counter)
            if guessAccuracyF>0.75 and len(timeArrayAvgF)==j:
                timeArrayAvgF.append(counter)
            if guessAccuracyT>0.75 and len(timeArrayAvgT)==j:
                timeArrayAvgT.append(counter)
            if guessAccuracySF>0.75 and len(timeArrayAvgSF)==j:
                timeArrayAvgSF.append(counter)
            if len(timeArrayAvgZ+timeArrayAvgF+timeArrayAvgT+timeArrayAvgSF) == 4*(j+1):
                continueLooping = False
            if counter >1000:
                if len(timeArrayAvgZ)==j:
                    timeArrayAvgZ.append(counter)
                if len(timeArrayAvgF)==j:
                    timeArrayAvgF.append(counter)
                if len(timeArrayAvgT)==j:
                    timeArrayAvgT.append(counter)
                if len(timeArrayAvgSF)==j:
                    timeArrayAvgSF.append(counter)
                continueLooping = False
    timeArrayZ.append(sum(timeArrayAvgZ)/subloops)
    timeArrayF.append(sum(timeArrayAvgF)/subloops)
    timeArrayT.append(sum(timeArrayAvgT)/subloops)
    timeArraySF.append(sum(timeArrayAvgSF)/subloops)
    # for i in agentArray:
    #     print(i)
firstNumber = 0.5+1/loops*0.5
plt.plot(np.linspace(firstNumber,1,loops),timeArrayZ)
plt.plot(np.linspace(firstNumber,1,loops),timeArrayF)
plt.plot(np.linspace(firstNumber,1,loops),timeArrayT)
plt.plot(np.linspace(firstNumber,1,loops),timeArraySF)
plt.legend(["No Testing","Tester", "Lesser Tester", "Zealous Tester"])
plt.xlabel("Agent Reliability")
plt.ylabel("Number of Iterations to 75% accuracy")
plt.title("Performance of Testing Behaviours against Agent Reliabilty")
plt.savefig("agentRelTestTestER"+str(int(100*reliability))+".png")
# plt.show()
