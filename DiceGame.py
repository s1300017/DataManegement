import random

print("What is your name?")
print("> ", end = "")
name = input()
print("Hello, " + name + "!")


die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

sum = die1 + die2

print("Rolling dice")
print("Die 1:", die1)
print("Die 2:", die2)
print("Total value:", sum)

if sum > 7:
    print(name, "won!")
else :
    print(name, "lost")