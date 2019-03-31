#####################################################
# Name: Alex Anderson, Shawn Chauvin, Karey Higuera #
# Description: A real life implementation of KTANE  #
#       (Keep Talking and Nobody Explodes)          #
#####################################################

#Base class for the bomb. This will handle all major game functions.
class Bomb(object):
    def __init__(self, timer=60):
        self.timer = timer
        self.strikes = 0

    @property
    def timer(self):
        return self._timer

    @property
    def strikes(self):
        return self._strikes

    @timer.setter
    def timer(self, time):
        self._timer = time

    @strikes.setter
    def strikes(self, strikes):
        self._strikes = strikes
        #if the bomb has reached 3 strikes, game over
        if (self._strikes >= 3):
            self.explode()

    def explode(self):
        print "BOOM!"

#Abstract module class. All sub-modules extend this.
class Module(object):
    def __init__(self):
        pass

    #add a strike to the main bomb instance
    def strike(self, bomb):
        bomb.strikes += 1