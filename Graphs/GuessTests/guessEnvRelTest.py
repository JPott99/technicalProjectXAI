import independentGuessXAI
import dependentGuessXAI
from matplotlib import pyplot as plt
import numpy as np
import sys
reliability = float(sys.argv[1])
theTruth = "12345" #list(string.ascii_lowercase)
timeArrayT = []
timeArrayTError = []
timeArrayC = []
timeArrayCError = []
loops = int(sys.argv[2])
for k in range(loops):
    environmentReliability = 0.7+(k+1)/loops*0.3
    timeArrayAvgT = []
    timeArrayAvgC = []
    subloops = int(sys.argv[3])
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
                agentArrayT[i] = independentGuessXAI.agentAction(agentArrayT[i], environmentReliability, agentArrayT, theTruth,0, 0.35, 0.35)
                guessAccuracyT += independentGuessXAI.checkAgentGuessAccuracy(agentArrayT[i][4],theTruth)/len(agentArrayT)
                agentArrayC[i] = dependentGuessXAI.agentAction(agentArrayC[i], environmentReliability, agentArrayC, theTruth,0, 0.35, 0.35)
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
    timeArrayTError.append(np.std(np.array(timeArrayAvgT)))
    timeArrayC.append(sum(timeArrayAvgC)/subloops)
    timeArrayCError.append(np.std(np.array(timeArrayAvgC)))

    # for i in agentArray:
    #     print(i)
firstNo = 1/loops*0.3+0.7
x = np.linspace(firstNo,1,loops)
plt.plot(x,timeArrayT)
plt.fill_between(x,np.array(timeArrayT)-np.array(timeArrayTError),np.array(timeArrayT)+np.array(timeArrayTError), alpha = 0.5)
plt.plot(x,timeArrayC)
plt.fill_between(x,np.array(timeArrayC)-np.array(timeArrayCError),np.array(timeArrayC)+np.array(timeArrayCError), alpha = 0.5)
plt.legend(["Independent","Dependent"])
plt.xlabel("Environmental Reliability")
plt.ylabel("Iterations to 75%")
plt.title("Guess Dependence Performance against $\it{E}$")
plt.savefig("Graphs/GuessTests/envGuessTestAR"+str(int(100*reliability))+".png")
# plt.show()
