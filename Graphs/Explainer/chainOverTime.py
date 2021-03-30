from explainerTools import *
import frameworkXAI
import math
import matplotlib.pyplot as plt
import numpy as np

theTruth = "12345"
loops = 200
avgChain = []
maxChain = []
for i in range(loops):
    avgChain.append([])
    maxChain.append([])
subloops = 100
for j in range(subloops):
    agentArray = frameworkXAI.genAgents(50,0.99)
    for k in range(loops):
        for i in range(len(agentArray)):
            agentArray[i] = frameworkXAI.agentAction(agentArray[i], 0.99, agentArray, theTruth, 0, 0.1, 0.6)
        avgChain[k].append(findAvgChainLength(agentArray))
        maxChain[k].append(findMaxChainLength(agentArray))

avgChainA = []
avgChainE = []
for i in avgChain:
    avgChainA.append(sum(i)/len(i))
    avgChainE.append(np.std(np.array(i)))
graphAvgChainLen(avgChainA,avgChainE,"Chains/",str(loops)+"test60")

maxChainA = []
maxChainE = []
for i in maxChain:
    maxChainA.append(sum(i)/len(i))
    maxChainE.append(np.std(np.array(i)))
graphMaxChainLen(maxChainA,maxChainE,"Chains/",str(loops)+"test60")
