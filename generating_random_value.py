import random

for i in range(3):
    print(random.randint(10, 20))


members = ['John', 'Mary', 'Bob', 'Kevin']
leader = random.choice(members)
print(leader)
