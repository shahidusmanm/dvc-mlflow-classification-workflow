import mlflow
import config

def deploy_azureml():

    if config.final_model:
        deploy = 123
    else:
        print ("Model was not deployed because the fianl model flag is set to False")


def deploy_sagemaker():

    if config.final_model:
        deploy = 123
    else:
        print ("Model was not deployed because the fianl model flag is set to False")


def deploy_custom():
    
    if config.final_model:
        deploy = 123
    else:
        print ("Model was not deployed because the fianl model flag is set to False")


