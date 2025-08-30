import time
import datetime
import pygame #for sound we use it 

# If we want to remove the hello from pygame community then we need to go to pygame folder and go to __init__ and comment out the if statement at the bottom

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "my_music.mp3"
    is_running = True
    
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        if current_time == alarm_time:
            print("WAKE_UP! 😒")
            
            pygame.mixer.init()# to play music we can use mixer method and the initialize method to call the constructor directly where we can pass arguments like buffer,channel etc.
            pygame.mixer.music.load(sound_file) # load music
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy(): #to stop the music
                time.sleep(1)
            
            is_running = False

        
        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
