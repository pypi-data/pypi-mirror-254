************************
Test scenario definition
************************

In the current release, it is possible to supply a configuration file
in ``JSON`` format for running your tests.

In the following sections, we will provide a detailed explanation of the
structure and all parameters in the JSON configuration file.

Structure
=========

A quick short reference for the structure:

.. code-block:: json

   {
       "server": "<bb_server_name_or_ip:str>",
       "meeting_point": "<bb_meeting_point_name_or_ip:str>",
       "source": {
           "name": "<source_name:str>",
           "interface": "<bb_interface_name:str>",
           "uuid":"<endpoint_uuid:str>",
           "ipv4": "<ipv4_address:str>|dhcp|true",
           "netmask": "<ipv4_address:str>",
           "gateway": "<ipv4_address:str>",
           "nat": "<nat_resolution:bool>",
           "ipv6": "dhcp|slaac|true"
       },
       "destination": {
           "name": "<destination_name:str>",
           "interface": "<bb_interface_name:str>",
           "uuid":"<endpoint_uuid:str>",
           "ipv4": "<ipv4_address:str>|dhcp|true",
           "netmask": "<ipv4_address:str>",
           "gateway": "<ipv4_address:str>",
           "nat": "<nat_resolution:bool>",
           "ipv6": "dhcp|slaac|true"
       },
       "duration": "<trial_duration:int>",
       "max_iterations": "<max_iterations:int>",
       "frame_configs": [
           {
               "size": "<frame_length:int>",
               "initial_bitrate": "<initial_frame_rate:int>",
               "tolerated_frame_loss": "<frame_loss:float>",
               "accuracy": "<accuracy:float>",
               "expected_bitrate": "<expected_frame_rate:int>"
           }
       ]
   }

JSON schema
===========

The complete structure and documentation of the file is available
in `Configuration file JSON schema <json/config-schema.json>`_,
and documented below.

Server
------

.. jsonschema:: extra/test-cases/rfc-2544/json/config-schema.json#/$defs/server_address
   :auto_reference:
   :auto_target:
   :lift_title: False

Meeting point
-------------

.. jsonschema:: extra/test-cases/rfc-2544/json/config-schema.json#/$defs/meeting_point_address
   :auto_reference:
   :auto_target:
   :lift_title: False

Ports
-----

The ``"source"`` and ``"destination"`` blocks define ByteBlower ports
(simulated hosts) at a given ByteBlower interface. Where a ByteBlower
interface is the physical connection on either the *non-trunking interface*
(direct connection at a ByteBlower server) or a *trunking interface*
(connection at a physical port on the ByteBlower switch).

Each port supports IPv4 address assignment using static IPv4 configuration
or DHCP. IPv6 address configuration is possible through DHCPv6 or
Stateless autoconfiguration (SLAAC).

When an (IPv4) port is located behind a NAT gateway, then the test framework
will perform additional setup flow steps to resolve the NAT's public IPv4
address and UDP port (*when required*).

Since version 1.2.0, the Byteblower Test Framework also supports Byteblower
endpoints. They can be configured by:

#. Providing the *meeting point address* and the *UUID* of the endpoint.
#. Setting the IPv4 or IPv6 parameter to ``true``.

.. jsonschema:: extra/test-cases/rfc-2544/json/config-schema.json#/$defs/port
   :auto_reference:
   :auto_target:
   :lift_title: False

.. jsonschema:: extra/test-cases/rfc-2544/json/config-schema.json#/$defs/vlans
   :auto_reference:
   :auto_target:

Frame configurations
--------------------

This defines a list of frame configurations for each frame size. These
configurations are related to the RFC 2544 throughput test specifications.

As stated in the `RFC 2544 basic requirements <overview.html#rfc-2544-basic-requirements>`_,
at least five frame sizes **SHOULD** be tested for at least 60 seconds
per test trial. Also, frame size with the largest MTU supported by the protocol
under test SHOULD be used.

.. jsonschema:: extra/test-cases/rfc-2544/json/config-schema.json#/$defs/frame_configs
   :auto_reference:
   :auto_target:
   :lift_title: False

**Default frames configuration**

Frame configurations can be removed entirely from the configuration file.
In case no frame configuration is provided, default frame configurations
in the ``byteblower.test_case.rfc_2544.definitions`` module will be used.

.. code-block:: json

   [
       {
           "size": 60,
           "initial_bitrate": 3e8,
           "tolerated_frame_loss": 1e-3,
           "expected_bitrate": 3.7e8,
           "accuracy": 1e5
       },
       {
           "size": 124,
           "initial_bitrate": 6e8,
           "tolerated_frame_loss": 1e-3,
           "expected_bitrate": 4.5e8,
           "accuracy": 1e5
       },
       {
           "size": 252,
           "initial_bitrate": 8e8,
           "tolerated_frame_loss": 1e-3,
           "expected_bitrate": 5.7e8,
           "accuracy": 1e5
       },
       {
           "size": 508,
           "initial_bitrate": 8e8,
           "tolerated_frame_loss": 1e-3,
           "expected_bitrate": 6.6e8,
           "accuracy": 1e5
       },
       {
           "size": 1020,
           "initial_bitrate": 1e9,
           "tolerated_frame_loss": 1e-3,
           "expected_bitrate": 7.15e8,
           "accuracy": 1e5
       },
       {
           "size": 1276,
           "initial_bitrate": 1e9,
           "tolerated_frame_loss": 1e-3,
           "expected_bitrate": 7.25e8,
           "accuracy": 1e5
       },
       {
           "size": 1514,
           "initial_bitrate": 1e9,
           "tolerated_frame_loss": 1e-3,
           "expected_bitrate": 7.35e8,
           "accuracy": 1e5
       }
   ]

These values could be used as is. However, you preferably should change
these default values to comply to your network and test specifications.

Other parameters
----------------

.. jsonschema:: extra/test-cases/rfc-2544/json/config-schema.json#/$defs/maximum_run_time

.. jsonschema:: extra/test-cases/rfc-2544/json/config-schema.json#/$defs/max_iterations

Configuration file example
==========================

- Using `ByteBlower Ports <json/port/rfc_2544.json>`_

  .. literalinclude:: extra/test-cases/rfc-2544/json/port/rfc_2544.json
     :language: json

- Using `ByteBlower Endpoint <json/endpoint/rfc_2544.json>`_

  .. literalinclude:: extra/test-cases/rfc-2544/json/endpoint/rfc_2544.json
     :language: json
