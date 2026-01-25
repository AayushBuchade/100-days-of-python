print("Welcome to the Tip Calculator")

bill = float(input("What was your total bill? ₹"))
tip_percent = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people will split the bill? "))

tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount
amount_per_person = total_bill / people
final_amount_per_person = round(amount_per_person, 2)
print(f"Each person should pay: ₹{final_amount_per_person}")
