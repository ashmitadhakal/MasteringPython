

class Item:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class CartIterator:
    def __init__(self, items):
        self.__items=items
        self.__index=0

    def __next__(self):
        if self.__index<len(self.__items):
            item=self.__items[self.__index]
            self.__index +=1
            return item
        raise StopIteration

class Cart:
    def __init__(self):
        self.__items = []

    def __iter__(self):
        return CartIterator(self.__items)

    def add(self,item):
        self.__items.append(item)
    
    def total(self):
        total_price = 0.0
        for item in self.__items:
            total_price += item.price
        return total_price
    
cart = Cart()
cart.add(Item("apples",1.99))
cart.add(Item("eggs",5.99))

print(cart.total())

for item in cart:
    print(f"{item.name}: {item.price}")
