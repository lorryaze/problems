'''
    Given a  list of intervals [start, end]
    Finde the lenght of the maximal set of mutually disjoint intervals

    1 <= N <= 1e5
    1 <= A[i][0] <= A[i][1] <= 1e9

    The intuition here its get the intervals that ends early, so we need to sort
    the list of interval by the end of each interval.
'''

intervals = [[1,2], [2,10], [4,6]]
intervals_2 = [[1,4], [2,3], [4,6], [8,9]]

def greedy(intervals):
    #sort the intervals
    intervals.sort(key=lambda x: x[1])
    
    #get the first start and end of the first interval
    prev_start, prev_end = intervals[0]
    #compute de val of the fisrt interval already setted on the previous step
    count = 1
    for start, end in intervals:
        #if start of the interval is smaller than the end of the previous interval
        #this means that the intervals are intersected and e only what disjoint intervals
        if start <= prev_end:
            pass
        else:
            #if not we update the values of prev_start and prev_end and update our counting
            prev_start = start
            prev_end = end
            count += 1
    return count

def clean_greedy_implementation(intervals):
    intervals.sort(key=lambda x: x[1])
    prev_end = float('inf')
    count = 0
    for interval in intervals:
        if interval[0] < prev_end:
            count += 1
    return count
result = greedy(intervals)
print(result, greedy(intervals_2))
