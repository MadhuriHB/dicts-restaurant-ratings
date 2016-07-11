def restaurant_ratings(filename):
    query_restaurant = raw_input("Please enter a restaurant name: ")
    query_rating = int(raw_input("Please enter the restaurant rating: "))
    
    myDict = {}

    myDict[query_restaurant] = query_rating

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
