print("Tax Calculator")


#Taking input salary by taxpayer citizen
sal=int(input("Enter your salary: "))

#for salary less trhan 100000, no tax
if sal <= 100000:
    print("NO TAX!")

#10% between 100000 to 500000
elif sal > 100000 and sal <= 500000:
    sal2 = sal - 100000
    tax = sal2 * 0.10
    print("Tax Payable is INR.", tax)

#20 thereafter 500000
else:
    tax1 = 400000 * 0.10
    sal3 = sal - 500000
    tax2 = sal3 * 0.20
    print("Tax Payable is INR.", tax1 + tax2)

print("Thankyou for using tax calculator!")
