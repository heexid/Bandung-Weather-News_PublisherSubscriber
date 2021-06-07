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
    print('sensor_3', mid)

#inisiasi sensor
sensor_3 = mqtt.Client('sensor_3')
sensor_3.on_publish = on_publish
sensor_3.connect('127.0.0.1', port=6969)


sensor_3.loop_start()
while True:
    suhu = getSuhu()
    if suhu > 1:
        sensor_3.publish(TOPIK,suhu)
    sleep(10)

sensor_3.disconnect()
sensor_3.loop_stop()
print('Sensor Dimatikan')
