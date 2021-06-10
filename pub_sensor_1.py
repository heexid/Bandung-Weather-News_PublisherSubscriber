#import library
import random as ran
from time import sleep
from paho.mqtt import client as mqtt

#listening suhu
def getSuhu():
    #generate random int mendapatkan suhu
    return ran.randint(12,31)
    
#inisiasi topik
TOPIK = 'Bandung_Weather_News'

#publish data
def on_publish(client, userdata, mid):
    print('sensor_1', mid)

#inisiasi sensor
sensor_1 = mqtt.Client('sensor_1')
sensor_1.on_publish = on_publish
sensor_1.connect('mqtt.eclipseprojects.io', port=1883)


sensor_1.loop_start()
while True:
    suhu = getSuhu()
    if suhu > 1:
        sensor_1.publish(TOPIK,suhu)
    sleep(10)

sensor_1.disconnect()
sensor_1.loop_stop()
print('Sensor Dimatikan')
