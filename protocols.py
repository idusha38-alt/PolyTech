import threading
import pygame
from gpiozero import LED
from time import sleep
import paho.mqtt.client as mqtt

client = mqtt.Client()
// pygame.mixer.init()




def start_protocol(animal_name): 
    if animal_name == "deer":
        // sound_file = ""
        print("Deer detected")
    elif animal_name == "elephant":
        // sound_file = ""
        print("Elephant detected")

    elif animal_name == "wild_boar":
       //  sound_file = ""
        print("Wild boardetected")
    
    else:
        print("unknown animal")
        return

    try:
        pygame.mixer.music.load()
        pygame.mixer.music.play()
        
        // while pygame.mixer.music.get_busy() or light.is_lit:
            sleep(0.1)
    except:
        pass
    display_message = f"ALARM ACTIVE: {animal_name.upper()} DETECTED!"
    client.publish("alerts/display", display_message) 

def on_connect(client, userdata, flags, rc):
    client.subscribe("yolo/data")

def on_message(client, userdata, msg):
    start_protocol(msg.payload.decode().strip())

client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883, 60)
client.loop_forever()
