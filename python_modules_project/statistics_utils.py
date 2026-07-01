def calculate_average(values):
    return sum(values) / len(values)


def calculate_accuracy(correct_predictions, total_predictions):
    return round(
        (correct_predictions / total_predictions) * 100,
        2
    )