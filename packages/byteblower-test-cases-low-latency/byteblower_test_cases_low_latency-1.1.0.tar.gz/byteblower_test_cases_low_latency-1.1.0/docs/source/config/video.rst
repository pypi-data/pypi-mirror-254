**********
Video Flow
**********

.. code-block:: json

   {
    "type":  "video",
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
    "segment_size": "<segment_size:int>",
    "segment_duration": "<segment_duration:float|timedelta>",
    "buffering_goal": "<buffering_goal:float|timedelta>",
    "play_goal": "<play_goal:float|timedelta>"
 }

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/video_flow
   :auto_reference:
   :auto_target:
   :lift_title: False
