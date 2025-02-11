multiplayer-opentelemetry
============================================================================
##  Introduction
The multiplayer-otlp-go module integrates OpenTelemetry with the Multiplayer platform to enable seamless trace collection and analysis. This exporter helps developers monitor, debug, and document application performance with detailed trace data. It supports flexible trace ID generation, sampling strategies.


## Installation

To install the `multiplayer-opentelemetry` module, use the following command:

```bash
pip install multiplayer-opentelemetry 
```

## Multiplayer Http Trace Exporter

```python
from multiplayer.opentelemetry.exporter.http.trace_exporter import MultiplayerOTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, SERVICE_VERSION, DEPLOYMENT_ENVIRONMENT, Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace import TracerProvider

resource = Resource(attributes={
    SERVICE_NAME: "<service-name>",
    SERVICE_VERSION: "<service-version>",
    DEPLOYMENT_ENVIRONMENT: "<environement-name>"
})

traceProvider = TracerProvider(
    resource = resource,
    sampler = sampler,
    id_generator = id_generator
)

processor = BatchSpanProcessor(MultiplayerOTLPSpanExporter(
    url: '<opentelemetry-collector-url>', # url is optional and can be omitted - default is https://api.multiplayer.app/v1/traces
    apiKey = "<multiplayer-otel-key>"
)) # apiKey is optional
traceProvider.add_span_processor(processor)
```

## Multiplayer Http Log Exporter

```python
from opentelemetry.sdk.resources import SERVICE_NAME, SERVICE_VERSION, DEPLOYMENT_ENVIRONMENT, Resource
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from multiplayer.opentelemetry.exporter.http.log_exporter import MultiplayerOTLPLogExporter

resource = Resource(attributes={
    SERVICE_NAME: "<service-name>",
    SERVICE_VERSION: "<service-version>",
    DEPLOYMENT_ENVIRONMENT: "<environement-name>"
})

traceProvider = TracerProvider(
    resource = resource,
)

logger_provider = LoggerProvider(
    resource = Resource.create(
        {
            "service.name": "<service-name>"
        }
    ),
)
set_logger_provider(logger_provider)
exporter = MultiplayerOTLPLogExporter(
    url: "<opentelemetry-collector-url>", # url is optional and can be omitted - default is https://api.multiplayer.app/v1/logs
    apiKey = "<multiplayer-otel-key>"
)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
handler = LoggingHandler(level=logging.NOTSET, logger_provider=logger_provider)
```

## Multiplayer Grpc Trace Exporter

```python
from multiplayer.opentelemetry.exporter.grpc.trace_exporter import MultiplayerOTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, SERVICE_VERSION, DEPLOYMENT_ENVIRONMENT, Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace import TracerProvider

resource = Resource(attributes={
    SERVICE_NAME: "<service-name>",
    SERVICE_VERSION: "<service-version>",
    DEPLOYMENT_ENVIRONMENT: "<environement-name>"
})

traceProvider = TracerProvider(
    resource = resource,
    sampler = sampler,
    id_generator = id_generator
)

processor = BatchSpanProcessor(MultiplayerOTLPSpanExporter(
    url: '<opentelemetry-collector-url>', # url is optional and can be omitted - default is https://api.multiplayer.app/v1/traces
    apiKey = "<multiplayer-otel-key>"
)) # apiKey is optional
traceProvider.add_span_processor(processor)
```

## Multiplayer Grpc Log Exporter

```python
from opentelemetry.sdk.resources import SERVICE_NAME, SERVICE_VERSION, DEPLOYMENT_ENVIRONMENT, Resource
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from multiplayer.opentelemetry.exporter.grpc.log_exporter import MultiplayerOTLPLogExporter

resource = Resource(attributes={
    SERVICE_NAME: "<service-name>",
    SERVICE_VERSION: "<service-version>",
    DEPLOYMENT_ENVIRONMENT: "<environement-name>"
})

traceProvider = TracerProvider(
    resource = resource,
)

logger_provider = LoggerProvider(
    resource = Resource.create(
        {
            "service.name": "<service_name>"
        }
    ),
)
set_logger_provider(logger_provider)
exporter = MultiplayerOTLPLogExporter(
    url: "<opentelemetry-collector-url>", # url is optional and can be omitted - default is https://api.multiplayer.app/v1/logs
    apiKey = "<multiplayer-otel-key>"
)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
handler = LoggingHandler(level=logging.NOTSET, logger_provider=logger_provider)
```


## Multiplayer trace Id generator

```python
from multiplayer.opentelemetry.trace.sampler import MultiplayerTraceIdRatioBasedSampler

sampler = MultiplayerTraceIdRatioBasedSampler(rate = 1/2)
```

## Multiplayer trace id ratio based sampler

```python
from multiplayer.opentelemetry.trace.id_generator import MultiplayerRandomIdGenerator

id_generator = MultiplayerRandomIdGenerator(autoDocTracesRatio = 1/1000)
```
