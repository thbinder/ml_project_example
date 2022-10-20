from zenml.steps import BaseParameters, step


class DeploymentTriggerConfig(BaseParameters):
    """Deployment Trigger params"""

    seiling: float = 0.8


@step(enable_cache=False)
def deployment_trigger(config: DeploymentTriggerConfig, test_acc: float) -> bool:
    """Only deploy if the global test accuracy > seiling."""

    if test_acc > config.seiling:
        print("Accuracy threshold: {:.2f}".format(config.seiling))
        print("Model Accuracy on Test: {:.2f}".format(test_acc))
        print("Deployment accepted.")
    else:
        print("Accuracy threshold: {:.2f}".format(config.seiling))
        print("Model Accuracy on Test: {:.2f}".format(test_acc))
        print("Deployment declined.")

    return test_acc > config.seiling
