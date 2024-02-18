from __future__ import annotations

from kubernetes_utils.custom_object import CustomObject
from resemble.v1alpha1 import server_config_pb2


def get_server_config_unique_name(obj: ServerConfig) -> str:
    """Return a unique name for a ServerConfig object."""
    kubernetes_namespace = obj.metadata.namespace

    if kubernetes_namespace is not None and len(kubernetes_namespace) > 0:
        return f'{kubernetes_namespace}.{obj.spec.server_deployment_name}'

    return obj.spec.server_deployment_name


class ServerConfig(CustomObject[server_config_pb2.ServerConfig]):
    """
    This Python class wraps a generated proto object representing a k8s custom
    object. The CustomObject children knows how to talk to the k8s API to
    instantiate these objects in k8s.

    Class variables:
    group        [optional]: The k8s api group. Default: 'reboot.dev'.
    version      [optional]: The k8s api version name. Default: 'v1'.
    """

    Spec = server_config_pb2.ServerConfig.Spec
