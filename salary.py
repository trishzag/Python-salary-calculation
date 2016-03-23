# 1. - determine pay and benefits of employees

# receive input for employee name
employee = input("Please enter employee name:")

#receive input for employee grade
# Grade  Allowance Grade 1 $1750, 2 $1250,3 $750, 4 $250
grade = int(input("Please enter employee grade (MUST BE BETWEEN 1 and 4, INCLUSIVE):"))
if (grade < 1 or grade > 4):
    grade = input("Invalid entry; Please re-enter grade between 1 and 4, inclusive:")
elif (grade == 1):
    allowance = 1750
elif grade == 2:
    allowance = 1250
elif grade == 3:
    allowance = 750
elif grade == 4:
    allowance = 250

#receive input for employee salary
basic_pay = float(input("Please enter employee salary:"))

# ensure valid entry 
while basic_pay <=0:
    basic_pay = float(input("Invalid entry; Please enter a valid salary:"))

#determine HRA - HRA is 25% of basic pay
hra = basic_pay * .25

#calculate gross pay
gross_pay = (basic_pay + hra + allowance)

# determine tax
#Gross Pay          Tax Rate 
#<=2000             No Tax
#>2000 and <=3000   3% of Gross Pay
#>3000 and <=5000   5% of Gross Pay
#>50000             8% of Gross Pay
if gross_pay <= 2000:
    tax = 0
elif gross_pay > 2000 and gross_pay <=3000:
    tax = gross_pay * .03
elif gross_pay > 3000 and gross_pay <=5000:
    tax = gross_pay * .05
elif gross_pay > 5000:
    tax = gross_pay * .08

net_pay = gross_pay - tax

#concatenating strings with the variables
print (employee + " Pay information:")
print ("Basic Pay = $" + str(format(basic_pay, '.2f')) + "  HRA = $" + str(format(hra, '.2f')) + "  Allowance = $" + str(format(allowance, '.2f')))
print("Gross Pay = $" + str(format(gross_pay, '.2f')) + " LESS Taxes of: $" + str(format(tax, '.2f')) + " EQUALS Net Pay of: $" + str(format(net_pay, '.2f')))

#setting format within string
print ("Employee:  ", employee)
print ("HRA: %.2f" %(hra))
print ("Basic Pay: %.2f" %(basic_pay))
print ("Perks: %.2f" %(allowance))
print ("Gross Pay: %.2f" %(gross_pay))
print ("Taxes: %.2f" %(tax))
print ("NET PAY: %.2f" %(net_pay))
