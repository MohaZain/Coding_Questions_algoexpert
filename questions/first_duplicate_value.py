def firstDuplicateValue(array):
    # Write your code here.
    result = len(array) + 1
    for i,num in enumerate(array):   
        for j in range(i + 1,len(array)):
            if array[i] == array[j]:
                if j < result:
                    result = j
    if result == len(array) + 1:
        return -1
    return array[result] 
