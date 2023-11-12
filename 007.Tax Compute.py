import sys
#prompt the user to enter filing status:
status = eval(input(
      "(0-single filer, 1-married jointly,\n" +
      "2-married separately, 3-head of household)\n" +
      "Enter the filing status:"))

#prompt the user to enter taxable income
income = eval(input("Enter the taxable income:"))

#compute tax
tax = 0

if status == 0:
    if income <=8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 8350 *0.10 + (33950 - 8350) * 0.15 + \
              (income - 33950) * 0.25
    elif income <= 171550:
        tax = 8350 *0.10 + (33950 - 8350) * 0.15 + \
              (82250 - 33950) * 0.25 + (income - 82250) * 0.28
    elif income <= 372950:
        tax = 8350 *0.10 + (33950 - 8350) * 0.15 + \
              (82250 - 33950) * 0.25 + (171550  - 82250) * 0.28 + \
              (income - 171550) * 0.33

    else:
        tax = 8350 *0.10 + (33950 - 8350) * 0.15 + \
              (82250 - 33950) * 0.25 + (171550  - 82250) * 0.28 + \
              (372950 - 171550) * 0.33 +(income - 372950) * 0.35;
#tax compute for married file jointly
elif status == 1:
    print("left as exercise")

#tax compute for married separately
elif status == 2:
    print("left as exercise")

#tax compute tax for head of household
elif status == 3:
    print("left as exercise")

else:
    print("Error: invalid status")
    sys.exit()

#display the result
print("Tax is", format(tax,".2f"))






    
        
