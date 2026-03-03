import threading
import pygame
from gpiozero import LED
from time import sleep
import paho.mqtt.client as mqtt



pygame.mixer.init()

def run_logic(animal_name):
    if animal_name == "deer":
        print("Deer detected")
    elif animal_name == "elephant":
        print("Elephant detected")
    elif animal_name == "wild_boar":
        print("Wild boar detected")
    else:
        print("unknown animal")
        return

    try:
        # pygame.mixer.music.load("sound.mp3")
        # pygame.mixer.music.play()
        sleep(2) 
    except:
        pass

    display_message = f"ALARM ACTIVE: {animal_name.upper()} DETECTED!"
    client.publish("alerts/display", display_message)

def on_connect(client, userdata, flags, rc, properties=None):
    client.subscribe("yolo/data")

def on_message(client, userdata, msg):
    animal = msg.payload.decode().strip()
    threading.Thread(target=run_logic, args=(animal,)).start()

try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
except:
    client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883, 60)
client.loop_forever()
