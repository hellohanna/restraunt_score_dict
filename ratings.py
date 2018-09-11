def rating_restaurant(file_name):
    """Restaurant rating lister."""

    rating_dict = {}

    for line in open(file_name):
        line = line.rstrip()
        key_value_list = line.split(":")
        key = key_value_list[0]
        value = key_value_list[1]
        rating_dict[key] = int(value)

   


    restaurant_name = input("What is the Restaurant's name? ")
    restaurant_score = input("What is the Restaurant's rating?") 

    while True:
        if restaurant_score in ['1','2','3','4','5']:
            break
        else:
            restaurant_score = input("Incorrect input! Please enter values of 1 to 5. ")




    rating_dict[restaurant_name] = int(restaurant_score)


  
    for key in sorted(rating_dict):
        print("{} is rated at {}".format(key, rating_dict[key]))





rating_restaurant("scores.txt")



# put your code here
