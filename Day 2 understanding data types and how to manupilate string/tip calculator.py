print("welcome to the tip calculator ")
bill = int(input("What is the total bill "))
tip = int(input("how much tip would you like to give 10 ,15 and 20 " ))
people = int(input("how many people will split the bill "))
total_bill = bill + bill*tip/100
bill_per_person = round(total_bill/people,2) ## round of to two decimal places
print(f"you need to pay {bill_per_person} per person") 