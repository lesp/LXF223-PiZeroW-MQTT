import time
import paho.mqtt.client as mqtt
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
client = mqtt.Client()
client.connect("192.168.0.13", 1883, 60)
while True:
    temp = sensor.get_temperature()
    hall = temp
    client.publish("temp",hall)
    print(hall)
    time.sleep(10)
