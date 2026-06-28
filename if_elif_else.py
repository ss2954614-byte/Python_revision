model_accuracy = 87.4

if model_accuracy >= 90:
    performance = "Excellent"
elif model_accuracy >= 80:
    performance = "Good"
elif model_accuracy >= 70:
    performance = "Average"
else:
    performance = "Requires Optimization"

print(f"Model Performance: {performance}")