'''
    Given N bulbs, either on (1) or of(0).
    turning on ith bulb case causes all remaining bulbs on 
    the right to flip.

    Find the min number of switches to turn all the bulbs on.
    1 <= N <= 1e5
    A[i] = {0, 1}
'''
bulbs = [0, 1, 0, 1, 1, 0, 1, 1]

def brute_force(bulbs):
    cost = 0
    for i in range(len(bulbs)):
        if bulbs[i] == 0:
            for j in range(len(bulbs)):
                bulbs[j] = not bulbs[j]
            cost += 1
    return cost

def greedy(bulbs):
    cost = 0
    for b in bulbs:
        if cost % 2 == 0:
            b = b
        else:
            b = not b
        if b % 2 == 1: continue
        else: cost += 1
    return cost

result_brute = brute_force(bulbs)
result_greedy = greedy(bulbs)

print(result_brute, result_greedy)

