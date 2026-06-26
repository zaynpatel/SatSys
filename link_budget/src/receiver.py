"""receiver
"""
from link_budget.src.radio import Radio

class Receiver(Radio):
    def __init__(self, feeder_loss: float, efficiency: float, frequency: float, noise_figure: float):
        """
        Initializes the receiver object (radio and other electronics that connect to the antenna).

        :param feeder_loss: Loss that occurs on the feed line to the transmitter
        :type feeder_loss: float
        :param efficiency: Power-to-radio efficiency (determines how efficiently physical energy is converted to electrical signals)
        :type efficiency: float
        :param frequency: Radio frequency of the transmitter in Hz
        :type frequency: float
        :param noise_figure: Ratio of the total available power at the output to the noise of an ideal receiver
        :type noise_figure: float
        """
        super().init__(feeder_loss, efficiency, frequency, noise_figure)
