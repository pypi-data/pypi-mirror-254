************************
Test scenario definition
************************

In the current release, it is possible to supply a configuration file
in ``JSON`` format for running your tests.

In the following sections, we will provide a detailed explanation of the
structure and all parameters in the JSON configuration file.

Structure
=========

The JSON configuration file consists of:

* ByteBlower server address (and optionally a ByteBlower meeting point)
* List of port definitions: Where you want to send traffic from/to
* List of flow definitions: We currently support a set of UDP frame blasting
  based flows (voice, video, conference, etc.) and stateful TCP (HTTP) flows.
* (*optional*) Reporting parameters
* Test-specific parameters: like types of reporting (HTML, JSON, and XML),
  the maximum runtime, including a new feature that allows to run scouting
  flows to initialize the test network entries (like ARP) before running the
  actual test.

A quick short reference for the structure:

.. code-block:: json

   {
       "server": "<bb_server_name_or_ip:str>",
       "meeting_point": "<bb_meeting_point_name_or_ip:str>",
       "ports": [
           {
               "name": "<port_name:str>",
               "interface": "<bb_interface_name:str>",
               "uuid": "<endpoint_uuid:str>",
               "ipv4": "<ipv4_address:str>|dhcp|true",
               "netmask": "<ipv4_netmask:str>",
               "gateway": "<ipv4_gateway:str>",
               "nat": "<enable_nat_resolution:bool>",
               "ipv6": "dhcp|slaac|true",
               "port_group": [
                   "<port_group:str>"
               ]
           }
       ],
       "flows": [],
       "report": {
           "html": "<enable_html_reporting:bool>",
           "json": "<enable_json_reporting:bool>",
           "junit_xml": "<enable_junit_xml_reporting:bool>"
       },
       "enable_scouting_flows": "<enable_scouting_flows:bool>",
       "maximum_run_time": "<scenario_max_run_time:float>"
   }

Where ``flows`` contains the list of flows.

JSON schema
===========

The complete structure and documentation of the file is available
in `Configuration file JSON schema <../json/config-schema.json>`_,
and documented below.

Server
------

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/server_address
   :auto_reference:
   :auto_target:
   :lift_title: False

Meeting point
-------------

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/meeting_point_address
   :auto_reference:
   :auto_target:
   :lift_title: False

Ports list
----------

The port list defines a set of ByteBlower ports (== simulated hosts) at a given
ByteBlower interface. Where a ByteBlower interface is the physical connection
on either the *non-trunking interface* (direct connection at a ByteBlower
server) or a *trunking* interface (connection at a physical port on the
ByteBlower switch).

These ports define ByteBlower ports which simulate hosts at the operator side
or at the customer side of the network under test (typically simulating a
device behind a NAT gateway).

It is allowed to specify multiple virtual ByteBlower ports on a single
physical ByteBlower interface. Each port supports IPv4 address assignment
using static IPv4 configuration or DHCP. IPv6 address configuration is possible
through DHCPv6 or stateless autoconfiguration (SLAAC).

When an (IPv4) port is located behind a NAT gateway, then the test framework
will perform additional setup flow steps to resolve the NAT's public IPv4
address and UDP port (*when required*).

Since version 1.2.0, the Byteblower Test Framework also supports Byteblower
endpoints. They can be configured by:

#. Providing the *meeting point address* and the *UUID* of the endpoint.
#. Setting the IPv4 or IPv6 parameter to ``true``.

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/port_list
   :auto_reference:
   :auto_target:
   :lift_title: False

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/port
   :auto_reference:
   :auto_target:

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/vlans
   :auto_reference:
   :auto_target:

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/port_group
   :auto_reference:
   :auto_target:

Flow list
---------

Current release supports a set of UDP-based flows and HTTP (stateful TCP) flow.
Each type of traffic you like to send using ByteBlower is initiated using
a flow definition in the flow list.

At least one flow definition must be defined. Default values will apply
on other parameters. Each flow definition entry must contain at least the
*type*, one *source* port group, and one port group *destination* ports.
A ByteBlower port can belong to one or many port groups.

A flow is created on the matrix of all source/destination flow's ports
combinations. It is only generated between ports of the same layer 3
address family (IPv4 or IPv6).

When reverse flow is enabled, the same flow definition is used
in both directions.

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/flow_list
   :auto_reference:
   :auto_target:
   :lift_title: False

.. toctree::
   :maxdepth: 1
   :caption: Flow type specific configuration

   frame_blasting
   dynamic_frame_blasting
   l4s_frame_blasting
   voice
   video
   gaming
   conference
   http

Test scenario parameters
------------------------

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/maximum_run_time
   :auto_reference:
   :auto_target:

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/enable_scouting_flows
   :auto_reference:
   :auto_target:

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/reporting_parameters
   :auto_reference:
   :auto_target:
