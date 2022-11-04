from machine import Pin
import adc1_cal

ADC_PIN   = 35                # ADC input pin no.
DIV       = 1                 # div = V_measured / V_input; here: no input divider
AVERAGING = 10                # no. of samples for averaging (default: 10)
    
# vref = None -> V_ref calibration value is read from efuse
ubatt = ADC1Cal(Pin(ADC_PIN, Pin.IN), DIV, None, AVERAGING, "ADC1 Calibrated")
    
# set ADC result width
ubatt.width(ADC.WIDTH_10BIT)
# set attenuation
ubatt.atten(ADC.ATTN_6DB)

print('ADC Vref: {:4}mV'.format(ubatt.vref))

print('Voltage:  {:4.1f}mV'.format(ubatt.voltage))
