from explainerTools import *
import frameworkXAI
import math
import matplotlib.pyplot as plt

theTruth = "12345"
agentArray = frameworkXAI.genAgents(50,0.99)
loops = 10
for k in range(loops):
    for i in range(len(agentArray)):
        agentArray[i] = frameworkXAI.agentAction(agentArray[i], 0.99, agentArray, theTruth, 0, 0.35, 0.35)
knowledgeChainGraph(agentArray,0,"Chains/", "Iter"+str(loops))
knowledgeChainSystemGraph(agentArray,"Chains/", "Iter"+str(loops))
loops = 15
for k in range(loops):
    for i in range(len(agentArray)):
        agentArray[i] = frameworkXAI.agentAction(agentArray[i], 0.99, agentArray, theTruth, 0, 0.35, 0.35)
knowledgeChainGraph(agentArray,0,"Chains/", "Iter"+str(loops+10))
knowledgeChainSystemGraph(agentArray,"Chains/", "Iter"+str(loops+10))
loops = 25
for k in range(loops):
    for i in range(len(agentArray)):
        agentArray[i] = frameworkXAI.agentAction(agentArray[i], 0.99, agentArray, theTruth, 0, 0.35, 0.35)
knowledgeChainGraph(agentArray,0,"Chains/", "Iter"+str(loops+25))
knowledgeChainSystemGraph(agentArray,"Chains/", "Iter"+str(loops+25))
loops = 50
for k in range(loops):
    for i in range(len(agentArray)):
        agentArray[i] = frameworkXAI.agentAction(agentArray[i], 0.99, agentArray, theTruth, 0, 0.35, 0.35)
knowledgeChainGraph(agentArray,0,"Chains/", "Iter"+str(loops+50))
knowledgeChainSystemGraph(agentArray,"Chains/", "Iter"+str(loops+50))
