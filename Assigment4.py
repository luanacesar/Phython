name = input("Please enter your name: ")
hours = float(input("Please enter your number of hours/day:   "))
hoursPaid = float(input("How much you get per hour?"))
tax = float(input("Please enter your tax:   "))
vacationPay = float(input("Please enter your vacation pay:  "))
dayWorked = float(input("Please enter the number of day did you work/week:  "))

WeeklyP = ((dayWorked * hoursPaid * hours) - tax + vacationPay)

print('', " Name of employee is {} and Weekly pay is ${:g}.".format(name, WeeklyP), '', sep='***')





