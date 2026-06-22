"""antenna
"""
import math

from link_budget import constants

class Antenna:
    def __init__(self, gain=None, diameter=None, pointing_error=None, polarization="RHCP"):
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
        """
        self.gain = gain
        self.diameter = diameter
        self.pointing_error = pointing_error
        self.polarization = polarization
        self.polarization_loss = 0.2

    def calculate_beamwidth(self, frequency: float, ndigits=2):
        """
        A beam is a concentration of radio waves. We characterize these as "narrow beam" (directionally concentrated in one direction)
        and "wide beam" (directionally concentrated over a wider area).

        Gain, another important RF parameter, is a way to quantify how well a beam is directing power in desired direction.
        The gain of an antenna is not the same in every direction and the beamwidth is an important metric to determine
        the concentration of a beam. Beamwidth is the angle between peak gain and a decrease in gain.

        The symbolic formula for beamwidth is k * (λ / d) where λ is wavelength, d is the antenna diameter, and k is a scaling coefficient.
        It is an industry standard to use k = 70 which is what this implementation uses.

        :param frequency: Radio frequency of the transmitter in Hz
        :type frequency: `Transmitter`
        :param ndigits: Number of digits to round
        :type ndigits: int
        :return: Beamwidth of an antenna in *degrees*
        :rtype: float
        """
        return round(70 * (constants.SPEED_OF_LIGHT / (frequency * self.diameter)), ndigits)
    
    def calculate_gain(self, efficiency: float, frequency: float, linear=False, ndigits=1):
        """
        For a given antenna, power is not transmitted equally in all directions. 
        To measure the effectiveness of power transmission and reception we define gain.

        Gain is a ratio: antenna power emitted in one direction / theoretical power emitted by an isotropic antenna.
        Max gain is written, symbolically as:

        G_max = (4π / λ^2) * A_eff OR G_max = A_eff / (λ^2 / 4π)

        :param efficiency: Power-to-radio efficiency of the antenna
        :type efficiency: float
        :param frequency: Frequency of the transmitter
        :type frequency: `Transmitter`
        :param linear: If the output is preferred in decibels or not
        :type linear: bool
        :return: Max gain in dB for an antenna with circular aperture
        :rtype: float
        """
        max_gain = efficiency * (((math.pi * self.diameter) / (constants.SPEED_OF_LIGHT / frequency)) ** 2)
        if not linear:
            db_conversion = round(10 * math.log(max_gain, 10), ndigits)
            return db_conversion
        return max_gain

    def calculate_pointing_loss(self, frequency: float, ndigits=2):
        """
        Pointing loss is the drop in signal power due to misalignment between the transmitter and receiver.

        It is calculated by a ratio between the pointing error and the 3 dB beamwidth.

        :param frequency: Frequency of the transmitter
        :type frequency: float
        :return: Pointing loss in dB
        :rtype: float
        """
        pointing_ratio = (self.pointing_error / self.calculate_beamwidth(frequency)) ** 2
        return round(10 * math.log(12 * pointing_ratio, 10), ndigits)

    def antenna_polarization(self):
        """
        #TODO: Implement after receiver
        """
        pass
