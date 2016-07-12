def restaurant_ratings(filename):

    myDict = {}
    input_file = open(filename)
    for line in input_file:
        line = line.rstrip()
        words = line.split(":")
        myDict[words[0]] = words[1]  

    while True:
        
        query_restaurant = raw_input("Please enter a restaurant name or 'q' to quit: ")

        if query_restaurant == 'q':
            break

        else:     

            query_rating = int(raw_input("Please enter the restaurant rating: "))
        

            myDict[query_restaurant] = query_rating  
            myKeys = sorted(myDict)  

            for items in myKeys:
                print "%s is rated at %s." %(items, myDict[items])
            input_file.close()

restaurant_ratings("scores.txt")




