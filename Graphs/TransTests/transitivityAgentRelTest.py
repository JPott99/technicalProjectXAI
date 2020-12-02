import transitiveXAI
import transitiveCXAI
from matplotlib import pyplot as plt
import numpy as np
theTruth = "12345" #list(string.ascii_lowercase)
timeArrayT = []
timeArrayC = []
loops = 20
for k in range(loops):
    print(k)
    environmentReliability = 0.99
    timeArrayAvgT = []
    timeArrayAvgC = []
    subloops = 10
    for j in range(subloops):
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
firstNo = 1/loops*0.5+0.5
plt.plot(np.linspace(firstNo,1,loops),timeArrayT)
plt.plot(np.linspace(firstNo,1,loops),timeArrayC)
plt.legend(["Transitive","No Transitivity"])
plt.xlabel("Agent Reliability")
plt.ylabel("Number of Iterations to Convergence")
plt.title("Graph comparing performance of Transitivity against Agent Reliability")
plt.savefig("agentTransTestER99.png")
plt.show()
