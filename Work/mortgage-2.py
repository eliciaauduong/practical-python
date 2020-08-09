# exercise 1.8

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
month = 0

while principal > 0:
    if month < 12:
        principal = principal * (1 + rate/12) - (payment + extra_payment)
        total_paid = total_paid + payment + extra_payment
    else:
        principal = principal * (1 + rate/12) - payment
        total_paid = total_paid + payment
    month += 1

print('Total paid', total_paid)
print('Number of months required', month)
