rel1 = 1
rel2 = 0.99
rel3 = 0.9

loops = 1
subloops = 1

all:
	python Graphs/FlexTests/agentRelOverTime.py 1 $(loops) $(subloops)
	python Graphs/FlexTests/agentRelOverTime.py 0.99 $(loops) $(subloops)
	python Graphs/FlexTests/agentRelOverTime.py 0.9 $(loops) $(subloops)
	python Graphs/FlexTests/envRelOverTime.py 1 $(loops) $(subloops)
	python Graphs/FlexTests/envRelOverTime.py 0.99 $(loops) $(subloops)
	python Graphs/FlexTests/envRelOverTime.py 0.9 $(loops) $(subloops)
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
	python Graphs/TesterTests/agentRelOverTime.py 1 $(loops) $(subloops)
	python Graphs/TesterTests/agentRelOverTime.py 0.99 $(loops) $(subloops)
	python Graphs/TesterTests/agentRelOverTime.py 0.9 $(loops) $(subloops)
	python Graphs/TesterTests/envRelOverTime.py 1 $(loops) $(subloops)
	python Graphs/TesterTests/envRelOverTime.py 0.99 $(loops) $(subloops)
	python Graphs/TesterTests/envRelOverTime.py 0.9 $(loops) $(subloops)
	python Graphs/TransTests/transitivityAgentRelTest.py $(rel1) $(loops) $(subloops)
	python Graphs/TransTests/transitivityAgentRelTimeTest.py $(rel1) $(loops) $(subloops)
	python Graphs/TransTests/transitivityEnvRelTest.py $(rel1) $(loops) $(subloops)
	python Graphs/TransTests/transitivityEnvRelTimeTest.py $(rel1) $(loops) $(subloops)
	python Graphs/TransTests/transitivityAgentRelTest.py $(rel2) $(loops) $(subloops)
	python Graphs/TransTests/transitivityAgentRelTimeTest.py $(rel2) $(loops) $(subloops)
	python Graphs/TransTests/transitivityEnvRelTest.py $(rel2) $(loops) $(subloops)
	python Graphs/TransTests/transitivityEnvRelTimeTest.py $(rel2) $(loops) $(subloops)
	python Graphs/TransTests/transitivityAgentRelTest.py $(rel3) $(loops) $(subloops)
	python Graphs/TransTests/transitivityAgentRelTimeTest.py $(rel3) $(loops) $(subloops)
	python Graphs/TransTests/transitivityEnvRelTest.py $(rel3) $(loops) $(subloops)
	python Graphs/TransTests/transitivityEnvRelTimeTest.py $(rel3) $(loops) $(subloops)
