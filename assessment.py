"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

def is_hometown(town, hometown):
    """Compare a town name to your hometown. Returns True if it is your hometown.

    >>> is_hometown("san francisco", "novato")
    False

    >>> is_hometown("novato", "novato")
    True

"""

# instead of hard-coding the hometown, I chose to take it as an argument to
#   improve flexibility

    if town == hometown:
        right_town = True
    else:
        right_town = False

    return right_town

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.


def write_full_name(first_name, last_name):
    """Turn a user's first name and last name into a string with their full name.

    >>> write_full_name("Kris", "Kringle")
    'Kris Kringle'
"""
    full_name = first_name + " " + last_name

    return full_name

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.

# This function reuires the additional hometown argument as per my choice on line 62


def write_name_town(town, hometown, first_name, last_name):
    """Greet user and comment on their town

    >>> write_name_town("san francisco", "novato", "Kris", "Kringle")
    Hi, Kris Kringle, where are you from?

    """

    full_name = write_full_name(first_name, last_name)

    if is_hometown(town, hometown) is True:
        print "Hi, {}, we're from the same place!".format(full_name)
    else:
        print "Hi, {}, where are you from?".format(full_name)


###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""

    valid_berries = ["strawberry", "cherry", "blackberry"]

    if fruit in valid_berries:
        return True
    else:
        return False

# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.


def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""

    if is_berry(fruit) is True:
        return 0
    elif is_berry(fruit) is False:
        return 5

# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.


def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""

    lst.append(num)
    return lst

# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.


def calculate_price(base_price, state, tax_rate=.05):
    """Calculates total item price given base price, state, and tax rate.

        Depending on the state, the tax rate changes, and additional
            fees may apply.

"""

    final_price = base_price + (base_price * tax_rate)

    if state == "CA":
        final_price += final_price * .03
        final_price = round(final_price, 1)
    elif state == "PA":
        final_price += 2.00
    elif state == "MA":
        if base_price < 100.00:
            final_price += 1.00
        elif base_price >= 100.00:
            final_price += 3.00
    else:
        int(final_price)

    return final_price


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.


def append_to_list(orig_list, *list_args):
    """Take a list and append an unknown number of arguments.

    >>> append_to_list(["berries", "cherries", "pears"] , "apples", "kiwis")
    ['berries', 'cherries', 'pears', 'apples', 'kiwis']

    >>> append_to_list(["berries", "cherries", "pears"] , "apples", "kiwis", "bananas", "oranges")
    ['berries', 'cherries', 'pears', 'apples', 'kiwis', 'bananas', 'oranges']

    """

    list_args = list(list_args)

    return orig_list + list_args

# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


def inner_function(word):
    """Take a word and multiply that word by three.

    >>> inner_function("Starburst")
    'StarburstStarburstStarburst'

    """

    inner_results = word*3
    return inner_results


def outer_function(word):
    """Take a word as input and return that word and the results of the
        inner_function.

    >>> outer_function("Starburst")
    ('Starburst', 'StarburstStarburstStarburst')

        """

    return word, inner_function(word)


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
