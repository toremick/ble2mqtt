# ble2mqtt
home assistant ingics, ruuvitag and xiaomi ( LYWSD03MMC custom firmware)   trough mqtt

### install pip and git  
```sudo apt install python3-pip git```


### install paho-mqtt for python  
```sudo pip3 install paho-mqtt```  


### install ble2mqtt in /opt
```cd /opt```  
```sudo git clone https://github.com/toremick/ble2mqtt.git```  



### copy ble2mqtt to /etc/init.d/
```cd /opt/ble2mqtt```  
```sudo cp examples/ble2mqtt /etc/init.d/```  

### update rc.d  
```sudo update-rc.d ble2mqtt defaults```   

### create config file from example   
```sudo cp examples/config_example.py config.py```   

### open in editor
```sudo nano config.py``` 

### edit following line to reflect your mqtt server:      
```broker_address="192.168.2.30"```      
```broker_username="my-mqtt-username"```  
```broker_password="my-mqtt-password"```  

### make changes and save with "ctrl+x" then y and enter    


### Set up your gateway as shown below (change your ip to match, and set request interval to 60)


![Gateway setup](/images/setup%20gateway.PNG)



### finally start the service  
```sudo systemctl start ble2mqtt``` 
