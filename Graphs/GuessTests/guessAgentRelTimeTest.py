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
timeArrayT = []
timeArrayTError = []
timeArrayC = []
timeArrayCError = []
loops = int(sys.argv[2])
for k in range(loops):
    environmentReliability = reliability
    timeArrayAvgT = []
    timeArrayAvgC = []
    timeTimeAvgT = []
    timeTimeAvgC = []
    subloops = int(sys.argv[3])
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
                agentArrayT[i] = independentGuessXAI.agentAction(agentArrayT[i], environmentReliability, agentArrayT, theTruth,0.38, 0.35)
                guessAccuracyT += independentGuessXAI.checkAgentGuessAccuracy(agentArrayT[i][4],theTruth)/len(agentArrayT)
                timeT += time.time() - startTime
                startTime = time.time()
                agentArrayC[i] = dependentGuessXAI.agentAction(agentArrayC[i], environmentReliability, agentArrayC, theTruth, 0.38, 0.35)
                guessAccuracyC += dependentGuessXAI.checkAgentGuessAccuracy(agentArrayC[i][4],theTruth)/len(agentArrayC)
                timeC += time.time() - startTime
            counter+=1
            if guessAccuracyT>0.75 and len(timeArrayAvgT)==j:
                timeArrayAvgT.append(timeT)
                timeTimeAvgT.append(timeT)
            if guessAccuracyC>0.75 and len(timeArrayAvgC)==j:
                timeArrayAvgC.append(timeC)
                timeTimeAvgC.append(timeC)
            if len(timeArrayAvgT+timeArrayAvgC) == 2*(j+1):
                continueLooping = False
            if counter >1000:
                if len(timeArrayAvgT)==j:
                    timeArrayAvgT.append(timeT)
                    timeTimeAvgT.append(timeT)
                if len(timeArrayAvgC)==j:
                    timeArrayAvgC.append(timeC)
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
plt.legend(["Independent","Dependent"])
plt.xlabel("Agent Reliability")
plt.ylabel("Time to 75% (s)")
plt.title("Guess Dependence Performance against $\it{A}$")
plt.savefig("Graphs/GuessTests/agentGuessTimeTestER"+str(int(100*reliability))+".png")
# plt.show()
