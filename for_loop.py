student_scores = [78, 91, 67, 88, 95, 72]

for score in student_scores:
    if score >= 80:
        print(f"{score}: High Performer")
    else:
        print(f"{score}: Needs Improvement")



model_results = {
    "Logistic Regression": 0.84,
    "Random Forest": 0.89,
    "Decision Tree": 0.81,
    "KNN": 0.86
}

for model, accuracy in model_results.items():
    print(f"{model}: {accuracy * 100:.2f}%")