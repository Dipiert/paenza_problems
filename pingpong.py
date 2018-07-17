import random

class Pingpong:	
	players = {'a': 0, 'b': 0, 'c': 0}

	def play(self, p1, p2):
		if (random.random() > 0.5):
			return p1, p2
		return p2, p1

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

p = Pingpong()
match = 1
end = False
while not end:
	p1, p2 = random.sample(p.players.keys(), 2)
	winner, loser = p.play(p1, p2)
	print "Match:" + str(match)
	print "Jugaron " + p1 + " y " + p2
	print "Perdio: " + loser
	p.players[p1] += 1
	p.players[p2] += 1
	end = p.is_end_condition_met()	
	if (p.has_reset()):
		match = 1
	else:
		match += 1
