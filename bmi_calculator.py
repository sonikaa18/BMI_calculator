print("BMI CALCULATOR")
#Type Concersion
height=float(input("Enter your height in metres\n"))
weight=float(input("Enter your weight in kg\n"))
BMI= int(weight//height**2)
#---fString-----
print(f"your Body Mass Index is :{BMI}")
