class SeatManager(object):

    def __init__(self, n):
        self.l=[0]*n
        self.dep=1
        self.index = 0

    def reserve(self):
        if self.dep : 
            self.l[self.index]=1
            self.index+=1
            return self.index
        else: 
            aux = self.l.index(0)
            self.l[aux]=1
            return aux+1

        

    def unreserve(self, seatNumber):
        self.dep=0
        self.l[seatNumber-1] = 0
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)