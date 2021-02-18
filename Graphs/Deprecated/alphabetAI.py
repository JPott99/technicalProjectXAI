import string
import random

def genAgents():
    alphabet = list(string.ascii_lowercase)
    agentDB = []
    for i in range(len(alphabet)):
        agentProfile = [alphabet[i]]
        if random.randint(0,5) == 0:
            agentProfile.append([[alphabet[i],"=",i,1,[alphabet[i]]]])
        else:
            agentK = random.randint(0,25)
            if agentK != i:
                if i<agentK:
                    agentProfile.append([[alphabet[i],"<",alphabet[agentK],1,[alphabet[i]]]])
                if i>agentK:
                    agentProfile.append([[alphabet[i],">",alphabet[agentK],1,[alphabet[i]]]])
            else:
                agentProfile.append([[alphabet[agentK],"=",agentK,1,[alphabet[i]]]])
        agentDB.append(agentProfile)
    random.shuffle(agentDB)
    return agentDB

def meetAgents(agent1, agent2):
    [agent1Name,agent1Knowledge] = agent1
    [agent2Name,agent2Knowledge] = agent2
    agent1KnowledgeNew = random.choice(agent2Knowledge)
    agent2KnowledgeNew = random.choice(agent1Knowledge)
    does1KnowThis = False
    for i in agent1Knowledge:
        if i[0:3] == agent1KnowledgeNew[0:3]:
            does1KnowThis = True
    if does1KnowThis == False:
        agent1Prop = agent1KnowledgeNew[4] + [agent1Name]
        agent1Knowledge.append(agent1KnowledgeNew[0:4]+[agent1Prop])
    does2KnowThis = False
    for i in agent2Knowledge:
        if i[0:3] == agent2KnowledgeNew[0:3]:
            does2KnowThis = True
    if does2KnowThis == False:
        agent2Prop = agent2KnowledgeNew[4] + [agent2Name]
        agent2Knowledge.append(agent2KnowledgeNew[0:4]+[agent2Prop])
    return [[agent1Name,agent1Knowledge],[agent2Name,agent2Knowledge]]

def checkMyKnowledge(agent):
    [agentName,agentKnowledge] = agent
    for i in range(len(agentKnowledge)):
        for j in range(len(agentKnowledge)):
            if i != j:
                if areTwoFigsTheSame(agentKnowledge[i][0],agentKnowledge[j][0]):
                    agentKnowledge = createNewKnowledge(agentKnowledge[i],0,agentKnowledge[j],0,agentKnowledge,agentName)
                if areTwoFigsTheSame(agentKnowledge[i][0],agentKnowledge[j][2]):
                    agentKnowledge = createNewKnowledge(agentKnowledge[i],0,agentKnowledge[j],2,agentKnowledge,agentName)
                if areTwoFigsTheSame(agentKnowledge[i][2],agentKnowledge[j][0]):
                    agentKnowledge = createNewKnowledge(agentKnowledge[i],2,agentKnowledge[j],0,agentKnowledge,agentName)
                if areTwoFigsTheSame(agentKnowledge[i][2],agentKnowledge[j][2]):
                    agentKnowledge = createNewKnowledge(agentKnowledge[i],2,agentKnowledge[j],2,agentKnowledge,agentName)
    return [agentName, agentKnowledge]

def areTwoFigsTheSame(i,j):
    if isinstance(i,str) and isinstance(j,str):
        if i == j:
            return True
    return False

def createNewKnowledge(i,iIndex, j, jIndex, agentKnowledge, agentName):
    newKnowledge = 0
    # {(x < y; x > z),(x < y; z < x),(y > x; z < x), (y > x; x > z)}  -> {y > z, z < y}
    if iIndex == jIndex:
        if iIndex == 0:
            if (i[1] == "<" and j[1] == ">"):
                newKnowledge = [j[2],"<",i[2],1,[agentName]]
        else:
            if (i[1] == ">" and j[1] == "<"):
                newKnowledge = [j[2],"<",i[2],1,[agentName]]
    else:
        if iIndex == 0:
            if (i[1] == "<" and j[1] == "<"):
                newKnowledge = [j[2],"<",i[2],1,[agentName]]
        else:
            if (i[1] == ">" and j[1] == ">"):
                newKnowledge = [j[2],"<",i[2],1,[agentName]]
    # If either knowledge is "="
    if i[1] != j[1]:
        if i[1] == "=":
            if jIndex == 2:
                newKnowledge = [j[0],j[1],i[2],1,[agentName]]
            else:
                newKnowledge = [i[0],j[1],j[2],1,[agentName]]
        if j[1] == "=":
            if iIndex == 2:
                newKnowledge = [i[0],i[1],j[2],1,[agentName]]
            else:
                newKnowledge = [j[2],i[1],i[2],1,[agentName]]

    for i in agentKnowledge:
        if newKnowledge != 0:
            if i[0:3] == newKnowledge[0:3]:
                newKnowledge = 0
    # any other combo is useless...
    if newKnowledge == 0:
        return agentKnowledge
    else:
        if newKnowledge[0] != newKnowledge[2]:
            print(agentName,"worked out that",newKnowledge[0],newKnowledge[1],newKnowledge[2])
            return (agentKnowledge+[newKnowledge])
        else:
            return agentKnowledge


agentDB = genAgents()

for counter in range(10):
    for i in range(len(agentDB)):
        agentToMeet = i
        while agentToMeet == i:
            agentToMeet = random.randint(0,25)
        agentDB[i],agentDB[agentToMeet] = meetAgents(agentDB[i],agentDB[agentToMeet])
        agentDB[i] = checkMyKnowledge(agentDB[i])

print(agentDB)
