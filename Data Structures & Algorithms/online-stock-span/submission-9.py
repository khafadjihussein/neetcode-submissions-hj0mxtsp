class StockSpanner:

    def __init__(self):
        self.stack = []
        """we want number of days the stock is less than or equal
        todays stock, if we come across a stock that is less than
        the most previous one, span is 1 for that
        we could have a monotonically increasing stack
        could have monotonically decreasing stack
        worth mentioning that each prices span is plus 1 or greater of the
        span that any other price that is anything larger than it
        monotonically decreasing stack, when we get a new price keep popping
        and adding prev spans until we reach a greater price, then we add that
        to top of stack and append its price"""
        currspan = 1
        

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append([price, 1])
            currspan = 1
            return currspan
        else:
            currspan = 1
            
            while self.stack and price >= self.stack[-1][0]:
                prevprice, prevspan = self.stack.pop()
                currspan += prevspan
            self.stack.append([price, currspan])
            span = currspan
            currspan = 1
            return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)