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

def environmentKnowledge(agentProfile, environmentReliability, theTruth):
    # Function that gives a given agent knowledge of a given reliability.
    # The knowledge is a statement comparing the positions of 2 letters of the
    # alphabet, known as theTruth. Two letters are compared, and then presented
    # to the agent in the form:
    #       [letter1, "<", letter2, agentBeleif, knowledgeHistory]
    # where the agentBeleif is how much the agent trusts the information (it is
    # assumed that agents know the reliability of the environment) and
    # knowledge is a list of where knowledge has come from, in this case
    # originating from "E", the environment, and passed to agentID.
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
        impartedWisdom = invertKnowledge(impartedWisdom)
    agentProfile[2].append(impartedWisdom)
    return agentProfile

def invertKnowledge(knowledgeBit):
    # Function that takes a bit of knowledge and flips the comparison,
    # for use if agent/environment fail a reliability check.
    tempVar = knowledgeBit[0]
    knowledgeBit[0] = knowledgeBit[2]
    knowledgeBit[2] = tempVar
    return knowledgeBit

def meetAgent(agentProfile, agentArray):
    otherAgentID = random.randint(0,len(agentArray)-1)
    otherAgentProfile = agentArray[otherAgentID]

def transitiveDeduction(agentProfile):
    # Function which checks through an agents knowledge base and identifies
    # if any obvious transitive deductions can be made in the form:
    # {x < y, b < x} -> {b < y}
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
    # Function that checks that the knowledge about to be learned is novel,
    # and if not checks if it is more beleived than the existing knowledge
    # and replaces the knowledge if so.
    for i in agentKnowledge:
        if i[0] == newKnowledge[0]:
            if i[2] == newKnowledge[2]:
                if i[3]>=newKnowledge[3]:
                    return agentKnowledge
                else:
                    i[3] = newKnowledge[3]
                    i[4] = newKnowledge[4]
                    return agentKnowledge
    agentKnowledge.append(newKnowledge)
    return agentKnowledge

def genHypotheses(agentProfile, truthLength):
    [agentID, agentReliability, agentKnowledge, agentHypotheses] = agentProfile
    agentHypotheses = [] # Reset hypotheses.

def agentThink(agentProfile, truthLength):
    # Function to represent an agent thinking through their knowledge.
    agentProfile = transitiveDeduction(agentProfile)
    agentProfile = genHypotheses(agentProfile, truthLength)
    return agentProfile

def agentAction(agentProfile, environmentReliability, agentArray, theTruth):
    # Function to represent an agent deciding what to do, currently choosing to
    # learn from either the environment or another agent, or to think through
    # their existing knowledge
    whatToDo = random.uniform(0,1)
    if whatToDo < 0.5:
        agentProfile = meetAgent(agentProfile, agentArray)
    elif whatToDo > 0.9:
        agentProfile = environmentKnowledge(agentProfile, environmentReliability, theTruth)
    else:
        agentProfile = agentThink(agentProfile, len(theTruth))
    return agentProfile


theTruth = "pith"#list(string.ascii_lowercase)
environmentReliability = 1
agentArray = genAgents(30)
counter  = 0
continueLooping = True
while continueLooping == True:
    for i in agentArray:
        i = agentAction(i, environmentReliability, agentArray, theTruth)
    counter+=1
    if counter == 30:
        continueLooping = False
if agentArray[0][2] != []:
    print(agentArray[0])
