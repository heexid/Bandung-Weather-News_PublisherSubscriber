from paho.mqtt import client as mqtt
from time import sleep

TOPIK = 'Bandung_Weather_News'
received_messages= []

def on_message(client, user_data, msg):
    #simpan message dan convert dalam variable int
    received_messages.append(int(msg.payload.decode('utf-8')))

    #tampilkan suhu rata-rata yang didapat
    print('Rata-Rata Suhu Bandung Saat Ini', sum(received_messages)/len(received_messages))



sub_1 = mqtt.Client('sub_1')
sub_1.on_message = on_message

sub_1.connect('127.0.0.1', port=6969)

sub_1.loop_start()

while True:
    sub_1.subscribe(TOPIK)
    sleep(1)

sub_1.disconnect()
sub_1.loop_stop()
print('Selesai')