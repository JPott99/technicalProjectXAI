rel1 = 1
rel2 = 0.99
rel3 = 0.9

loops = 25
subloops = 25

all:
	python Graphs/FlexTests/agentRelOverTime.py 1
	python Graphs/FlexTests/agentRelOverTime.py 0.99
	python Graphs/FlexTests/agentRelOverTime.py 0.9
	python Graphs/FlexTests/envRelOverTime.py 1
	python Graphs/FlexTests/envRelOverTime.py 0.99
	python Graphs/FlexTests/envRelOverTime.py 0.9
	python Graphs/GuessTests/guessAgentRelTest.py $(rel1) $(loops) $(subloops)
	python Graphs/GuessTests/guessAgentRelTimeTest.py $(rel1) $(loops) $(subloops)
	python Graphs/GuessTests/guessEnvRelTest.py $(rel1) $(loops) $(subloops)
	python Graphs/GuessTests/guessEnvRelTimeTest.py $(rel1) $(loops) $(subloops)
	python Graphs/GuessTests/guessAgentRelTest.py $(rel2) $(loops) $(subloops)
	python Graphs/GuessTests/guessAgentRelTimeTest.py $(rel2) $(loops) $(subloops)
	python Graphs/GuessTests/guessEnvRelTest.py $(rel2) $(loops) $(subloops)
	python Graphs/GuessTests/guessEnvRelTimeTest.py $(rel2) $(loops) $(subloops)
	python Graphs/GuessTests/guessAgentRelTest.py $(rel3) $(loops) $(subloops)
	python Graphs/GuessTests/guessAgentRelTimeTest.py $(rel3) $(loops) $(subloops)
	python Graphs/GuessTests/guessEnvRelTest.py $(rel3) $(loops) $(subloops)
	python Graphs/GuessTests/guessEnvRelTimeTest.py $(rel3) $(loops) $(subloops)
	python Graphs/TesterTests/agentRelOverTime.py 1
	python Graphs/TesterTests/agentRelOverTime.py 0.99
	python Graphs/TesterTests/agentRelOverTime.py 0.9
	python Graphs/TesterTests/envRelOverTime.py 1
	python Graphs/TesterTests/envRelOverTime.py 0.99
	python Graphs/TesterTests/envRelOverTime.py 0.9
	python Graphs/TransTests/transitivityAgentRelTest.py $(rel1)
	python Graphs/TransTests/transitivityAgentRelTimeTest.py $(rel1)
	python Graphs/TransTests/transitivityEnvRelTest.py $(rel1)
	python Graphs/TransTests/transitivityEnvRelTimeTest.py $(rel1)
	python Graphs/TransTests/transitivityAgentRelTest.py $(rel2)
	python Graphs/TransTests/transitivityAgentRelTimeTest.py $(rel2)
	python Graphs/TransTests/transitivityEnvRelTest.py $(rel2)
	python Graphs/TransTests/transitivityEnvRelTimeTest.py $(rel2)
	python Graphs/TransTests/transitivityAgentRelTest.py $(rel3)
	python Graphs/TransTests/transitivityAgentRelTimeTest.py $(rel3)
	python Graphs/TransTests/transitivityEnvRelTest.py $(rel3)
	python Graphs/TransTests/transitivityEnvRelTimeTest.py $(rel3)
