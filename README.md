# 5x5_RGB_breakout

This is a home-made library for the Pimoroni 5x5 RGB breakout.  I really just wanted to write one myself for the challenge.

Current state:  roughly functional, but needs documentation and additional functions.




This library works by setting all LEDs to "on" and then modulating the brightness of those LEDs with the PWM function.  To turn the LED "off" it simply sets the PWM brightness to 0.  

# Registers `0x00` to `0x11`: Turning the LEDs on and off

Registers `0x00` to `0x11` control whether each LED is on or off.  Each register holds one byte, and each bit of that byte corresponds to a single LED.  If that bit is set to `0` the LED is off, if it is set to `1` the LED is on.  So, each byte controls 8 LEDs, and the IS31FL3731 chip theoretically controls 144 LEDs, so there are 144/8=18 registers which control this (`0x00` to `0x11`).  Because this library controls brightness using PWM, all of these are set to on (every bit is set to `1`).

# Registers `0x24` to `0xB3`: Setting individual LED brightness with PWM

Every LED has 8-bit PWM brightness, where the higher the value the brighter the LED.  That gives "off" and 255 levels of brightness.  Because each LED has a separate brightness setting and the IS31FL3731 can control 144 LEDs, there are 144 registers storing this data, where each register corresponds to a single LED.  

Pimoroni have set their 5x5 breakout up so that the RGB LEDs are treated as three separate LEDs, with a separate PWM value for each colour.  Unfortunately they're not set up in a logical order (I'm assuming this was required to make the PCB traces easier to organise), so the PWM values for LED1 R, G and B are all over the PWM registers.  The table below represents the breakout, with a cell for each LED on the breakout.  Each cell contains three values corresponding to R, G and B.  The values correspond to where in the 144 bytes of data the PWM value for that colour of that LED is stored.  E.g., the bottom right cell contains the values for the bottom right-most LED on the breakout.  The values, `10,91,107`, mean that the R brightness for that LED is stored in register 10, G in register 91 and B in register 107.  Bear in mind these are numbered 0-143, so if you want to write these to the chip you would need to start writing these to register `0x24`.

|        | Column1 | Column 2 | Column 3 | Column 4 | Column 5
|--------|----------|----------|----------|---------|--------
|Row 1 | 118/69/85|117/68/101|116/84/100|115/83/99|114/82/98
|Row 2 | 132/19/35|133/20/36|134/21/37|112/80/96|113/81/97
|Row 3 | 131/18/34|130/17/50|129/33/49|128/32/48|127/47/63
|Row 4 | 125/28/44|124/27/43|123/26/42|122/25/58|121/41/57
|Row 5 | 126/29/45|15/95/111|8/89/105|9/90/106|10/91/107




