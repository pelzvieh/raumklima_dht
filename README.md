# Raumklima_DHT

This is a extremely simple daemon that reads temperature and humidity from a DHT22 sensor using
the dht11 kernel module. It writes the readings in a json file. This is intended to be referred from a
web server, providing a poor man's temperature/humidity API.

# Setup

It is required to set up the dht11 module by configuring it as dtoverlay. This would be achieved
by adding the following setting to /boot/config.txt in the example if the sensor
is connected to GPIO 4
````
dtoverlay=dht11,gpiopin=4
````

# Incomplete

Caution, this is unfinished work! Scripts to compile and install are merely blank templates. Feel free to contribute!

