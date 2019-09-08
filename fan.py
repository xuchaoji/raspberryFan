#!/usr/bin/python2.7
import RPi.GPIO as GPIO
import time
import commands

T_HIGH = 50
T_LOW = 42
fan_pin = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(fan_pin, GPIO.OUT)

def get_gpu_temp():
    gpu_temp = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
    return  float(gpu_temp)

while 1:
    gpu_temp_loop = get_gpu_temp()
    print 'CPU temperature: ', gpu_temp_loop, ' C'
    if gpu_temp_loop > T_HIGH:
        GPIO.output(fan_pin, 0)
    if gpu_temp_loop < T_LOW:
        GPIO.output(fan_pin, 1)
    time.sleep(3)
    if GPIO.input(fan_pin) == 0:
        print 'fan is working...'
