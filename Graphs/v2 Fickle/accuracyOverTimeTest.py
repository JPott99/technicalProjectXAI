from fickleXAI import *
from matplotlib import pyplot as plt

theTruth = "12345" #list(string.ascii_lowercase)
subloops = 33
guessAccuraciesAvg0 = [0]*301
guessAccuraciesAvg1 = [0]*301
guessAccuraciesAvg2 = [0]*301
for j in range(subloops):
    print(j)
    agentArray0 = genAgents(50, 0.9)
    agentArray1 = genAgents(50, 0.9)
    agentArray2 = genAgents(50, 0.9)
    counter  = 0
    continueLooping = True
    guessAccuracies0 = []
    guessAccuracies1 = []
    guessAccuracies2 = []
    while continueLooping == True:
        guessAccuracy0 = 0
        guessAccuracy1 = 0
        guessAccuracy2 = 0
        for i in range(len(agentArray0)):
            agentArray0[i] = agentAction(agentArray0[i], 1, agentArray0, theTruth, 0.5, 0.1)
            guessAccuracy0 += checkAgentGuessAccuracy(agentArray0[i][4],theTruth)/len(agentArray0)
            agentArray1[i] = agentAction(agentArray1[i], 0.99, agentArray1, theTruth, 0.5, 0.1)
            guessAccuracy1 += checkAgentGuessAccuracy(agentArray1[i][4],theTruth)/len(agentArray1)
            agentArray2[i] = agentAction(agentArray2[i], 0.9, agentArray2, theTruth, 0.5, 0.1)
            guessAccuracy2 += checkAgentGuessAccuracy(agentArray2[i][4],theTruth)/len(agentArray2)
        guessAccuracies0.append(guessAccuracy0)
        guessAccuracies1.append(guessAccuracy1)
        guessAccuracies2.append(guessAccuracy2)
        counter+=1
        # if guessAccuracy>0.75:
        #     continueLooping = False
            # print(guessAccuracy)
            # print(counter-1)
        if counter >300:
            # print("TiME OUT!")
            continueLooping = False
            # print(guessAccuracy)
    for i in range(len(guessAccuracies0)):
        guessAccuraciesAvg0[i]+=guessAccuracies0[i]/subloops
        guessAccuraciesAvg1[i]+=guessAccuracies1[i]/subloops
        guessAccuraciesAvg2[i]+=guessAccuracies2[i]/subloops
    # for i in agentArray:
    #     print(i)
plt.plot(guessAccuraciesAvg0)
plt.plot(guessAccuraciesAvg1)
plt.plot(guessAccuraciesAvg2)
plt.legend(["e=100%","e=99%", "e=90%"])
plt.xlabel("Iterations")
plt.ylabel("Accuracy")
plt.title("Accuracy over Time")
plt.savefig("envTestOverTime.png")
plt.show()
