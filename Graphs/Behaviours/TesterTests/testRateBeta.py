import testerXAI
import sys
from matplotlib import pyplot as plt
import numpy as np
theTruth = "12345" #list(string.ascii_lowercase)
timeArray = []
timeArrayError = []
loops = 100
# input = float(sys.argv[1])
for k in range(loops):
    agentReliability = 0.5
    # print(k, agentReliability)
    environmentReliability = 0.99
    timeArrayAvg = []
    subloops = 100
    for j in range(subloops):
        agentArray = testerXAI.genAgents(50,agentReliability)
        counter  = 0
        continueLooping = True
        while continueLooping == True:
            guessAccuracy = 0
            for i in range(len(agentArray)):
                agentArray[i] = testerXAI.agentAction(agentArray[i], environmentReliability, agentArray, theTruth,0, 0.35, 0.35,k/loops)
                guessAccuracy += testerXAI.checkAgentGuessAccuracy(agentArray[i][4],theTruth)/len(agentArray)
            counter+=1
            if guessAccuracy>0.75 and len(timeArrayAvg)==j:
                timeArrayAvg.append(counter)
            if len(timeArrayAvg) == 1*(j+1):
                continueLooping = False
            if counter >1000:
                if len(timeArrayAvg)==j:
                    timeArrayAvg.append(counter)
    timeArray.append(sum(timeArrayAvg)/subloops)
    timeArrayError.append(np.std(np.array(timeArrayAvg)))


firstNo = 0
x = np.linspace(firstNo,1,loops)
plt.plot(x,timeArray)
plt.fill_between(x,np.array(timeArray)-np.array(timeArrayError),np.array(timeArray)+np.array(timeArrayError), alpha = 0.5)


# plt.legend(["No Testing","25% Tester", "50% Tester","75% Tester"])
plt.xlabel("Testing Rate")
plt.ylabel("Number of Iterations to 75% accuracy")
plt.title("Performance against testing rate.")
plt.savefig("TestingRateLowEnv.png")
# plt.show()
