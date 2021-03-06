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
timeArrayTError = []
timeArrayCError = []
timeTimeT = []
timeTimeC = []
loops = int(sys.argv[2])
for k in range(loops):
    # print(k)
    environmentReliability = reliability
    timeArrayAvgT = []
    timeArrayAvgC = []
    timeTimeAvgT = []
    timeTimeAvgC = []
    subloops = int(sys.argv[3])
    for j in range(subloops):
        agentReliability = 0.5+(k+0)/loops*0.5
        agentArrayT = transitiveXAI.genAgents(50,agentReliability)
        agentArrayC = transitiveCXAI.genAgents(50,agentReliability)
        timeT = 0
        timeC = 0
        counter  = 0
        continueLooping = True
        while continueLooping == True:
            guessAccuracyT = 0
            guessAccuracyC = 0
            for i in range(len(agentArrayT)):
                startTime = time.time()
                agentArrayT[i] = transitiveXAI.agentAction(agentArrayT[i], environmentReliability, agentArrayT, theTruth,0, 0.35, 0.35)
                guessAccuracyT += transitiveXAI.checkAgentGuessAccuracy(agentArrayT[i][4],theTruth)/len(agentArrayT)
                timeT += time.time() - startTime
                startTime = time.time()
                agentArrayC[i] = transitiveCXAI.agentAction(agentArrayC[i], environmentReliability, agentArrayC, theTruth,0, 0.35, 0.35)
                guessAccuracyC += transitiveCXAI.checkAgentGuessAccuracy(agentArrayC[i][4],theTruth)/len(agentArrayC)
                timeC += time.time() - startTime
            counter+=1
            if guessAccuracyT>0.75 and len(timeArrayAvgT)==j:
                timeArrayAvgT.append(timeT)
                timeTimeAvgT.append(timeT)
            if guessAccuracyC>0.75 and len(timeArrayAvgC)==j:
                timeArrayAvgC.append(timeT)
                timeTimeAvgC.append(timeC)
            if len(timeArrayAvgT+timeArrayAvgC) == 2*(j+1):
                continueLooping = False
            if counter >1000:
                if len(timeArrayAvgT)==j:
                    timeArrayAvgT.append(timeT)
                    timeTimeAvgT.append(timeT)
                if len(timeArrayAvgC)==j:
                    timeArrayAvgC.append(timeT)
                    timeTimeAvgC.append(timeC)
                continueLooping = False
    timeArrayT.append(sum(timeArrayAvgT)/subloops)
    timeArrayTError.append(np.std(np.array(timeArrayAvgT)))
    timeArrayC.append(sum(timeArrayAvgC)/subloops)
    timeArrayCError.append(np.std(np.array(timeArrayAvgC)))

# for i in agentArray:
#     print(i)
firstNo = 1/loops*0.5+0.5
x = np.linspace(firstNo,1,loops)
plt.plot(x,timeArrayT)
plt.fill_between(x,np.array(timeArrayT)-np.array(timeArrayTError),np.array(timeArrayT)+np.array(timeArrayTError), alpha = 0.5)
plt.plot(x,timeArrayC)
plt.fill_between(x,np.array(timeArrayC)-np.array(timeArrayCError),np.array(timeArrayC)+np.array(timeArrayCError), alpha = 0.5)
plt.legend(["Transitivity","No Transitivity"])
plt.xlabel("Agent Reliability")
plt.ylabel("Time to 75% (s)")
plt.title("Transitivity Performance against $\it{A}$")
plt.savefig("Graphs/TransTests/agentTransTimeTestER"+str(int(100*reliability))+".png")
# plt.savefig("agentTransTimeTestER"+str(int(100*reliability))+".png")
# plt.show()
