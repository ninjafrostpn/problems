from random import randInt as rand

name = input("Hi, I'm Doug, what's your name?\n>> ")
age = input("And so you're... %d years old, right?\n>> " % rand(25, 51))
if age > 50:
  print("Wow")
  print("%s is old" % name)
elif age < 25:
  print("Oh, okay")
  print("%s is young" % name)
else:
  print("Yay!")
  print("%s is %d years old" % (name, age))
  print("I'm %d years old too!" % age)
