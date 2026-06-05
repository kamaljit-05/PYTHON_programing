class SimpleInterest:
    def __init__(self):
        self.__principal = 0
        self.__rate = 0
        self.__time = 0

    @property
    def principal(self):
        return self.__principal

    @principal.setter
    def principal(self, value):
        self.__principal = value

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, value):
        self.__rate = value

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value

    def calculate_si(self):
        return (self.principal * self.rate * self.time) / 100


obj = SimpleInterest()

obj.principal = 10000
obj.rate = 5
obj.time = 2

print("Principal =", obj.principal)
print("Rate =", obj.rate)
print("Time =", obj.time)
print("Simple Interest =", obj.calculate_si())