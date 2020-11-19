import random

def genAgents(numOfAgents, agentReliability):
    # Function that generates a list containing a given number of agents.
    # Agent Form:
    #       [agentID, agentReliability, agentKnowledge, agentHypotheses, agentGuess, lastAction]
    # where agentID is a number for reference to the agent, agentReliability is a measure of
    # how likely an agent will relay correct information, and agentKnowledge,
    # agentHypotheses and agentGuess are empty arrays, at time of agent generation.
    agentArray = []
    for i in range(numOfAgents):
        agentKnowledge = []
        agentHypotheses = []
        agentGuess = []
        lastAction = "null"
        agentProfile = [i,agentReliability,agentKnowledge,agentHypotheses,agentGuess, lastAction]
        agentArray.append(agentProfile)
    return agentArray

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
    whichTest = random.uniform(0,1)
    if whichTest < 0.1 or len(agentProfile[2]) < 4:
        firstLetter = random.randint(0,len(theTruth)-1)
        otherLetter = firstLetter
        while otherLetter == firstLetter:
            otherLetter = random.randint(0,len(theTruth)-1)
        history = ["E"]
    else:
        environmentReliability = environmentReliability*1.001
        minProb = 5
        for i in agentProfile[2]:
            if i[3] < minProb:
                minProb = i[3]
                knowledgeToTest = i
        firstLetter = theTruth.index(knowledgeToTest[0])
        otherLetter = theTruth.index(knowledgeToTest[2])
        history = knowledgeToTest[4] + ["E"]
    if firstLetter < otherLetter:
        impartedWisdom = [theTruth[firstLetter],"<",theTruth[otherLetter], environmentReliability, history]
    else:
        impartedWisdom = [theTruth[otherLetter],"<",theTruth[firstLetter], environmentReliability, history]
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
            newKnowledge = otherAgentProfile[2][chosenHypothesis[4][i]][:]
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
    newKnowledge = newKnowledge[:]
    for i in agentKnowledge:
        if i[0] == newKnowledge[0] and i[2] == newKnowledge[2]:
            if i[3]>newKnowledge[3]:
                return agentKnowledge
            else:
                i[3] = newKnowledge[3]
                i[4] = newKnowledge[4][:]+[agentID]
                return agentKnowledge
        if i[2] == newKnowledge[0] and i[0] == newKnowledge[2]:
            if i[3]>newKnowledge[3]:
                return agentKnowledge
            else:
                i[0] = newKnowledge[0]
                i[2] = newKnowledge[2]
                i[3] = newKnowledge[3]
                i[4] = newKnowledge[4][:]+[agentID]
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
    newHypothesis = []
    for i in theTruth:
        hypothesisEvidence = []
        relevantKnowledge= []
        for j in range(len(agentProfile[2])):
            if agentProfile[2][j][0] == i or agentProfile[2][j][2] == i:
                hypothesisEvidence+=[j]
                relevantKnowledge += [[agentProfile[2][j][0],"<",agentProfile[2][j][2],agentProfile[2][j][3]]]
        possibleWorlds = [[]]
        for j in relevantKnowledge:
            trueWorld = possibleWorlds.copy()
            falseWorld = []
            for k in possibleWorlds:
                falseWorld.append(k.copy())
            for k in range(len(possibleWorlds)):
                trueWorld[k].append(j)
                falseWorld[k].append(notTrue(j))
            possibleWorlds = trueWorld + falseWorld
        possibleHypotheses = []
        for j in possibleWorlds:
            possibleHypotheses.append(makeAHypothesis(j,i, theTruth))
        for j in range(len(possibleHypotheses[0])):
            weightedProb = 0
            for k in range(len(possibleHypotheses)):
                weightedProb += possibleHypotheses[k][j][3]
            newHypothesis.append([i,"=",j,weightedProb,hypothesisEvidence])
    agentGuess = guessTheTruth(newHypothesis, theTruth)
    agentProfile[3] = newHypothesis
    agentProfile[4] = agentGuess
    return agentProfile

def notTrue(knowledge):
    return [knowledge[2],"<",knowledge[0], 1-knowledge[3]]

def makeAHypothesis(knowledgeSet,i, theTruth):
    groupWeighting = 1
    lessThans = 0
    greaterThans = 0
    for j in knowledgeSet:
        groupWeighting = groupWeighting*j[3]
        if j[0] == i:
            lessThans += 1
        elif j[2] == i:
            greaterThans += 1
    k = 0
    myHypothesis = []
    while k < greaterThans:
        myHypothesis.append([i,"=",k,0])
        k+=1
    while k < len(theTruth)-lessThans:
        myHypothesis.append([i,"=",k,groupWeighting/(len(theTruth)-greaterThans-lessThans)])
        k+=1
    while k < len(theTruth):
        myHypothesis.append([i,"=",k,0])
        k+=1
    return myHypothesis

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
