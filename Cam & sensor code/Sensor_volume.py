import RPi.GPIO as GPIO
import time
import alsaaudio

TRIG=23
ECHO=24

# class maken voor text kleur
class Style():
  RED = "\033[31m"
  GREEN = "\033[32m"
  BLUE = "\033[34m"
  RESET = "\033[0m"

# get current volume
m = alsaaudio.Mixer()
current_volume = m.getvolume() 

print("Starting distance measurement")


GPIO.setmode(GPIO.BCM)
while True:
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    if distance >= 100:
        print(f"{Style.RED}Distance = 100.00+ cm")
    else :
        print(f"{Style.BLUE}Distance =" , distance, "cm")

    if distance > 0 and distance < 100:
        m.setvolume(round(distance)) # Set volume depanding on the distance
    else :
        m.setvolume(100) # Set volume to 100 if distace is > then 100
    time.sleep(0.1)

