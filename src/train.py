import mlflow
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import config
import pandas as pd

def dt (max_depth):
    return DecisionTreeClassifier(max_depth = max_depth)

def rf ():
    return RandomForestClassifier()

def svm ():
    return SVC()


def train_model (model_type, train_df, test_df, max_depth):
    mlflow.start_run()
    mlflow.sklearn.autolog()

    if model_type == 'dt':
        model = dt(max_depth=max_depth)
    elif model_type == 'rf':
        model = rf()
    elif model_type == 'svm':
        model = svm()
    else:
        print ('Unsupported Model; Please choose from dt, rf or svm')
    
    X = train_df.drop (columns = ['label'])
    y = train_df ['label']

    model.fit (X, y)
    test_acc = model.score (test_df.drop(columns=['label']), test_df['label'])
    print ('Testing accuracy: ' + str(test_acc))
    mlflow.log_metric("Testing Accuracy", test_acc)

    if config.final_model:
        run_id = mlflow.active_run().info.run_id
        with open(config.root_dir + "src/feature_store/loggedmodel.txt", "w") as text_file:
            print(run_id, file=text_file)
    else:
        run_id = None
    mlflow.end_run()
    
    return model, run_id



#Main Execution
train_df = pd.read_csv(config.root_dir + 'src/feature_store/train.csv')
test_df = pd.read_csv(config.root_dir + 'src/feature_store/test.csv')

if config.final_model:
    train_df = pd.concat([train_df, test_df], ignore_index=True, sort=False)
    train_model (config.model, train_df, test_df, config.max_depth)

else:
    #Use this function to do model exploration. DVC will automatically track any 
    #changes to this file and will only run this stage on subsequent pipeline runs.
    #Current values are provided as placeholders.
    
    train_model ('dt', train_df, test_df, 5)
