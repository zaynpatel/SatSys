"""transmitter
"""

class Transmitter:
    def __init__(self, tx_feeder_loss=1.0, efficiency=0.65, frequency=10e6):
        """
        Initializes the transmitter object (radio and other electronics that connect to the antenna).

        :param tx_feeder_loss: Loss that occurs on the feed line to the transmitter
        :type tx_feeder_loss: float
        :param efficiency: Power-to-radio efficiency (determines how efficiently physical energy is converted to electrical signals)
        :type efficiency: float
        :param frequency: Radio frequency of the transmitter in Hz
        :type frequency: float
        """
        self.tx_feeder_loss = tx_feeder_loss
        self.efficiency = efficiency
        self.frequency = frequency
