######################################################
#           Project: RaspPi Bomb Defusal             #
# Names: Alex Anderson, Shawn Chauvin, Karey Higuera #
# Description: A real life implementation of KTANE   #
#       (Keep Talking and Nobody Explodes)           #
######################################################
"""Whether or not running on a raspberryPi, if false
    will disable the Pi specific functionality for testing"""
raspberryPi = False

#Abstraction
import abc
#GPIO
import RPi.GPIO as GPIO
#Keypad
import digitalio
import board
import adafruit_matrixkeypad
#Timer
import time
import datetime
from Adafruit_LED_Backpack import SevenSegment
######################################################
#the pins used for the Cut The Wires module
wirePin1 = 4
wirePin2 = 5
wirePin3 = 6

#create 3 basic wires for default mission setting
wire1 = {'pin': wirePin1}
wire2 = {'pin': wirePin2}
wire3 = {'pin': wirePin3}

#the basic wire setup for Cut The Wires
defaultWireConfig = {
    'wire1' : wire1,
    'wire2' : wire2,
    'wire3' : wire3,
    'wiresToSolve' : [wire1],
    'wiresToLeave' : [wire2, wire3]
}
secondWireConfig = {
    'wire1' : wire1,
    'wire2' : wire2,
    'wire3' : wire3,
    'wiresToSolve' : [wire2, wire3],
    'wiresToLeave' : [wire1]
}

if raspberryPi:
    #Setup for the keypad
    cols = [digitalio.DigitalInOut(x) for x in (board.D18, board.D19, board.D20)]
    rows = [digitalio.DigitalInOut(x) for x in (board.D21, board.D22, board.D23, board.D24)]
    keys = ((1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            ('*', 0, '#'))

    keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

#basic object for keypad module
defaultKeypadConfig = {
    'word' : "HELLO",
    "hint" : "YORE",
    'sequence' : "43556"
}

if raspberryPi:
    # use the broadcom pin layout
    GPIO.setmode(GPIO.BCM) 
    #set wire pins to pulldown inputs
    GPIO.setup(wirePin1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(wirePin2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(wirePin3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    segment = SevenSegment.SevenSegment(address=0x70)

    # Initialize the display. Must be called once before using the display.
    segment.begin()

#the bomb container for all games
bomb = None
#the modules containers for all games
module1 = None
module2 = None
module3 = None

#############
###CLASSES###
#############

#Base class for the bomb. This will handle all major game functions.
class Bomb(object):
    def __init__(self, timer=60):
        self.timer = timer
        self.strikes = 0
        self.modules = [0,0,0]

    @property
    def timer(self):
        return self._timer

    @property
    def strikes(self):
        return self._strikes

    @property
    def modules(self):
        return self._modules

    @timer.setter
    def timer(self, time):
        self._timer = time

    @strikes.setter
    def strikes(self, strikes):
        self._strikes = strikes

        #change time allotted depending on # of strikes
        if (self.strikes == 1):
            self.timer = self.timer - 5
        elif (self.strikes == 2):
            self.timer = self.timer - 10
        
        #if the bomb has reached 3 strikes, game over
        if (self._strikes >= 3):
            self.explode()

    @modules.setter
    def modules(self, modules):
        self._modules = modules
        print("checking modules")
        print(self.modules)
        #if all the modules are solved, finish the game
        if self.modules == [1,1,1]:
            self.win()

    def startBomb(self):
        #stores the time that the bomb started 
        self.startTime = datetime.datetime.now()
        #start the game
        playGame()

    def moduleComplete(self, modNumber):
        #pull a copy of the list of module states
        updatedModules = self.modules
        #set the indicated module to complete
        updatedModules[modNumber] = 1
        #push this updated list to the Bomb
        self.modules = updatedModules

    def explode(self):
        print ("BOOM!")
        while(True):
            #TODO - Add tkinter updates here so that restart button works
            if raspberryPi:
            #flash the timer on and off
                segment.set_digit(0, 0)
                segment.set_digit(1, 0)
                segment.set_digit(2, 0)
                segment.set_digit(3, 0)
                segment.set_colon(True)
                segment.write_display()
                time.sleep(0.5)

                segment.clear()
                segment.write_display()
                time.sleep(0.5)

    def win(self):
        print ("You win!")
        #get the time left when module solved and split it
        timeLeft = getTimeLeft()
        minutes, seconds, hundSecs = splitTimeLeft(timeLeft)

        while(True):
            #TODO - Add tkinter updates here so that restart button works
            if raspberryPi:

                #flash the timer on and off with winning time
                writeToClock(minutes, seconds, hundSecs)
                time.sleep(0.5)

                segment.clear()
                segment.write_display()
                time.sleep(0.5)

#Abstract Module class. All sub-modules extend this.
class Module(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, modNumber):
        #This modNumber is the spot in the Bomb modules array that marks whether this module is complete or not.
        self.modNumber = modNumber
        #This is a reference to the main bomb instance, the owner of this module
        self.bomb = bomb
        #whether or not the module is solved
        self.solved = False

    @property
    def modNumber(self):
        return self._modNumber

    @property
    def bomb(self):
        return self._bomb

    @modNumber.setter
    def modNumber(self, modNumber):
        self._modNumber = modNumber

    @bomb.setter
    def bomb(self, bomb):
        self._bomb = bomb

    #add a strike to the main bomb instance
    def strike(self):
        self.bomb.strikes += 1
        print("got a strike!")

    #let the bomb know that this module is complete
    def solve(self):
        self.bomb.moduleComplete(self.modNumber)
        self.solved = True
        print("module solved!")

    #abstract method to determine if a module is complete
    #each module type will need to define this
    @abc.abstractmethod
    def checkModule(self):
        """This determines the solved state of a module"""

class CutTheWires(Module):
    def __init__(self, modNumber, wireConfig = defaultWireConfig):
        Module.__init__(self, modNumber)
        self.wire1 = wireConfig['wire1']
        self.wire2 = wireConfig['wire2']
        self.wire3 = wireConfig['wire3']
        self.wiresToSolve = wireConfig['wiresToSolve']
        self.wiresToLeave = wireConfig['wiresToLeave']


    def checkModule(self):
        ##BAD WIRES##
        for wire in self.wiresToLeave:
            # see if the wire is connected
                wireState = GPIO.input(wire['pin'])
                #if the wire has been cut
                if wireState == False:
                    # remove this wire from the list of wires to check
                    self.wiresToLeave.remove(wire)
                    #give a strike for cutting a bad wire
                    self.strike()

        ##GOOD WIRES##
        # check each wire that needs to be solved
        for wire in self.wiresToSolve:
            # see if the wire is connected
            wireState = GPIO.input(wire['pin'])
            #if the wire has been cut
            if wireState == False:
                # remove this wire from the list of wires to check
                self.wiresToSolve.remove(wire)

        #if module is unsolved
        if(not self.solved):
            # if all necessary wires have been cut, solve the module
            if self.wiresToSolve == []:
                self.solve()

class Keypad(Module):
    def __init__(self, modNumber, keypadConfig = defaultKeypadConfig):
        Module.__init__(self, modNumber)
        self.word = keypadConfig["word"]
        self.hint = keypadConfig["hint"]
        self.sequence = keypadConfig["sequence"]
        self.typedNumbers = ""
        self.lastPressed = None

    def checkModule(self):
        #this is the time gone by since last keypad read
        timeDiff = (datetime.datetime.now() - self.lastPressed).total_seconds()

        #ignore keypresses if module is solved and debounce 3/4 second
        if (raspberryPi and not self.solved and timeDiff > .75):
            #pull the currently pressed keys from the keypad (array)
            keys = keypad.pressed_keys

            #record the time the last keypress was recorded
            self.lastPressed = datetime.datetime.now()

            if(keys):
                print("Keys pressed: {}".format(keys))
                #store the number pressed
                self.typedNumbers += str(keys[0])
                print("Current sequence: {}".format(self.typedNumbers))

                #if the typed numbers is the max (5)
                if(len(self.typedNumbers) >= 5):
                    #check if typed numbers matches sequence
                    if(self.typedNumbers == self.sequence):
                        self.solve()
                    else:
                        #reset the typed numbers array
                        self.typedNumbers = ""
                        self.strike()


class BigButton(Module):
    def __init__(self, modNumber):
        Module.__init__(self, modNumber)

    def checkModule(self):
        pass

###################
###OTHER METHODS###
###################

#this method writes the remaining time to the screen
def writeToClock(minutes, seconds, hundSecs):
    segment.clear()    

    # show minutes and seconds on the clock
    if(minutes > 0):
        #set minutes
        segment.set_digit(0, int(minutes/10))
        segment.set_digit(1, minutes%10)
        #set seconds
        segment.set_digit(2, int(seconds / 10))
        segment.set_digit(3, seconds % 10)
        pass
    #show seconds and hundredths on the clock
    else:
        #set seconds
        segment.set_digit(0, int(seconds/10))
        segment.set_digit(1, seconds%10)
        #set hundredths
        segment.set_digit(2, int(int(hundSecs) / 10))
        segment.set_digit(3, int(hundSecs) % 10)
        pass

    # Toggle colon
    if(seconds > 10):
        segment.set_colon(seconds % 2)          # Toggle colon every second
    else:
        segment.set_colon(int(hundSecs) > 50)   # Toggle colon every half second

    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    segment.write_display()

#this method initializes the bomb
#this is triggered by "New Game" or "Try Again" button
''' this could be extended to support multiple levels/configs
    based on parameters passed in'''
def gameSetup():
    global bomb
    global module1, module2, module3
    bomb = Bomb(120)
    module1 = CutTheWires(0)
    module2 = Keypad(1)
    module3 = BigButton(2)

def getTimeLeft():
    #this is the time right now
    currentTime = datetime.datetime.now()
    #this is the total number of seconds that have gone by
    timeDiff = (currentTime - bomb.startTime).total_seconds()
    #this is the time left
    timeLeft = bomb.timer - timeDiff
    return timeLeft

def splitTimeLeft(timeLeft):
    #split up the time left
    minutes = int(timeLeft/60)
    timeLeft -= minutes*60
    seconds = int(timeLeft/1)
    #get just the microseconds, round to two places, strip off the 
    #leading zero and the decimal point
    hundSecs = str(round(timeLeft%1, 2))[2:4]
    return minutes, seconds, hundSecs

#runs the gameplay
#this is triggered by the "Start" button
def playGame():
    while(True):
        ###TIMER###
        timeLeft = getTimeLeft()
        #split up the time left
        minutes, seconds, hundSecs = splitTimeLeft(timeLeft)

        if(timeLeft <= 0):
            if raspberryPi:
                writeToClock(0,0,0)
            bomb.explode()

        else:
            print("time left: {}:{}:{}".format(minutes, seconds, hundSecs))

            if raspberryPi:
                writeToClock(minutes, seconds, hundSecs)

        ###MODULES###
        #check the state of each module
        module1.checkModule()
        module2.checkModule()

        time.sleep(0.05)


gameSetup()

bomb.startBomb()