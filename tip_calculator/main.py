bill = float(input("what is the total bill: "))
tip_amount = float(input("How much tip would you like to give: "))
bill_split = int(input("How many peple to split the bill: "))

each_person = (bill / bill_split + tip_amount)

print(f"Each person should pay: {each_person}")
