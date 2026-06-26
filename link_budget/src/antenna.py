from abc import ABC, abstractmethod

from link_budget import helpers

class Antenna(ABC):
    def __init__(self, angle_of_elevation, diameter: float, pointing_error: float, sensitivity, mode: str, polarization="RHCP"):
        """
        Initializes the antenna object
        
        :param gain: Gain of the antenna
        :type gain: float
        :param diameter: Diameter of the antenna
        :type diameter: float
        :param pointing_error: Error between antenna pointing and satellite object
        :type pointing_error: float
        :param polarization: Describes the direction of an electric field of a wave
        :type polarization: str
        :param angle_of_elevation: Angle of elevation that the antenna sees the satellite above the horizon (in degrees)
        :type angle_of_elevation: float
        """
        self.angle_of_elevation = helpers.convert_degrees_to_radians(angle_of_elevation)
        self.diameter = diameter
        self.pointing_error = pointing_error
        self.sensitivity = sensitivity
        self.mode = mode
        self.polarization = polarization
        self.polarization_loss = 0.2

    @abstractmethod
    def calculate_beamwidth(self, frequency: float, ndigits=2):
        pass

    @abstractmethod
    def calculate_gain(self, efficiency: float, frequency: float, ndigits=1):
        pass

    @abstractmethod
    def calculate_pointing_loss(self, frequency: float, ndigits=2):
        pass

    @abstractmethod
    def antenna_polarization(self):
        pass
