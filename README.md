# Raspberry Pi Bomb Defusal
A real life implementation of the popular game **Keep Talking and Nobody Explodes**

This project is built in Python 3.7.

Fritzing wiring diagrams are included in the /diagrams directory. 

Manual pages for the Expert are in the /manual directory.

## Getting started
In order to run the program, some dependencies will need to be installed.
### For the 7-segment display
`sudo apt-get update`

`sudo apt-get install -y git build-essential python-dev python-smbus python-imaging python-pip python-pil`

`git clone https://github.com/adafruit/Adafruit_Python_LED_Backpack.git`

`cd Adafruit_Python_LED_Backpack`

`sudo python setup.py install`

### For the keypad
`sudo pip3 install adafruit-circuitpython-matrixkeypad`

