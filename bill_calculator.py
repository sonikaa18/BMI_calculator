print("Welcome to the tip calculator!")
total_bill=float(input("what eas the total bill? $"))
tip=int(input("how much tip would you like to give? 10, 12 or 15 ? $"))
total_people=int(input("how many people to split the bill? "))
per_person_bill= (total_bill+tip)/total_people
# using round() function
print(f"Each person should pay: ${round(per_person_bill,2)}")
# convert the float into a string of format --> "{:.3f}"
print(type("{:.3f}".format(round(per_person_bill,2))))
#print("{:.2f}".format(round(per_person_bill, 2)))
