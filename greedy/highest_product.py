'''
    Given an array of N integers. 
    Find the highest product by multiplying 3 elements of the array.

    3 <= N <= 5e5
'''
import time

arr = [1, 4, 2, 3]

def brute_force(arr):
    result = float('-inf')
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                mult = arr[i] * arr[j] * arr[k]
                if mult > result:
                    result = mult
    return result


def greedy_n_log_n(arr):
    arr.sort()
    n = len(arr)
    p1 = arr[n-1] * arr[n-2] * arr[n-3]
    p2 = arr[0] * arr[1] * arr[n-1]
    return max(p1, p2)

def greedy_o_n(arr):
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')
    for i in arr:
        if i > max1:
            max3 = max2
            max2 = max1
            max1 = i
        elif i > max2:
            max3 = max2
            max2 = i
        elif i > max3:
            max3 = i
        if i < min1:
            min2 = min1
            min1 = i
        elif i < min2:
            min2 = i
    p1 = max1 * max2 * max3
    p2 = max1 * min1 * min2
    return max(p1, p2)

start_time = time.time()
result_brute = greedy_o_n(arr)
print(result_brute)
end_time = time.time()

print('execution time', end_time)
