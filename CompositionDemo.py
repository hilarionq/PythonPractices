class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y

    def substract(self):
        return self.x - self.y

class Math2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def product(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y

class Math3:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.math_1 = Math(x,y)
        self.math_2 = Math2(x,y)
    
    def power(self):
        return self.x ** self.y

    def add(self):
        return self.math_1.add()

    def substract(self):
        return self.math_1.substract()

    def product(self):
        return self.math_2.product()

    def divide(self):
        return self.math_2.divide()

############ Another example

class CountUp():
    def increment(self, num):
        self.counter = num + 1
        return self.counter


class CountDown():
    def decrement(self, num):
        self.counter = num - 1
        return self.counter


class NewClass():
    def __init__(self, start = 0):
        self.counter = start
        self.cup = CountUp()
        self.cdown = CountDown()
    
    def increment(self):
        self.counter = self.cup.increment(self.counter)
    
    def decrement(self):
        self.counter = self.cdown.decrement(self.counter)

    def reset(self):
        self.counter = 0
    
    def get_counter(self):
        return self.counter