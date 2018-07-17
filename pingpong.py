import random, time

class Pingpong:   
   played_matches = {'A': 0, 'B': 0, 'C': 0}
   expected_matches = {'A': 10, 'B': 15, 'C': 17}

   def show_played_matches_status(self):
      print("\tA: %s" % self.played_matches['A'])
      print("\tB: %s" % self.played_matches['B'])
      print("\tC: %s" % self.played_matches['C'])

   def play(self, p1, p2):
      if random.random() > 0.5:
         return p1
      return p2

   def is_end_condition_met(self):
      return self.played_matches['A'] == self.expected_matches['A'] \
         and self.played_matches['B'] == self.expected_matches['B'] \
         and self.played_matches['C'] == self.expected_matches['C'] 

   def must_reset(self):
      must_reset = self.played_matches['A'] > self.expected_matches['A'] \
         or self.played_matches['B'] > self.expected_matches['B'] \
         or self.played_matches['C'] > self.expected_matches['C']

      if must_reset:
         self.played_matches = {'A': 0, 'B': 0, 'C': 0}
      return must_reset

def exclude_key(d, key):
    return {x: d[x] for x in d if x != key}

def show_match_result():
   print("Match: %s" % match)
   print("In this match: %s and %s" % (p1, p2))
   print("Loser: %s" % loser)

def show_result_info(elapsed_time):
   elapsed_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
   print("Iterations: %d" % iterations)
   print("Elapsed Time: %s" % elapsed_time)
   
def update_played_matches():
   p.played_matches[p1] += 1
   p.played_matches[p2] += 1

start_time = time.time()
p = Pingpong()
match = 1
iterations = 0
end = False
p1, p2 = random.sample(p.played_matches.keys(), 2)
while not end:
   iterations += 1
   loser = p.play(p1, p2)
   show_match_result()
   update_played_matches()   
   player_candidates = exclude_key(p.played_matches, loser)
   p1, p2 = random.sample(player_candidates, 2)
   p.show_played_matches_status()  
   end = p.is_end_condition_met()   
   if p.must_reset():
      match = 1
   else:
      match += 1
elapsed_time = time.time() - start_time
show_result_info(elapsed_time)
