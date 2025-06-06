import os

MULTIPLAYER_OTEL_DEFAULT_TRACES_EXPORTER_HTTP_URL = 'https://api.multiplayer.app/v1/traces'

MULTIPLAYER_OTEL_DEFAULT_LOGS_EXPORTER_HTTP_URL = 'https://api.multiplayer.app/v1/logs'

MULTIPLAYER_OTEL_DEFAULT_TRACES_EXPORTER_GRPC_URL = 'https://api.multiplayer.app:4317/v1/traces'

MULTIPLAYER_OTEL_DEFAULT_LOGS_EXPORTER_GRPC_URL = 'https://api.multiplayer.app:4317/v1/logs'

MULTIPLAYER_TRACE_DOC_PREFIX = 'd0cd0c'

MULTIPLAYER_TRACE_DEBUG_PREFIX = 'debdeb'

MULTIPLAYER_OTLP_KEY = os.environ.get("MULTIPLAYER_OTLP_KEY")
