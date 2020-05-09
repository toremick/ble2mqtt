#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import struct
from defs import *

#mqtt server address
broker_address="192.168.2.30"


#eksempel data 
#$GPRP,A06FAA4F74AF,CC4B7399BCB2,-87,02011A0C26FE88080101A26FAA4F74AE



def getTemp(msg):
    val_one = int(msg[24:26], 16)
    val_two = int(msg[26:28], 16)

    vals = (val_one, val_two)
    btarray = bytearray(vals)
    integer = struct.unpack('h'*(len(btarray)//2), btarray)
    temp = integer[0]/100.0
    return temp

    

def getBatt(msg):
    val_one = int(msg[18:20], 16)
    val_two = int(msg[20:22], 16)

    vals = (val_one, val_two)
    btarray = bytearray(vals)
    integer = struct.unpack('h'*(len(btarray)//2), btarray)
    temp = integer[0]/100.0
    return temp

    
def on_message(client, userdata, message):
    try:
        client.publish("ble2mqtt/state", "online")
        data = str(message.payload.decode("utf-8"))
        data = data.split(',')
        mac = data[1]
        signal = data[3]
        payload = data[4]
        #temp = getTemp(payload) 
        senstype = payload[0:14]
        if senstype  == "02010612FF0D00":
            extra = payload[22:24]
            if extra == '01':
                button = "on"
            elif extra == '00':
                button = "off"    
            batt = getBatt(payload)
            temp = getTemp(payload)
            #batt = int(batt)
            batt = round((float(batt)/3.3)*100, 2)
            topic = "ignics/" + str(mac) + "/"
            
            batt_cfg = battery_cfg.replace('MACADDRESS', str(mac))
            temp_cfg = temperature_cfg.replace('MACADDRESS', str(mac))
            link_cfg = signal_cfg.replace('MACADDRESS', str(mac))
            
            tpmsg = topicmsg.replace('BATT', str(batt))
            tpmsg = tpmsg.replace('TEMP', str(temp))
            tpmsg = tpmsg.replace('LINK', str(signal))
            
            
            client.publish("homeassistant/sensor/" + mac + "/battery/config", batt_cfg, retain=True)
            client.publish("homeassistant/sensor/" + mac + "/temperature/config", temp_cfg, retain=True)
            client.publish("homeassistant/sensor/" + mac + "/linkquality/config", link_cfg, retain=True)
            #print(batt_cfg)
            client.publish("ble2mqtt/" + mac, tpmsg)
            #client.publish(topic + "temperature/value", str(temp))
            #client.publish(topic + "button/value", button)
            #client.publish(topic + "signal/value", str(signal))
            #client.publish(topic + "battery/value", str(batt))
            #print("mac: " + mac + " signal: " + signal + " type: " + str(senstype) + " temp: " + str(temp) + " button: " + button + " payload: " + str(payload))    
                
    except Exception as e:
        print("exception: ")
        print(e)
    #print("message received " ,str(message.payload.decode("utf-8")))
    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)



#print("creating new instance")
client = mqtt.Client("ble2mqttscript")
#print("connecting to broker")
client.connect(broker_address)
client.subscribe("tores/#")
client.publish("ble2mqtt/state", "online")
client.on_message=on_message
client.loop_forever()