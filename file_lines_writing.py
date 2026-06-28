predictions = [
    "Placed",
    "Not Placed",
    "Placed",
    "Placed"
]

with open("predictions.txt", "w") as file:
    file.writelines(
        prediction + "\n"
        for prediction in predictions
    )

print("Predictions saved.")