import sys


def clean_up_data(filename):
    """Parses a text file for sorting."""

    restaurant_scores = {}

    list_of_ratings = open(filename)
    for line in list_of_ratings:
        line = line.rstrip()
        rest_ratings = line.split(":")

        restaurant_scores[rest_ratings[0]] = rest_ratings[1]

    return restaurant_scores


def show_sorted_ratings():
    """Parses a text file and returns
    an alphabetized list of restaurant ratings."""

    restaurant_scores = clean_up_data(sys.argv[1])

    sorted_rests = sorted(restaurant_scores.items())

    for rest_rating in sorted_rests:
        print "{} has a rating of {}.".format(rest_rating[0], rest_rating[1])


show_sorted_ratings()

# new function taking user input (twice)
    # takes restaurant name
    # takes restaurant score
