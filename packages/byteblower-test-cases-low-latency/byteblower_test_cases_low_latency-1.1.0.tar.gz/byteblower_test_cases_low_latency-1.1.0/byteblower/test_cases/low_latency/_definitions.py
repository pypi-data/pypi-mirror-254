"""Shared type definitions and constants."""
from typing import Any, Dict  # for type hinting

# Type aliases
TestConfig = Dict[str, Any]
PortConfig = Dict[str, Any]

#: Default path to store the reports to:
#: ``None`` (== current directory)
DEFAULT_REPORT_PATH = None
#: Default prefix for the ByteBlower report file names.
DEFAULT_REPORT_PREFIX = 'byteblower'

DEFAULT_ENABLE_HTML = True
DEFAULT_ENABLE_JSON = True
DEFAULT_ENABLE_JUNIT_XML = True

LOGGING_PREFIX = 'Test Case: LLD: '

#: Default maximum average latency in milliseconds
#: used in the latency and frame loss related analysers.
DEFAULT_MAX_LATENCY_THRESHOLD: float = 5  # [ms]

# Maximum and Minimum bitrate defining the variation range for the
# dynamic FrameBlasting flow

MAX_BITRATE_THRESHOLD = 5e7
MIN_BITRATE_THRESHOLD = 5e6

# Scaling rate/interval for dynamic FrameBlasting flow

DEFAULT_SCALING_INTERVAL = 3
DEFAULT_SCALING_RATE = 5

MIN_PERCENTILE = 10
MAX_PERCENTILE = 90
