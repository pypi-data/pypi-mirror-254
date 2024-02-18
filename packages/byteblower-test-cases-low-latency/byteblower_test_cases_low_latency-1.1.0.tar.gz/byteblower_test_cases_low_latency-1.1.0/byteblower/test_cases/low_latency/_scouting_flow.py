from time import sleep
from typing import Any, Mapping, Optional, Union  # for type hinting

from byteblower_test_framework.endpoint import (  # for type hinting
    Endpoint,
    Port,
)
from byteblower_test_framework.exceptions import log_api_error
from byteblower_test_framework.factory import create_frame
from byteblowerll.byteblower import Stream  # for type hinting

# Type aliases
FrameConfig = Mapping[str, Any]


class ScoutingFlow:  # pylint: disable=too-few-public-methods

    @staticmethod
    @log_api_error
    def run_udp_flow(
        source: Port,
        destination: Union[Port, Endpoint],
        frame_config: Optional[FrameConfig] = None,
    ) -> None:

        if isinstance(destination, Endpoint):
            destination.bb_endpoint.Lock(True)
        try:
            frame = create_frame(source, **(frame_config or {}))
            frame_content = frame.build_frame_content(source, destination)

            # Configure stream
            stream: Stream = source.bb_port.TxStreamAdd()
            stream.InterFrameGapSet(50 * 1000 * 1000)  # 50ms
            stream.NumberOfFramesSet(10)

            # Add frame to the stream
            frame.add(frame_content, stream)

            # Start resolution process
            stream.Start()

            sleep(0.5)

            # Stop stream (should have stopped by itself already)
            stream.Stop()
            # Remove the stream, no longer required
            source.bb_port.TxStreamRemove(stream)
        finally:
            if isinstance(destination, Endpoint):
                destination.bb_endpoint.Lock(False)
