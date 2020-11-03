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
