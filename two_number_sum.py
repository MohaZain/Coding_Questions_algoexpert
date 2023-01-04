def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    for i in range(len(array)):
        pointer = i 
        for j in range(len(array[i+1:])):
            pointer +=1
            if array[i] + array[pointer] == targetSum:
                return [array[i] , array[pointer]]

    return []