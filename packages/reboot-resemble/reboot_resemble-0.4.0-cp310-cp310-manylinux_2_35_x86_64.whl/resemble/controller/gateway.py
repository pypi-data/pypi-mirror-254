from kubernetes_utils.custom_object import CustomObject
from resemble.v1alpha1.istio import gateway_pb2
# Re-export Istio's Gateway proto with the more-appropriate-for-us name
# of `GatewaySpec`. This represents that Istio's Gateway proto
# actually describes the `spec` field of the Gateway CRD.
from resemble.v1alpha1.istio.gateway_spec_pb2 import \
    Gateway as GatewaySpec  # noqa: F401


class Gateway(CustomObject[gateway_pb2.Gateway]):
    """
    This Python class wraps a generated proto object representing a k8s custom
    object. The CustomObject children know how to talk to the k8s API to
    instantiate these objects in k8s.

    Class variables:
    group        [optional]: The k8s api group. Default: 'reboot.dev'.
    version      [optional]: The k8s api version name. Default: 'v1'.
    """

    group = "networking.istio.io"
    version = "v1alpha3"  # Matching the Istio version we run.
