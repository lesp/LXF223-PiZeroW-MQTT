import paho.mqtt.client as mqtt
from blinkt import set_pixel, set_brightness, show, clear, set_all
import time

set_brightness(0.1)

clear()


def on_connect(client, userdata, flags, rc):  
        print("Connected with result code "+str(rc))
        client.subscribe("temp")

def on_message(client, userdata, msg):  
        message = str(msg.payload)
        message = message[2:(len(message)-1)]
        message = float(message)
        print(message)
        if message < 10.0 and message >= 0.0:
                print("The hall is cold")
                clear()
                set_all(0,0,255)
                show()
        elif message >= 10.0 and message < 20:
                print("The hall is at an average temperature")
                clear()
                set_all(255,255,51)
                show()
        elif message >=20 and message <30:
                print("The hall is hot")
                clear()
                set_all(255,0,0)
                show()   
        

client = mqtt.Client()  
client.on_connect = on_connect  
client.on_message = on_message  
client.connect("192.168.0.13", 1883, 60)

client.loop_forever()  
