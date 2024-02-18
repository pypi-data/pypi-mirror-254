"""Main test execution with given test configuration (from JSON file)."""
import copy
import logging
from collections import abc, defaultdict
from datetime import timedelta
from typing import (  # for type hinting
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    Union,
)

from byteblower_test_framework._traffic.frameblastingflow import (
    FrameBlastingFlow,
)
from byteblower_test_framework.endpoint import NatDiscoveryIPv4Port, Port
from byteblower_test_framework.exceptions import log_api_error
from byteblower_test_framework.host import MeetingPoint, Server
from byteblower_test_framework.report import (
    ByteBlowerHtmlReport,
    ByteBlowerJsonReport,
    ByteBlowerUnitTestReport,
    Layer2Speed,
)
from byteblower_test_framework.run import Scenario

from ._definitions import (
    DEFAULT_ENABLE_HTML,
    DEFAULT_ENABLE_JSON,
    DEFAULT_ENABLE_JUNIT_XML,
    DEFAULT_REPORT_PATH,
    DEFAULT_REPORT_PREFIX,
)
from ._definitions import LOGGING_PREFIX as _LOGGING_PREFIX
from ._definitions import TestConfig
from ._endpoint_factory import initialize_endpoint
from ._flow_factory import FlowFactory, initialize_flows
from ._port_factory import initialize_port
from ._scouting_flow import FrameConfig, ScoutingFlow
from .csvaggregator import CsvAggregator  # TODO: not used (for now ?)
from .exceptions import InvalidInput, MaximumUdpPortExceeded

if TYPE_CHECKING:
    # for type hinting
    from byteblower_test_framework.endpoint import Endpoint

    from ._definitions import PortConfig

__all__ = ('run', )

# Type aliases
_FlowConfiguration = Dict[str, Any]
_FlowConfigurationList = Sequence[_FlowConfiguration]

# Either single port configuration or list of port configurations:
_PortConfigCollection = Union[Sequence['PortConfig'], 'PortConfig']
_PortGroupList = Sequence[str]
_PortList = Sequence['Port']
_PortGroupMap = Mapping[str, _PortList]
_PortPairSet = Set[Tuple['Port', 'Port']]

#: Default maximum run time of a test scenario
#: in seconds. Set to `None` for the end of the last flow.
# DEFAULT_MAXIMUM_RUN_TIME: float = 30.0
DEFAULT_MAXIMUM_RUN_TIME: Optional[float] = None
#: Default reported Layer 2 speed:
#: Ethernet frame size without FCS
DEFAULT_LAYER2_SPEED = Layer2Speed.frame


def run(
    test_config: TestConfig,
    report_path: Optional[str] = DEFAULT_REPORT_PATH,
    report_prefix: str = DEFAULT_REPORT_PREFIX
) -> None:
    """Run a ByteBlower test.

    Using the configuration provided in the ``test_config``
    (for example loaded from JSON file)

    :param test_config: Dictionary of all configuration parameters
       for ByteBlower test
    :type test_config: TestConfig
    :param report_path: Path to the report directory,
       defaults to :const:`DEFAULT_REPORT_PATH`
    :type report_path: Optional[str], optional
    :param report_prefix: Prefix of the resulting reports,
       defaults to :const:`DEFAULT_REPORT_PREFIX`
    :type report_prefix: str, optional
    """
    # Parse the test configuration

    # - ByteBlower server parameters
    server_name = test_config['server']

    # - ByteBlower port parameters
    port_configs = test_config['ports']

    # - Meeting Point parameters
    meeting_point_name = test_config.get('meeting_point')

    # - Flow configuration parameters
    flow_configurations = test_config['flows']

    # - Scenario parameters
    enable_scouting_flows = test_config.get('enable_scouting_flows', False)
    maximum_run_time: Optional[float] = test_config.get('maximum_run_time')
    if maximum_run_time is None:
        maximum_run_time = DEFAULT_MAXIMUM_RUN_TIME

    # - Reporting parameters
    layer2_speed = test_config.get('layer2_speed')

    report_config = test_config.get('report', {})
    html_report = report_config.get('html', DEFAULT_ENABLE_HTML)
    json_report = report_config.get('json', DEFAULT_ENABLE_JSON)
    junit_xml_report = report_config.get('junit_xml', DEFAULT_ENABLE_JUNIT_XML)

    # Make Flow and Scenario configurations usable
    # for the ByteBlower Test Framework.
    if layer2_speed is not None:
        layer2_speed = Layer2Speed(layer2_speed)
    else:
        layer2_speed = DEFAULT_LAYER2_SPEED

    # Connect to the ByteBlower server
    server = Server(server_name)

    # Connect to the Meeting Point if provided
    meeting_point = MeetingPoint(
        meeting_point_name
    ) if meeting_point_name else None

    # Initialize ports
    port_group_map = _initialize_ports(server, meeting_point, port_configs)

    # create and run scouting flows
    if enable_scouting_flows:
        for flow in flow_configurations:
            _run_scouting_flows(flow, port_group_map)

    # Create new test scenario
    scenario = Scenario()

    if html_report:
        # Generate a HTML report
        byteblower_html_report = ByteBlowerHtmlReport(
            output_dir=report_path,
            filename_prefix=report_prefix,
            layer2_speed=layer2_speed
        )
        scenario.add_report(byteblower_html_report)

    if junit_xml_report:
        # Generate a JUnit XML report
        byteblower_unittest_report = ByteBlowerUnitTestReport(
            output_dir=report_path, filename_prefix=report_prefix
        )
        scenario.add_report(byteblower_unittest_report)

    if json_report:
        # Generate a JSON summary report
        byteblower_summary_report = ByteBlowerJsonReport(
            output_dir=report_path, filename_prefix=report_prefix
        )
        scenario.add_report(byteblower_summary_report)

    # create flows and add flows to scenario
    _initialize_flows(
        scenario, flow_configurations, layer2_speed, port_group_map
    )

    # Run the scenario and build the report
    _run_scenario(
        scenario,
        timedelta(seconds=maximum_run_time)
        if maximum_run_time is not None else maximum_run_time,
    )


@log_api_error
def _run_scenario(
    scenario: Scenario, maximum_run_time: Optional[timedelta]
) -> None:
    logging.info('%sStarting', _LOGGING_PREFIX)
    scenario.run(maximum_run_time=maximum_run_time)
    logging.info('%sfinished', _LOGGING_PREFIX)
    scenario.report()


def _report_to_csv(scenario: Scenario):
    # Report to CSV
    # TODO: Not used (for now)
    csv_aggregator = CsvAggregator()
    for flow in scenario.flows:
        for analyser in flow.analysers:
            csv_aggregator.add_analyser(analyser)
    if csv_aggregator.can_render():
        csv_aggregator.store('l4s.csv')


@log_api_error
def _initialize_ports(
    server: Server, meeting_point: Optional[MeetingPoint],
    port_configs: _PortConfigCollection
) -> _PortGroupMap:
    """Initialize source and destination ports.

    .. note::
       The given ``port_configs`` will be altered.

    :param server: Server instance to create the ports on.
    :type server: Server
    :param meeting_point: MeetingPoint instance to create the endpoint on.
    :type meeting_point: Optional[MeetingPoint]
    :param port_configs: Configuration list for source and destination ports.
    :type port_configs: _PortConfigCollection
    :return: Mapping of *port group* to list of initialized ports.
    :rtype: _PortGroupMap
    """
    # Normalize to Port lists
    if isinstance(port_configs, abc.Sequence):
        port_configs_list = port_configs

    # Create the Ports and build Port
    port_group_map: _PortGroupMap = defaultdict(list)
    for port_config in port_configs_list:
        port_groups = port_config.pop('port_group', None)
        if 'interface' in port_config:
            port = initialize_port(server, port_config)
        elif 'uuid' in port_config:
            if meeting_point is not None:
                port = initialize_endpoint(meeting_point, port_config)
            else:
                raise InvalidInput(
                    "Please provide meeting point address"
                    " to initialize endpoint"
                )
        else:
            raise InvalidInput(
                "Please provide either Port or Endpoint configuration"
            )

        for grp in port_groups:
            port_group_map[grp].append(port)

    return port_group_map


def _run_scouting_flows(
    flow_configuration: _FlowConfigurationList,
    port_group_map: _PortGroupMap,
) -> None:
    logging.info("Run scouting flows")

    udp_dynamic_port = FlowFactory.udp_dynamic_port
    source_groups = flow_configuration.get("source")
    destination_groups = flow_configuration.get("destination")
    flow_type = flow_configuration.get("type")
    flow_name = flow_configuration.get("name", "<unnamed flow>")

    def get_udp_ports() -> Tuple[int, int]:
        nonlocal flow_configuration, udp_dynamic_port

        udp_src = flow_configuration.get("udp_src", udp_dynamic_port)
        udp_dest = flow_configuration.get("udp_dest", udp_dynamic_port)

        return udp_src, udp_dest

    # Increment default UDP source port for each flow
    def advance_udp_port():
        nonlocal udp_dynamic_port

        if udp_dynamic_port < 65535:
            udp_dynamic_port += 1
        else:
            raise MaximumUdpPortExceeded('Exceeded Max UDP port Number')

    # Don't run for TCP-based flows
    if flow_type in ('http', 'video'):
        return

    # TODO: Implement for conference flows (consists of three UDP flows)
    for src_group in source_groups['port_group']:
        for dest_group in destination_groups['port_group']:

            port_pairs = _create_port_pairs(
                port_group_map, src_group, dest_group
            )
            for _src_port, _dest_port in port_pairs:
                if isinstance(_src_port, Port):
                    udp_src, udp_dest = get_udp_ports()
                    # Always run an scouting flow in the same direction
                    frame_config = {
                        'udp_src': udp_src,
                        'udp_dest': udp_dest,
                    }
                    _run_frameblasting_scouting_flow(
                        _src_port, _dest_port, flow_name, frame_config
                    )
                    # If destination is behind a NAT/NAPT gateway,
                    # send also a reverse scouting flow.
                    # ScoutingFlow only supports `Port` objects,
                    # so we only run for endpoint implementations
                    # which are children of a `Port`.
                    if isinstance(_dest_port, NatDiscoveryIPv4Port):
                        frame_config = {
                            'udp_src': udp_dest,
                            'udp_dest': udp_src,
                        }
                        _run_frameblasting_scouting_flow(
                            _dest_port, _src_port, flow_name, frame_config
                        )

                advance_udp_port()


def _run_frameblasting_scouting_flow(
    src_port: Port,
    dest_port: Port,
    flow_name: str,
    frame_config: Optional[FrameConfig] = None
) -> None:
    logging.info(
        "Run scouting flow for %r (%r <> %r)", flow_name, src_port.name,
        dest_port.name
    )
    ScoutingFlow.run_udp_flow(src_port, dest_port, frame_config=frame_config)


@log_api_error
def _initialize_flows(
    scenario: Scenario,
    flow_configurations: _FlowConfigurationList,
    layer2_speed: Layer2Speed,
    port_group_map: _PortGroupMap,
) -> None:

    for flow_configuration in flow_configurations:
        flow_name = flow_configuration.get("name", "<unnamed flow>")
        flow_type = flow_configuration["type"]

        # Sanity checks
        if flow_type.lower() != "frame_blasting" and (
                "nat_keep_alive" in flow_configuration
                or "napt_keep_alive" in flow_configuration):
            raise InvalidInput(
                f"{flow_name}: NAT/NAPT keep-alive (nat_keep_alive) is only"
                " supported for frame blasting flows"
            )

        add_reverse_direction = flow_configuration.pop(
            "add_reverse_direction", False
        )
        reverse_flow_group = flow_configuration.pop("reverse_flow_group", [])

        # NOTE: Deprecated ``nat_keep_alive`` in v1.2.0,
        # TODO: Remove ``napt_keep_alive`` in v1.4.0
        nat_keep_alive = flow_configuration.pop("nat_keep_alive", None)
        napt_keep_alive = flow_configuration.pop("napt_keep_alive", None)
        if napt_keep_alive is not None:
            if nat_keep_alive is not None:
                raise InvalidInput(
                    f"{flow_name}: Prefer nat_keep_alive over napt_keep_alive."
                    " Do not specify both."
                )
            logging.warning(
                'Flow napt_keep_alive parameter is deprecated and will be removed'
                ' soon. Please provide nat_keep_alive instead.'
            )
            nat_keep_alive = napt_keep_alive
        elif nat_keep_alive is None:
            nat_keep_alive = False

        _initialize_port_flows(
            scenario,
            flow_configuration,
            layer2_speed,
            port_group_map,
            add_reverse_direction=add_reverse_direction,
            reverse_flow_group=reverse_flow_group,
            nat_keep_alive=nat_keep_alive
        )


def _initialize_port_flows(
    scenario: Scenario,
    flow_configuration: _FlowConfiguration,
    layer2_speed: Layer2Speed,
    port_group_map: _PortGroupMap,
    add_reverse_direction: bool = False,
    reverse_flow_group: List = None,
    nat_keep_alive: bool = False
) -> None:

    src_port_groups: _PortGroupList = (
        flow_configuration.pop("source")["port_group"]
    )
    dest_port_groups: _PortGroupList = (
        flow_configuration.pop("destination")["port_group"]
    )
    flow_group = flow_configuration.pop("flow_group", [])
    # Create all flows
    for src_group in src_port_groups:
        for dest_group in dest_port_groups:
            port_pairs = _create_port_pairs(
                port_group_map, src_group, dest_group
            )
            for source, destination in port_pairs:
                flow_config = copy.deepcopy(flow_configuration)
                flows = initialize_flows(
                    flow_config, layer2_speed, source, destination, flow_group
                )
                for flow in flows:
                    scenario.add_flow(flow)

                # If an endpoint is behind a NAT/NAPT gateway, send also a
                # flow at very low rate (1 frame every 5s) to keep
                # NAT entries alive
                # (if nat_keep_alive is True)
                if nat_keep_alive:
                    for flow in flows:
                        _add_nat_keep_alive_flows(scenario, flow, layer2_speed)

                # Check for reverse flow
                if add_reverse_direction:
                    flow_config = copy.deepcopy(flow_configuration)
                    reverse_flows = initialize_flows(
                        flow_config, layer2_speed, destination, source,
                        reverse_flow_group
                    )
                    for flow in reverse_flows:
                        scenario.add_flow(flow)


def _create_port_pairs(
    port_group_map, source_group, destination_group
) -> _PortPairSet:
    port_pairs: _PortPairSet = set()
    # create port pairs that have matching flow sets
    for src_port in port_group_map[source_group]:
        for dest_port in port_group_map[destination_group]:
            if src_port != dest_port:
                port_pairs.add((src_port, dest_port))

    return port_pairs


def _create_nat_keep_alive_flow(
    flow: FrameBlastingFlow, layer2_speed: Layer2Speed, source: 'Port',
    destination: 'Port'
):
    udp_destination = flow.frame_list[0].udp_src
    udp_source = flow.frame_list[0].udp_dest
    flow_config = {
        "name": f"{flow.name}:NAT/NAPT keep-alive",
        "type": "frame_blasting",
        "frame_size": 60,
        "frame_rate": 0.2,
        "udp_src": udp_source,
        "udp_dest": udp_destination,
    }
    keepalive_flow = initialize_flows(
        flow_config,
        layer2_speed,
        source,
        destination,
    )
    return keepalive_flow[0]


def _add_nat_keep_alive_flows(
    scenario: Scenario,
    flow: FrameBlastingFlow,
    layer2_speed: Layer2Speed,
):
    # Enable a flow to keep Network Address (and Port) Translation (NAPT)
    # entries alive.
    # The direction will be from the endpoint behind a NAT/NAPT gateway
    # to the port at the public side of the NAT/NAPT gateway.
    #
    # We always enable the NAT/NAPT keep alive when the user
    # asks for it, even when:
    # * the reverse flow is enabled and source
    #   and destination UDP ports are the same
    # * the source is the endpoint behind the NAT/NAPT gateway:
    #   An initial time to wait on the flow can still cause
    #   the NAPT entries at the gateway might still timeout
    #   before the traffic starts. This might cause the
    #   NAPT gateway to create a new (and maybe different!)
    #   NAPT entry, causing our traffic analysis to fail
    #   (with 100% loss).
    source = flow.source
    destination = flow.destination

    if destination.require_nat_discovery:
        keepalive_flow = _create_nat_keep_alive_flow(  # pylint: disable=arguments-out-of-order
            flow, layer2_speed, destination, source
        )
        scenario.add_flow(keepalive_flow)
    if source.require_nat_discovery:
        keepalive_flow = _create_nat_keep_alive_flow(
            flow, layer2_speed, source, destination
        )
        scenario.add_flow(keepalive_flow)
