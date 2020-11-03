import string

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


print(genAgents(5))
