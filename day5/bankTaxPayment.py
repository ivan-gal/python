
total = balance
monthlyInteresRate = annualInterestRate / 12.0
minimunPayment = monthlyPaymentRate

for m in range(12):
    unPaidBalance = total - total * minimunPayment
    total = unPaidBalance + unPaidBalance * monthlyInteresRate

print('Remaining balance: ' + str(round(total, 2)))
