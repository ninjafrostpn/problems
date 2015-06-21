num = [i for i in range(0, 100)]


def sum(nos, interval=1):
  if interval == 0:
    return "INFINITY"
  else:
    usednos = nos[::interval]
    tot = 0
    for n in range(0, len(usednos)):
      tot += usednos[n]
    return tot


for x in range(1, 4):
  print(sum(num, x))
