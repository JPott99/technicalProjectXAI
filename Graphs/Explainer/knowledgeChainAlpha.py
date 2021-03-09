import frameworkXAI
import explainerTools
import sys
from matplotlib import pyplot as plt
import numpy as np
theTruth = "12345" #list(string.ascii_lowercase)
timeArray = []
timeArrayError = []
loops = 100
# input = float(sys.argv[1])
for k in range(loops):
    agentReliability = 0.99
    # print(k, agentReliability)
    environmentReliability = 0.99
    timeArrayAvg = []
    subloops = 15
    for j in range(subloops):
        agentArray = frameworkXAI.genAgents(50,agentReliability)
        counter  = 0
        continueLooping = True
        while continueLooping == True:
            guessAccuracy = 0
            for i in range(len(agentArray)):
                agentArray[i] = frameworkXAI.agentAction(agentArray[i], environmentReliability, agentArray, theTruth,-1+k/loops*2, 0.35, 0.35)
                guessAccuracy += frameworkXAI.checkAgentGuessAccuracy(agentArray[i][4],theTruth)/len(agentArray)
            counter+=1
            # if guessAccuracy>0.75 and len(timeArrayAvg)==j:
            #     timeArrayAvg.append(counter)
            if counter >100:
                if len(timeArrayAvg)==j:
                    continueLooping = False
            if len(timeArrayAvg) == 1*(j+1):
                continueLooping = False
        timeArrayAvg.append(explainerTools.findAvgChainLength(agentArray))
        # print(k,explainerTools.findAvgChainLength(agentArray))
    # print(timeArrayAvg)
    timeArray.append(sum(timeArrayAvg)/subloops)
    timeArrayError.append(np.std(np.array(timeArrayAvg)))

firstNo = -1
x = np.linspace(firstNo,1,loops)
plt.plot(x,timeArray)
plt.fill_between(x,np.array(timeArray)-np.array(timeArrayError),np.array(timeArray)+np.array(timeArrayError), alpha = 0.5)

plt.xlabel(r"$\alpha$ Factor of Flexibility")
plt.ylabel("Average Chain Length")
plt.title(r"Average Chain Length against $\alpha$ Factor")
plt.savefig("aRatioA"+str(int(100*agentReliability))+"E"+str(int(100*environmentReliability))+".png")
# plt.show()
