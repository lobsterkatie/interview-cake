"""
Writing programming interview questions hasn't made me rich. Maybe trading
Apple stocks will.

Suppose we could access yesterday's stock prices as a list, where:

    The indices are the time in minutes past trade opening time, which was
    9:30am local time. The values are the price in dollars of Apple stock at
    that time.

So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the
best profit I could have made from 1 purchase and 1 sale of 1 Apple stock
yesterday.

For example:

    stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

    get_max_profit(stock_prices_yesterday)
    # Returns 6 (buying for $5 and selling for $11)

No "shorting"—you must buy before you sell. You may not buy and sell in the
same time step (at least 1 minute must pass).

"""

def get_max_profit(stock_prices):
    """Find the maximum possible profit, given the prices for the day.

        Runs in O(n) time and space.

        >>> get_max_profit([10, 7, 5, 11, 9, 4])
        6

    """

    #make sure we have at least two prices to compare
    assert len(stock_prices) > 1, "too few prices!"

    #keep track of the lowest price previous to any given price
    mins_to_left = [stock_prices[0]]
    for i, price in enumerate(stock_prices):
        #the first price doesn't have anything less than it to the left
        if i == 0:
            continue

        #either the previous minimum or the previous price will be the
        #lowest price before the current price
        mins_to_left.append(min(mins_to_left[i-1], stock_prices[i-1]))

    # print stock_prices
    # print mins_to_left

    max_profit = 0
    for i, price in enumerate(stock_prices):
        #you can't sell in the first minute, because you haven't bought anything
        #yet
        if i == 0:
            continue

        #greedily find the max profit
        profit = price - mins_to_left[i]
        if profit > max_profit:
            max_profit = profit

    return max_profit


def get_max_profit2(stock_prices):
    """Find the maximum possible profit, given the prices for the day.

        Runs in O(n) time and O(1) space.

        >>> get_max_profit2([10, 7, 5, 11, 9, 4])
        6

        >>> get_max_profit2([10, 9, 8, 7, 6, 5])
        -1

    """

    #make sure we have at least two prices to compare
    assert len(stock_prices) > 1, "too few prices!"

    #keep running track of the cheapest previous buying price and the best
    #possible profit so far
    min_to_left = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    #scan the prices to find the best we can do
    for i, price in enumerate(stock_prices):
        #you can't sell in the first minute, because you haven't bought
        #anything yet
        if i == 0:
            continue

        #if the price right before this one is lower than the previous low
        #buying price, update min_to_left
        min_to_left = min(min_to_left, stock_prices[i-1])

        #now that we know that the lowest possible buying price is, see if
        #selling at this price will increase our profit, and update
        #max_profit if so
        profit = price - min_to_left
        max_profit = max(max_profit, profit)

    #return the results
    return max_profit



if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print

