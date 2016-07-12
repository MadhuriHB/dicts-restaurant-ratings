from random import choice

def restaurant_ratings(filename):

    myDict = {}
    input_file = open(filename)
    for line in input_file:
        line = line.rstrip()
        words = line.split(":")
        myDict[words[0]] = words[1]  

    while True:
        query_name = raw_input("Please enter your name: ")
        print "Hello {}".format(query_name)
        query_restaurant = raw_input("Please enter a restaurant name or 'q' to quit: ")

        if query_restaurant == 'q':
            break

        else:     

            query_rating = int(raw_input("Please enter the restaurant rating: "))
        

            myDict[query_restaurant] = query_rating  
            myKeys = sorted(myDict)
            random_restaurant = choice(myKeys)

            print "The random restaurant choice is {} ".format(random_restaurant)
            print "The random restaurant choice {} rating is {}".format(random_restaurant, myDict[random_restaurant])
            rating_update = int(raw_input("What is the random restaurant choice new rating?: "))
            myDict[random_restaurant] = rating_update

            for key in myKeys:
                print "%s is rated at %s." %(key, myDict[key])

            input_file.close()

restaurant_ratings("scores.txt")




