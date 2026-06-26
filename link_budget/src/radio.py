"""radio
"""

class Radio:
    def __init__(self, feeder_loss: float, efficiency: float, frequency: float, noise_figure: float):
        """
        High-level class for radio transmitter and receiver
        """
        self.feeder_loss = feeder_loss
        self.efficiency = efficiency
        self.frequency = frequency
        self.noise_figure = noise_figure
