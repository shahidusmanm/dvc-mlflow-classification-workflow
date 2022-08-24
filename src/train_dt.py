import mlflow
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


def dt ():
    return DecisionTreeClassifier()

def rf ():
    return RandomForestClassifier()

def svm ():
    return SVC()


def train_model (model_type, train_df):
    mlflow.sklearn.autolog()

    if model_type == 'dt':
        model = dt()
    elif model_type == 'rf':
        model = rf()
    elif model_type == 'svm':
        model = svm()
    else:
        print ('Unsupported Model; Please choose from dt, rf or svm')
    
    X = train_df.drop (columns = ['label'])
    y = train_df ['label']

    model.fit (X, y)

    return model

