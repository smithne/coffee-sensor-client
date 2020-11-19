# coffee-sensor-client

Python client for reading temperature controller for Lelit MaraX via a USB to Serial adapter. This client sends real time sensor data to InfluxDB via HTTP, and updates a TFT attached to the Raspberry Pi to show current stats.

## InfluxDB

## Display

This project assumes you're using an Adafruit Mini PiTFT - 135x240 Color TFT Add-on for Raspberry Pi (https://www.adafruit.com/product/4393).

### Setup

Adapted from https://learn.adafruit.com/adafruit-mini-pitft-135x240-color-tft-add-on-for-raspberry-pi/python-setup:

1. Follow the https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi to setup SPI, I2C, and required Python modules for running the display.
1. Add Python RGB display libraries:
    1. ```sudo pip3 install adafruit-circuitpython-rgb-display```
    1. ```sudo pip3 install --upgrade --force-reinstall spidev```
1. Install DejaVu TTF Font: ```sudo apt-get install ttf-dejavu```
1. Install Python Imaging Library: ```sudo apt-get install python3-pil```
1. Install NumPy (which is used for some RGB_Display library optimizations): ```sudo apt-get install python3-numpy```
