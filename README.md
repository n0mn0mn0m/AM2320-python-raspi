# AM2320 Python Library

## Overview
This is a small library to get started with the AM2320 temperature and humidity sensor via i2C. It has a few functions available to get temperature in both celcius and farenheit along with the humidity in percent. See below for the pinout connections to get in hooked up to your device. I developed this on a Raspberry Pi using python3, so unsure if wit will work on other devices.
## Pinout
![https://i1.wp.com/www.esp32learning.com/wp-content/uploads/2018/01/am2320-2.jpg?resize=620%2C427](https://i1.wp.com/www.esp32learning.com/wp-content/uploads/2018/01/am2320-2.jpg?resize=620%2C427)
## Usage
### Dependencies
- smbus2
```bash
pip3 install smbus2
```
### Example
```python3
#!/usr/bin/env python3

from AM2320 import AM2320

if __name__ == '__main__':
	am2320 = AM2320(1)
	print("Temperature: {}°C".format(am2320.getTempC()))
	print("Temperature: {}°F".format(am2320.getTempF()))
	print("Humidity: {}%".format(am2320.getHumidity()))
```
### Functions
#### getTempC
Returns the temperature of from the device in celcius.
#### getTempF
Returns the temperature from the device in farenheit. This isn't directly from the sensor but a calculation made on the getTempC function.
#### getHumidity
Returns the humidity in percentage.
#### wakeUp
Useful function if you want to wake up the sensor as it falls asleep sometimes.
