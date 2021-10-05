#WRITE YOUR CODE IN THIS FILE
def hasL(w): 


    for x in range(0, len(w)): 
        if w[x] == "l": 
            return True

    else: 
        return False 

print(hasL("alligator"))