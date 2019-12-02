print("Hello, This program converts units. Specifically kilometers into miles.")
retry = "yes"
while retry == "yes":
    try:
        kilometers = float(input("Please enter a distance in kilometers to convert to miles: "))
    except ValueError:
        print ("That's not something I can use to calculate a distance. Please enter a digit and use a point for decimals. ")
    else:
        miles = (kilometers * 0.621371)
        print ("the distance in miles is", miles,"miles")
    finally:
        retry = input("type 'yes' if you want to make another calculation: ")
        if retry != "yes":
            print("see you next time!")


