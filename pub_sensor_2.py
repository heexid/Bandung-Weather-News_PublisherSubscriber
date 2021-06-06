#import library
import random as ran
from time import sleep
from paho.mqtt import client as mqtt

#listening suhu
def getSuhu():
    #generate random int mendapatkan suhu atau tidak
    listening = ran.randint(0,1)

    if listening == 1:
        return ran.randint(12,31)
    else:
        return listening
    
#inisiasi topik
TOPIK = 'Bandung_Weather_News'

#publish data
def on_publish(client, userdata, mid):
    print('sensor_2', mid)

#inisiasi sensor
sensor_2 = mqtt.Client('sensor_2')
sensor_2.on_publish = on_publish
sensor_2.connect('127.0.0.1', port=6969)


sensor_2.loop_start()
while True:
    suhu = getSuhu()
    if suhu > 1:
        sensor_2.publish(TOPIK,suhu)
    sleep(10)

sensor_2.disconnect()
sensor_2.loop_stop()
print('Sensor Dimatikan')
