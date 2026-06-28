try:
    cgpa = float(input("Enter CGPA: "))

    if not 0 <= cgpa <= 10:
        raise ValueError("CGPA must be between 0 and 10.")

    print("Input accepted.")

except ValueError as error:
    print(error)