import random

random_answer = random.randint(0, 1)
print(random_answer)
if random_answer == 0:
    print("Tails")
else:
    print("Heads")