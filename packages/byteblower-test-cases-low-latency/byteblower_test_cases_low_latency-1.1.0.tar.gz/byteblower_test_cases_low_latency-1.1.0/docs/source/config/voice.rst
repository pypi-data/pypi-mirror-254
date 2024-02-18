**********
Voice Flow
**********

Only one type of analysers is available currently for the voice flow.
This analyser calculates the Mean Opinion Score (MOS) which indicates the
quality of the voice flow.


.. code-block:: json

   {
      "type":  "voice",
      "name":  "<flow_name:str>",
      "source": {
            "port_group": [
               "<source_group:str>"
            ]
      },
      "destination": {
            "port_group": [
               "<destination_group:str>"
            ]
      },
      "ecn": "<ecn_code_point:str|int>",
      "dscp": "<dscp_code_point:str|int>",
      "udp_src": "<udp_source_port:int>",
      "udp_dest": "<udp_destination_port:int>",
      "add_reverse_direction": "<add_reverse_direction_flow:bool>",
      "initial_time_to_wait": "<initial_time_to_wait:float|int|timedelta>",
      "duration": "<flow_duration:float|int|timedelta>",
      "packetization": "<packetization_time:int>",
      "number_of_frames": "<number_of_frames:int>",
      "analysis": {
         "mos": "<enable_mos:bool>"
      }
   }

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/voice_flow
   :auto_reference:
   :auto_target:
   :lift_title: False

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/mos
   :auto_target:
   :auto_reference:
   :lift_title: False
