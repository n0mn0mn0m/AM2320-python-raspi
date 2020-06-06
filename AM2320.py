#!/usr/bin/env python3

## AM2320 Temperate and Humidity Sensor Library
## This library is used to get the temperate and humidity from a AM2320 sensor via i2c.
## This sensor has a sleep function to it were you need to wake it up before each call
## which can be seen in any function returning data via the wakeUp function.

## Device address: 0x5c
## Reading Bus: 0x03
## Temperate Registers: 0x02, 0x03
## Humidity Registers: 0x00, 0x01

## Other registers available see datasheet: https://akizukidenshi.com/download/ds/aosong/AM2320.pdf

import smbus2
import time

class AM2320:
	def __init__(self, channel):
		self.channel = channel
		self.bus = smbus2.SMBus(self.channel)
		self.address = 0x5c

	# Wake up the sensor before reading data from it
	def wakeUp(self):
		try:
			self.bus.write_byte_data(self.address, 0x00, 0)
		except:
			pass
		time.sleep(0.01)
	
	# Get the temperature in Celcius
	def getTempC(self):
		self.wakeUp()
		self.bus.write_i2c_block_data(self.address, 0x03, [0x02, 0x04]) # Write to get the sensor to return data
		data = self.bus.read_i2c_block_data(self.address, 0x00, 4) # Read the response
		return (data[2] << 8 | data[3]) / 10.0

	# Just converts the getTempC response to Farenheit - doesn't actually get it from the sensor in that format
	def getTempF(self):
		return (self.getTempC() * 1.8) + 32
	
	# Get the humidity
	def getHumidity(self):
		self.wakeUp()
		self.bus.write_i2c_block_data(self.address, 0x03, [0x00, 0x02])
		data = self.bus.read_i2c_block_data(self.address, 0x00, 4)
		return (data[2] << 8 | data[3]) / 10.0
	
	
