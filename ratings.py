import sys


def restaurant_rating_sorter(filename):
    """Parses a text file and returns
    an alphabetized list of restaurant ratings."""
# read the file

    restaurant_scores = {}

    list_of_ratings = open(filename)
    for line in list_of_ratings:
        line = line.rstrip()
        rest_ratings = line.split(":")

        # for restaurant, score in restaurants_and_scores:
        restaurant_scores[rest_ratings[0]] = rest_ratings[1]

    sorted_rests = sorted(restaurant_scores.items())

    for rest_rating in sorted_rests:
        print "{} has a rating of {}.".format(rest_rating[0], rest_rating[1])


# store them in a dictionary
# sort by restaurant name

restaurant_rating_sorter(sys.argv[1])
