from link_budget.src.antenna import Antenna
from link_budget.src.chain import TransmitChain
from link_budget.src.transmitter import Transmitter
from link_budget.src.satellite import Satellite

def test_calculate_path_length():
    antenna = Antenna(angle_of_elevation=50)
    satellite = Satellite(altitude=35786)
    transmitter = Transmitter()
    tc = TransmitChain(antenna=antenna, transmitter=transmitter, satellite=satellite)
    assert tc.calculate_path_length() == 37078.38

def test_calculate_propagation_loss():
    antenna = Antenna(angle_of_elevation=50)
    transmitter = Transmitter(frequency=12e9)
    satellite = Satellite(altitude=35786)
    tc = TransmitChain(antenna=antenna, transmitter=transmitter, satellite=satellite)
    path_length = tc.calculate_path_length()
    fspl = tc.calculate_path_loss(path_length)  # direct line-of-sight connection
    loss = fspl + 1.5
    assert loss == 206.91

def test_eirp():
    antenna = Antenna(diameter=4, pointing_error=0.5, angle_of_elevation=0.0)
    transmitter = Transmitter(tx_feeder_loss=3, efficiency=0.65)
    satellite = Satellite(altitude=35786)
    tc = TransmitChain(antenna, transmitter, satellite)
    assert tc.calculate_eirp() == 54.63
