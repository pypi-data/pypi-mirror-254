***************
TCP (HTTP) flow
***************

.. code-block:: json

   {
      "type":  "http",
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
      "tcp_server_port": "<tcp_server_port:int>",
      "tcp_client_port": "<tcp_client_port:int>",
      "request_size":"<request_size:int>",
      "duration": "<duration:float|int|timedelta>",
      "initial_time_to_wait": "<initial_time_to_wait:float|int|timedelta>",
      "maximum_bitrate": "<maximum_bitrate:float>",
      "receive_window_scaling": "<receive_window_scaling:int>",
      "slow_start_threshold": "<slow_start_threshold:int>",
      "add_reverse_direction": "<add_reverse_direction_flow:bool>"
   }

.. jsonschema:: ../extra/test-cases/low-latency/json/config-schema.json#/$defs/http_flow
   :auto_reference:
   :auto_target:
   :lift_title: False
