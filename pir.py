import gpio
import time

pir = gpio.GPIO(129, 'in')
led = gpio.GPIO(128, 'out')

led.write_value(0)

while True:
    data = pir.read_value().strip()
    print('pir sensor state :',data)
    if data == '0':
        led.write_value(0)
    else:
        led.write_value(1)
    time.sleep(1)
