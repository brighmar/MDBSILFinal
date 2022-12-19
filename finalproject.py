import RPi.GPIO as GPIO
from time import sleep
from pygame import mixer
import pygame
#import all the modules necessary: RPi.GPIO for the pi, time for sleep statements and pygame for the music

GPIO.setmode (GPIO.BCM)

def snoopy_tail () :
    """wags Snoopy's tail back and forth"""
    tail_servo_pin = 27
    GPIO.setup (tail_servo_pin, GPIO.OUT)
    tail_servo = GPIO.PWM (27, 50)
    tail_servo.start (3)
    #sets up a PWM to choose the angle of the servo

    for i in range (3, 11, 1) : #max and min for mini servo
        tail_servo.ChangeDutyCycle (i)
        sleep (0.01)
    for i in range (11, 3, -1) :
        tail_servo.ChangeDutyCycle (i)
        sleep (0.01)
    #changes the duty cycle in increments to slow the movement of the tail back and forth

def ship_swing () :
    """Swings the ship back an forth on its pendulum"""
    tail_servo_pin = 22
    GPIO.setup (tail_servo_pin, GPIO.OUT)
    tail_servo = GPIO.PWM (22, 50)
    tail_servo.start (0)
    #sets up a PWM to choose the angle of the servo
    
    tail_servo.ChangeDutyCycle(2)
    sleep(0.75) #a longer sleep here allows the servo to complete the entire swing
    tail_servo.ChangeDutyCycle(12)
    sleep(0.1)

def ship_crash () :
    """Makes the ship crash by shaking at one position and making a crash sound"""
    ship_servo_pin = 23
    GPIO.setup (ship_servo_pin, GPIO.OUT)
    ship_servo = GPIO.PWM (23, 50)
    #sets up a PWM to choose the angle of the servo

    ship_servo.start (5.75)
    sleep (0.01)
    ship_servo.ChangeDutyCycle (6)
    sleep (0.01)
    ship_servo.ChangeDutyCycle (6.25)
    sleep (0.01)
    #small changes in the angle make the ship shake to simulate a crash
    
        
def blunt () :
    """Makes Snoopy's blunt flicker, or breathe, using PWM"""
    blunt_LED_pin = 24
    GPIO.setup (blunt_LED_pin, GPIO.OUT)
    blunt_breathe = GPIO.PWM (blunt_LED_pin, 100)
    blunt_breathe.start (0)
    #sets up a PWM to change the brightness of the LED

    for i in range (1, 100, 5) :
        blunt_breathe.ChangeDutyCycle (i)
        sleep (0.01)
    for i in range (100, 0, -5) :
        blunt_breathe.ChangeDutyCycle (i)
        sleep (0.01)
    #makes the LED get brighter and dimmer so that it breathes

def music():
    """Plays either a crash sound or a Snoop Dogg song based on which of two switches are switched on."""
    playing_music = mixer.music.get_busy()

    if not GPIO.input (crash_switch) and GPIO.input (snoop_switch) and not playing_music:
        mixer.music.load ("snoop.mp3")
        mixer.music.play()
        #plays Snoop Dogg's "Drop it like it's Hot" when the snoop switch is on
    elif GPIO.input (crash_switch) and not GPIO.input (snoop_switch) and not playing_music:
        mixer.music.load ("crash.mp3")
        mixer.music.play()
        #plays a crash sound effect when the crash switch is on
    elif GPIO.input (crash_switch) and GPIO.input (snoop_switch) and playing_music:
        mixer.music.stop()
        
pygame.init()        
mixer.init()

crash_switch = 25
GPIO.setup (crash_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
snoop_switch = 5
GPIO.setup (snoop_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        snoopy_tail ()
        ship_swing ()
        ship_crash ()
        blunt ()
        music ()
    #cycles through each of the functions over and over again

except KeyboardInterrupt:
    pass

GPIO.cleanup()