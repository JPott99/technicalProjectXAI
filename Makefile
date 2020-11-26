folderName = "v4 Super Fickle"
all:
	python chatChanceSpeedVsAgentCountSpeed.py $(folderName)
	python chatChanceSpeedVsTestChanceSpeed.py $(folderName)
	python chatChanceVsAgentRel.py $(folderName)
	python testChanceVsEnvRel.py $(folderName)
	python truthLenVagentCount.py $(folderName)
	python agentRelVenvRel.py $(folderName)
