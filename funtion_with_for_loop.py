def min_max_scale(values):
    minimum = min(values)
    maximum = max(values)

    scaled_values = [
        (value - minimum) / (maximum - minimum)
        for value in values
    ]

    return scaled_values


scores = [55, 68, 72, 88, 91]

print(min_max_scale(scores))