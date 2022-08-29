import mlflow
from mlflow.sagemaker import SageMakerDeploymentClient
import config


def deploy_sagemaker():

    if config.final_model:
        vpc_config = {
            'SecurityGroupIds': [
                'sg-123456abc',
            ],
            'Subnets': [
                'subnet-123456abc',
            ]
        }
        config=dict(
            assume_role_arn=config.assume_role_arn,
            execution_role_arn=config.execution_role_arn,
            bucket_name=config.bucket_name,
            image_url=config.image_url,
            region_name=config.region_name,
            mode="create",
            archive=False,
            instance_type=config.instance_type,
            instance_count=config.instance_count,
            synchronous=config.synchronous,
            timeout_seconds=config.timeout_seconds,
            vpc_config=vpc_config
        )
        client = SageMakerDeploymentClient("sagemaker")
        client.create_deployment(
            "my-deployment",
            model_uri="/src/feature_store/loggedmodel.txt",
            flavor="python_function",
            config=config
        )
    else:
        print ("Model was not deployed because the fianl model flag is set to False")


def deploy_custom():
    
    if config.final_model:
        #Custom deployment code
        deploy123 = 5
    else:
        print ("Model was not deployed because the fianl model flag is set to False")


if __name__ == "__main__":
    if config.deployment_type == 'aws':
        deploy_sagemaker()

    elif config.deployment_type == 'custom':
        deploy_custom()
    
    else:
        print ('Error: This deployment platform is not supported.')

