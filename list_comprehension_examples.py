placement_scores = [62, 74, 81, 55, 90, 78, 69]

qualified_scores = [
    score
    for score in placement_scores
    if score >= 70
]

score_labels = [
    "Qualified" if score >= 70 else "Not Qualified"
    for score in placement_scores
]

print(qualified_scores)
print(score_labels)