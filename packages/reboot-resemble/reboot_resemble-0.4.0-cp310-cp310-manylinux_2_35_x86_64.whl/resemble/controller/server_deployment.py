from kubernetes_utils.custom_object import CustomObject
from resemble.v1alpha1 import server_deployment_pb2


class ServerDeployment(CustomObject[server_deployment_pb2.ServerDeployment]):
    """
    This Python class wraps a generated proto object representing a k8s custom
    object. The CustomObject parents knows how to talk to the k8s API to
    instantiate these objects in k8s.

    Class variables:
    group        [optional]: The k8s api group. Default: 'reboot.dev'.
    version      [optional]: The k8s api version name. Default: 'v1'.
    """

    Spec = server_deployment_pb2.ServerDeployment.Spec
