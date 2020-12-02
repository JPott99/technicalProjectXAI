import transitiveXAI
import transitiveCXAI
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
    print(k)
    environmentReliability = reliability
    timeArrayAvgT = []
    timeArrayAvgC = []
    timeTimeAvgT = []
    timeTimeAvgC = []
    subloops = 10
    for j in range(subloops):
        startTime = time.time()
        agentReliability = 0.5+(k+1)/loops*0.5
        agentArrayT = transitiveXAI.genAgents(50,agentReliability)
        agentArrayC = transitiveCXAI.genAgents(50,agentReliability)
        counter  = 0
        continueLooping = True
        while continueLooping == True:
            guessAccuracyT = 0
            guessAccuracyC = 0
            for i in range(len(agentArrayT)):
                agentArrayT[i] = transitiveXAI.agentAction(agentArrayT[i], environmentReliability, agentArrayT, theTruth, 0.5, 0.1)
                guessAccuracyT += transitiveXAI.checkAgentGuessAccuracy(agentArrayT[i][4],theTruth)/len(agentArrayT)
                agentArrayC[i] = transitiveCXAI.agentAction(agentArrayC[i], environmentReliability, agentArrayC, theTruth, 0.5, 0.1)
                guessAccuracyC += transitiveCXAI.checkAgentGuessAccuracy(agentArrayC[i][4],theTruth)/len(agentArrayC)
            counter+=1
            if guessAccuracyT>0.75 and len(timeArrayAvgT)==j:
                timeArrayAvgT.append(counter)
                timeTimeAvgT.append(time.time()-startTime)
            if guessAccuracyC>0.75 and len(timeArrayAvgC)==j:
                timeArrayAvgC.append(counter)
                timeTimeAvgC.append(time.time()-startTime)
            if len(timeArrayAvgT+timeArrayAvgC) == 2*(j+1):
                continueLooping = False
            if counter >1000:
                if len(timeArrayAvgT)==j:
                    timeArrayAvgT.append(counter)
                    timeTimeAvgT.append(time.time()-startTime)
                if len(timeArrayAvgC)==j:
                    timeArrayAvgC.append(counter)
                    timeTimeAvgC.append(time.time()-startTime)
                continueLooping = False
    timeArrayT.append(sum(timeTimeAvgT)/subloops)
    timeArrayC.append(sum(timeTimeAvgC)/subloops)
    # for i in agentArray:
    #     print(i)
firstNo = 1/loops*0.5+0.5
plt.plot(np.linspace(firstNo,1,loops),timeArrayT)
plt.plot(np.linspace(firstNo,1,loops),timeArrayC)
plt.legend(["Transitivity","No Transitivity"])
plt.xlabel("Agent Reliability")
plt.ylabel("Time to 75% (s)")
plt.title("Transitivity Performance against Agent Reliability")
plt.savefig("agentTransTimeTestER"+str(int(100*reliability))+".png")
# plt.show()