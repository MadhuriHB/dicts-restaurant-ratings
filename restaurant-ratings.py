def restaurant_ratings(filename):

    myDict = {}

    input_file = open(filename)
    for line in input_file:
        line = line.rstrip()
        words = line.split(":")
        myDict[words[0]] = words[1]  
    myKeys = sorted(myDict)  
    for items in myKeys:
        print "%s is rated at %s." %(items, myDict[items])
    input_file.close()

restaurant_ratings("scores.txt")
