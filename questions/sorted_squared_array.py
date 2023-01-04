def sortedSquaredArray(array):
    # Write your code here.
    seq_arr = []
    for num in array:
        seq_arr.append(num*num)

    seq_arr.sort()
    return seq_arr
