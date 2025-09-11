# Base class
class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must override the pay() method.")


# Subclass for Credit Card Payment
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f" Processing credit card payment of ₹{amount}...")
        print(" Credit card payment successful.\n")


# Subclass for UPI Payment
class UPIPayment(Payment):
    def pay(self, amount):
        print(f" Initiating UPI payment of ₹{amount}...")
        print(" UPI payment successful.\n")


# Subclass for Cash on Delivery (COD)
class CODPayment(Payment):
    def pay(self, amount):
        print(f" Order placed with Cash on Delivery for ₹{amount}.")
        print(" Please pay the amount upon delivery.\n")


# ----------- Example Usage -----------

# Create instances of each payment method
credit_card = CreditCardPayment()
upi = UPIPayment()
cod = CODPayment()

# Use polymorphism: same method name, different behavior
payment_methods = [credit_card, upi, cod]
amount = 999

for method in payment_methods:
    method.pay(amount)
