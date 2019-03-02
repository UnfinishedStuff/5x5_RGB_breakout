#!/usr/bin/python3

import os, fcntl, time

#Setup the i2c bus
address = 0x74
slave = 0x0703
fd = os.open("/dev/i2c-1", os.O_RDWR)
fcntl.ioctl(fd, slave, address)

#Set the shutdown register 0x0A to 1
def turn_on():
  #point to the function register
	os.write(fd, b'\xfd\x0b')
	#Set the shutdown reg to 0x01
	os.write(fd, b'\x0a\x01')

#Set the shutdown register 0x0A to 0
def turn_off():
	#point to the function register
	os.write(fd, b'\xfd\x0b')
	#Set the shutdown reg to 0x00
	os.write(fd, b'\x0a\x00')

#Read a register
def read_reg(page, register, numbytes ):
	#Send the configure command 0xFD, point the chip to the desired page
	os.write(fd, bytearray([0xFD, page]))
	#Point the chip to the desired register to read from
	os.write(fd, bytearray([register]))
	#Ask to read "numbytes" number of bytes
	rec = os.read(fd, numbytes)
	#Return the read bytes
	return(rec)

#Transfer an array of bytes to the device
def write_reg(page, register, byte):
	#Send the configure command 0xFD and the desired page
	os.write(fd, bytearray([0xFD, page]))
	#Point the chip to the desired register and write the byte(s)
	os.write(fd, bytearray([register] + byte))

#Set all of the LEDs to ON
def fill_page(page):
	for x in range (0,18):
		write_reg(page, x, [0xff])


def min_brightness(page):
	for x in range (0x24,0xb4):
		write_reg(page, x, [0x00])


outputBuffer = [0]*144
leds = [[118,69,85], [117,68,101], [116,84,100], [115,83,99], [114,82,98],
	[132,19,35], [133,20,36], [134,21,37], [112,80,96], [113,81,97],
	[131,18,34], [130,17,50], [129,33,49], [128, 32, 48], [127,47,63],
	[125,28,44], [124,27,43], [123,26,42], [122, 25, 58], [121, 41, 57],
	[126,29,45], [15,95,111], [8,89,105], [9,90,106], [10,91,107]]

def set_pixel(pixel, r, g, b, outputBuffer=outputBuffer, leds=leds):
	outputBuffer[leds[pixel][0]] = r
	outputBuffer[leds[pixel][1]] = g
	outputBuffer[leds[pixel][2]] = b

def show(outputBuffer=outputBuffer):
	write_reg(0x00,0x24,outputBuffer)

try:

	#############
	#Boilerplate#
	#############

	#All LEDs set to ON
	#All brightnesses set to ZERO


	turn_on()
	#Set to picture display mode
	write_reg(0x0b, 0x00, [0x00])
	#Set picture display to frame 1
	write_reg(0x0b, 0x01, [0x00])
	#Turn all LEDs of Page 1 to ON
	fill_page(0x00)
	#Turn all LEDs of Page 1 to 0 brightness
	min_brightness(0x00)



	#############
	#Actual code#
	#############





except KeyboardInterrupt:
	turn_off()
