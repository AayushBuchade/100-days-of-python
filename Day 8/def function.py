def life_in_weeks(age):
    years_left = 90 - int(age)

    weeks_left = years_left * 52
    day_left = weeks_left * 7

    print(f"you have {weeks_left} weeks left")
    print(f"you have {day_left} days left ")


life_in_weeks(int(input("your age : ")))