class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        # Create tables of infinities that'll soon be releaxed.
        prices = [float("inf")] * n

        # Make the prices at the source node, 0.
        prices[src] = 0

        # Bellman Ford Algorithm:
        # We will be doing breadth first search only up to the limit denoted by k
        # If our prices ends up with infinity on the target node, we can safely say
        # That our target node wasn't reached in the designated amount of flights
        for i in range(k + 1):
            tmpPrices = prices[:]

            for source, destination, price in flights:
                # If the price of the source is undefined
                # We won't be able to calculate the price for going
                # To the next node
                if prices[source] == float("inf"):
                    continue

                # Relaxation: 
                # If the new price is less than the current price
                # Make that new price change
                if prices[source] + price < tmpPrices[destination]:
                    tmpPrices[destination] = prices[source] + price 
            prices = tmpPrices

        if prices[dst] == float("inf"):
            return -1
        return prices[dst]
