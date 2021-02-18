import csv
import frameworkXAI
import math
import matplotlib.pyplot as plt

def exportSim(agentArray, fileName = 'exportedAgentArray.csv'):
    with open(fileName, mode='w', newline = '') as exporter:
        csvWriter = csv.writer(exporter, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in agentArray:
            csvWriter.writerow(i[0:2])
            csvWriter.writerow(["Knowledge"])
            for j in i[2]:
                csvWriter.writerow(j)
            csvWriter.writerow(["Hypothesis"])
            for j in i[3]:
                csvWriter.writerow(j)
            csvWriter.writerow(["Guess"])
            csvWriter.writerow(i[4])

def importSim(fileName):
    with open(fileName) as file:
        csvReader = csv.reader(file, delimiter=',')
        importedData = []
        for row in csvReader:
            importedData.append(row)
    agentArray = []
    justReset = True
    lastWord = "null"
    for i in importedData:
        if justReset:
            justReset = False
            currentAgent = []
            currentAgent.append(int(i[0]))
            currentAgent.append(float(i[1]))
        if lastWord == "Knowledge" and len(i)>1:
            currentKnowledge = [i[0],i[1],i[2],float(i[3])]
            history = i[4][6:-1]+","
            buffer = []
            newHistory = ['E']
            for j in history:
                if j != ",":
                    if j != " ":
                        buffer.append(int(j))
                elif j == ",":
                    strings = [str(k) for k in buffer]
                    a_string = "".join(strings)
                    an_integer = int(a_string)
                    newHistory.append(an_integer)
                    buffer = []
            currentKnowledge.append(newHistory)
            currentData.append(currentKnowledge)
        if lastWord == "Hypothesis" and len(i)>1:
            currentHypothesis = [i[0],i[1],int(i[2]),float(i[3])]
            evidence = i[4][1:-1]+","
            buffer = []
            newHistory = []
            for j in evidence:
                if j != ",":
                    if j != " ":
                        buffer.append(int(j))
                elif j == ",":
                    strings = [str(k) for k in buffer]
                    a_string = "".join(strings)
                    an_integer = int(a_string)
                    newHistory.append(an_integer)
                    buffer = []
            currentHypothesis.append(newHistory)
            currentData.append(currentHypothesis)
        if lastWord == "Guess":
            currentAgent.append(i)
            agentArray.append(currentAgent)
            justReset = True
            lastWord = "null"
        if i == ["Knowledge"]:
            lastWord = i[0]
            currentData = []
        if i == ["Hypothesis"]:
            lastWord = i[0]
            currentAgent.append(currentData)
            currentData = []
        if i == ["Guess"]:
            currentAgent.append(currentData)
            lastWord = i[0]
    return agentArray

def showFacts(agentArray,agentID, partsToShow = "all"):
    i = agentArray[agentID]
    for j in range(len(i[2])):
        if partsToShow != "all":
            for k in partsToShow:
                if k in i[2][j]:
                    printFacts(i[2],j, agentID)
        else:
            printFacts(i[2],j, agentID)


def printFacts(agentFacts, factID, agentID):
    print("Agent",agentID,"believes Fact", factID,"("+ str(agentFacts[factID][0]), agentFacts[factID][1],str(agentFacts[factID][2])+")", "with beleif of", str(agentFacts[factID][3])+".")

def explainFact(agentArray,agentID,factID):
    currentFact = agentArray[agentID][2][factID]
    lengthOfChain = len(currentFact[4])-1
    if lengthOfChain%10 == 1:
        numEnd = "st"
    elif lengthOfChain%10 == 2:
        numEnd = "nd"
    elif lengthOfChain%10 == 3:
        numEnd = "rd"
    else:
        numEnd = "th"
    print("Agent",agentID,"learned",currentFact[0], currentFact[1],currentFact[2], "as", str(lengthOfChain)+numEnd,"hand Knowledge with chain",currentFact[4], "giving beleif", str(currentFact[3])+".")

def showHypotheses(agentArray, agentID, partsToShow = "all"):
    i = agentArray[agentID]
    lengthToIterate = int(math.sqrt(len(i[3])))
    for j in range(lengthToIterate):
        j = j*lengthToIterate
        if partsToShow != "all":
            for k in partsToShow:
                if k == i[3][j][0]:
                    printHypotheses(i[3],j, agentID)
        else:
            printHypotheses(i[3],j, agentID)

def printHypotheses(agentHypotheses, hypothesisID, agentID):
    counter = 0
    posBeleifs = []
    while counter < 5:
        posBeleifs.append([hypothesisID+counter])
        posBeleifs.append(agentHypotheses[hypothesisID+counter][3])
        counter += 1
    print("Agent",agentID, "believes that", agentHypotheses[hypothesisID][0], "has position distribution", str(posBeleifs)+".")

def explainHypothesis(agentArray,agentID, hypothesisID):
    currentHypothesis = agentArray[agentID][3][hypothesisID]
    hypothesisEvidence = currentHypothesis[4]
    evidenceList = []
    for i in hypothesisEvidence:
        evidence = agentArray[agentID][2][i]
        evidenceToJoin = ["("+str(i)+")"," "]+evidence[:3]+[" ","("+str(evidence[3])+")"]
        evidenceString = "".join(evidenceToJoin)
        evidenceList.append(evidenceString)
    print("Agent", agentID, "thinks", currentHypothesis[0],"is in position",currentHypothesis[2],"with beleif",currentHypothesis[3], "becuase", str(evidenceList)+".")


def makeHypothesisGraph(agentArray, agentID, elementID, dir = "", title = ""):
    currentHypotheses = agentArray[agentID][3]
    values = []
    for i in currentHypotheses:
        if elementID in i:
            values.append(i[3])
    x = list(range(1,len(values)+1))
    plt.figure()
    plt.bar(x, values)
    plt.xlabel('Position')
    plt.ylabel('Belief')
    plt.title('Distribution in Agent '+ str(agentID) + '\'s belief in Element '+ elementID+'\'s position.')
    plt.savefig(dir+"beleifDistAgent"+str(agentID)+"El"+elementID+title+".png")

def makeSystemHypothesisGraph(agentArray,elementID, dir = "", title = ""):
    agentCount = len(agentArray)
    values = []
    for i in agentArray:
        currentHypotheses = i[3]
        for k in currentHypotheses:
            if elementID in k:
                if len(values)<=k[2]:
                    values.append(0)
                values[k[2]]+=k[3]/agentCount
    x = list(range(1,len(values)+1))
    plt.figure()
    plt.bar(x, values)
    plt.xlabel('Position')
    plt.ylabel('Belief')
    plt.title('Distribution of System\'s belief in Element '+ elementID+'\'s position.')
    plt.savefig(dir+"beleifDistSystemEl"+elementID+title+".png")

def knowledgeChainGraph(agentArray,agentID, dir="", title=""):
    currentKnowledge = agentArray[agentID][2]
    values = [0]
    for i in currentKnowledge:
        lenChain = len(i[4])
        while len(values) <= lenChain-2:
            values.append(0)
        values[lenChain-2]+=1
    x = list(range(1,len(values)+1))
    plt.figure()
    plt.bar(x, values)
    plt.xlabel('Degrees Of Seperation from Knowledge Source')
    plt.ylabel('Count')
    plt.title('Distribution of Agent '+ str(agentID) + '\'s knowledge degree.')
    plt.savefig(dir+"knowledgeDegreeAgent"+str(agentID)+title+".png")

def knowledgeChainSystemGraph(agentArray, dir="", title=""):
    values = [0]
    for agentID in range(len(agentArray)):
        currentKnowledge = agentArray[agentID][2]
        for i in currentKnowledge:
            lenChain = len(i[4])
            while len(values) <= lenChain-2:
                values.append(0)
            values[lenChain-2]+=1
    x = list(range(1,len(values)+1))
    plt.figure()
    plt.bar(x, values)
    plt.xlabel('Degrees Of Seperation from Knowledge Source')
    plt.ylabel('Count')
    plt.title('Distribution of System\'s knowledge degree.')
    plt.savefig(dir+"knowledgeDegreeSystem"+title+".png")

def guessAccuracyGraph(agentArray, guessFunction, theTruth,dir="", title=""):
    values = []
    for i in agentArray:
        currentGuess = i[4]
        guessAcc = guessFunction(currentGuess, theTruth)
        values.append(guessAcc)
    x = list(range(1,len(values)+1))
    plt.figure()
    plt.bar(x, values)
    plt.xlabel('Agent')
    plt.ylabel('Guess Accuracy')
    plt.title('Guess Accuracy of Each Agent in System.')
    plt.savefig(dir+"allAgentGuessAcc"+title+".png")

def findMaxChainLength(agentArray):
    for agentID in range(len(agentArray)):
        currentKnowledge = agentArray[agentID][2]
        maxChain = 0
        for i in currentKnowledge:
            lenChain = len(i[4])-1
            if lenChain > maxChain:
                maxChain = lenChain
    return maxChain

def graphMaxChainLen(maxChainA,dir="", title=""):
    plt.figure()
    plt.plot(maxChainA)
    plt.xlabel('Iterations')
    plt.ylabel('Maximum Chain Length')
    plt.title('Maximum Chain Length over Time')
    plt.savefig(dir+"maxChainGraph"+title+".png")

def findAvgChainLength(agentArray):
    for agentID in range(len(agentArray)):
        currentKnowledge = agentArray[agentID][2]
        avgChain = []
        for i in currentKnowledge:
            lenChain = len(i[4])-1
            avgChain.append(lenChain)
    if len(avgChain)>0:
        avgChainFin = sum(avgChain)/len(avgChain)
    else:
        avgChainFin = 0
    return avgChainFin

def graphAvgChainLen(avgChainA,dir="", title=""):
    plt.figure()
    plt.plot(avgChainA)
    plt.xlabel('Iterations')
    plt.ylabel('Average Chain Length')
    plt.title('Average Chain Length over Time')
    plt.savefig(dir+"avgChainGraph"+title+".png")

# Testing code for import export functions.
# theTruth = "12345" #list(string.ascii_lowercase)
# environmentReliability = 0.99
# agentArray = frameworkXAI.genAgents(50, 0.99)
# counter  = 0
# continueLooping = True
# while continueLooping == True:
#     guessAccuracy = 0
#     for i in range(len(agentArray)):
#         agentArray[i] = frameworkXAI.agentAction(agentArray[i], environmentReliability, agentArray, theTruth, 0.5, 0.1)
#     counter+=1
#     if counter > 100:
#         continueLooping = False
# print(agentArray[0][:-1])
# exportSim(agentArray)
# agentArrayI = importSim("exportedAgentArray.csv")
# agentArray = importSim("exportedAgentArray.csv")
theTruth = "12345"
agentArray = frameworkXAI.genAgents(50,0.99)
loops = 300
avgChainA = []
maxChainA = []
for k in range(loops):
    for i in range(len(agentArray)):
        agentArray[i] = frameworkXAI.agentAction(agentArray[i], 0.99, agentArray, theTruth, 0.5, 0.1)
    avgChainA.append(findAvgChainLength(agentArray))
    maxChainA.append(findMaxChainLength(agentArray))
graphAvgChainLen(avgChainA,"Graphs/Explainer/", "testChance10")
graphMaxChainLen(maxChainA,"Graphs/Explainer/", "testChance10")
# makeHypothesisGraph(agentArray,0,'1',"Graphs/Explainer/", "25Iter")
# makeSystemHypothesisGraph(agentArray,'1',"Graphs/Explainer/", "25Iter")
# knowledgeChainSystemGraph(agentArray,"Graphs/Explainer/", "Iter"+str(loops))
guessAccuracyGraph(agentArray,frameworkXAI.checkAgentGuessAccuracy, theTruth,"Graphs/Explainer/", "Iter"+str(loops))
# print(agentArray[0])
# showFacts(agentArray,0,["1"])
# explainFact(agentArray,0,0)
# showHypotheses(agentArray,0)
# explainHypothesis(agentArray,0,0)
