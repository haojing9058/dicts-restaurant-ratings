import sys


def clean_up_data(filename):
    """Parses a text file for sorting."""

    restaurant_scores = {}

    # list_of_ratings = open(filename)
    with open(filename) as list_of_ratings:
        for line in list_of_ratings:
            line = line.rstrip()
            rest_name, rest_score = line.split(":")

            restaurant_scores[rest_name] = rest_score

    return restaurant_scores


def add_users_rating():
    """Asks for user's restaurant and rating, returns info in a list."""

    users_restaurant = raw_input("Where have you eaten recently? > ")
    users_restaurant = users_restaurant.title()

    while True:
        users_score = raw_input("Cool! How would you rate it out of 5? > ")

        if users_score not in "12345":
            print "Sorry, please type a number from 1-5."
            continue

        else:
            users_score = int(users_score)
            break

    return [users_restaurant, users_score]


def show_sorted_ratings():
    """Prints an alphabetized display of restaurant ratings."""

    restaurant_scores = clean_up_data(sys.argv[1])
    # users_restaurant, users_score = add_users_rating()

    # restaurant_scores[users_restaurant] = users_score

    sorted_rests = sorted(restaurant_scores.items())

    for rest_name, rest_score in sorted_rests:
        print "{} has a rating of {}.".format(rest_name, rest_score)

# show_sorted_ratings()


def main_menu():
    """Displays options to user."""

    print """
                (S)ee all restaurant ratings
                (A)dd a new restaurant rating
                (Q)uit
    """

    user_choice = raw_input("What would you like to do? > ")

    restaurant_scores = {}

    if user_choice == "S":
        show_sorted_ratings()

        # pass
        # function to show all ratings sorted

    elif user_choice == "A":
        users_restaurant, users_score = add_users_rating()
        restaurant_scores[users_restaurant] = users_score
        print restaurant_scores
        # function to add a restaurant

    elif user_choice == "Q":
        pass
    else:
        print "Sorry, I didn't understand your choice!"


main_menu()
