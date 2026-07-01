placement_scores = [58, 67, 72, 81, 91, 76, 63]

processed_scores = list(
    map(
        lambda score: score + 5,
        filter(
            lambda score: score >= 60,
            placement_scores
        )
    )
)

print(processed_scores)