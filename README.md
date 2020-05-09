## ha-ble
home assistant ignics trough mqtt

#install pip  
apt install python3-pip  
#install paho-mqtt for python  
pip3 install paho-mqtt  

#copy ble2mqtt to /etc/init.d/  
cp ble2mqtt /etc/init.d/  
#update rc.d  
update-rc.d ble2mqtt defaults  


![Gateway setup](/images/setup%20gateway.PNG)


