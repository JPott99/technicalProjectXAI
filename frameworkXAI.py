import string
import random

def genAgents(numOfAgents):
    # Function that generates a list containing a given number of agents.
    # Agent Form:
    #       [agentID, agentReliability, agentKnowledge, agentHypotheses, agentGuess, lastAction]
    # where agentID is a number for reference to the agent, agentReliability is a measure of
    # how likely an agent will relay correct information, and agentKnowledge,
    # agentHypotheses and agentGuess are empty arrays, at time of agent generation.
    agentArray = []
    for i in range(numOfAgents):
        reliability = defineReliability()
        agentKnowledge = []
        agentHypotheses = []
        agentGuess = []
        lastAction = "null"
        agentProfile = [i,reliability,agentKnowledge,agentHypotheses,agentGuess, lastAction]
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
        impartedWisdom = [theTruth[firstLetter],"<",theTruth[otherLetter], environmentReliability, ["E"]]
    else:
        impartedWisdom = [theTruth[otherLetter],"<",theTruth[firstLetter], environmentReliability, ["E"]]
    isMistDescended = random.uniform(0,1)
    if isMistDescended > environmentReliability:
        impartedWisdom = invertKnowledge(impartedWisdom)
    agentProfile[2] = checkKnowledge(agentProfile[2],impartedWisdom,agentProfile[0])
    return agentProfile

def invertKnowledge(knowledgeBit):
    # Function that takes a bit of knowledge and flips the comparison,
    # for use if agent/environment fail a reliability check.
    tempVar = knowledgeBit[0]
    knowledgeBit[0] = knowledgeBit[2]
    knowledgeBit[2] = tempVar
    return knowledgeBit

def meetAgent(agentProfile, agentArray):
    # A function that represents the agent being told a hypothesis, and given
    # evidence for why it is beleived.
    otherAgentID = agentProfile[0]
    while otherAgentID == agentProfile[0]:
        otherAgentID = random.randint(0,len(agentArray)-1)
    otherAgentProfile = agentArray[otherAgentID]
    if otherAgentProfile[3] != []:
        chosenHypothesis = random.choice(otherAgentProfile[3])
        for i in range(len(chosenHypothesis[4])):
            newKnowledge = otherAgentProfile[2][chosenHypothesis[4][i]]
            newKnowledge[3] = newKnowledge[3]*otherAgentProfile[1]
            willIScrewUp = random.uniform(0,1)
            if willIScrewUp > otherAgentProfile[1]:
                newKnowledge = invertKnowledge(newKnowledge)
            agentProfile[2] = checkKnowledge(agentProfile[2], newKnowledge, agentProfile[0])
    return agentProfile

def transitiveDeduction(agentProfile):
    # Function which checks through an agents knowledge base and identifies
    # if any obvious transitive deductions can be made in the form:
    # {x < y, b < x} -> {b < y}
    for i in range(len(agentProfile[2])):
        if agentProfile[2][i][1] == "<":
            for j in range(len(agentProfile[2])):
                if agentProfile[2][j][1] == "<":
                    if i != j:
                        if agentProfile[2][i][0] == agentProfile[2][j][2]:
                            # {x < y, b < x} -> {b < y}
                            combinedProb = agentProfile[2][i][3]*agentProfile[2][i][3]
                            newKnowledge = [agentProfile[2][j][0],"<",agentProfile[2][i][2],combinedProb,[str(agentProfile[0]) + "["+str(i)+"]"+"["+str(j)+"]"]]
                            agentProfile[2] = checkKnowledge(agentProfile[2],newKnowledge,agentProfile[0])
    return agentProfile

def checkKnowledge(agentKnowledge, newKnowledge, agentID):
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
    newKnowledge[4].append(agentID)
    agentKnowledge.append(newKnowledge)
    return agentKnowledge

def genHypotheses(agentProfile, theTruth):
    # A function that takes the knowledge of an agent, and converts it into
    # hypotheses about the position of each element in the truth.
    # A hypothesis exists in the form:
    #       [element,"=",position,agentBeleif,evidence]
    # where the evidence is a list of indexes for knowledge in the agentKnowledge.
    newHypothesis = [] # Gen new hypotheses.
    for i in theTruth:
        lessThans = 0
        greaterThans = 0
        hypothesisEvidence = []
        for j in range(len(agentProfile[2])):
            if agentProfile[2][j][0] == i:
                lessThans += 1
                hypothesisEvidence.append(j)
            elif agentProfile[2][j][2] == i:
                greaterThans += 1
                hypothesisEvidence.append(j)
        k = 0
        while k < greaterThans:
            newHypothesis.append([i,"=",k,0,hypothesisEvidence])
            k+=1
        while k < len(theTruth)-lessThans:
            newHypothesis.append([i,"=",k,1/(len(theTruth)-greaterThans-lessThans),hypothesisEvidence])
            k+=1
        while k < len(theTruth):
            newHypothesis.append([i,"=",k,0,hypothesisEvidence])
            k+=1
    agentGuess = guessTheTruth(newHypothesis, theTruth)
    agentProfile[3] = newHypothesis
    agentProfile[4] = agentGuess
    return agentProfile

def guessTheTruth(myHypothesis, theTruth):
    # A function that given a hypothesis, will create a possible ordering.
    # Currently treats each position as independent.
    myGuess = []
    for i in range(len(theTruth)):
        optionsList = []
        optionProbs = []
        for j in myHypothesis:
            if i == j[2] and j[3] > 0:
                optionsList.append(j[0])
                optionProbs.append(j[3])
        bestProb = max(optionProbs)
        bestOptions = []
        for i in range(len(optionProbs)):
            if optionProbs[i] == bestProb:
                bestOptions.append(i)
        bestOption = random.choice(bestOptions)
        myGuess.append(optionsList[bestOption])
    return myGuess

def agentThink(agentProfile, theTruth):
    # Function to represent an agent thinking through their knowledge.
    agentProfile = transitiveDeduction(agentProfile)
    agentProfile = genHypotheses(agentProfile, theTruth)
    return agentProfile

def agentAction(agentProfile, environmentReliability, agentArray, theTruth, chatChance, testChance):
    # Function to represent an agent deciding what to do, currently choosing to
    # learn from either the environment or another agent, or to think through
    # their existing knowledge
    whatToDo = random.uniform(0,1)
    if whatToDo < chatChance:
        agentProfile = meetAgent(agentProfile, agentArray)
        agentProfile[5] = "meet"
    elif whatToDo > 1-testChance:
        agentProfile = environmentKnowledge(agentProfile, environmentReliability, theTruth)
        agentProfile[5] = "test"
    else:
        if agentProfile[5] != "thought":
            agentProfile = agentThink(agentProfile, theTruth)
            agentProfile[5] = "thought"
    return agentProfile


def checkAgentGuessAccuracy(myGuess,theTruth):
    # A function that compares the accuracy of an agents guess against the truth.
    guessAccuracy = 0
    for i in range(len(myGuess)):
        if myGuess[i]==theTruth[i]:
            guessAccuracy += 1/len(myGuess)
    return guessAccuracy

theTruth = "123456789" #list(string.ascii_lowercase)
environmentReliability = 1
agentArray = genAgents(7)
counter  = 0
continueLooping = True
while continueLooping == True:
    guessAccuracy = 0
    for i in range(len(agentArray)):
        agentArray[i] = agentAction(agentArray[i], environmentReliability, agentArray, theTruth, 0.5, 0.1)
        guessAccuracy += checkAgentGuessAccuracy(agentArray[i][4],theTruth)/len(agentArray)
    counter+=1
    if guessAccuracy>0.80:
        continueLooping = False
        print(guessAccuracy)
        print(counter)
    if counter >10000:
        continueLooping = False
        print(guessAccuracy)
for i in agentArray:
    print(i)
