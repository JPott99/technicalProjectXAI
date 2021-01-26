import independentGuessXAI
import dependentGuessXAI
from matplotlib import pyplot as plt
import numpy as np
import sys
reliability = float(sys.argv[1])
theTruth = "12345" #list(string.ascii_lowercase)
timeArrayT = []
timeArrayC = []
loops = 20
for k in range(loops):
    environmentReliability = 0.7+(k+1)/loops*0.3
    timeArrayAvgT = []
    timeArrayAvgC = []
    subloops = 15
    for j in range(subloops):
        agentReliability = reliability
        agentArrayT = independentGuessXAI.genAgents(50,agentReliability)
        agentArrayC = dependentGuessXAI.genAgents(50,agentReliability)
        counter  = 0
        continueLooping = True
        while continueLooping == True:
            guessAccuracyT = 0
            guessAccuracyC = 0
            for i in range(len(agentArrayT)):
                agentArrayT[i] = independentGuessXAI.agentAction(agentArrayT[i], environmentReliability, agentArrayT, theTruth, 0.5, 0.1)
                guessAccuracyT += independentGuessXAI.checkAgentGuessAccuracy(agentArrayT[i][4],theTruth)/len(agentArrayT)
                agentArrayC[i] = dependentGuessXAI.agentAction(agentArrayC[i], environmentReliability, agentArrayC, theTruth, 0.5, 0.1)
                guessAccuracyC += dependentGuessXAI.checkAgentGuessAccuracy(agentArrayC[i][4],theTruth)/len(agentArrayC)
            counter+=1
            if guessAccuracyT>0.75 and len(timeArrayAvgT)==j:
                timeArrayAvgT.append(counter)
            if guessAccuracyC>0.75 and len(timeArrayAvgC)==j:
                timeArrayAvgC.append(counter)
            if len(timeArrayAvgT+timeArrayAvgC) == 2*(j+1):
                continueLooping = False
            if counter >1000:
                if len(timeArrayAvgT)==j:
                    timeArrayAvgT.append(counter)
                if len(timeArrayAvgC)==j:
                    timeArrayAvgC.append(counter)
                continueLooping = False
    timeArrayT.append(sum(timeArrayAvgT)/subloops)
    timeArrayC.append(sum(timeArrayAvgC)/subloops)
    # for i in agentArray:
    #     print(i)
firstNo = 1/loops*0.3+0.7
plt.plot(np.linspace(firstNo,1,loops),timeArrayT)
plt.plot(np.linspace(firstNo,1,loops),timeArrayC)
plt.legend(["Independent","Dependent"])
plt.xlabel("Environmental Reliability")
plt.ylabel("Iterations to 75%")
plt.title("Guess Dependence Performance against Environmental Reliability")
plt.savefig("envGuessTestAR"+str(int(100*reliability))+".png")
# plt.show()
