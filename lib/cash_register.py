#!/usr/bin/env python3
class CashRegister:
    
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.price_list = []
    
    def add_item(self, item, price, quantity=1):
        self.item = item
        self.items.extend([item] * quantity)
        self.price_list.append(
            {"item": item, "quantity": quantity, "price": price}
        )
        self.price = price

        if quantity > 1:
            self.total = self.total + (price * quantity)
        else:
            self.total = self.total + price


    def apply_discount(self):
        if self.discount == 0:
            print('There is no discount to apply.')
        else:
            self.total = self.total * (1 - (self.discount / 100))
            t = int(self.total)
            print(f'After the discount, the total comes to ${t}.')
    

    def void_last_transaction(self):
        if not self.price_list:
            return 'There are no transactions to void.'
        self.total -= (
            self.price_list[-1]["price"]
            * self.price_list[-1]["quantity"]
        )
        for _ in range(self.price_list[-1]["quantity"]):
            self.items.pop()
        self.price_list.pop()
    