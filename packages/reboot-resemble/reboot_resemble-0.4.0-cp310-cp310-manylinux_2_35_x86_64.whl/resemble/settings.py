# The settings below must match their equivalents, if applicable, in:
# * resemble/settings.h
# * <possibly other languages by the time you read this>

# gRPC max message size to transmit large actor state data.
MAX_SIDECAR_GRPC_MESSAGE_LENGTH_BYTES = 100 * 1024 * 1024

ENVOY_PROXY_IMAGE = 'envoyproxy/envoy:v1.24.0'

# The path to the directory where Resemble state is stored.
RESEMBLE_STATE_DIRECTORY = '/var/run/resemble/state'

# The names of environment variables that are only present when running in `rsm dev`.
ENVVAR_RSM_DEV = 'RSM_DEV'
ENVVAR_RSM_DEV_NAME = 'RSM_DEV_NAME'
ENVVAR_RSM_DOT_RSM_DEV_DIRECTORY = 'RSM_DOT_RSM_DEV_DIRECTORY'
ENVVAR_RSM_DEV_LOCAL_ENVOY = 'RSM_DEV_LOCAL_ENVOY'
ENVVAR_RSM_DEV_LOCAL_ENVOY_PORT = 'RSM_DEV_LOCAL_ENVOY_PORT'
ENVVAR_RSM_DEV_INSPECT_PORT = 'RSM_DEV_INSPECT_PORT'

# The name of an environment variable that's only present when running on
# Kubernetes.
ENVVAR_KUBERNETES_SERVICE_HOST = 'KUBERNETES_SERVICE_HOST'

# We need this to be able to accept trafic from the Docker
# container running Envoy. It is also useful to be able to accept
# the trafic from other test machines, for example mobile devices.
LOCALHOST_LISTEN_ADDRESS = '0.0.0.0'

# Ports that Resemble is, by default, reachable on for gRPC and HTTP traffic
# from clients running outside the Resemble cluster. These are the ports that
# users will use in their configuration/code when they choose how to connect to
# a Resemble cluster.
#
# Note that these are defaults; some environments may override these settings.
# Furthermore, many environments may only have one of these ports exposed.
#
# The insecure port serves unencrypted traffic. The secure port serves traffic
# that uses TLS.
DEFAULT_INSECURE_PORT = 9990
DEFAULT_SECURE_PORT = 9991
