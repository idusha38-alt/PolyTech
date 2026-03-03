import threading
import pygame
from gpiozero import LED
from time import sleep
import paho.mqtt.client as mqtt

try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
except:
    client = mqtt.Client() # Fallback for older versions

# pygame.mixer.init() # Commented out using #

  
# light = LED(17) 

def start_protocol(animal_name): 
    print(f"Checking animal: {animal_name}")
    
    if animal_name == "deer":
        # sound_file = ""
        print(">>> Protocol: Deer detected")
    elif animal_name == "elephant":
        # sound_file = ""
        print(">>> Protocol: Elephant detected")
    elif animal_name == "wild_boar":
        # sound_file = ""
        print(">>> Protocol: Wild boar detected")
    else:
        print(f"Unknown animal: {animal_name}")
        return

    display_message = f"ALARM ACTIVE: {animal_name.upper()} DETECTED!"
    client.publish("alerts/display", display_message) 
    print(f"Sent to website: {display_message}")

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("CONNECTED TO BROKER SUCCESSFULLY")
        # Subscribe to the topic YOLO will send to
        client.subscribe("yolo/data")
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    animal = msg.payload.decode().strip()
    print(f"\nReceived message from MQTT: {animal}")
    
    t = threading.Thread(target=start_protocol, args=(animal,))
    t.start()

client.on_connect = on_connect
client.on_message = on_message

print("Attempting to connect...")
client.connect("broker.emqx.io", 1883, 60)

# This keeps the script running
client.loop_forever()
