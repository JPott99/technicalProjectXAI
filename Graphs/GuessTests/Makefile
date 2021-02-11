rel1 = 1
rel2 = 0.99
rel3 = 0.9

loops = 25
subloops = 30
all:
	python guessAgentRelTest.py $(rel1) $(loops) $(subloops)
	python guessAgentRelTimeTest.py $(rel1) $(loops) $(subloops)
	python guessEnvRelTest.py $(rel1) $(loops) $(subloops)
	python guessEnvRelTimeTest.py $(rel1) $(loops) $(subloops)
	python guessAgentRelTest.py $(rel2) $(loops) $(subloops)
	python guessAgentRelTimeTest.py $(rel2) $(loops) $(subloops)
	python guessEnvRelTest.py $(rel2) $(loops) $(subloops)
	python guessEnvRelTimeTest.py $(rel2) $(loops) $(subloops)
	python guessAgentRelTest.py $(rel3) $(loops) $(subloops)
	python guessAgentRelTimeTest.py $(rel3) $(loops) $(subloops)
	python guessEnvRelTest.py $(rel3) $(loops) $(subloops)
	python guessEnvRelTimeTest.py $(rel3) $(loops) $(subloops)
