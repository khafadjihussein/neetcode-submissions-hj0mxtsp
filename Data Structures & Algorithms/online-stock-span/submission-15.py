class StockSpanner:

    def __init__(self):
        self.stack = []
        
        

    def next(self, price: int) -> int:
        span = 1
        if not self.stack:
            self.stack.append([price, 1])
            return 1
        else:
            while self.stack and price >= self.stack[-1][0]:
                x, prevspan = self.stack.pop()
                span += prevspan
            self.stack.append([price, span])
            return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)