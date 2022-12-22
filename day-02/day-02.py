# PROJECT 2
print('Welcome to the tip calculator.')
gross_bill = input('What was the total bill? $')
tip_porcentaje = input('What porcentage tip would you like to give? 10, 12, or 15? ')
total_people = input('How many people to split the bill? ')

tip = (float(gross_bill) * int(tip_porcentaje)) / 100

net_bill = float(gross_bill) + tip

result = net_bill / int(total_people)

final_amount = "{:.2f}".format(round(result, 2))

print(f'each person should pay: ${final_amount}')
