cgpa_scores = [7.2, 8.5, 6.9, 9.1, 7.8]

percentage_scores = list(
    map(
        lambda cgpa: round((cgpa / 10) * 100, 2),
        cgpa_scores
    )
)

print(percentage_scores)