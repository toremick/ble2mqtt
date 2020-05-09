# ble2mqtt
home assistant ignics trough mqtt

### install pip  
```apt install python3-pip```


### install paho-mqtt for python  
```pip3 install paho-mqtt```  


### install ble2mqtt in /opt
```cd /opt```
```git clone https://github.com/toremick/ble2mqtt.git```



### copy ble2mqtt to /etc/init.d/
```cd /opt/ble2mqtt```
```cp ble2mqtt /etc/init.d/```
### update rc.d
```update-rc.d ble2mqtt defaults```

### change your mqtt server in main.py   
```nano main.py```   
### edit following line to reflect your mqtt server:    
```broker_address="192.168.2.30"```      
```broker_username="your-username"```  
```broker_password="your-password"```  
### make changes and save with "ctrl+x" then y and enter    

### Set up your gateway as shown below (change your ip to match)


![Gateway setup](/images/setup%20gateway.PNG)


