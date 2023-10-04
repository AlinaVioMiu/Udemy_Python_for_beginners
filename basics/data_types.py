id = 1
first_name = 'John'
last_name = '   Bailey'
ssn = '123-45-6789'
has_insurance = True
billing_amount = '10000'
print(type(billing_amount))
billing_amount = float(billing_amount)
print(id, first_name, last_name.lstrip(), ssn, has_insurance, billing_amount, ssn[7:len(ssn)])
