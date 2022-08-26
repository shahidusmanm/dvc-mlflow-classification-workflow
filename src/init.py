import mlflow, os
import config
from pathlib import Path

def set_tracking_server():
    if not os.path.exists(config.tracking_folder):
        os.makedirs(config.tracking_folder) 
        
    mlflow.set_tracking_uri(Path(config.tracking_folder).as_uri())

def init_experiment ():
    # Create an experiment name, which must be unique and case sensitive
    set_tracking_server()

    if mlflow.get_experiment_by_name(config.experiment_name) == None: 
        experiment_id = mlflow.create_experiment(
            config.experiment_name,
            tags={"version": "v1", "priority": "P1"},
        )
        experiment = mlflow.get_experiment(experiment_id)
        print("Name: {}".format(experiment.name))
        print("Experiment_id: {}".format(experiment.experiment_id))
        print("Artifact Location: {}".format(experiment.artifact_location))
        print("Tags: {}".format(experiment.tags))
        print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))

    mlflow.set_tracking_uri("")
    tracking_uri = mlflow.get_tracking_uri()
    print("Current tracking uri: {}".format(tracking_uri))

    return config.experiment_name


def start_experiment ():
    set_tracking_server()
    experiment = mlflow.set_experiment(config.experiment_name) 


if __name__ == "__main__":
    #Main execution
    init_experiment()
