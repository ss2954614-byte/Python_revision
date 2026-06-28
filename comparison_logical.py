age = 21
cgpa = 8.2

print(age >= 18)
print(cgpa > 7.5)

eligible = age >= 18 and cgpa > 7.0
print("Eligible for Internship:", eligible)

print(age < 18 or cgpa > 8.0)
print(not eligible)