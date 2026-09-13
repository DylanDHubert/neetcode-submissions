from heapq import heapify, heappush, heappop

class MedianFinder:

    def __init__(self):
        self.little = [] # MAX HEAP (-v)
        self.big = [] # MIN HEAP (+v)

    def addNum(self, num: int) -> None:
        if (len(self.little) == 0) and (len(self.big) == 0):
            heappush(self.little, -num)
            self.balance()
            return  
        if (len(self.big) == 0):
            if num < -self.little[0]: 
                heappush(self.little, -num)
                self.balance()
            else:
                heappush(self.big, num)
                self.balance()
            return
        if (len(self.little) == 0):
            if num > self.big[0]:
                heappush(self.big, num)
                self.balance()
            else:
                heappush(self.little, -num)
                self.balance()
            return 

        biggestLittle, littlestBig = -self.little[0], self.big[0] # !
        if biggestLittle >= num:
            heappush(self.little, -num)
        elif littlestBig <= num:
            heappush(self.big, num)
        else: # biggestLittle < num < littestBig
            heappush(self.little, -num)

        self.balance()
    
    def balance(self):
        littleSize, bigSize = len(self.little), len(self.big)

        if littleSize + 1 < bigSize: # ONE OFF IS OK!
            littestBig = heappop(self.big)
            heappush(self.little, -littestBig) # PUSH NEGATIVE INTO SMALL
            
        if bigSize + 1 < littleSize:
            biggestLittle = -heappop(self.little) # NEGATE NEGATIVE FROM SMALL
            heappush(self.big, biggestLittle)

    def findMedian(self) -> float:
        if len(self.big) == 0: return -self.little[0]
        if len(self.little) == 0: return self.big[0]
        littleSize, bigSize = len(self.little), len(self.big)
        biggestLittle, littlestBig = -self.little[0], self.big[0]

        if littleSize == bigSize: return (biggestLittle + littlestBig) / 2
        if littleSize > bigSize: return biggestLittle
        if littleSize < bigSize: return littlestBig
        
        