import sys


def restaurant_rating_sorter(filename):
    """"""
# read the file

    restaurant_scores = {}

    list_of_ratings = open(filename)
    for line in list_of_ratings:
        line = line.rstrip()
        rest_ratings = line.split(":")

        # for restaurant, score in restaurants_and_scores:
        restaurant_scores[rest_ratings[0]] = rest_ratings[1]

    print restaurant_scores


# store them in a dictionary
# sort by restaurant name

restaurant_rating_sorter(sys.argv[1])
