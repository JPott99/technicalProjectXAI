# import zealousXAI
import fickleXAI
import testerXAI
import lessTesterXAI
import zealousTesterXAI
import greatTesterXAI
import sys
from matplotlib import pyplot as plt
import numpy as np
theTruth = "12345" #list(string.ascii_lowercase)
timeArrayZ = []
timeArrayZError = []
timeArrayF = []
timeArrayFError = []
timeArrayT = []
timeArrayTError = []
timeArrayTG = []
timeArrayTGError = []
loops = int(sys.argv[2])
reliability = float(sys.argv[1])
for k in range(loops):
    agentReliability = 0.5+(k+1)/loops*0.5
    # print(k, agentReliability)
    environmentReliability = reliability
    timeArrayAvgZ = []
    timeArrayAvgF = []
    timeArrayAvgT = []
    timeArrayAvgTG = []
    subloops = int(sys.argv[3])
    for j in range(subloops):
        agentArrayZ = fickleXAI.genAgents(50,agentReliability)
        agentArrayF = testerXAI.genAgents(50,agentReliability)
        agentArrayT = lessTesterXAI.genAgents(50,agentReliability)
        agentArrayTG = greatTesterXAI.genAgents(50,agentReliability)
        counter  = 0
        continueLooping = True
        while continueLooping == True:
            guessAccuracyZ = 0
            guessAccuracyF = 0
            guessAccuracyT = 0
            guessAccuracyTG = 0
            for i in range(len(agentArrayZ)):
                agentArrayZ[i] = fickleXAI.agentAction(agentArrayZ[i], environmentReliability, agentArrayZ, theTruth, 0.35, 0.35)
                guessAccuracyZ += fickleXAI.checkAgentGuessAccuracy(agentArrayZ[i][4],theTruth)/len(agentArrayZ)
                agentArrayF[i] = testerXAI.agentAction(agentArrayF[i], environmentReliability, agentArrayF, theTruth, 0.35, 0.35)
                guessAccuracyF += testerXAI.checkAgentGuessAccuracy(agentArrayF[i][4],theTruth)/len(agentArrayF)
                agentArrayT[i] = lessTesterXAI.agentAction(agentArrayT[i], environmentReliability, agentArrayT, theTruth, 0.35, 0.35)
                guessAccuracyT += lessTesterXAI.checkAgentGuessAccuracy(agentArrayT[i][4],theTruth)/len(agentArrayTG)
                agentArrayTG[i] = greatTesterXAI.agentAction(agentArrayTG[i], environmentReliability, agentArrayTG, theTruth, 0.35, 0.35)
                guessAccuracyTG += greatTesterXAI.checkAgentGuessAccuracy(agentArrayTG[i][4],theTruth)/len(agentArrayTG)
            counter+=1
            if guessAccuracyZ>0.75 and len(timeArrayAvgZ)==j:
                timeArrayAvgZ.append(counter)
            if guessAccuracyF>0.75 and len(timeArrayAvgF)==j:
                timeArrayAvgF.append(counter)
            if guessAccuracyT>0.75 and len(timeArrayAvgT)==j:
                timeArrayAvgT.append(counter)
            if guessAccuracyTG>0.75 and len(timeArrayAvgTG)==j:
                timeArrayAvgTG.append(counter)
            if len(timeArrayAvgZ+timeArrayAvgF+timeArrayAvgT+timeArrayAvgTG) == 4*(j+1):
                continueLooping = False
            if counter >1000:
                if len(timeArrayAvgZ)==j:
                    timeArrayAvgZ.append(counter)
                if len(timeArrayAvgF)==j:
                    timeArrayAvgF.append(counter)
                if len(timeArrayAvgT)==j:
                    timeArrayAvgT.append(counter)
                if len(timeArrayAvgTG)==j:
                    timeArrayAvgTG.append(counter)
                continueLooping = False
    timeArrayZ.append(sum(timeArrayAvgZ)/subloops)
    timeArrayZError.append(np.std(np.array(timeArrayAvgZ)))
    timeArrayF.append(sum(timeArrayAvgF)/subloops)
    timeArrayFError.append(np.std(np.array(timeArrayAvgF)))
    timeArrayT.append(sum(timeArrayAvgT)/subloops)
    timeArrayTError.append(np.std(np.array(timeArrayAvgT)))
    timeArrayTG.append(sum(timeArrayAvgTG)/subloops)
    timeArrayTGError.append(np.std(np.array(timeArrayAvgTG)))

firstNo = 1/loops*0.5+0.5
x = np.linspace(firstNo,1,loops)
plt.plot(x,timeArrayZ)
plt.fill_between(x,np.array(timeArrayZ)-np.array(timeArrayZError),np.array(timeArrayZ)+np.array(timeArrayZError), alpha = 0.5)
plt.plot(x,timeArrayF)
plt.fill_between(x,np.array(timeArrayF)-np.array(timeArrayFError),np.array(timeArrayF)+np.array(timeArrayFError), alpha = 0.5)
plt.plot(x,timeArrayT)
plt.fill_between(x,np.array(timeArrayT)-np.array(timeArrayTError),np.array(timeArrayT)+np.array(timeArrayTError), alpha = 0.5)
plt.plot(x,timeArrayTG)
plt.fill_between(x,np.array(timeArrayTG)-np.array(timeArrayTGError),np.array(timeArrayTG)+np.array(timeArrayTGError), alpha = 0.5)

plt.legend(["No Testing","Tester", "Lesser Tester","Greater Tester"])
plt.xlabel("Agent Reliability")
plt.ylabel("Number of Iterations to 75% accuracy")
plt.title("Performance of Testing Behaviours against $\it{A}$")
plt.savefig("Graphs/TesterTests/agentRelTestTestER"+str(int(100*reliability))+".png")
# plt.show()
