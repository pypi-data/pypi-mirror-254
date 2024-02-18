from kubernetes_utils.custom_object import CustomObject
from resemble.v1alpha1.istio import virtual_service_pb2 as vs_pb2
# Re-export Istio's VirtualService proto with the more-appropriate-for-us name
# of `VirtualServiceSpec`. This represents that Istio's VirtualService proto
# actually describes the `spec` field of the VirtualService CRD.
from resemble.v1alpha1.istio.virtual_service_spec_pb2 import \
    VirtualService as VirtualServiceSpec  # noqa: F401


class VirtualService(CustomObject[vs_pb2.VirtualService]):
    """
    This Python class wraps a generated proto object representing a k8s custom
    object. The CustomObject children knows how to talk to the k8s API to
    instantiate these objects in k8s.

    Class variables:
    group        [optional]: The k8s api group. Default: 'reboot.dev'.
    version      [optional]: The k8s api version name. Default: 'v1'.
    """

    group = "networking.istio.io"
    version = "v1alpha3"  # Matching the Istio version we run.
