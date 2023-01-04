def moveElementToEnd(array, toMove):
    # Write your code here.
    num_count = 0 
    if toMove in array:
        num_count = array.count(toMove)
        for i in range(num_count):
            array.remove(toMove)
        array = array + num_count*[toMove]
        return array
    return array
