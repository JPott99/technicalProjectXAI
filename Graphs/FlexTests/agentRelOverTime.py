from frameworkXAI import *
import sys
from matplotlib import pyplot as plt
import numpy as np
theTruth = "12345" #list(string.ascii_lowercase)
timeArrayZ = []
timeArrayZError = []
timeArrayFu = []
timeArrayFuError = []
timeArrayF = []
timeArrayFError = []
# timeArrayT = []
timeArraySF = []
timeArraySFError = []
loops = int(sys.argv[2])
reliability = float(sys.argv[1])
for k in range(loops):
    agentReliability = 0.5+(k+1)/loops*0.5
    environmentReliability = reliability
    timeArrayAvgZ = []
    timeArrayAvgF = []
    timeArrayAvgFu = []
    # timeArrayAvgT = []
    timeArrayAvgSF = []
    subloops = int(sys.argv[3])
    for j in range(subloops):
        agentArrayZ = genAgents(50,agentReliability)
        agentArrayF = genAgents(50,agentReliability)
        agentArrayFu = genAgents(50,agentReliability)
        agentArraySF = genAgents(50,agentReliability)
        counter  = 0
        continueLooping = True
        guessAccuracyZold=[0]
        guessAccuracyFold=[0]
        guessAccuracyFuold=[0]
        guessAccuracySFold=[0]
        while continueLooping == True:
            guessAccuracyZ = 0
            guessAccuracyF = 0
            guessAccuracyFu = 0
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
            accuracy = 0.0001
            # if abs(guessAccuracyZ-sum(guessAccuracyZold)/len(guessAccuracyZold))<accuracy and len(timeArrayAvgZ)==j:
            #     timeArrayAvgZ.append(counter)
            #     # print("Z =",guessAccuracyZ)
            # if abs(guessAccuracyF-sum(guessAccuracyFold)/len(guessAccuracyFold))<accuracy and len(timeArrayAvgF)==j:
            #     timeArrayAvgF.append(counter)
            #     # print("F =",guessAccuracyF)
            # # if guessAccuracyT>0.75 and len(timeArrayAvgT)==j:
            # #     timeArrayAvgT.append(counter)
            # if abs(guessAccuracySF-sum(guessAccuracySFold)/len(guessAccuracySFold))<accuracy and len(timeArrayAvgSF)==j:
            #     timeArrayAvgSF.append(counter)
            #     # print("SF =",guessAccuracySF)
            if guessAccuracyZ>0.75 and len(timeArrayAvgZ)==j:
                timeArrayAvgZ.append(counter)
            if guessAccuracyF>0.75 and len(timeArrayAvgF)==j:
                timeArrayAvgF.append(counter)
            if guessAccuracyFu>0.75 and len(timeArrayAvgFu)==j:
                timeArrayAvgFu.append(counter)
            if guessAccuracySF>0.75 and len(timeArrayAvgSF)==j:
                timeArrayAvgSF.append(counter)
            # print(timeArrayAvgSF)
            if len(timeArrayAvgZ+timeArrayAvgF+timeArrayAvgFu+timeArrayAvgSF) == 4*(j+1):
                continueLooping = False
            if counter >1000:
                if len(timeArrayAvgZ)==j:
                    timeArrayAvgZ.append(counter)
                if len(timeArrayAvgF)==j:
                    timeArrayAvgF.append(counter)
                if len(timeArrayAvgFu)==j:
                    timeArrayAvgFu.append(counter)
                if len(timeArrayAvgSF)==j:
                    timeArrayAvgSF.append(counter)
                continueLooping = False
            # guessAccuracyZold.append(guessAccuracyZ)
            # if len(guessAccuracyZold)>3:
            #     guessAccuracyZold.pop(0)
            # guessAccuracyFold.append(guessAccuracyF)
            # if len(guessAccuracyFold)>3:
            #     guessAccuracyFold.pop(0)
            # guessAccuracySFold.append(guessAccuracySF)
            # if len(guessAccuracySFold)>3:
            #     guessAccuracySFold.pop(0)

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
firstNo = 1/loops*0.5+0.5
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
plt.xlabel("Agent Reliability")
plt.ylabel("Number of Iterations to 75% accuracy")
plt.title("Performance of Agent flexibility against $\it{A}$")
plt.savefig("Graphs/FlexTests/agentRelFlexTestER"+str(int(100*reliability))+".png")
# plt.show()
