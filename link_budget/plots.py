from matplotlib import pyplot as plt
import numpy as np

from link_budget.src.antenna import Antenna
from link_budget.src.chain import TransmitChain
from link_budget.src.transmitter import Transmitter
from link_budget.src.satellite import Satellite

def plot_fspl(elevation_angle_start: int, elevation_angle_stop: int):
    """
    Plots free space path loss for a given range of elevation angles
    """
    path_losses = []

    satellite = Satellite(altitude=658)
    transmitter = Transmitter(frequency=19e9)
    for angle in range(elevation_angle_stop + 1):
        antenna = Antenna(angle_of_elevation=angle)  # I do not like having to call an instance each time
        tc = TransmitChain(antenna=antenna, transmitter=transmitter, satellite=satellite)
        pl = tc.calculate_path_length()
        fspl = tc.calculate_path_loss(pl)
        path_losses.append(fspl)
    
    x = np.arange(elevation_angle_start, elevation_angle_stop + 1)
    plt.xlabel("Elevation angle (degrees)")
    plt.ylabel("Free space path loss (dB)")
    plt.title("FSPL as a function of elevation angle")
    plt.plot(x, path_losses)
    plt.show()

plot_fspl(0, 90)
