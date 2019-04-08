######################################################
#           Project: RaspPi Bomb Defusal             #
# Names: Alex Anderson, Shawn Chauvin, Karey Higuera #
# Description: A real life implementation of KTANE   #
#       (Keep Talking and Nobody Explodes)           #
######################################################
import time
import datetime

from Adafruit_LED_Backpack import SevenSegment
######################################################
segment = SevenSegment.SevenSegment(address=0x70)

# Initialize the display. Must be called once before using the display.
segment.begin()

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

    def win(self):
        print ("You win!")

#Abstract Module class. All sub-modules extend this.
class Module(object):

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
        segment.set_colon(seconds % 2)              # Toggle colon every second
    else:
        segment.set_colon(int(hundSecs) > 50)              # Toggle colon every half second

    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    segment.write_display()

def playGame():
    while(True):
        #this is the time right now
        currentTime = datetime.datetime.now()
        #this is the total number of seconds that have gone by
        timeDiff = (currentTime - bomb.startTime).total_seconds()
        #this is the time left
        timeLeft = bomb.timer - timeDiff
        
        if(timeLeft <= 0):
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

            writeToClock(minutes, seconds, hundSecs)

            time.sleep(0.2)

##SAMPLE CODE##
bomb = Bomb(60)

bomb.startBomb()