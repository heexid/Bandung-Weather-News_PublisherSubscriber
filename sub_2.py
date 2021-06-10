from paho.mqtt import client as mqtt
from time import sleep

TOPIK = 'Bandung_Weather_News'
received_messages= []

def on_message(client, user_data, msg):
    #simpan message dan convert dalam variable int
    received_messages.append(int(msg.payload.decode('utf-8')))

    #tampilkan suhu rata-rata yang didapat
    print('Rata-Rata Suhu Bandung Saat Ini', sum(received_messages)/len(received_messages))



sub_2 = mqtt.Client('sub_2')
sub_2.on_message = on_message

sub_2.connect('127.0.0.1', port=6969)

sub_2.loop_start()

while True:
    sub_2.subscribe(TOPIK)
    sleep(1)

sub_2.disconnect()
sub_2.loop_stop()
print('Selesai')