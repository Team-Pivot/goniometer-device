# goniometer-device
This is the frontend of a full stack application that enables goniometer functionality using a rasbperry pi 3, encoder, and touchscreen.
## Raspberry Pi Setup
If using a brand new device, refer to the official raspberry pi website for setup instructions: https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up

Make sure to use the Raspbian OS instead of NOOBS or this may cause ssh connection issues later.

### Reformatting the microSD
In the case where an old pi is being used, there is a chance that the files on the microSD card may be corrupt. In this case, the microSD will have to be formatted. Follow the instructions on this page: https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/2

Note that a microSD to SD adapter may be needed to connect the microSD to your computer.

### Installing Raspbian OS
Once the Raspbian archive file has been downloaded, extract the disk image file to your computer (not to the microSD).

Flashing this disk image will differ based on your computer's OS. This website covers macOS & Windows: https://howchoo.com/g/ywmxmza2ndf/raspbian-buster-install-or-upgrade

Do not remove the microSD before enabling ssh.

### Enabling SSH
It would be more convenient to access the pi from a computer rather than connecting a separate keyboard, mouse, and monitor directly to it. To access it from your computer, ssh will be used. Put simply, ssh allows for remotely access another computer from your own.

To enable ssh on the pi, navigate to the root (highest level) directory of the microSD and create an empty file called ssh.

Make sure that the type of this file is not 'text' but instead 'file'.

To do this, edit the file name and delete the .text part. On Windows, you should get a warning saying changing the file extension may make the file unusable. Click 'yes'.

At this point, you can remove the microSD.

PuTTY is a program that makes using ssh easier. Install it from here: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

## Connecting the Sensors
Once the raspberry pi is running, the next step is to connect the touchscreen and the encoder.

### Touchscreen
The touchscreen being used is a 3.5" LCD display: https://www.adafruit.com/product/2097

The pins on the display correspond to the pins on the raspberry pi. It's worth noting that not all pins connected are being used.

Connecting the screen using wires as opposed to snapping it on will allow extra pins on the pi for the encoder to be connected.

The "Interface" section of the following wiki provides all the relevant pins to connect the touchscreen using wires: http://www.lcdwiki.com/3.5inch_RPi_Display

The wiki also has a section for driver installation.

### Encoder
We used an encoder as the sensor to detect rotation and interpret angle. We used software to convert these values in context of an extension/flexion.

We used this encoder: https://www.ebay.com/itm/2-x-Digital-Rotary-Encoder-Module-for-Arduino-Raspberry-Pi-etc-/391771177795?_trksid=p2385738.m4383.l4275.c10

To minimize cost, we opted for an encoder with 24 detents (clicks) instead of a fully continuous encoder. We believe this is appropriate as the product is in a prototype state.

Follow this tutorial to setup the encoder: https://thepihut.com/blogs/raspberry-pi-tutorials/how-to-use-a-rotary-encoder-with-the-raspberry-pi

## Running the App
This project uses a python UI library known as PyQt 5. Install it with the command: `sudo apt-get install python3-pyqt5`

Once the pi and sensors are setup, clone this project and navigate to the root directory. 

This project requires Python 3 to run. To run the application, use the terminal command `python3 main.py`
