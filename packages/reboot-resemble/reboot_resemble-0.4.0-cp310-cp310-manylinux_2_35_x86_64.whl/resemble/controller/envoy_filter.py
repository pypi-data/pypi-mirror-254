import google.protobuf
import kubernetes_asyncio
from envoy.extensions.filters.http.grpc_json_transcoder.v3 import (
    transcoder_pb2,
)
from google.protobuf import any_pb2, struct_pb2
from google.protobuf.json_format import MessageToDict
from kubernetes_utils.custom_object import CustomObject
from kubernetes_utils.resources.deployments import Deployments
from resemble.v1alpha1.istio import envoy_filter_pb2 as ef_pb2
from resemble.v1alpha1.istio.envoy_filter_spec_pb2 import \
    EnvoyFilter as EnvoyFilterSpec
from resemble.v1alpha1.istio.envoy_filter_spec_pb2 import WorkloadSelector
from typing import Optional


class EnvoyFilter(CustomObject[ef_pb2.EnvoyFilter]):
    """
    This Python class wraps a generated proto object representing a k8s custom
    object. The CustomObject children knows how to talk to the k8s API to
    instantiate these objects in k8s.

    Class variables:
    group        [optional]: The k8s api group. Default: 'reboot.dev'.
    version      [optional]: The k8s api version name. Default: 'v1'.
    """

    group = "networking.istio.io"
    version = "v1alpha3"

    def __init__(
        self,
        metadata: Optional[kubernetes_asyncio.client.V1ObjectMeta] = None,
        **kwargs,
    ):
        super().__init__(
            metadata=metadata,
            # Istio defines its fields in "camelCase", so we must convert our
            # "snake_case" proto field names to that shape.
            preserve_proto_field_names=False,
            **kwargs,
        )

    @staticmethod
    def build_json_transcoder(
        proto_descriptor_bin: bytes,
        service: list[str],
        app: str,
        name: str,
    ) -> google.protobuf.message.Message:
        """
        Istio exposes a complex proto for EnvoyFilter that must be built
        out of inner messages, enums and an Envoy proto object.
        """
        envoy_transcoder = transcoder_pb2.GrpcJsonTranscoder(
            proto_descriptor_bin=proto_descriptor_bin, services=service
        )
        envoy_transcoder_any = any_pb2.Any()
        envoy_transcoder_any.Pack(envoy_transcoder)

        patch_value_struct = struct_pb2.Struct()
        patch_value_struct.update(
            {'typed_config': MessageToDict(envoy_transcoder_any)}
        )

        return EnvoyFilter(
            metadata=kubernetes_asyncio.client.V1ObjectMeta(name=name),
            spec=EnvoyFilterSpec(
                config_patches=[
                    EnvoyFilterSpec.EnvoyConfigObjectPatch(
                        apply_to=EnvoyFilterSpec.ApplyTo.HTTP_FILTER,
                        match=EnvoyFilterSpec.EnvoyConfigObjectMatch(
                            context=EnvoyFilterSpec.PatchContext.
                            SIDECAR_INBOUND,
                            listener=EnvoyFilterSpec.ListenerMatch(
                                filter_chain=EnvoyFilterSpec.ListenerMatch.
                                FilterChainMatch(
                                    filter=EnvoyFilterSpec.ListenerMatch.
                                    FilterMatch(
                                        name=
                                        'envoy.filters.network.http_connection_manager',
                                        sub_filter=EnvoyFilterSpec.
                                        ListenerMatch.SubFilterMatch(
                                            name='envoy.filters.http.router'
                                        )
                                    )
                                ),
                                port_number=50051
                            )
                        ),
                        patch=EnvoyFilterSpec.Patch(
                            operation=EnvoyFilterSpec.Patch.Operation.
                            INSERT_BEFORE,
                            value=patch_value_struct
                        )
                    )
                ],
                workload_selector=WorkloadSelector(
                    labels={Deployments.DEPLOYMENT_NAME_LABEL: app}
                )
            )
        )
