cost1 = float(input("Enter the cost of your first item :"))
cost2 = float(input("Enter the cost of your second item :"))


if cost1 + cost2 > 10.00:
     print("sorry too much" )
else:
     change = 10 - cost1 - cost2
     print("that will be" + str(change))
