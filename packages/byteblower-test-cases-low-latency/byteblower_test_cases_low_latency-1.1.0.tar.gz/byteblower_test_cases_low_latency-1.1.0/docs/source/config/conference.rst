***************
Conference Flow
***************

This flow allows to simulate a video conference call which
could involve the exchanges of three types of flows: Video, audio, and
screensharing. Each one is simulated as a UDP frame blasting flow with possible
parameters similar to the basic FrameBlasting flow.

Unlike the other types of flows, the conference flow takes separate
configurations for each one of the video, voice, and screen sharing flows.
The configuration structure is as follows:

.. code-block:: json

   {
      "type":  "conference",
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
      "video":{
         "ecn": "<ecn_code_point:str|int>",
         "dscp": "<dscp_code_point:str|int>",
         "add_reverse_direction": "<add_reverse_direction_flow:bool>",
         "initial_time_to_wait": "<initial_time_to_wait:float|int|timedelta>",
         "bitrate": "<flow_bitrate:float>",
         "frame_size": "<frame_size_without_crc:int>",
         "frame_rate": "<frame_rate:float>",
         "number_of_frames": "<number_of_frames:float>",
         "duration": "<flow_duration:float|int|timedelta>",
         "udp_src": "<udp_source_port:int>",
         "udp_dest": "<udp_destination_port:int>",
         "analysis": {
            "latency":"<enable_latency_analysis:bool>",
            "max_threshold_latency": "<max_threshold_latency:float>",
            "max_loss_percentage": "<max_loss_percentage:float>",
            "quantile": "<quantile:float>",
            "min_percentile": "<min_percentile:float>",
            "max_percentile": "<max_percentile:float>"
         }
      },
      "voice":{
         "ecn": "<ecn_code_point:str|int>",
         "dscp": "<dscp_code_point:str|int>",
         "add_reverse_direction": "<add_reverse_direction_flow:bool>",
         "initial_time_to_wait": "<initial_time_to_wait:float|int|timedelta>",
         "bitrate": "<flow_bitrate:float>",
         "frame_size": "<frame_size_without_crc:int>",
         "frame_rate": "<frame_rate:float>",
         "number_of_frames": "<number_of_frames:float>",
         "duration": "<flow_duration:float|int|timedelta>",
         "udp_src": "<udp_source_port:int>",
         "udp_dest": "<udp_destination_port:int>",
         "analysis": {
            "mos": "<enable_mos:bool>"
         }
      },
      "screenshare":{
         "ecn": "<ecn_code_point:str|int>",
         "dscp": "<dscp_code_point:str|int>",
         "add_reverse_direction": "<add_reverse_direction_flow:bool>",
         "initial_time_to_wait": "<initial_time_to_wait:float|int|timedelta>",
         "bitrate": "<flow_bitrate:float>",
         "frame_size": "<frame_size_without_crc:int>",
         "frame_rate": "<frame_rate:float>",
         "number_of_frames": "<number_of_frames:float>",
         "duration": "<flow_duration:float|int|timedelta>",
         "udp_src": "<udp_source_port:int>",
         "udp_dest": "<udp_destination_port:int>",
         "analysis": {
            "latency":"<enable_latency_analysis:bool>",
            "max_threshold_latency": "<max_threshold_latency:float>",
            "max_loss_percentage": "<max_loss_percentage:float>",
            "quantile": "<quantile:float>",
            "min_percentile": "<min_percentile:float>",
            "max_percentile": "<max_percentile:float>"
         }
      },
      "add_reverse_direction": "<add_reverse_direction_flow:bool>"
   }

All of the conference's flows are configured as basic FrameBlasting flows.

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/conference_flow
   :auto_target:
   :auto_reference:
   :lift_title: False
