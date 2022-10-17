from machine import Pin, ADC
from time import sleep
import onewire
import ds18x20
from datetime import date


class Sensor:
    def __init__(self, pin):
        self.pin = Pin(pin)
        self.date = date.today()
        self.data = None

    def now(self):
        self.date = date.today()


class DS18B20(Sensor):
    def __init__(self, pin):
        Sensor.__init__(self, pin)
        self.ow = onewire.OneWire(self.pin)
        self.ow.scan()
        self.ds = ds18x20.DS18X20(self.ow)

    def read(self):
        self.ds.convert_temp()
        self.roms = self.ds.scan()
        self.ds.convert_temp()
        for rom in self.roms:
            return self.ds.read_temp(rom)


class LM35(Sensor):
    def __init__(self, pin):
        Sensor.__init__(self, pin)
        self.adc = ADC(self.pin)
        self.adc.atten(ADC.ATTN_11DB)

    def raw(self):
        self.reading = self.adc.read()

    def temp_c(value):
        return value / 10

    def read(self):
        self.raw()
        self.celsius_temp = self.temp_c(self.reading)
        return self.celsius_temp


    def fahrenheit(self):
        return (self.read() * (9 / 5)) + 32


while True:
    sensor_digital = DS18B20(26)
    print(f'DS18B20: {sensor_digital.read()} graus.')
    sensor_analogico = LM35(32)
    print(f'LM35: {sensor_analogico.read()} graus.')
    sleep(1)

