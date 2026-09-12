import os

files_to_delete = ["data/cleaned/data-cleaned.csv",
                   "data/preprocessed/data_train.csv",
                   "data/preprocessed/data_test.csv",
                   "data/prediction-baseline/prediction_baseline.csv",
                   "data/prediction-linear-regression/prediction_linear_regression.csv"]

for file_path in files_to_delete:
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Successfully deleted: {file_path}")
        else:
            print(f"Skipped (File does not exist): {file_path}")

    except PermissionError:
        print(f"Permission denied: Could not delete {file_path}")
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")