#dictionary showing available stock
prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print (key)
    print ("price: %s" % prices[key])
    print ("stock: %s" % stock[key])

#Total price of goods
total = 0
for key in prices: 
    total = prices[key]*stock[key] + total 
print (total)

#total with stock updates
def compute_bill(food):
    total = 0
    for i in food:
        if stock[i] > 0:
            total += prices[i]
            stock[i] -= 1
    return total