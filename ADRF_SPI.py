#!/usr/bin/python

import RPi.GPIO as GPIO
import spidev
import time

from ADRF_Struct import ADRF_Ctl

temp_s = ADRF_Ctl()

GPIO.setmode(GPIO.BCM)
cs = 2
GPIO.setup(cs, GPIO.OUT)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 3900000
spi.mode = 0b00


# spi.lsbfirst = True

# Split an integer input into a two byte array to send via SPI
def write_SPI(input):
	GPIO.output(cs, GPIO.LOW)
	spi.xfer(input)
	GPIO.output(cs, GPIO.HIGH)


def read_SPI():
	GPIO.output(cs, GPIO.LOW)
	ret = "".join(bin(i)[2:] for i in spi.readbytes(2))
	GPIO.output(cs, GPIO.HIGH)
	return ret


while True:
	write_SPI(temp_s.GetMessage())
	time.sleep(0.1)
	print read_SPI()
	time.sleep(0.1)
