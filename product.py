# Define the Product class
class Product:
    def __init__(self, id, name, category, price):
        self.id = id
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', category='{self.category}', price={self.price})"


# Define the ProductSearch class with simulated static polymorphism
class ProductSearch:
    def __init__(self, products):
        self.products = products

    def search(self, name=None, **kwargs):
        results = self.products

        # Search by name (if provided)
        if name:
            results = [p for p in results if name.lower() in p.name.lower()]

        # Search by category (if provided)
        category = kwargs.get("category")
        if category:
            results = [p for p in results if category.lower() == p.category.lower()]

        # Search by price range (if both min_price and max_price are provided)
        min_price = kwargs.get("min_price")
        max_price = kwargs.get("max_price")
        if min_price is not None and max_price is not None:
            results = [p for p in results if min_price <= p.price <= max_price]

        return results


# Sample products
products = [
    Product(1, "iPhone 14", "Electronics", 999),
    Product(2, "Samsung Galaxy", "Electronics", 850),
    Product(3, "Nike Shoes", "Footwear", 120),
    Product(4, "Puma Shoes", "Footwear", 110),
    Product(5, "iPhone Case", "Accessories", 25),
    Product(6, "MacBook Pro", "Electronics", 1999),
    Product(7, "Adidas Running Shoes", "Footwear", 130),
]

# Initialize ProductSearch with the product list
search_engine = ProductSearch(products)

# ---- Example Searches ----

# 1. Search by name only
print("Search by name (iPhone):")
print(search_engine.search(name="iPhone"))

# 2. Search by name and category
print("\nSearch by name (iPhone) and category (Electronics):")
print(search_engine.search(name="iPhone", category="Electronics"))

# 3. Search by name, category, and price range
print("\nSearch by name (Shoes), category (Footwear), and price range (100-125):")
print(search_engine.search(name="Shoes", category="Footwear", min_price=100, max_price=125))

# 4. Search by category only
print("\nSearch by category only (Footwear):")
print(search_engine.search(category="Footwear"))

# 5. Search by price range only
print("\nSearch by price range only (1000-2000):")
print(search_engine.search(min_price=1000, max_price=2000))
