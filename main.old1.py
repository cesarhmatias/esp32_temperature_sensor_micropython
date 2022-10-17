from machine import Pin, ADC 
from time import sleep
import onewire
import ds18x20
import time

ow = onewire.OneWire(Pin(26))   #Init wire
ow.scan()
ds=ds18x20.DS18X20(ow)
adc = ADC(Pin(32))            #creating potentiometer object
#adc = ADC(0)
adc.atten(ADC.ATTN_11DB)

def temp(value):
    return value/10

def fahrenheit(celsius):
    return (celsius * (9/5)) + 32

while True:
    reading = adc.read()

    celsius_temp = temp(reading)
    print(celsius_temp)
    sleep(1)
    roms=ds.scan()                #scan ds18x20
    ds.convert_temp()             #convert temperature
    for rom in roms:
        print(ds.read_temp(rom))    #display 
    time.sleep(1)
    #fahrenheit_temp = fahrenheit(celsius_temp)

    #print("TMP36 reading {}\nDegrees Celsius {}\nDegrees Fahrenheit {}".format(reading, celsius_temp, fahrenheit_temp))

