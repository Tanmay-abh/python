# Create the product tuple
product = ("Laptop", 50000, "Black", "Samsung", "Electronics")
print("Product tuple:", product)

# Access and print the second element
print("Second element:", product[1])

# Slice and print the last two elements
print("Last two elements:", product[-2:])

# Check for "Electronics" in the tuple
if "Electronics" in product:
    print('"Electronics" is present in the product tuple.')

# Create a prices tuple and count 1000
prices = (1000, 1500, 1200, 1100, 900)
count_1000 = prices.count(1000)
print("Number of times 1000 appears in prices:", count_1000)

# Find and print the max and min price
print("Maximum price:", max(prices))
print("Minimum price:", min(prices))

# Print each item in the product tuple on a new line
print("Product items:")
for item in product:
    print(item)

# Convert tuple to list, change price, convert back to tuple
product_list = list(product)
product_list[1] = 55000  # Change price
product = tuple(product_list)
print("Updated product tuple with new price:", product)

# Add a new item "In Stock" by concatenation
product = product + ("In Stock",)
print("Product tuple after adding 'In Stock':", product)

# Remove "Electronics" by converting to list
product_list = list(product)
if "Electronics" in product_list:
    product_list.remove("Electronics")
product = tuple(product_list)
print("Product tuple after removing 'Electronics':", product)

# Unpack the tuple into variables (adjust based on current length)
# Assuming the tuple now has exactly 5 items
name, price, color, brand, stock_status = product
print("Unpacked values:")
print("Name:", name)
print("Price:", price)
print("Color:", color)
print("Brand:", brand)
print("Stock Status:", stock_status)

# Create a nested tuple of 3 product tuples
product1 = ("Tablet", 20000, "White", "Lenovo", "Electronics")
product2 = ("Monitor", 15000, "Black", "LG", "Electronics")
product3 = ("Smartphone", 30000, "Blue", "OnePlus", "Electronics")
nested_products = (product1, product2, product3)

# Access and print the name of the second product
print("Name of the second product in nested tuple:", nested_products[1][0])
