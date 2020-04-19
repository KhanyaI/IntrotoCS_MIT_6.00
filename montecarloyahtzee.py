import random

"""
yahtze = []
leftover = []
numTrials = 10000
for i in range(0,numTrials+1):
	for i in range(0, 6):
		num = random.randrange(1,7)
		yahtze.append(num)
		yahtze.sort()
		yahtzeset = set(yahtze)
	
	if len(yahtzeset) == 1:
		print(yahtzeset, yahtzeset[i])
	else:
		leftover.append(yahtzeset)


"""

yahtze = 0
numTrials = 100
for i in range(0,numTrials+1):
	if random.random() < 0.83:
		yahtze += 1
prob = yahtze/numTrials
print(prob)


