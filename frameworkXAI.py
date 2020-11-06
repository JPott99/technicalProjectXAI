import string
import random

def genAgents(numOfAgents):
    # Function that generates a list containing a given number of agents.
    # Agent Form:
    #       [agentID, agentReliability, agentKnowledge, agentHypotheses]
    # where agentID is a number for reference to the agent, agentReliability is a measure of
    # how likely an agent will relay correct information, and agentKnowledge
    # and agentHypotheses are empty arrays, at time of agent generation.
    agentArray = []
    for i in range(numOfAgents):
        reliability = defineReliability()
        agentKnowledge = []
        agentHypotheses = []
        agentProfile = [i,reliability,agentKnowledge,agentHypotheses]
        agentArray.append(agentProfile)
    return agentArray


def defineReliability():
    # A function that determines reliability of any agent.
    # Currently included for future use, so defaults to 1.
    return 1

def environmentKnowledge(agentProfile, environmentReliability):
    # Function that gives a given agent knowledge of a given reliability.
    # The knowledge is a statement comparing the positions of 2 letters of the
    # alphabet, known as theTruth. Two letters are compared, and then presented
    # to the agent in the form:
    #       [letter1, "<", letter2, agentBeleif, knowledgeHistory]
    # where the agentBeleif is how much the agent trusts the information (it is
    # assumed that agents know the reliability of the environment) and
    # knowledge is a list of where knowledge has come from, in this case
    # originating from "E", the environment, and passed to agentID.
    theTruth = list(string.ascii_lowercase)
    firstLetter = random.randint(0,len(theTruth)-1)
    otherLetter = firstLetter
    while otherLetter == firstLetter:
        otherLetter = random.randint(0,len(theTruth)-1)
    if firstLetter < otherLetter:
        impartedWisdom = [theTruth[firstLetter],"<",theTruth[otherLetter], environmentReliability, ["E", agentProfile[0]]]
    else:
        impartedWisdom = [theTruth[otherLetter],"<",theTruth[firstLetter], environmentReliability, ["E", agentProfile[0]]]
    isMistDescended = random.uniform(0,1)
    if isMistDescended > environmentReliability:
        impartedWisdom = [impartedWisdom[2],"<",impartedWisdom[0], environmentReliability, ["E", agentProfile[0]]]
    agentProfile[2].append(impartedWisdom)
    return agentProfile

def meetAgent(agentProfile, agentArray):
    otherAgentID = random.randint(0,len(agentArray))
    otherAgentProfile = agentArray[otherAgentID]

def transitiveDeduction(agentProfile):
    [agentID, agentReliability, agentKnowledge, agentHypotheses] = agentProfile
    for i in range(len(agentKnowledge)):
        if agentKnowledge[i][1] == "<":
            for j in range(len(agentKnowledge)):
                if agentKnowledge[j][1] == "<":
                    if i != j:
                        if agentKnowledge[i][0] == agentKnowledge[j][2]:
                            # {x < y, b < x} -> {b < y}
                            combinedProb = 1 #placeholder
                            newKnowledge = [agentKnowledge[j][0],"<",agentKnowledge[i][2],combinedProb,[str(agentID) + "["+str(i)+"]"+"["+str(j)+"]"]]
                            agentKnowledge = checkKnowledge(agentKnowledge,newKnowledge)
    agentProfile = [agentID, agentReliability, agentKnowledge, agentHypotheses]
    return agentProfile

def checkKnowledge(agentKnowledge, newKnowledge):
    for i in agentKnowledge:
        if i[0] == newKnowledge[0]:
            if i[2] == newKnowledge[2]:
                if i[3]>=newKnowledge[3]:
                    return agentKnowledge
                else:
                    i[3] = newKnowledge[3]
                    i[4].append(newKnowledge[4][0])
                    return agentKnowledge
    agentKnowledge.append(newKnowledge)
    return agentKnowledge


def agentThink(agentProfile):
    agentProfile = transitiveDeduction(agentProfile)
    return agentProfile

def agentAction(agentProfile, environmentReliability, agentArray):
    whatToDo = random.uniform(0,1)
    if whatToDo < 0.5:
        agentProfile = meetAgent(agentProfile, agentArray)
    elif whatToDo > 0.9:
        agentProfile = environmentKnowledge(agentProfile, environmentReliability)
    else:
        agentProfile = agentThink(agentProfile)
    return agentProfile

print(agentThink([0,1,[["a","<","b",1,["E",0]],["b","<","c",1,["E",0]]],[]]))
