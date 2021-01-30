def add(*args):
    print(args[3])
    sum = 0
    for n in args:
        sum += n
    return sum

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(2, add=3, multiply=5))
# print(add(3, 5, 7, 5))

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Opel")#, model="Zafira")
print(my_car.model)