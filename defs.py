battery_cfg="""
{"unit_of_measurement":"%",
"device_class":"battery",
"value_template":"{{ value_json.battery }}",
"state_topic":"ble2mqtt/MACADDRESS",
"json_attributes_topic":"ble2mqtt/MACADDRESS",
"name":"MACADDRESS_battery",
"unique_id":"MACADDRESS_battery_ble2mqtt",
"device":{"identifiers":["ble2mqtt_MACADDRESS"],
"name":"MACADDRESS",
"sw_version":"ble2mqtt 1.0",
"model":"iBS03T",
"manufacturer":"IGNICS"},
"availability_topic":"ble2mqtt/state"}"""

signal_cfg = """
{"icon":"mdi:signal",
"unit_of_measurement":"lqi",
"value_template":"{{ value_json.linkquality }}",
"state_topic":"ble2mqtt/MACADDRESS",
"json_attributes_topic":"ble2mqtt/MACADDRESS",
"name":"MACADDRESS_linkquality",
"unique_id":"MACADDRESS_linkquality_ble2mqtt",
"device":{"identifiers":["ble2mqtt_MACADDRESS"],
"name":"MACADDRESS",
"sw_version":"ble2mqtt 1.0",
"model":"iBS03T",
"manufacturer":"IGNICS"},
"availability_topic":"ble2mqtt/state"}"""

temperature_cfg = """
{"unit_of_measurement":"°C",
"device_class":"temperature",
"value_template":"{{ value_json.temperature }}",
"state_topic":"ble2mqtt/MACADDRESS",
"json_attributes_topic":"ble2mqtt/MACADDRESS",
"name":"MACADDRESS_temperature",
"unique_id":"MACADDRESS_temperature_ble2mqtt",
"device":{"identifiers":["ble2mqtt_MACADDRESS"],
"name":"MACADDRESS",
"sw_version":"ble2mqtt 1.0",
"model":"iBS03T",
"manufacturer":"IGNICS"},
"availability_topic":"ble2mqtt/state"}"""


topicmsg = """
{"battery":BATT,
"linkquality":LINK,
"temperature":TEMP}"""
