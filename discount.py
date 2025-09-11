class Discount:
    def apply_discount(self, *args, **kwargs):
        """
        Simulates static polymorphism to apply:
        
        1. Flat discount:
           apply_discount(amount=500, discount_type='flat', value=50)

        2. Percentage discount:
           apply_discount(amount=1000, discount_type='percentage', value=10)

        3. Buy One Get One (BOGO):
           apply_discount('bogo', price_per_item, quantity)
        """

        # Case 1 & 2: Flat or Percentage discount via kwargs
        if 'discount_type' in kwargs:
            amount = kwargs.get('amount', 0)
            discount_type = kwargs.get('discount_type')
            value = kwargs.get('value', 0)

            if discount_type == 'flat':
                discounted_price = max(0, amount - value)
                print(f" Flat Discount of ₹{value} applied.")
                return discounted_price

            elif discount_type == 'percentage':
                discounted_price = max(0, amount - (amount * value / 100))
                print(f" {value}% Percentage Discount applied.")
                return discounted_price

            else:
                print(" Invalid discount type.")
                return amount

        # Case 3: BOGO using *args
        elif len(args) == 3 and args[0] == 'bogo':
            _, price_per_item, quantity = args
            if quantity <= 0:
                return 0
            effective_qty = (quantity // 2) + (quantity % 2)
            total_price = effective_qty * price_per_item
            print(f" BOGO Applied: Pay for {effective_qty}, Get {quantity}")
            return total_price

        else:
            print(" Invalid discount parameters.")
            return 0


# ----------- Example Usage (Direct Execution) -----------

d = Discount()

# Flat discount of ₹50 on ₹500
price1 = d.apply_discount(amount=500, discount_type='flat', value=50)
print(f" Final Price after flat discount: ₹{price1}\n")

# Percentage discount of 10% on ₹1000
price2 = d.apply_discount(amount=1000, discount_type='percentage', value=10)
print(f" Final Price after percentage discount: ₹{price2}\n")

# Buy One Get One Free on item costing ₹200, buying 3 items
price3 = d.apply_discount('bogo', 200, 3)
print(f" Final Price after BOGO discount: ₹{price3}\n")

# Invalid usage examples (for reference)
price4 = d.apply_discount('bogo', 200)  # missing quantity
price5 = d.apply_discount(amount=300, discount_type='unknown', value=10)
