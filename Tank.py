"""
Defines Abstract Class from which tanks are derived

"""
#System Imports
from abc import ABC, abstractmethod
#Local Imports
#3rd Party Imports

class Tank(ABC):

    def __init__(self,x,y,z):
        self.Volume = x * y * z
        self.Filtration = []
        self.BacteriaCount = 0
        self.FishList = []
        self.PlantList = []
        self.Substrate = "Glass"
        self.DecoList = []
        self.AmmPPM = 0
        self.NO2PPM = 0
        self.NO3PPM = 0
        self.Particulate = 0
        self.Temperature = None
        self.Heater = None
        self.PH = None
        self.Hardness = None
        self.CO2PPM = 0
    def
