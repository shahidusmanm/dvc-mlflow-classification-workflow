import mlflow, config
import pandas as pd

def evaluate_validation (run_id, holdout_data):
    if run_id == None:
        print ('ModelError: Final Model Flag has not been set in config.py')
    else:
        trained_model_uri = 'runs:/'+run_id+'/model'
        result = mlflow.evaluate(
            trained_model_uri,
            holdout_data,
            targets="label",
            model_type="classifier",
            dataset_name="PotterVStarwars-1670",
            evaluators=["default"],
        )


if config.final_model:
    with open(config.root_dir + "src/feature_store/loggedmodel.txt", "r") as file:
        run_id = file.read().rstrip('\n')
        
    holdout_df = pd.read_csv(config.root_dir + 'src/feature_store/blind_holdout.csv')
    holdout_df['label'].replace(['Harry'], 0)
    holdout_df['label'].replace(['Starwars'], 1)

    evaluate_validation (run_id, holdout_df)
