import random

# TEST OF PROCEDERAL GENERATION
# set seed for random object
random.seed()

"""
    Using random.randint(0,1) gives either a 0 or 1
"""
level_map = []

for i in range(10):
    
    level_map.append([])

    for j in range(20):

        level_map[i].append(str(random.randint(0,1)))

level_map[2][3] = "P"