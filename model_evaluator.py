class ModelEvaluator:
    def __init__(self, model_name, accuracy):
        self.model_name = model_name
        self.accuracy = accuracy

    def evaluate(self):
        if self.accuracy >= 0.90:
            return "Excellent"

        if self.accuracy >= 0.80:
            return "Good"

        return "Needs Improvement"


logistic_regression = ModelEvaluator(
    model_name="Logistic Regression",
    accuracy=0.87
)

print(logistic_regression.evaluate())