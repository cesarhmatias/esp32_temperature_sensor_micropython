from machine import Pin, ADC
from time import sleep
import esp32
import onewire
import ds18x20
# from datetime import date
# import pandas as pd


class Sensor:
    def __init__(self, pin):
        self.pin = Pin(pin)
        # self.date = date.today()
        self.data = None
        # self.list_date = []
        self.list_data = []
        self.list_index = []
        # self.df = pd.DataFrame()
        self.dict = {
                        'index':[],
                        # 'date':[],
                        'raw':[],
                    }

    # def now(self):
    # self.date = date.today()

    def store_data(self, number, time):
        for i in range(number):
            self.list_index.append(i)
            # self.list_date[i] = date.today()
            self.list_data.append(self.read())
            
            sleep(time + 1)
            
        self.dict['index'] = self.list_index
        # self.dict['date'] = self.list_date
        self.dict['raw'] = self.list_data
        return self.dict

    # def parse_df(self):
    #     self.df.index = self.list_index
    #     # self.df['Date'] = self.date
    #     self.df['raw'] = self.data
    #     return self.df

    def read(self):
        raise NotImplemented()


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
        self.schedule = 1000
        self.total = 0
        self.reading = 0

    def raw(self):
        self.reading = self.adc.read()
        return self.reading

    def temp_c(self, value):
        return value / 10

    def read(self):
        self.total = 0
        self.reading = 0
        self.total = 0
        for i in range(self.schedule):
            old = self.reading
            self.raw()
            self.total = old + self.total
        self.celsius_temp = self.temp_c(self.total/self.schedule - 1)
        
        return self.celsius_temp

    def fahrenheit(self):
        return (self.read() * (9 / 5)) + 32


sensor_digital = DS18B20(26)
print(f'DS18B20: {sensor_digital.read()} graus.')
sensor_analogico = LM35(32)
print(f'LM35: {sensor_analogico.raw()} graus.')
print(sensor_digital.store_data(5, 1))
print(sensor_analogico.store_data(5, 1))
