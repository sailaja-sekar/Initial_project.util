name="Sailaja"
age=25
product_price=1500
discount_price=product_price*0.1
if discount_price>100:
    final_price=product_price-discount_price
else:
    final_price=product_price
print("Name:", name)
print("Age:", age)
print("Product Price:", product_price)
print("Discount Price:", discount_price)
print("Final Price:", final_price)