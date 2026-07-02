def prediction_stream(predictions):
    for prediction in predictions:
        yield {
            "prediction": prediction,
            "status": "Processed"
        }


results = [
    "Placed",
    "Placed",
    "Not Placed",
    "Placed"
]

for item in prediction_stream(results):
    print(item)