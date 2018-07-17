import random, time

class Pingpong:	
	players = {'a': 0, 'b': 0, 'c': 0}

	def play(self, p1, p2):
		if (random.random() > 0.5):
			return p1
		return p2

	def is_end_condition_met(self):
		print "\tA: " + str(self.players['a'])
		print "\tB: " + str(self.players['b'])
		print "\tC: " + str(self.players['c'])
		return self.players['a'] == 10 and self.players['b'] == 15 and self.players['c'] == 17 

	def has_reset(self):
		has = self.players['a'] > 10 or self.players['b'] > 15 or self.players['c'] > 17
		if has:
			self.players = {'a': 0, 'b': 0, 'c': 0}
		return has

def exclude_key(d, key):
    return {x: d[x] for x in d if x != key}

p = Pingpong()
match = 1
iterations = 0
end = False
p1, p2 = random.sample(p.players.keys(), 2)
start_time = time.time()
while not end:
	iterations += 1
	loser = p.play(p1, p2)
	print "Match:" + str(match)
	print "In this match: " + p1 + " and " + p2
	print "Loser: " + str(loser)
	p.players[p1] += 1
	p.players[p2] += 1
	candidates = exclude_key(p.players, loser)
	p1, p2 = random.sample(candidates, 2)	
	end = p.is_end_condition_met()	
	if p.has_reset():
		match = 1
	else:
		match += 1
elapsed_time = time.time() - start_time
elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
print "Iterations: " + str(iterations)
print "Elapsed Time: " + str(elapsed_time)
