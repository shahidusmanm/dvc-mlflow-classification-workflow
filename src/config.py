#Directory Config
root_dir = 'C:/Users/Usman/dvc-mlflow-classification-workflow/'

#MLFlow Experiment Config
experiment_name = 'MLFlow'
tracking_folder = 'C:/Users/Usman/dvc-mlflow-classification-workflow/src/mlruns'

#Train/Test Split config
#15% of the Original Data is always set aside as the Blind Holdout Dataset. It is used in src/evaluate.py
train_ratio = 0.7 

#Final Model Config
final_model = False #Setting this to True trains and registers a model with MLFlow. Keep False until a model needs to be deployed.
model = 'dt'
max_depth = 5
model_name = 'Decision Tree Production' 