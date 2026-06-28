# First function: Calculate the accuracy of a model based on correct and total predictions

def calculate_accuracy(correct_predictions, total_predictions):
    accuracy = (correct_predictions / total_predictions) * 100
    return round(accuracy, 2)


accuracy = calculate_accuracy(842, 1000)

print(f"Model Accuracy: {accuracy}%")




# Second function: Summarize a dataset by calculating count, minimum, maximum, and average values

def summarize_dataset(values):
    summary = {
        "count": len(values),
        "minimum": min(values),
        "maximum": max(values),
        "average": round(sum(values) / len(values), 2)
    }

    return summary


cgpa_scores = [7.8, 8.1, 6.9, 8.7, 7.5]

print(summarize_dataset(cgpa_scores))