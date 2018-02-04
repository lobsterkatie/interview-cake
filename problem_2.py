"""
You have a list of integers, and for each index you want to find the product
of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list
of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Do not use division in your solution.

"""

def find_products_of_others(nums):
    """Given a list of numbers, return a list of products, where each product
       is the result of multiplying all nums in the original list other than
       the one at the corresponding index. Linear time and space, no division
       allowed.

       >>> find_products_of_others([1, 2, 3, 4])
       [24, 12, 8, 6]

       >>> find_products_of_others([1, 7, 3, 4])
       [84, 12, 28, 21]

       >>> find_products_of_others([4, 9])
       [9, 4]

    """

    #make sure we have enough numbers
    assert len(nums) >= 2, "too few numbers!"

    #create a results list, which is the final length, but only contains 1's
    results = [1] * len(nums)

    #working left to right, make sure each result is the product of all
    #numbers to its left
    prod_of_all_to_left = 1
    for i in xrange(len(nums)):
        #there are no numbers to the left of the first one
        if i == 0:
            continue

        #update our running product and our current result
        prod_of_all_to_left *= nums[i-1]
        results[i] *= prod_of_all_to_left

    #now do the same thing from right to left
    prod_of_all_to_right = 1
    for i in xrange(-1, -len(nums) - 1, -1):
        #there are no numbers to the right of the last one
        if i == -1:
            continue

        #update our running product and our current result
        prod_of_all_to_right *= nums[i+1]
        results[i] *= prod_of_all_to_right

    return results


import doctest
if doctest.testmod().failed == 0:
    print "*** ALL TESTS PASSED ***"