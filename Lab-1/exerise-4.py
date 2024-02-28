# Develop a class ‘car’ that takes the attributes of wheels, miles, make, model, year, sold_on by default.
# Develop two methods ‘sales_price’ and ‘purchase_price’. The ‘sales_price’ checks if ‘sold_on’ is none
# then return price (non-zero value) otherwise return zero value. . The ‘purchase_price’ checks if
# ‘sold_on’ is none then return price (zero value) otherwise return price (non-zero value).
class car:
    wheels=''
    miles=''
    make=''
    model=''
    year=''
    sold_on=None
    def sales_price(self):
        if self.sold_on == None:
            return "Price=200$"
        else:
            return "0"

    def purchase_price(self):
        if self.sold_on == None:
            return "0"  
        else:
            return "Price=200$"

obj=car()
result1=obj.purchase_price()
result2=obj.sales_price()
print(result1)
print(result2)

obj1=car()
obj1.sold_on='2024-02-28'
result1=obj1.purchase_price()
result2=obj1.sales_price()

print(result1)
print(result2)
