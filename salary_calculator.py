hours = float(input('PLease provide your monthly ours amount '))                          # amount of hours worked totaly
euros_hour = float(input('Please provide your hourly payment brutto in euros '))          # the price of one hour brutto

monthly_salary_total_brutto = hours * euros_hour                                          # total monthly salary brutto
if monthly_salary_total_brutto < 500:
    print('Advice tax agency')
    breakpoint()

print('')
print('Your total monthly income is ', round(monthly_salary_total_brutto, 2), 'euros.')

minimum_bare = 500                                                                        # minimum non taxable income


monthly_tax = ((monthly_salary_total_brutto - minimum_bare) / 100) * 24                   # total monthly taxes
#social_tax = ((monthly_salary_total_brutto - minimum_bare) / 100) * 2                    # social tax(2%)
#pension_fund = social_tax                                                                # pension fund(2%)


#print(monthly_tax)

netto_income = monthly_salary_total_brutto - minimum_bare - monthly_tax + minimum_bare    # clean monthly income minus all taxes


print('Your total monthly tax is ', round(monthly_tax, 2), 'euros.', 'Wich is 20% income tax, 2% social tax & 2% pension fund.')
print('     info: By the law of Estonian republic the minimal non taxable income is 500 euros.')
print('Your monthly income after taxes is ', round(netto_income, 2), 'euros.')

print('Have a nice day.')