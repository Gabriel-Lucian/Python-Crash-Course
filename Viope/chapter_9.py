class Cart:
    """This calss manage the shoping cart."""

    shoppingcart = []

    def addstuff(self):
        esine = input("What will be added to the cart?: ")
        self.shoppingcart.append(esine)

    def checkout(self):
        print("Following objects were added: ")
        for i in range(0, len(self.shoppingcart)):
            print(self.shoppingcart[i], end = " ")

def main():
    customer = Cart()
    while True:
        selection = input("Add more of go to checkout?")
        if selection == "checkout":
            customer.checkout()
            break
        else:
            customer.addstuff()

if __name__ == "__main__":
    main()

