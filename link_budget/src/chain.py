"""chain
"""
import math

from link_budget import constants, helpers
from link_budget.src.antenna import Antenna
from link_budget.src.transmitter import Transmitter
from link_budget.src.satellite import Satellite


class TransmitChain:
    def __init__(self, antenna: Antenna, transmitter: Transmitter, satellite: Satellite):
        self.antenna = antenna
        self.transmitter = transmitter
        self.satellite = satellite

    def raw_transmit_power(self, target_eirp: float, antenna_gain: float, output_metric="dbW"):
        """
        Effective Radiative Isotropic Power (EIRP) is the power output of a transmitter when sending a signal to the receiver.
        To calculate the raw power we need to subtract gain and add feeder loss.

        This function returns different output metrics (W, dbW, dBm) depending on the user's situation. 
        We can add dB that share the same scale (e.g. dB + dBi) but we cannot add two dB terms with different
        scales of the same unit. For example, we cannot add dBW to dBm.

        :param gain: Gain of the antenna
        :type gain: float
        :param tx_feeder_loss: Feeder loss between power amplifier and antenna
        :type tx_feeder_loss: float
        :param output_metric: Preferred dB scale (dB, dBW, dBm)
        :return: Raw rf power
        :rtype: float
        """
        if output_metric == "W":
            return helpers.power_ratio((target_eirp - antenna_gain) + self.transmitter.tx_feeder_loss)
        elif output_metric == "dBm":
            return 30 + (target_eirp - antenna_gain) + self.transmitter.tx_feeder_loss
        return (target_eirp - antenna_gain) + self.transmitter.tx_feeder_loss
    
    def calculate_eirp(self, ndigits=2):
        """
        Effective Radiative Isotropic Power (EIRP) measures the power that could effectively reach the receiver.

        Since the raw transmit power is computed using dBm but EIRP is typically reported in dBW, 30 dB is subtracted from
        the final answer.

        :return: EIRP in dBW
        :rtype: float
        """
        antenna_gain = self.antenna.calculate_gain(self.transmitter.efficiency, self.transmitter.frequency)
        raw_transmit_power = self.raw_transmit_power(target_eirp=5, antenna_gain=antenna_gain, output_metric="dBm")
        pointing_loss = self.antenna.calculate_pointing_loss(self.transmitter.frequency)
        return round((raw_transmit_power + antenna_gain - pointing_loss - self.antenna.polarization_loss - self.transmitter.tx_feeder_loss)  - 30, ndigits)

    def calculate_path_loss(self, R):
        """
        Calculates free space path loss (FSPL).

        The symbolic formula for path loss, in dB, is: 20 * log_10 (4πR / λ) where 4π is the steradians of a sphere, R is the distance between
        ground station and satellite, and λ is wavelength.

        :param R: Distance between ground station and satellite
        :type R: float
        :return: FSPL in dB
        :rtype: float
        """
        wavelength = constants.SPEED_OF_LIGHT / self.transmitter.frequency
        return round(20 * (math.log((4 * math.pi * R * 1000) / wavelength, 10)), 2)

    def calculate_path_length(self, ndigits=2) -> float:
        """
        Calculates the line-of-sight path length between a ground station and a satellite.
        """
        side_length_calculations = (constants.RADIUS_OF_EARTH ** 2) + ((constants.RADIUS_OF_EARTH + self.satellite.altitude) ** 2)
        sin_calculation = math.sin(self.antenna.angle_of_elevation + math.asin((constants.RADIUS_OF_EARTH / (constants.RADIUS_OF_EARTH + self.satellite.altitude)) * math.cos(self.antenna.angle_of_elevation)))
        return round(math.sqrt(side_length_calculations - (2 * constants.RADIUS_OF_EARTH * (constants.RADIUS_OF_EARTH + self.satellite.altitude) * sin_calculation)), ndigits)
