from sklearn.metrics import accuracy_score
import mlflow

def evaluate_validation (trained_model, holdout_data):
    mlflow.sklearn.autolog()
    predictions = trained_model.predict (holdout_data.drop(columns=['label']))
    acc = accuracy_score (holdout_data['label'], predictions)
    print ('Accuracy on the Blind Holdout Set: ' + str(acc))
    return acc