# DVC & MLFlow Classification Workflow

### Set up the environment

You can set up the environment through any of the following ways;

##### Through the exported YAML file

If you're using anaconda, you just need to import the provided `conda_env.yml` file. You can import it by running the following command:

```
$  conda env create -f conda_env.yml
```


#### Through the Python requirements file

If you don't have anaconda installed, you can import all the required python dependecies by running:

```
$  pip install -r requirements.txt
```


### Running workflow stages through the Jupyter Notebook

You can use the provided `ML Project Management with Git, DVC, and MLFlow.ipynb` to run individual pipeline stages. The global variables can be set in the `src/config.py` or by passing them as arguments through individual function calls.

**Note:** For training stages to work properly through the notebook, the `final_model` flag in the `config.py` file needs to be set to `False`. The flag indicates to the DVC pipeline that model exploration has been completed and that the pipeline run should result in a model that needs to be registered and published.


### Running workflow stages through the shell

You can also run individual stages via the commandline. You should just execute which ever stage you want by running its respective `py` file. For example, you can train a model by running;

```
$  python src/train.py
```

All config paramaters including the model type and hyperparameters will be set through `config.py` in this case. A future release of this workflow will include passing these parameters as shell arguments.


### Running the pipeline via DVC

Once you're happy with the model, you can run the entire pipeline by running the following command in shell:

```
$  dvc repro
```

### Visualizing the Pipeline DAG

You can visualize the end-to-end pipeline configured by running

```
$  dvg dag
```

### View MLFlow Tracking UI

The main benefit of this workflow is the ability to track model artifacts and analyze them via an easy-to-use interface. These artifacts are recorded and tracked by MLFlow and can be analyzed by their Web UI. To run the UI server;

```
$  cd src
$  mlflow ui
```
**Note:** You must be in the `src` directory before you launch the UI because all the MLFlow data is stored in `src/mlruns`. Future releases of this workflow will have the functionality to store MLFlow artifacts to a custom location.