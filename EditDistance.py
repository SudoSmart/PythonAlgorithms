def cost(a,b):
    return 0 if a==b else 1

def distance(firstString,secondString):
    if len(firstString) == 1 and len(secondString)==1:
        return cost(firstString,secondString)
    if len(firstString) == 1 or len(secondString) == 1:
        return cost(firstString[0],secondString[0])

    return min(distance(firstString,secondString[:-1])+1 , distance(firstString[:-1],secondString)+1 , distance(firstString[:-1],secondString[:-1]) + cost(firstString[-1],secondString[-1]))

