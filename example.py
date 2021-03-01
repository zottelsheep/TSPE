# Example script for the usage of TSPE

import scipy.io as sio
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import TSPE

# Load Spiketrain. Simplify cells is used to make the format workable
data = sio.loadmat("ExampleSpikeTrain.mat", simplify_cells=True)['data']

# Simulation up to one hour
rec_dur_ms = 60*1000*30     # Recording duration for connectivity estimation
plot_dur_ms = 10*1000       # Duration for raster plot

# Shortening Data to Recording-duration

for i in range(data['NumEL_rec']):
    data['asdf'][i] = data['asdf'][i][data['asdf'][i] < rec_dur_ms]

# Last Cell contains information of the number of recorded neurons and the recording duration
data['asdf'][-1] = [data['NumEL_rec'], rec_dur_ms]

# Plot Spiketrain

# Setting Plot Backend (qt5aag -> qt required, if not installed use tkagg)
matplotlib.use('qt5agg')

for i in range(data['NumEL_rec']):
    data_plot = data['asdf'][i][data['asdf'][i] < plot_dur_ms]/data['SaRa_Hz']
    plt.plot(data_plot, i*np.ones(len(data_plot), dtype=int), 'ko', markersize=1)

plt.xlabel('Time in s')
plt.ylabel('Index of neuron')
plt.title('SpikeTrains of simulation')
plt.show()






