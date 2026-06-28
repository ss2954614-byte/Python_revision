from datetime import datetime

accuracy = 0.8734

with open("training_log.txt", "a") as file:
    file.write(
        f"{datetime.now()} | Logistic Regression | Accuracy: {accuracy:.2%}\n"
    )

print("Training log updated.")