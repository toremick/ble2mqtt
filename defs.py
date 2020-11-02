#battery_cfg="""
#{"unit_of_measurement":"%",
#"device_class":"battery",
#"value_template":"{{ value_json.battery }}",
#"state_topic":"ble2mqtt/MACADDRESS",
#"json_attributes_topic":"ble2mqtt/MACADDRESS",
#"name":"MACADDRESS_battery",
#"unique_id":"MACADDRESS_battery_ble2mqtt",
#"device":{"identifiers":["ble2mqtt_MACADDRESS"],
#"name":"MACADDRESS",
#"sw_version":"ble2mqtt 1.0",
#"model":"MODELNAME",
#"manufacturer":"MANUFACTURENAME"},
#"availability_topic":"ble2mqtt/state"}"""

battery_cfg = """
{
  "availability_topic": "ble2mqtt/state",
  "device": {
    "identifiers": [
      "ble2mqtt_MACADDRESS"
    ],
    "manufacturer": "MANUFACTURENAME",
    "model": "MODELNAME",
    "name": "MACADDRESS",
    "sw_version": "ble2mqtt 1.0"
  },
  "device_class": "battery",
  "json_attributes_topic": "ble2mqtt/MACADDRESS",
  "name": "MACADDRESS_battery",
  "state_topic": "ble2mqtt/MACADDRESS",
  "unique_id": "MACADDRESS_battery_ble2mqtt",
  "unit_of_measurement": "%",
  "value_template": "{{ value_json.battery }}"
}"""

#signal_cfg = """
#{"icon":"mdi:signal",
#"unit_of_measurement":"lqi",
#"value_template":"{{ value_json.linkquality }}",
#"state_topic":"ble2mqtt/MACADDRESS",
#"json_attributes_topic":"ble2mqtt/MACADDRESS",
#"name":"MACADDRESS_linkquality",
#"unique_id":"MACADDRESS_linkquality_ble2mqtt",
#"device":{"identifiers":["ble2mqtt_MACADDRESS"],
#"name":"MACADDRESS",
#"sw_version":"ble2mqtt 1.0",
#"model":"MODELNAME",
#"manufacturer":"MANUFACTURENAME"},
#"availability_topic":"ble2mqtt/state"}"""

signal_cfg = """
{
  "availability_topic": "ble2mqtt/state",
  "device": {
    "identifiers": [
      "ble2mqtt_MACADDRESS"
    ],
    "manufacturer": "MANUFACTURENAME",
    "model": "MODELNAME",
    "name": "MACADDRESS",
    "sw_version": "ble2mqtt 1.0"
  },
  "icon": "mdi:signal",
  "json_attributes_topic": "ble2mqtt/MACADDRESS",
  "name": "MACADDRESS_signal",
  "state_topic": "ble2mqtt/MACADDRESS",
  "unique_id": "MACADDRESS_linkquality_ble2mqtt",
  "unit_of_measurement": "lqi",
  "value_template": "{{ value_json.linkquality }}"
}"""

#temperature_cfg = """
#{"unit_of_measurement":"°C",
#"device_class":"temperature",
#"value_template":"{{ value_json.temperature }}",
#"state_topic":"ble2mqtt/MACADDRESS",
#"json_attributes_topic":"ble2mqtt/MACADDRESS",
#"name":"MACADDRESS_temperature",
#"unique_id":"MACADDRESS_temperature_ble2mqtt",
#"device":{"identifiers":["ble2mqtt_MACADDRESS"],
#"name":"MACADDRESS",
#"sw_version":"ble2mqtt 1.0",
#"model":"MODELNAME",
#"manufacturer":"MANUFACTURENAME"},
#"availability_topic":"ble2mqtt/state"}"""

temperature_cfg = """
{
  "availability_topic": "ble2mqtt/state",
  "device": {
    "identifiers": [
      "ble2mqtt_MACADDRESS"
    ],
    "manufacturer": "MANUFACTURENAME",
    "model": "MODELNAME",
    "name": "MACADDRESS",
    "sw_version": "ble2mqtt 1.0"
  },
  "device_class": "temperature",
  "json_attributes_topic": "ble2mqtt/MACADDRESS",
  "name": "MACADDRESS_temperature",
  "state_topic": "ble2mqtt/MACADDRESS",
  "unique_id": "MACADDRESS_temperature_ble2mqtt",
  "unit_of_measurement": "°C",
  "value_template": "{{ value_json.temperature }}"
}"""

#humidity_cfg = """
#{"unit_of_measurement":"%",
#"device_class":"humidity",
#"value_template":"{{ value_json.humidity }}",
#"state_topic":"ble2mqtt/MACADDRESS",
#"json_attributes_topic":"ble2mqtt/MACADDRESS",
#"name":"MACADDRESS_humidity",
#"unique_id":"MACADDRESS_humidity_ble2mqtt",
#"device":{"identifiers":["ble2mqtt_MACADDRESS"],
#"name":"MACADDRESS",
#"sw_version":"ble2mqtt 1.0",
#"model":"MODELNAME",
#"manufacturer":"MANUFACTURENAME"},
#"availability_topic":"ble2mqtt/state"}"""

humidity_cfg = """
{
  "availability_topic": "ble2mqtt/state",
  "device": {
    "identifiers": [
      "ble2mqtt_MACADDRESS"
    ],
    "manufacturer": "MANUFACTURENAME",
    "model": "MODELNAME",
    "name": "MACADDRESS",
    "sw_version": "ble2mqtt 1.0"
  },
  "device_class": "humidity",
  "json_attributes_topic": "ble2mqtt/MACADDRESS",
  "name": "MACADDRESS_humidity",
  "state_topic": "ble2mqtt/MACADDRESS",
  "unique_id": "MACADDRESS_humidity_ble2mqtt",
  "unit_of_measurement": "%",
  "value_template": "{{ value_json.humidity }}"
}"""

topicmsg = """
{"battery":BATT,
"linkquality":LINK,
"temperature":TEMP}"""


topicmsgwhumid = """
{"battery":BATT,
"linkquality":LINK,
"temperature":TEMP,
"humidity":HUMID}"""





click_cfg = """
{"icon":"mdi:toggle-switch",
"value_template":"{{ value_json.click }}",
"state_topic":"ble2mqtt/MACADDRESS",
"json_attributes_topic":"ble2mqtt/MACADDRESS",
"name":"MACADDRESS_click",
"unique_id":"MACADDRESS_click_ble2mqtt",
"device":{"identifiers":["ble2mqtt_MACADDRESS"],
"name":"MACADDRESS",
"sw_version":"ble2mqtt 1.0",
"model":"MODELNAME",
"manufacturer":"MANUFACTURENAME"},
"availability_topic":"ble2mqtt/state"}"""