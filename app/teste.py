import random

random_start = ["computer", "player"]
first = random.choice(random_start)
print(first)
random_start.remove(first)
print(random_start[0])
