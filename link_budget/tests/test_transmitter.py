from link_budget.src.antenna import Antenna
from link_budget.src.chain import TransmitChain
from link_budget.src.transmitter import Transmitter


def test_max_gain():
    transmitter = Transmitter(feeder_loss=0, efficiency=0.65, frequency=12e9, noise_figure=0)
    antenna = Antenna(diameter=4)
    assert antenna.calculate_gain(transmitter.efficiency, transmitter.frequency) == 52.2

def test_calculate_beamwidth():
    transmitter = Transmitter(feeder_loss=0, efficiency=0.65, frequency=12e9, noise_figure=0)
    antenna = Antenna(diameter=4)
    assert antenna.calculate_beamwidth(transmitter.frequency) == 0.44

def test_calculate_pointing_loss():
    transmitter = Transmitter(feeder_loss=0, efficiency=0, frequency=12e9, noise_figure=0)
    antenna = Antenna(pointing_error=0.10, diameter=4)
    assert antenna.calculate_pointing_loss(transmitter.frequency) == -2.08
