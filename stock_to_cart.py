customers = ["Ada", "John", "Mike", "Zoe"]
carts = [2, 5, 3, 4]
stock = 13
served_customers = []
new_customers = []
underserve_list = []

for idx, (customer, cart) in enumerate(zip(customers, carts), start = 1):
    if stock > 0:
        serve = cart if stock > cart else stock
        underserve = cart - serve
        stock -= serve
        served_customers.append(customer)
        print(f"Served {customer} {serve} stock out of {cart} demanded\nUnmet demand is: {underserve}\nremaining stock: {stock}")
        if underserve > 0:
            underserve_list.append((customer, underserve))  
        new_customers.append(f"New Customer: {idx}")  # marketing adds more people mid-sale



print(f"New customers: {new_customers}")
customers.extend(new_customers)
print(f"Customers list: {customers}")
print("Final served:", served_customers)

print(f"Underserved customers and the remaining stock to balance: {underserve_list}")
non_serve = [customer for customer in customers if customer not in served_customers]
print(f"Non_serve: {non_serve}")
