def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    duration = 0 
    min_duration = 0
    for indx in range(len(queries)):
        if indx != 0:
            duration = duration + queries[indx - 1]
            min_duration = min_duration + duration        
    return min_duration