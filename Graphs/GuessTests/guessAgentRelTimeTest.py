import independentGuessXAI
import dependentGuessXAI
from matplotlib import pyplot as plt
import numpy as np
import time
import sys
reliability = float(sys.argv[1])
theTruth = "12345" #list(string.ascii_lowercase)
timeArrayT = []
timeArrayC = []
timeTimeT = []
timeTimeC = []
loops = 20
for k in range(loops):
    environmentReliability = reliability
    timeArrayAvgT = []
    timeArrayAvgC = []
    timeTimeAvgT = []
    timeTimeAvgC = []
    subloops = 10
    for j in range(subloops):
        agentReliability = 0.5+(k+1)/loops*0.5
        agentArrayT = independentGuessXAI.genAgents(50,agentReliability)
        agentArrayC = dependentGuessXAI.genAgents(50,agentReliability)
        timeT = 0
        timeC = 0
        counter  = 0
        continueLooping = True
        while continueLooping == True:
            guessAccuracyT = 0
            guessAccuracyC = 0
            for i in range(len(agentArrayT)):
                startTime = time.time()
                agentArrayT[i] = independentGuessXAI.agentAction(agentArrayT[i], environmentReliability, agentArrayT, theTruth, 0.5, 0.1)
                guessAccuracyT += independentGuessXAI.checkAgentGuessAccuracy(agentArrayT[i][4],theTruth)/len(agentArrayT)
                timeT += time.time() - startTime
                startTime = time.time()
                agentArrayC[i] = dependentGuessXAI.agentAction(agentArrayC[i], environmentReliability, agentArrayC, theTruth, 0.5, 0.1)
                guessAccuracyC += dependentGuessXAI.checkAgentGuessAccuracy(agentArrayC[i][4],theTruth)/len(agentArrayC)
                timeC += time.time() - startTime
            counter+=1
            if guessAccuracyT>0.75 and len(timeArrayAvgT)==j:
                timeArrayAvgT.append(counter)
                timeTimeAvgT.append(timeT)
            if guessAccuracyC>0.75 and len(timeArrayAvgC)==j:
                timeArrayAvgC.append(counter)
                timeTimeAvgC.append(timeC)
            if len(timeArrayAvgT+timeArrayAvgC) == 2*(j+1):
                continueLooping = False
            if counter >1000:
                if len(timeArrayAvgT)==j:
                    timeArrayAvgT.append(counter)
                    timeTimeAvgT.append(timeT)
                if len(timeArrayAvgC)==j:
                    timeArrayAvgC.append(counter)
                    timeTimeAvgC.append(timeC)
                continueLooping = False
    timeArrayT.append(sum(timeTimeAvgT)/subloops)
    timeArrayC.append(sum(timeTimeAvgC)/subloops)
    # for i in agentArray:
    #     print(i)
firstNo = 1/loops*0.5+0.5
plt.plot(np.linspace(firstNo,1,loops),timeArrayT)
plt.plot(np.linspace(firstNo,1,loops),timeArrayC)
plt.legend(["Independent","Dependent"])
plt.xlabel("Agent Reliability")
plt.ylabel("Time to 75% (s)")
plt.title("Guess Dependence Performance against Agent Reliability")
plt.savefig("agentGuessTimeTestER"+str(int(100*reliability))+".png")
# plt.show()
