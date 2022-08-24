import mlflow
import config
from pathlib import Path

def init_experiment ():
    # Create an experiment name, which must be unique and case sensitive
    if mlflow.get_experiment_by_name(config.experiment_name) == None: 
        experiment_id = mlflow.create_experiment(
            "Workflow Experiment ",
            artifact_location=Path.cwd().joinpath("mlruns").as_uri(),
            tags={"version": "v1", "priority": "P1"},
        )
        experiment = mlflow.get_experiment(experiment_id)
        print("Name: {}".format(experiment.name))
        print("Experiment_id: {}".format(experiment.experiment_id))
        print("Artifact Location: {}".format(experiment.artifact_location))
        print("Tags: {}".format(experiment.tags))
        print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))

    experiment = mlflow.set_experiment(config.experiment_name)

    return config.experiment_name

#Main execution
init_experiment()
