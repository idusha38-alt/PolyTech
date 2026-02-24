import threading
import pygame
from gpiozero import LED
from time import sleep

pygame.mixer.init()


light = LED() 


def start_protocol(animal_name):
    
    def run():
        
        if animal_name == "deer":
            sound_file = ""
            light.blink(0.2, 0.2, n=15) 
        elif animal_name == "elephant":
            sound_file = ""
            light.blink(0.05, 0.05, n=50) 

        elif animal_name == "wild_boar":
            sound_file = ""
            light.blink(0.2, 0.2, n=20) 
        
        else:
            print(“unknown animal”)
            return

        try:
            pygame.mixer.music.load()
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy() or light.is_lit:
                sleep(0.1)
                


    logic_thread = threading.Thread(target=run)
    logic_thread.start()
