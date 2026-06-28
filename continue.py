customer_ages = [22, 17, 34, 19, 45, 16, 28]

eligible_customers = []

for age in customer_ages:
    if age < 18:
        continue

    eligible_customers.append(age)

print(eligible_customers)