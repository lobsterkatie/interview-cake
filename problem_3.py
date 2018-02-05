"""
Given a list of integers, find the highest product you can get from three of
the integers.

The input list_of_ints will always have at least three integers.

"""

def highest_product_of_3(nums):
    """Given a list of integers, find the largest product of three
       of them.

       >>> highest_product_of_3([1, 10, -5, 1, -100])
       5000

       >>> highest_product_of_3([4, -6, 2, 9, 6])
       216

       >>> highest_product_of_3([-4, -6, -2, -1, -5])
       -8

       >>> highest_product_of_3([-3, -9, 2, -7, -5])
       126

       >>> highest_product_of_3([-6, -1, -8, 0])
       0

    """

    max_prod = min_prod = nums[0] * nums[1] * nums[2]
    max_factors = [nums[0], nums[1], nums[2]]
    min_factors = [nums[0], nums[1], nums[2]]
    for i, current_num in enumerate(nums):

        #we've already considered the first three numbers, so skip them
        if i <= 2:
            continue

        #try the current number  instead of each of the factors of our current
        #max_prod and min_prod, keeping track of which factor was replaced
        options = {current_num * max_factors[1] * max_factors[2]: ("max", 0),
                   max_factors[0] * current_num * max_factors[2]: ("max", 1),
                   max_factors[0] * max_factors[1] * current_num: ("max", 2),
                   current_num * min_factors[1] * min_factors[2]: ("min", 0),
                   min_factors[0] * current_num * min_factors[2]: ("min", 1),
                   min_factors[0] * min_factors[1] * current_num: ("min", 2)}

        #if any of the options is better than our current best, update our
        #trackers

        #find the max and min options
        max_option = max(options)
        min_option = min(options)

        #if the max option is better than our current max, reset max_prod and
        #its factors
        if max_option > max_prod:
            max_prod = max_option

            direction, index_to_replace = options[max_option]

            #if the factors used to be part of a min option rather than a max
            #option, first grab the min option's factors
            if direction == "min":
                max_factors = min_factors[:]

            #in either case, replace the relevant factor
            max_factors[index_to_replace] = current_num

        #if the min option is better than our current min, reset min_prod and
        #its factors
        if min_option < min_prod:
            min_prod = min_option

            direction, index_to_replace = options[min_option]

            #if the factors used to be part of a max option rather than a min
            #option, first grab the min option's factors
            if direction == "max":
                min_factors = max_factors[:]

            #in either case, replace the relevant factor
            min_factors[index_to_replace] = current_num

    return max_prod



import doctest
if doctest.testmod().failed == 0:
    print "*** ALL TESTS PASSED ***"


