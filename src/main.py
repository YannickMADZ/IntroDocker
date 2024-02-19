from similarity import Similarity

sim = Similarity()
score = sim.compute("I love my mum", " I'am trying to love my dad in order to please my mum")
print(score)