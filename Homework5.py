#დავალება1
class Currency:
    rates = {"GEL": 1, "USD": 2.7, "EUR": 3}

    def __init__(self, value, unit="GEL"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value:.2f} {self.unit}"

    def changeTo(self, new_unit):
        if new_unit == "USD":
            dolari = self.value / 2.2
            return Currency(dolari, "USD")
        elif new_unit == "EUR":
            euro = self.value / 3
            return Currency(euro, "EUR")
        else:
            return Currency(self.value, "GEL")

    def __add__(self, other):
        if isinstance(other, Currency):
            converted_other = other.changeTo(self.unit)
            return Currency(self.value + converted_other.value, self.unit)
        else:
            raise TypeError("Cannot add non-Currency object to Currency")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Currency(self.value * other, self.unit)
        else:
            raise TypeError("გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __gt__(self, other):
        converted_other = other.changeTo(self.unit)
        if converted_other.value > self.value:
            print(f"{converted_other} > {self}")
        elif converted_other.value < self.value:
            print(f"{converted_other} < {self}")
        else:
            print(f"{converted_other} = {self}")

c1 = Currency(100, "USD")
print(c1)
c2 = c1.changeTo("EUR")
print(c2)

c3 = Currency(200, "EUR")
print(c1.__add__(c3))

c5 = c1 * 3
print(c5)

c6 = Currency(300, "GEL")
c1.__gt__(c6)

#დავალება2
class Person:
    def __init__(self, name, deposit=100, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"{self.name} - Deposit: {self.deposit}, Loan: {self.loan}"

class House:
    def __init__(self, ID, price, owner=None):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = "for sale"

    def sell_house(self, buyer, loan=None):
        if loan is None:
            self.owner.deposit += self.price
            # self.owner.deposit -= self.price * 0.1  # 10% საკომისოა, არასავს 10%ს
            self.owner = buyer
            self.status = "sold"
            print(f"{self.ID} has been sold to {buyer.name} for {self.price}")
        else:
            self.owner.deposit += self.price
            self.owner.deposit -= self.price * 0.1
            self.owner.loan += loan
            self.owner = buyer
            self.status = "sold on loan"
            print(f"{self.ID} has been sold to {buyer.name} for {self.price} with a loan of {loan}")
owner = Person("John")
buyer = Person("Sarah", deposit=200)
house1 = House("წალენჯიხა#8", 100000, owner=owner)
house1.sell_house(buyer)
house1.sell_house(buyer, loan=50000)
print(owner)
print(buyer)

#დავალება3
class Plane:
    def Move(self):
        print("Plane can fly")
    def Speed(self):
        print("its speed is up to 900km/h")
class Bus:
    def Move(self):
        print("Bus can move on roads")
    def Speed(self):
        print("its speed is up to 180km/h")
def Movement(object):
    object.Move()
    object.Speed()
P1 = Plane()
B1 = Bus()
P1.Move()
P1.Speed()
B1.Move()
B1.Speed()
Movement(P1)
Movement(B1)





