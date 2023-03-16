#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantitiy=1):
        for element in range(quantitiy):
            self.items.append(title)

        self.total += price*quantitiy

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total*(self.discount * .01)
            print(
                f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")
