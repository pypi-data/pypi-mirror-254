**************************
Dynamic FrameBlasting Flow
**************************

.. code-block:: json

   {
      "type":  "dynamic_frame_blasting",
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
      "duration": "<flow_duration:float|int|timedelta>",
      "initial_time_to_wait": "<initial_time_to_wait:float|int|timedelta>",
      "frame_size": "<frame_size_without_crc:int>",
      "bitrate": "<flow_bitrate:float>",
      "frame_rate": "<frame_rate:float>",
      "number_of_frames": "<number_of_frames:float>",
      "nat_keep_alive": "<activate_nat_keep_alive:bool>",
      "max_bitrate": "<maximum_bitrate:int|float>",
      "min_bitrate": "<minimum_bitrate:int|float>",
      "scaling_interval": "<scaling_interval:float>",
      "scaling_rate": "<scaling_rate:int>",
      "analysis": {
         "latency":"<enable_latency_analysis:bool>",
         "max_threshold_latency": "<max_threshold_latency:float>",
         "max_loss_percentage": "<max_loss_percentage:float>",
         "quantile": "<quantile:float>",
         "min_percentile": "<min_percentile:float>",
         "max_percentile": "<max_percentile:float>"
      }
   }

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/dynamic_frame_blasting
   :auto_reference:
   :auto_target:
   :lift_title: False
