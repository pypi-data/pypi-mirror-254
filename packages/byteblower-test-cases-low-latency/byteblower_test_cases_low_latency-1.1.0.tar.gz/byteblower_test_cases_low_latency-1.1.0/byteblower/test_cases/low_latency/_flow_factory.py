"""Factory functions to create and initialize :class:`~Flow` instances."""
import logging
from itertools import count
from typing import Any, Dict, List, Optional, Tuple, Union  # for type hinting

from byteblower_test_framework.analysis import (
    FrameLossAnalyser,
    HttpAnalyser,
    LatencyCDFFrameLossAnalyser,
    LatencyFrameLossAnalyser,
    VoiceAnalyser,
)
from byteblower_test_framework.endpoint import (  # for type hinting
    Endpoint,
    Port,
)
from byteblower_test_framework.factory import create_frame
from byteblower_test_framework.report import Layer2Speed  # for type hinting
from byteblower_test_framework.traffic import Flow  # for type hinting
from byteblower_test_framework.traffic import (
    UDP_DYNAMIC_PORT_START,
    FrameBlastingFlow,
    GamingFlow,
    HTTPFlow,
    VideoFlow,
    VoiceFlow,
    string_array_to_int,
)

from ._definitions import (
    DEFAULT_MAX_LATENCY_THRESHOLD,
    DEFAULT_SCALING_INTERVAL,
    DEFAULT_SCALING_RATE,
    MAX_BITRATE_THRESHOLD,
    MIN_BITRATE_THRESHOLD,
)
from .dynamic_frameblastingflow import DynamicRateFrameBlastingFlow
from .exceptions import InvalidInput, MaximumUdpPortExceeded
from .l4s_analysers import L4SMarkingAnalyser
from .l4s_frameblastingflow import ECN_codepoint, L4SFrameBlastingFlow
from .outlier_latency_cdf_analyser import LatencyOutlierFrameLossAnalyser

__all__ = ('initialize_flows', )

FlowConfiguration = Dict[str, Any]


class FlowFactory():
    udp_dynamic_port = UDP_DYNAMIC_PORT_START
    _video_conf_number = count()

    @staticmethod
    def create_udp_flow(
        flow_config: FlowConfiguration,
        layer2_speed: Layer2Speed,
        source: Union[Port, Endpoint],
        destination: Union[Port, Endpoint],
        flow_tags: Optional[List[str]] = None,
    ) -> FrameBlastingFlow:
        # Parse arguments
        # NOTE - Create a copy before altering.
        #      * It is shared with other function (calls) !

        name = flow_config.pop("name", None)
        udp_src = flow_config.pop("udp_src", FlowFactory.udp_dynamic_port)
        udp_dest = flow_config.pop("udp_dest", FlowFactory.udp_dynamic_port)
        # Using default configuration if no frame_length given:
        frame_length = flow_config.pop("frame_size", None)

        udp_analysis = flow_config.pop("analysis", {})
        enable_latency = udp_analysis.pop('latency', False)
        enable_mos = udp_analysis.pop('mos', False)
        l4s_analysis = udp_analysis.pop('l4s', None)

        ip_ecn, ip_dscp = FlowFactory.ip_traffic_class_fields_getter(
            flow_config
        )

        if l4s_analysis is None:
            l4s_ecn = None
        elif l4s_analysis == 'marking':
            # NOTE: Also correct when ip_ecn == 0x00
            l4s_ecn = ip_ecn or ECN_codepoint.not_ect.value
        elif l4s_analysis == 'congestion':
            l4s_ecn = ECN_codepoint.ce.value
        else:
            raise InvalidInput(
                f"Flow {(name or '<unnamed flow>')!r}: L4S analysis must be"
                " either 'marking' or 'congestion'."
            )
        # Determine flow version and create frame
        frame = create_frame(
            source,
            length=frame_length,
            udp_src=udp_src,
            udp_dest=udp_dest,
            ip_ecn=ip_ecn,
            ip_dscp=ip_dscp,
            latency_tag=enable_latency or enable_mos
        )

        # Increment default UDP source port for each flow
        FlowFactory.advance_udp_port()

        # Configure frame blasting flow
        flow = FrameBlastingFlow(
            source, destination, name=name, frame_list=[frame], **flow_config
        )
        if flow_tags is not None:
            for tag in flow_tags:
                flow.add_tag(tag)

        logging.info(
            "Created flow %s from %s to %s", flow.name, source.name,
            destination.name
        )

        if l4s_ecn is not None:
            l4s_analyser = L4SMarkingAnalyser(ecn=l4s_ecn)
            flow.add_analyser(l4s_analyser)

        if enable_latency:
            flow.add_analyser(
                LatencyOutlierFrameLossAnalyser(
                    layer2_speed=layer2_speed, **udp_analysis
                )
            )
            # Remove parameters specific to "Outlier" frame loss analyser
            # (if exists)
            udp_analysis.pop('quantile', None)
            udp_analysis.pop('min_percentile', None)
            udp_analysis.pop('max_percentile', None)
            flow.add_analyser(
                LatencyFrameLossAnalyser(
                    layer2_speed=layer2_speed, **udp_analysis
                )
            )
            logging.info("Latency analyser created")
        elif enable_mos:
            flow.add_analyser(
                VoiceAnalyser(layer2_speed=layer2_speed, **udp_analysis)
            )
        else:
            flow.add_analyser(
                FrameLossAnalyser(layer2_speed=layer2_speed, **udp_analysis)
            )
            logging.info("Frame Loss analyser created")

        return flow

    @staticmethod
    def create_updating_udp_flow(
        flow_config: FlowConfiguration,
        layer2_speed: Layer2Speed,
        source: Port,
        destination: Port,
        flow_tags: Optional[List[str]] = None,
    ) -> FrameBlastingFlow:
        # Parse arguments
        # NOTE - Create a copy before altering.
        #      * It is shared with other function (calls) !

        name = flow_config.pop("name", None)
        udp_src = flow_config.pop("udp_src", FlowFactory.udp_dynamic_port)
        udp_dest = flow_config.pop("udp_dest", FlowFactory.udp_dynamic_port)
        # Using default configuration if no frame_length given:
        frame_length = flow_config.pop("frame_size", None)

        udp_analysis: dict = flow_config.pop("analysis", {})
        enable_latency = udp_analysis.pop('latency', False)

        max_bitrate = flow_config.pop('max_bitrate', MAX_BITRATE_THRESHOLD)
        min_bitrate = flow_config.pop('min_bitrate', MIN_BITRATE_THRESHOLD)
        scaling_interval = flow_config.pop(
            'scaling_interval', DEFAULT_SCALING_INTERVAL
        )
        scaling_rate = flow_config.pop('scaling_rate', DEFAULT_SCALING_RATE)

        ip_ecn, ip_dscp = FlowFactory.ip_traffic_class_fields_getter(
            flow_config
        )

        # Determine flow version and create frame
        frame = create_frame(
            source,
            length=frame_length,
            udp_src=udp_src,
            udp_dest=udp_dest,
            ip_ecn=ip_ecn,
            ip_dscp=ip_dscp,
            latency_tag=enable_latency
        )

        # Increment default UDP source port for each flow
        FlowFactory.advance_udp_port()

        # Configure frame blasting flow
        flow = DynamicRateFrameBlastingFlow(
            source,
            destination,
            name=name,
            frame_list=[frame],
            min_bitrate=min_bitrate,
            max_bitrate=max_bitrate,
            scaling_interval=scaling_interval,
            scaling_rate=scaling_rate,
            **flow_config,
        )
        if flow_tags is not None:
            for tag in flow_tags:
                flow.add_tag(tag)

        logging.info(
            "Created flow %s from %s to %s", flow.name, source.name,
            destination.name
        )

        if enable_latency:
            flow.add_analyser(
                LatencyOutlierFrameLossAnalyser(
                    layer2_speed=layer2_speed, **udp_analysis
                )
            )
            # Remove parameters specific to "Outlier" frame loss analyser
            # (if exists)
            udp_analysis.pop('quantile', None)
            udp_analysis.pop('min_percentile', None)
            udp_analysis.pop('max_percentile', None)
            flow.add_analyser(
                LatencyFrameLossAnalyser(
                    layer2_speed=layer2_speed, **udp_analysis
                )
            )
        else:
            flow.add_analyser(
                FrameLossAnalyser(layer2_speed=layer2_speed, **udp_analysis)
            )

        return flow

    @staticmethod
    def create_l4s_flow(
        flow_config: FlowConfiguration,
        layer2_speed: Layer2Speed,
        source: Port,
        destination: Port,
        flow_tags: Optional[List[str]] = None,
    ):
        name = flow_config.pop("name", None)

        # Check for analysis
        analysis = flow_config.pop("analysis", {})
        enable_latency = analysis.pop("latency", False)

        l4s_ecn, ip_dscp = FlowFactory.ip_traffic_class_fields_getter(
            flow_config, ecn_field_name="l4s_ecn"
        )

        if l4s_ecn == 'l4s':
            l4s_ecn = ECN_codepoint.l4s
        elif l4s_ecn == 'classic':
            l4s_ecn = ECN_codepoint.classic
        elif l4s_ecn == 'ce':
            # NOTE: Allowed to be able to "force" congestion-notified traffic
            l4s_ecn = ECN_codepoint.ce
        else:
            l4s_ecn = ECN_codepoint.not_ect

        # Retrieve UDP source and destination port number
        udp_src = flow_config.pop("udp_src", FlowFactory.udp_dynamic_port)
        udp_dest = flow_config.pop("udp_dest", FlowFactory.udp_dynamic_port)

        flow = L4SFrameBlastingFlow(
            source,
            destination,
            name=name,
            udp_src=udp_src,
            udp_dest=udp_dest,
            ip_dscp=ip_dscp,
            l4s_ecn=l4s_ecn,
            enable_latency=enable_latency,
            **flow_config,
        )

        # Increment default UDP source port for each flow
        FlowFactory.advance_udp_port()

        if flow_tags is not None:
            for tag in flow_tags:
                flow.add_tag(tag)

        logging.info(
            "Created flow %s from %s to %s", flow.name, source.name,
            destination.name
        )

        if enable_latency:
            flow.add_analyser(
                LatencyOutlierFrameLossAnalyser(
                    layer2_speed=layer2_speed, **analysis
                )
            )
            # Remove parameters specific to "Outlier" frame loss analyser
            # (if exists)
            analysis.pop('quantile', None)
            analysis.pop('min_percentile', None)
            analysis.pop('max_percentile', None)
            flow.add_analyser(
                LatencyFrameLossAnalyser(
                    layer2_speed=layer2_speed, **analysis
                )
            )
        else:
            flow.add_analyser(
                FrameLossAnalyser(layer2_speed=layer2_speed, **analysis)
            )

        return flow

    @staticmethod
    def create_conference_flows(
        conference_flow_config: FlowConfiguration,
        layer2_speed,
        source: Union[Port, Endpoint],
        destination: Union[Port, Endpoint],
        flow_tags: Optional[List[str]] = None,
    ) -> List[Flow]:
        # Get Flow classification parameters
        conference_flow_config = conference_flow_config.copy()
        # DEBUG:
        # logging.info('%sConference info %r', _LOGGING_PREFIX,
        #              conference_flow_config)
        flow_number = next(FlowFactory._video_conf_number)
        name = conference_flow_config.pop(
            "name", f"Video Conference {flow_number}"
        )
        conference_video_flow_config = conference_flow_config.pop(
            "video", None
        )
        conference_voice_flow_config = conference_flow_config.pop(
            "voice", None
        )
        conference_screenshare_flow_config = conference_flow_config.pop(
            "screenshare", None
        )

        # DEBUG:
        #
        # logging.info('%sVideo info %r', _LOGGING_PREFIX,
        #              conference_video_flow_config)
        # logging.info('%sAudio info %r', _LOGGING_PREFIX,
        #              conference_voice_flow_config)
        # logging.info('%sScreenshare info %r', _LOGGING_PREFIX,
        #              conference_screenshare_flow_config)

        conference_flows = []

        for flow_config, flow_name_suffix in \
                (conference_video_flow_config, f'{name}: Video'), \
                (conference_voice_flow_config, f'{name}: Audio'), \
                (conference_screenshare_flow_config, f'{name}: Screenshare'):

            if flow_config is None:
                continue
            # Build actual FrameBlastingFlow configuration
            udp_flow_config = conference_flow_config.copy()
            udp_flow_config["name"] = flow_name_suffix
            udp_flow_config.update(flow_config)
            flow = FlowFactory.create_udp_flow(
                udp_flow_config,
                layer2_speed,
                source,
                destination,
                flow_tags,
            )
            conference_flows.append(flow)
        return conference_flows

    @staticmethod
    def create_http_flow(
        flow_config: FlowConfiguration,
        source: Union[Port, Endpoint],
        destination: Union[Port, Endpoint],
    ) -> HTTPFlow:
        """Create a HTTP (TCP) flow.

        :param flow_config: Configuration parameters for the flow
        :type flow_config: FlowConfiguration
        :param source: Transmitter of the data traffic
        :type source: Union[Port, Endpoint]
        :param destination: Receiver of the data traffic
        :type destination: Union[Port, Endpoint]
        :return: Newly created flow
        :rtype: HTTPFlow
        """
        name = flow_config.pop("name", None)
        duration = flow_config.pop("duration", None)

        ip_ecn, ip_dscp = FlowFactory.ip_traffic_class_fields_getter(
            flow_config
        )

        flow = HTTPFlow(
            source,
            destination,
            name=name,
            request_duration=duration,
            ip_dscp=ip_dscp,
            ip_ecn=ip_ecn,
            **flow_config
        )

        logging.info(
            "Created flow %s from %s to %s", flow.name, source.name,
            destination.name
        )

        flow.add_analyser(HttpAnalyser())
        return flow

    @staticmethod
    def create_voice_flow(
        flow_config: FlowConfiguration,
        layer2_speed: Layer2Speed,
        source: Union[Port, Endpoint],
        destination: Union[Port, Endpoint],
    ) -> VoiceFlow:
        """Create a voice flow.

        :param flow_config: Configuration parameters for the flow
        :type flow_config: FlowConfiguration
        :param layer2_speed: Configuration setting to select the layer 2
           speed reporting, defaults to :attr:`~.options.Layer2Speed.frame`
        :type layer2_speed: ~options.Layer2Speed
        :param source: Transmitter of the data traffic
        :type source: Union[Port, Endpoint]
        :param destination: Receiver of the data traffic
        :type destination: Union[Port, Endpoint]
        :return: Newly created flow
        :rtype: VoiceFlow
        """
        name = flow_config.pop("name", None)
        udp_src = flow_config.pop("udp_src", FlowFactory.udp_dynamic_port)
        udp_dest = flow_config.pop("udp_dest", FlowFactory.udp_dynamic_port)

        analysis = flow_config.pop("analysis", {})
        enable_mos = analysis.pop("mos", True)

        ip_ecn, ip_dscp = FlowFactory.ip_traffic_class_fields_getter(
            flow_config
        )
        flow = VoiceFlow(
            source,
            destination,
            name=name,
            ip_dscp=ip_dscp,
            ip_ecn=ip_ecn,
            udp_src=udp_src,
            udp_dest=udp_dest,
            **flow_config,
            enable_latency=enable_mos
        )

        # Increment default UDP source port for each flow
        FlowFactory.advance_udp_port()

        logging.info(
            "Created flow %s from %s to %s", flow.name, source.name,
            destination.name
        )
        flow.add_analyser(VoiceAnalyser(layer2_speed=layer2_speed, **analysis))
        return flow

    @staticmethod
    def create_video_flow(
        flow_config: FlowConfiguration,
        source: Port,
        destination: Port,
    ) -> VideoFlow:
        """Create a video flow.

        :param flow_config: Configuration parameters for the flow
        :type flow_config: FlowConfiguration
        :param source: Transmitter of the data traffic
        :type source: Union[Port, Endpoint]
        :param destination: Receiver of the data traffic
        :type destination: Union[Port, Endpoint]
        :return: Newly created flow
        :rtype: VideoFlow
        """
        name = flow_config.pop("name", None)
        ip_ecn, ip_dscp = FlowFactory.ip_traffic_class_fields_getter(
            flow_config
        )
        flow = VideoFlow(
            source,
            destination,
            name=name,
            ip_dscp=ip_dscp,
            ip_ecn=ip_ecn,
            **flow_config
        )
        logging.info(
            "Created flow %s from %s to %s", flow.name, source.name,
            destination.name
        )
        return flow

    @staticmethod
    def create_gaming_flow(
        flow_config: FlowConfiguration,
        layer2_speed: Layer2Speed,
        source: Union[Port, Endpoint],
        destination: Union[Port, Endpoint],
    ) -> GamingFlow:
        """Create a gaming flow.

        :param flow_config: Configuration parameters for the flow
        :type flow_config: FlowConfiguration
        :param layer2_speed: Configuration setting to select the layer 2
           speed reporting, defaults to :attr:`~.options.Layer2Speed.frame`
        :type layer2_speed: ~options.Layer2Speed
        :param source: Transmitter of the data traffic
        :type source: Union[Port, Endpoint]
        :param destination: Receiver of the data traffic
        :type destination: Union[Port, Endpoint]
        :return: Newly created flow
        :rtype: GamingFlow
        """
        name = flow_config.pop("name", None)
        udp_src = flow_config.pop("udp_src", FlowFactory.udp_dynamic_port)
        udp_dest = flow_config.pop("udp_dest", FlowFactory.udp_dynamic_port)

        ip_ecn, ip_dscp = FlowFactory.ip_traffic_class_fields_getter(
            flow_config
        )

        gaming_analysis = flow_config.pop("analysis", {})
        enable_latency = gaming_analysis.pop('latency', False)
        max_threshold_latency = gaming_analysis.pop(
            'max_threshold_latency', DEFAULT_MAX_LATENCY_THRESHOLD
        )

        flow = GamingFlow(
            source,
            destination,
            name=name,
            ip_dscp=ip_dscp,
            ip_ecn=ip_ecn,
            udp_src=udp_src,
            udp_dest=udp_dest,
            max_threshold_latency=max_threshold_latency,
            **flow_config
        )

        # Increment default UDP source port for each flow
        FlowFactory.advance_udp_port()

        logging.info(
            "Created flow %s from %s to %s", flow.name, source.name,
            destination.name
        )

        if enable_latency:
            flow.add_analyser(
                LatencyFrameLossAnalyser(
                    layer2_speed=layer2_speed, **gaming_analysis
                )
            )
            flow.add_analyser(
                LatencyCDFFrameLossAnalyser(
                    layer2_speed=layer2_speed, **gaming_analysis
                )
            )
            logging.info("Flow %r: Latency analyser created", flow.name)
        else:
            flow.add_analyser(
                FrameLossAnalyser(
                    layer2_speed=layer2_speed, **gaming_analysis
                )
            )
            logging.info("Flow %r: Frame Loss analyser created", flow.name)

        return flow

    @staticmethod
    def ip_traffic_class_fields_getter(
        flow_config: FlowConfiguration,
        ecn_field_name: str = "ecn"
    ) -> Tuple[Optional[int], Optional[int]]:
        flow_name = flow_config.get('name', '<unnamed flow>')
        # Retrieve traffic class:
        ip_traffic_class = flow_config.pop("ip_traffic_class", None)
        if ip_traffic_class is not None:
            raise InvalidInput(
                f'Flow {flow_name!r}: Please define DSCP/ECN'
                'instead of IP TrafficClass'
            )
        # Retrieve ECN:
        ecn = flow_config.pop(ecn_field_name, None)
        if ecn is not None and ecn not in {'l4s', 'classic', 'ce', 'not_ect'}:
            ecn = string_array_to_int(ecn)
        # Retrieve DSCP:
        dscp = flow_config.pop("dscp", None)
        if dscp is not None:
            dscp = string_array_to_int(dscp)
        return ecn, dscp

    @classmethod
    def advance_udp_port(cls) -> None:
        if cls.udp_dynamic_port < 65535:
            cls.udp_dynamic_port += 1
        else:
            raise MaximumUdpPortExceeded('Exceeded Max. UDP port Number')


def initialize_flows(
    flow_config: FlowConfiguration,
    layer2_speed: Layer2Speed,
    source: Port,
    destination: Port,
    flow_tags: Optional[List[str]] = None,
) -> List[Flow]:
    flow_type = flow_config.pop("type")

    flows = []

    if flow_type.lower() == "frame_blasting":
        # UDP (Frame Blasting) flows
        flow = FlowFactory.create_udp_flow(
            flow_config, layer2_speed, source, destination, flow_tags
        )
        flows.append(flow)
    elif flow_type.lower() == "dynamic_frame_blasting":
        # UDP dynamic (Frame Blasting) flows
        flow = FlowFactory.create_updating_udp_flow(
            flow_config, layer2_speed, source, destination, flow_tags
        )
        flows.append(flow)

    elif flow_type.lower() == "l4s_frame_blasting":
        # UDP (L4S Frame Blasting) flows
        flow = FlowFactory.create_l4s_flow(
            flow_config, layer2_speed, source, destination, flow_tags
        )
        flows.append(flow)
    elif flow_type.lower() == "conference":
        # UDP (Conference) flows
        flows = FlowFactory.create_conference_flows(
            flow_config, layer2_speed, source, destination, flow_tags
        )

    elif flow_type.lower() == "http":
        # TCP (HTTP) flow
        flow = FlowFactory.create_http_flow(flow_config, source, destination)
        flows.append(flow)
    elif flow_type.lower() == "voice":
        # UDP (Voice) flow
        flow = FlowFactory.create_voice_flow(
            flow_config, layer2_speed, source, destination
        )
        flows.append(flow)
    elif flow_type.lower() == "video":
        # TCP (Video) flow
        flow = FlowFactory.create_video_flow(flow_config, source, destination)
        flows.append(flow)
    elif flow_type.lower() == "gaming":
        # UDP (Gaming) flow
        flow = FlowFactory.create_gaming_flow(
            flow_config, layer2_speed, source, destination
        )
        flows.append(flow)
    else:
        raise InvalidInput(f'Unsupported Flow type: {flow_type!r}')
    return flows
