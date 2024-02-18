***********
Gaming Flow
***********

.. code-block:: json

   {
      "type":  "gaming",
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
      "add_reverse_direction": "<add_reverse_direction_flow:bool>",
      "packet_length": "<packet_length:int>",
      "packet_length_deviation": "<packet_length_deviation:float>",
      "packet_length_min": "<packet_length_min:int>",
      "packet_length_max": "<packet_length_max:int>",
      "frame_rate": "<frame_rate:float>",
      "imix_number_of_frames": "<flow_duration:int>",
      "udp_src": "<udp_source_port:int>",
      "udp_dest": "<udp_destination_port:int>",
      "analysis": {
         "max_threshold_latency": "<max_threshold_latency:float>"
      }
   }

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/gaming_flow
   :auto_reference:
   :auto_target:
   :lift_title: False

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/latency_loss_analysis/properties/max_threshold_latency
   :auto_reference:
   :auto_target:
   :lift_title: False
