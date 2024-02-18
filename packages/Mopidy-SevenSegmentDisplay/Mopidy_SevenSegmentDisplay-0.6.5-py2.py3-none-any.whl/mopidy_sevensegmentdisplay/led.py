import colorsys
import random
import RPi.GPIO as GPIO
from lib_nrf24 import NRF24


class Led:
    
    def __init__(self, led_enabled):
        self._spi = None
        self._radio = None

        if (not led_enabled):
            return

        GPIO.setmode(GPIO.BCM)

        pipe = ["T", "x", "_", "_", "1"]

        import spidev
        self._spi = spidev.SpiDev()
        self._spi.open(0, 1)
        self._spi.cshigh = False
        self._spi.max_speed_hz = 500000
        self._spi.mode = 0

        self._radio = NRF24(GPIO, self._spi)
        self._radio.begin(1, 25)
        self._radio.setPayloadSize(32)
        self._radio.setChannel(0x7A)
        self._radio.setDataRate(NRF24.BR_1MBPS)
        self._radio.setPALevel(NRF24.PA_MIN)
        self._radio.setAutoAck(False)
        self._radio.openWritingPipe(pipe)
        self._radio.printDetails()
        
    def setColor(self, hue, sat = 1, val = 1):
        if self._radio is None:
            return

        c = colorsys.hsv_to_rgb(hue / 360.0, sat, val)
            
        self._radio.write([0, c[0] * 255, c[1] * 255, c[2] * 255])

    def setRandomColor(self):
        self.setColor(random.random() * 360)

    def setNoneColor(self):
        self.setColor(0, 0, 0)
        
    def stop(self):
        if self._spi is None:
            return
        
        self._spi.close()
