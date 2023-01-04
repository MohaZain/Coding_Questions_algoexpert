def firstNonRepeatingCharacter(string):
    # Write your code here.
    for indx,let in enumerate(string):
        if let not in string[indx+1:] and let not in string[:indx]:
            return indx
        
    return -1