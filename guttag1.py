# Minimum monthly payment = Minimum monthly payment rate x Balance
# (Minimum monthly payment gets split into interest paid and principal paid)
# Interest Paid = Annual interest rate / 12 months x Balance
# Principal paid = Minimum monthly payment – Interest paid
# Remaining balance = Balance – Principal paid 

""""
## Question 1: Write a program to calculate the credit card balance 
## after one year if a person only pays the minimum monthly payment required by the credit card company each month. 

balance = float(input('Please enter the outstanding balance on the credit card:'))
interest_rate = float(input('Please enter your annual interest rate:'))
min_payment_percent = float(input('Please enter your minimum monthly payment rate:' ))

for i in range(1,13):
	month = i
	print('month is:',i)
	min_payment = min_payment_percent * balance
	print('Minimum payment made:', min_payment)
	interest_paid = (interest_rate/12) * balance
	print('Out of that interest paid:', interest_paid)
	principal_paid = min_payment - interest_paid
	print('Out of that principal paid:', principal_paid)
	remaining_balance = balance - principal_paid
	print('Remaining balance:', remaining_balance)
	balance = remaining_balance

"""
## Question 2: 

##Monthly interest rate = Annual interest rate / 12.0
##Updated balance each month = Previous balance * (1 + Monthly interest rate) – Minimum monthly payment 


balance = float(input('Please enter the outstanding balance on the credit card:'))
interest_rate = float(input('Please enter your annual interest rate:'))
money_to_be_paid = (balance * interest_rate) + balance
monthly_payment = int(round(money_to_be_paid/24))
print(monthly_payment)

monthly_payment = 10
monthly_rate = interest_rate/24

while balance > 0:
	monthly_payment = monthly_payment+10
	month = 0


	while month < 24 and balance > 0:
		month = month+1
		interest = monthly_rate * balance
		balance = balance - monthly_payment
		balance = balance+interest


print("Monthly payment to pay off debt in 1 year", monthly_payment)
print("Number of months needed", month)
print("Balance",balance)







