from config import PROJECT_NAME
from dataset_utils import dataset_summary
from statistics_utils import calculate_accuracy
from validation_utils import validate_cgpa

summary = dataset_summary(10000, 12)

accuracy = calculate_accuracy(846, 1000)

cgpa = 8.1

print(PROJECT_NAME)
print(summary)
print(f"Accuracy: {accuracy}%")
print(validate_cgpa(cgpa))




# Project Structure

# python_modules_project/

# │
# ├── app.py
# ├── statistics_utils.py
# ├── validation_utils.py
# ├── dataset_utils.py
# └── config.py