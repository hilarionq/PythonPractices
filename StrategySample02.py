def strategy_user(strategy):
    strategy()

def strategy_one():
    print("strategy_one called")

class Strategy_Two:
    def __call__(self):
        print("Strategy_Two called")

class Strategy_Three:
    def run(self):
        print("Strategy_Three called")l

#our Strategy class from earlier using a static method instead
class Strategy_Four:
    @staticmethod
    def run():
        print("Strategy_Four called")

# using each of the Strategy types
strategy_user(strategy_one)
strategy_user(Strategy_Two())
strategy_user(Strategy_Three().run)
strategy_user(Strategy_Four.run)
