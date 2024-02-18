from time import sleep
from typing import Any, Mapping, Optional, Sequence, Union  # for type hinting

from byteblower_test_framework.endpoint import Port  # for type hinting
from byteblower_test_framework.factory import create_frame
from byteblower_test_framework.traffic import UDP_DYNAMIC_PORT_START
from byteblowerll.byteblower import Stream  # for type hinting

from .exceptions import PortLayer3Mismatch

# Type aliases
_FrameConfig = Mapping[str, Any]
_ImixFrameConfig = Mapping[str, int]
_ImixFrameConfigCollection = Sequence[_ImixFrameConfig]
_ImixConfig = Mapping[str, Union[int, _ImixFrameConfigCollection]]


class ScoutingFlow:
    """Prepares the network for the actual traffic defined in the test."""

    @staticmethod
    def run_udp_flow(
        source: Port,
        destination: Port,
        frame_config: Optional[_FrameConfig] = None,
    ) -> None:
        if source.layer3.__class__ != destination.layer3.__class__:
            raise PortLayer3Mismatch()

        # Create frame
        frame = create_frame(source, **(frame_config or {}))
        frame_content = frame.build_frame_content(source, destination)

        # Configure stream
        stream: Stream = source.bb_port.TxStreamAdd()
        stream.InterFrameGapSet(100 * 1000 * 1000)  # 100ms
        stream.NumberOfFramesSet(10)

        # Add frame to the stream
        frame.add(frame_content, stream)

        # Start resolution process
        stream.Start()

        sleep(1)

        # Stop stream (should have stopped by itself already)
        stream.Stop()
        # Remove the stream, no longer required
        source.bb_port.TxStreamRemove(stream)

    @staticmethod
    def run_udp_imix(
        source: Port,
        destination: Port,
        imix_config: _ImixConfig,
    ) -> None:
        frame_config = {
            'udp_src': imix_config.get('udp_src', UDP_DYNAMIC_PORT_START),
            'udp_dest': imix_config.get('udp_dest', UDP_DYNAMIC_PORT_START),
        }
        ScoutingFlow.run_udp_flow(source,
                                  destination,
                                  frame_config=frame_config)
