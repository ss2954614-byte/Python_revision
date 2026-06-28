epoch = 1
validation_accuracy = 0.0

while epoch <= 10:
    validation_accuracy += 0.03

    if validation_accuracy >= 0.90:
        print(f"Target achieved at epoch {epoch}")
        break

    epoch += 1