class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        drank = 0
        empty = 0 
        while numBottles > 0 : 
            drank = drank + numBottles
            empty = numBottles + empty
            numBottles = empty // numExchange
            empty = empty % numExchange
        return drank

            
            
            
        