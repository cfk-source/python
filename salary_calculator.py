hours = float(input('PLease provide your monthly ours amount '))                          # amount of hours worked totaly
euros_hour = float(input('Please provide your hourly payment brutto in euros '))          # the price of one hour brutto

monthly_salary_total_brutto = hours * euros_hour                                          # total monthly salary brutto

print('Your total monthly income is ', monthly_salary_total_brutto, 'euros.')

minimum_bare = 500                                                                        # minimum non taxable income


monthly_tax = ((monthly_salary_total_brutto - minimum_bare) / 100) * 24                   # total monthly taxes
#social_tax = ((monthly_salary_total_brutto - minimum_bare) / 100) * 2                   # social tax(2%)
#pension_fund = social_tax                                                               # pension fund(2%)


#print(monthly_tax)

netto_income = monthly_salary_total_brutto - minimum_bare - monthly_tax + minimum_bare    # clean monthly income minus all taxes


print('Your total monthly tax is ', monthly_tax, 'euros.', 'Wich is 20% income tax, 2% social tax & 2% pension fund.')
print('info: By the law of Estonian republic the minum non taxable income is 500 euros.')
print('Your monthly income after taxes is ', netto_income, 'euros.')

print('Have a nice day.')