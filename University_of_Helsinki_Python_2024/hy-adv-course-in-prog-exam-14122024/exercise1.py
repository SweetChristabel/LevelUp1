# Write your solution to exercise 1 here
class Product:
    def __init__(self, name: str, price: float, unit: str, quantity = 0):
        self.name = self.__checkname(name)
        self.price = self.__checkprice(price)
        self.unit = self.__checkunit(unit)
        self.quantity = self.__checkquantity(quantity)

    def __checkname(self, name: str):
        if type(name) != str:
            raise ValueError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name must be three characters or more")
        return name

    def __checkprice(self, price: float):
        if not (type(price) == float or type(price) == int):    #Added the support for integers for convenience
            raise ValueError("Price must be a number")
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        return float(price)                                     #The stored value will be a floating-point either way.

    def __checkunit(self, unit: str):
        if type(unit) != str:
            raise ValueError("Unit must be a string")
        return unit

    def __checkquantity(self, quantity: float):
        if not (type(quantity) == float or type(quantity) == int):
            raise ValueError("Quantity must be a number")
        return float(quantity)
    
    def changequantity(self, quantity: float):
        if not (type(quantity) == float or type(quantity) == int):
            raise ValueError("Quantity must be a number")
        else:
            self.quantity = quantity

    @property
    def total_price(self):
        totalprice = self.price * self.quantity
        return totalprice

    def __str__(self):
        return f"name: {self.name}, unit price: {format(self.price, '.2f')}€/{self.unit}, quantity: {format(self.quantity, '.2f')}{self.unit}, total price {format(self.price * self.quantity, '.2f')}€"


#It doesn't look like I'll be able to make adding total prices together work the way I'm expected to with the time I have left. 








