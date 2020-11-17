# coffee-sensor-client

Python client for reading temperature controller for Lelit MaraX via a USB to Serial adapter. This client sends real time sensor data to InfluxDB via HTTP, and updates a TFT attached to the Raspberry Pi to show current stats.

## InfluxDB

## Display

This project assumes you're using an Adafruit Mini PiTFT - 135x240 Color TFT Add-on for Raspberry Pi (https://www.adafruit.com/product/4393).

### Setup

1. Follow the https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi to setup SPI, I2C, and required Python modules for running the display.
