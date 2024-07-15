'''
    Given A array of a random permutation of numbers from 1 to N. 
    Given B, the number of swaps in A that we can make.

    Find the largest permutation possible.
    This problem input have all values from 1 to n, in this case the greedy solution
    works because the biggest value of the array will be the ith value (n-1 or n-i)
    1 <= N <= 1e6
    1 <= B <= 1e9
''' 
def greedy(array, swaps):
    n = len(array)
    d = {x: i for i, x in enumerate(array)}
    print(d)
    for i in range(n):
        if swaps == 0:
            break
        
        max_value = n - i
        if array[i] == max_value:
            continue
        
        max_index = d[max_value]
        d[array[i]], d[max_value] = max_index, i
        array[i], array[max_index] = array[max_index], array[i]
        swaps -= 1

    return array

# Exemplo de uso
inp = [3, 2, 4, 1, 5]
inp2 = [5, 4, 1, 2, 3]
b = 3
print(greedy(inp2, 1))  # Saída esperada: [5, 4, 3, 1, 2]

