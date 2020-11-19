folderName = "v1 Zealous"
default:
	python chatChanceSpeedVsAgentCountSpeed.py $(folderName)
	python chatChanceSpeedVsTestCountSpeed.py $(folderName)
	python chatChanceAgentRel.py $(folderName)
	python testChanceVsEnvRel.py $(folderName)
	python truthLenVagentCount.py $(folderName)
