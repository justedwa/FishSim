"""
This file defines the base class upon which all fish types will be created
"""
#System Imports
from abc import ABC, abstractmethod
#Local Imports
#3rd Party Imports

"""
Abstract Fish class shows implementation of all derived classes
Used to create new types of fish subclasses
"""

class fish(object):

    def __init__(self,name):
        pass

    def __str__(self):
        print(self.name)
#Getters and Setters
    def GetAmmOutput(self):
        pass

    def GetHunger(self):
        pass

    def GetMood(self):
        pass

    def GetAge(self):
        pass

    def GetHealth(self):
        pass

    def GetAggressionLevel(self):
        pass

    def SetAmmOutput(self):
        pass

    def SetHunger(self):
        pass

    def SetMood(self):
        pass

    def SetAge(self):
        pass

    def SetHealth(self):
        pass
