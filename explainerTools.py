import csv
import frameworkXAI

def exportSim(agentArray):
    with open('exportedAgentArray.csv', mode='w', newline = '') as exporter:
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




theTruth = "12345" #list(string.ascii_lowercase)
environmentReliability = 0.99
agentArray = frameworkXAI.genAgents(50, 0.99)
counter  = 0
continueLooping = True
while continueLooping == True:
    guessAccuracy = 0
    for i in range(len(agentArray)):
        agentArray[i] = frameworkXAI.agentAction(agentArray[i], environmentReliability, agentArray, theTruth, 0.5, 0.1)
    counter+=1
    if counter > 100:
        continueLooping = False
print(agentArray[0][:-1])
exportSim(agentArray)
agentArrayI = importSim("exportedAgentArray.csv")
print(agentArrayI[0])
