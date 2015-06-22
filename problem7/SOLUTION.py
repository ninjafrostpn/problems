buildcar = lambda type, cost, speed: {"type": type, "cost": cost, "speed": speed}

def compare(aspect, *interms):
  outterms = [interms[0]]
  for term in interms:
    

barracuda = buildcar("sports", 100000, 100)
termite = buildcar("city", 10000, 50)

costs = compare(barracuda, termite, "cost")
speeds = compare(barracuda, termite, "speed")
print("%s car is cheaper than %s car" % (costs[1], costs[0]))
print("%s car is faster than %s car" % (speeds[0], speeds[1]))
