file_path = "customer_data.csv"

try:
    with open(file_path, "r") as file:
        data = file.read()

    print("Dataset loaded successfully.")

except FileNotFoundError:
    print(f"Dataset '{file_path}' was not found.")