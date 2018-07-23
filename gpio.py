import time

pinctl = open('/sys/class/gpio/export','wb', 0)
led_red = 28
led_blue = 38
swt_red = 30
swt_blue = 32

class GPIO:
    def __init__(self, pinnum, direction):
        self.pinnum = pinnum
        self.export()
        self.set_direction(direction)

    def export(self):
        try:
            pinctl.write(str(self.pinnum).encode())
        except:
            pass

    def set_direction(self, direction):
        pinctldir = open('/sys/class/gpio/gpio%d/direction' % self.pinnum, 'wb', 0)
        try:
            pinctldir.write(direction.encode())
        except:
            pass

    def write_value(self, value):
        pin = open('/sys/class/gpio/gpio%d/value' % self.pinnum, 'wb', 0)
        try:
            pin.write(str(value).encode())
        except:
            pass