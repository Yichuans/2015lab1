import numpy as np


n_simulations = 1000


def guess_value():
	# random guess, 0, 1 or 2
	return np.random.randint(0,3)

def reward_value():
	# reward 0, 1, or 2
	return np.random.randint(0,3)

def success(pick, reward):
	if pick==reward:
		return 1
	else:
		return 0

def no_change(guess):
	pick = guess
	return pick

def change(guess, reward):
	valuepool = [0, 1, 2]
	remove_value = showvalue(guess, reward)

	# change
	valuepool.remove(guess)
	valuepool.remove(remove_value)
	pick = valuepool[0]

	return pick

def showvalue(guess, reward):
	# show the value
	valuepool = [0, 1, 2]
	valuepool.remove(reward)

	if reward==guess:
		# if guess is the reward, show one of the remaining values
		return np.random.choice(valuepool, 1)[0]
	else:
		# if guess is not the reward, show the only remaining value
		valuepool.remove(guess)
		return valuepool[0]

def asim(n_simulations, CHANGE):
	result = []
	for i in range(n_simulations):
		guess = guess_value()
		reward = reward_value()

		if not CHANGE:
			pick = no_change(guess)
		else:
			pick = change(guess, reward)

		if pick==reward:
			result.append(1)
		else:
			result.append(0)

	result = np.array(result)
	return result.mean()







