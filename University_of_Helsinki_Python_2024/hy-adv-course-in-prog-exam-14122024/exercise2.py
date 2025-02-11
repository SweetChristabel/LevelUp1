# Write your solution to exercise 2 here
class ShoppingList:
    def __init__(self):
        self.products = []
        
    def add_product(self, product: tuple):
        name = product[0]
        price = product[1]
        unit = product[2]
        quant = product[3]
        if quant <= 0:
            return
        self.products.append(Product(name, price, unit, quant))

    def return_product(self, product: str):
        for i in self.products:
            if i.name == product:
                return str(i)
        raise ValueError("Product not found on the shopping list")
    
    def remove_product(self, product: str, amount = 0.0):
        purge = ""     
        for i in self.products:
            if i.name == product:
                if amount == 0.0:
                    purge = i
                else:
                    if i.quantity <= amount:
                        purge = i
                    else:
                        i.quantity -= amount
        if purge != "":
            self.products.remove(purge)
        
  #Taking the easy route with the value changes here since there's no encapsulation and helper methods in the Product class.
  #I'm choosing not to implement them since I don't have that much time. I know it's a thing though and how to do it.
    
    def change_product_unit_price(self, product: str, newprice: float):
        for i in self.products:
            if i.name == product:
                i.price = newprice 

    def return_all_products(self):
        return [str(i) for i in self.products]
    
    def return_total_price_of_shopping_list(self):
        sum = 0
        for i in self.products:
            sum += i.price * i.quantity
        return sum            


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
