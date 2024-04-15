

# this project is to get the discounted cost of a given selling price
selling_price = int(input("enter the cost to be discounted : "))
discountPercent = int(input("enter the percentage of discount : "))
discount = selling_price - selling_price * discountPercent / 100
print("Original price : ", selling_price)
print("discounted price : ", discount)
