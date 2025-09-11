class Cart:
    def __init__(self):
        self.items = {}  # Dictionary to store products and their quantities

    def add_to_cart(self, *args, **kwargs):
        """
        Adds products to the cart using static polymorphism:
        - *args: ("product_name", quantity)
        - **kwargs: product_name=quantity, multiple at once
        """
        # Case 1: Single product using *args
        if args:
            if len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], int):
                product_name = args[0]
                quantity = args[1]
                self._add_item(product_name, quantity)
            else:
                print("Invalid usage of *args. Expected format: add_to_cart('product', quantity)")

        # Case 2: Multiple products using **kwargs
        for product_name, quantity in kwargs.items():
            if isinstance(product_name, str) and isinstance(quantity, int):
                self._add_item(product_name, quantity)
            else:
                print(f"Invalid entry: {product_name} = {quantity}. Must be (str, int).")

    def _add_item(self, product_name, quantity):
        """Helper method to add or update quantity in the cart"""
        if product_name in self.items:
            self.items[product_name] += quantity
        else:
            self.items[product_name] = quantity

    def show_cart(self):
        """Displays the current contents of the cart"""
        if not self.items:
            print(" Cart is empty.")
        else:
            print(" Cart Contents:")
            for product, qty in self.items.items():
                print(f"- {product}: {qty}")


# ---------- Direct Execution Starts Here ----------

cart = Cart()

# Add single item using *args
cart.add_to_cart("iPhone", 2)

# Add multiple items using **kwargs
cart.add_to_cart(Macbook=1, AirPods=3, Charger=2)

# Add more of an existing item using *args
cart.add_to_cart("iPhone", 1)

# Invalid usage examples
cart.add_to_cart("InvalidInputOnlyOneArg")
cart.add_to_cart(123, "NotAQuantity")
cart.add_to_cart(Headphones="two")  # Invalid type

# Show final cart contents
cart.show_cart()
