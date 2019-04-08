######################################################
#           Project: RaspPi Bomb Defusal             #
# Names: Alex Anderson, Shawn Chauvin, Karey Higuera #
# Description: A real life implementation of KTANE   #
#       (Keep Talking and Nobody Explodes)           #
######################################################
"""Whether or not running on a raspberryPi, if false
    will disable the Pi specific functionality for testing"""
raspberryPi = False

import time
import datetime
import abc

from Adafruit_LED_Backpack import SevenSegment
######################################################

if raspberryPi:
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
        #if the bomb has reached 3 strikes, game over
        if (self._strikes >= 3):
            self.explode()

    @modules.setter
    def modules(self, modules):
        self._modules = modules
        #if all the modules are solved, finish the game
        if self._modules == [1,1,1]:
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

#Abstract Module class. All sub-modules extend this.
class Module(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, modNumber, bomb):
        #This modNumber is the spot in the Bomb modules array that marks whether this module is complete or not.
        self.modNumber = modNumber
        #This is a reference to the main bomb instance, the owner of this module
        self.bomb = bomb

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

    #let the bomb know that this module is complete
    def solve(self):
        self.bomb.moduleComplete(self.modNumber)

    #abstract method to determine if a module is complete
    #each module type will need to define this
    @abc.abstractmethod
    def checkModule(self):
        """This determines the solved state of a module"""

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
    bomb = Bomb(15)
    module1 = Module(1, bomb)
    module2 = Module(2, bomb)
    module3 = Module(3, bomb)

#runs the gameplay
#this is triggered by the "Start" button
def playGame():
    while(True):
        ###TIMER###
        #this is the time right now
        currentTime = datetime.datetime.now()
        #this is the total number of seconds that have gone by
        timeDiff = (currentTime - bomb.startTime).total_seconds()
        #this is the time left
        timeLeft = bomb.timer - timeDiff
        
        if(timeLeft <= 0):
            if raspberryPi:
                writeToClock(0,0,0)
            bomb.explode()

        else:
            #split up the time left
            minutes = int(timeLeft/60)
            seconds = int(timeLeft/1)
            #get just the microseconds, round to two places, strip off the 
            #leading zero and the decimal point
            hundSecs = str(round(timeLeft%1, 2))[2:4]
            print("time left: {}:{}:{}".format(minutes, seconds, hundSecs))

            if raspberryPi:
                writeToClock(minutes, seconds, hundSecs)

        ###MODULES###
        #check the state of each module

        time.sleep(0.05)


gameSetup()

bomb.startBomb()