#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import struct
from defs import *
from config import *
import os.path

statefile= '/opt/ble2mqtt/sensors.state'

file_exists = os.path.isfile(statefile) 
if file_exists != True:
    with open(statefile, 'w+') as file:
        file.write("#known sensors\n");

def ingicsTemp(msg):
    val_one = int(msg[24:26], 16)
    val_two = int(msg[26:28], 16)
    vals = (val_one, val_two)
    btarray = bytearray(vals)
    integer = struct.unpack('h'*(len(btarray)//2), btarray)
    temp = integer[0]/100.0
    return temp

def ruuviTemp(msg):
    val_one = int(msg[18:20], 16)
    val_two = int(msg[20:22], 16)
    temp = (val_one & 127) + val_two / 100
    sign = (val_one >> 7) & 1
    if sign == 0:
        return round(temp, 2)
    return round(-1 * temp, 2)


def xiaomiTemp(msg):
    val_one = int(msg[20:24], 16)
    temp = val_one/10.0
    return temp

def xiaomiHum(msg):
    humi = int(msg[24:26], 16)
    return humi

def ruuviHum(msg):
    humi = int(msg[16:18], 16)
    return humi*0.5

def ruuviPress(msg):
    val_one = int(msg[22:24], 16)
    val_two = int(msg[24:26], 16)
    vals = (val_one, val_two)
    btarray = bytearray(vals)
    integer = struct.unpack('h'*(len(btarray)//2), btarray)
    temp = (integer[0]/10)
    return temp

def ingicsBatt(msg):
    val_one = int(msg[18:20], 16)
    val_two = int(msg[20:22], 16)
    vals = (val_one, val_two)
    btarray = bytearray(vals)
    integer = struct.unpack('h'*(len(btarray)//2), btarray)
    battval = integer[0]/100
    temp = int((battval/3.3)*100)
    return temp

def xiaomiBatt(msg):
    humi = int(msg[26:28], 16)
    return humi

def ruuviBatt(msg):
    battval =  int(msg[38:42], 16)
    temp = int(((battval/1000.0)/3.3)*100)
    if temp >= 100:
        temp = 100
    return temp

def check_if_string_in_file(string_to_search):
    with open(statefile, 'r+') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return False
        read_obj.write(string_to_search + "\n")
    return True

def on_message(client, userdata, message):
    try:
        data = str(message.payload.decode("utf-8"))
        data = data.split(',')
        mac = "BLE" + data[1]
        signal = data[3]
        payload = data[4]
        senstype = payload[0:14]
        accepted_sensor = 0
        humid = 0
        model = ""
        manu =""
        batt = 0
        temp = 0
        #type is ingics
        if senstype  == "02010612FF0D00":
            extra = payload[22:24]
            if extra == '01':
                button = "on"
            elif extra == '00':
                button = "off"    
            batt = ingicsBatt(payload)
            temp = ingicsTemp(payload)
            model = "iBS03T"
            manu = "INGICS"
            accepted_sensor = 1
            
        #type is ruuvitag    
        elif senstype == "02010611FF9904":
            temp= ruuviTemp(payload)
            humid = ruuviHum(payload)
            batt = ruuviBatt(payload)
            model = "ruuvitag"
            manu = "RUUVI"
            accepted_sensor = 1
        
        #type is xiaomi
        elif senstype == "10161A18A4C138":
            temp = xiaomiTemp(payload)
            humid = xiaomiHum(payload)
            batt = xiaomiBatt(payload)
            model = "LYWSD003MMC"
            manu = "XIAOMI"
            accepted_sensor = 1

        if accepted_sensor == 1:    
            batt_cfg = battery_cfg.replace('MACADDRESS', str(mac))
            batt_cfg = batt_cfg.replace('MODELNAME', str(model))
            batt_cfg = batt_cfg.replace('MANUFACTURENAME', str(manu))
            temp_cfg = temperature_cfg.replace('MACADDRESS', str(mac))
            temp_cfg = temp_cfg.replace('MODELNAME', str(model))
            temp_cfg = temp_cfg.replace('MANUFACTURENAME', str(manu))
            link_cfg = signal_cfg.replace('MACADDRESS', str(mac))
            link_cfg = link_cfg.replace('MODELNAME', str(model))
            link_cfg = link_cfg.replace('MANUFACTURENAME', str(manu))
            clicker_cfg = click_cfg.replace('MACADDRESS', str(mac))
            clicker_cfg = clicker_cfg.replace('MODELNAME', str(model))
            clicker_cfg = clicker_cfg.replace('MANUFACTURENAME', str(manu))
                  
            if humid > 1:            
                hum_cfg = humidity_cfg.replace('MACADDRESS', str(mac))
                hum_cfg = hum_cfg.replace('MODELNAME', str(model))
                hum_cfg = hum_cfg.replace('MANUFACTURENAME', str(manu))
                tpmsg = topicmsgwhumid.replace('HUMID', str(humid))
                tpmsg = tpmsg.replace('BATT', str(batt))
            else:
                tpmsg = topicmsg.replace('BATT', str(batt))    
            tpmsg = tpmsg.replace('TEMP', str(temp))
            tpmsg = tpmsg.replace('LINK', str(signal))

            if check_if_string_in_file(mac):
                client.publish("homeassistant/sensor/" + mac + "/battery/config", batt_cfg, retain=True)
                client.publish("homeassistant/sensor/" + mac + "/temperature/config", temp_cfg, retain=True)
                client.publish("homeassistant/sensor/" + mac + "/linkquality/config", link_cfg, retain=True)
                if humid > 1:
                    client.publish("homeassistant/sensor/" + mac + "/humidity/config", hum_cfg, retain=True)

            client.publish("ble2mqtt/" + mac, tpmsg)
            client.publish("ble2mqtt/state", "online")
                
    except Exception as e:
        print("on message exception: ")
        print(e)

def on_disconnect(client, userdata, rc):
    print("disconnecting reason  "  +str(rc))
    
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

def connectmqtt():
    client = mqtt.Client("ble2mqttscript-test")	
    if broker_username != "":
        client.username_pw_set(broker_username, broker_password)
        print("logging in")
    client.on_connect=on_connect
    client.on_disconnect=on_disconnect
    client.connect(broker_address, port=1883, keepalive=600)
    client.subscribe("ble2mqtt/sensors/#")
    client.publish("ble2mqtt/state", "online")
    client.on_message=on_message
    client.loop_forever()

while True:
    try:
        print("connectmqtt \n")
        connectmqtt()
        time.sleep(5)
    except Exception as e:
        print("retrying startmqtt..")
        time.sleep(5)
        print("startmqtt exception:")
        print(e)
