folderName = "v3.2 Zealous Tester"
all:
	python chatChanceSpeedVsAgentCountSpeed.py $(folderName)
	python chatChanceSpeedVsTestChanceSpeed.py $(folderName)
	python chatChanceVsAgentRel.py $(folderName)
	python testChanceVsEnvRel.py $(folderName)
	python truthLenVagentCount.py $(folderName)
	python agentRelVenvRel.py $(folderName)
