from random import randint
import numpy as np
prices = []
f = open("prices.txt")
for line in f:
    v = float(line.strip())
    prices.append(v)

def sample(data):
    random_indices = randint(0, len(data), len(data))
    return [data[idx] for idx in random_indices]


    result = []
    for num in range(len(data)):
        result.append(randint(0, len(data) - 1))
    return result

TRIALS = 20
X_List = [np.mean(sample(prices.txt)) for i in range(TRIALS)]




for i in range(TRIALS):
    sample_index = sample(data)
    sample_list = []
    for j in sample_index:
        sample_list.append(data[j])
    X_List.append(sum((sample_list)) / len(sample_list))
print X_List