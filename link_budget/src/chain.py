"""chain
"""
from link_budget.src.antenna import Antenna
from link_budget.src.transmitter import Transmitter
from link_budget import helpers


class TransmitChain:
    def __init__(self, antenna: Antenna, transmitter: Transmitter):
        self.antenna = antenna
        self.transmitter = transmitter
    
    def raw_rf_power(self, output_metric="dbW"):
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
        eirp = self.calculate_eirp()
        if output_metric == "W":
            return helpers.power_ratio((eirp - self.antenna.gain) + self.transmitter.tx_feeder_loss)
        elif output_metric == "dBm":
            return 30 + (eirp - self.antenna.gain) + self.transmitter.tx_feeder_loss
        return (eirp - self.antenna.gain) + self.transmitter.tx_feeder_loss
    
    def calculate_eirp(self):
        """
        Effective Radiative Isotropic Power (EIRP) measures the power that could effectively reach the receiver.
        
        :return: EIRP
        :rtype: float
        """
        raw_transmit_power = 52.2
        transmitter_gain = self.antenna.calculate_gain(self.transmitter.efficiency, self.transmitter.frequency, linear=True)
        print(f"THis is transmit gain: {transmitter_gain}")
        pointing_loss = self.antenna.calculate_pointing_loss(self.transmitter.frequency)
        return raw_transmit_power + transmitter_gain - pointing_loss - self.antenna.polarization_loss - self.transmitter.tx_feeder_loss
