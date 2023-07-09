import RPi.GPIO as GPIO
import time

bRed = 26
# bLeft = 20
bLeft = 13
bRight = 21
bUp = 12
bDown = 16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(bRed, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bLeft, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bRight, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bUp, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bDown, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    print("bLeft {}".format(GPIO.input(bLeft)))
    print("bRight {}".format(GPIO.input(bRight)))
    print("bUP {}".format(GPIO.input(bUp)))
    print("bDown {}".format(GPIO.input(bDown)))
    print('------------------------------------------')
    time.sleep(0.5)
