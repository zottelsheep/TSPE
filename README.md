# TSPE Python Conversion

This project aims to convert the TSPE Algorithm to Python in order to include it into the [Python Elephant Project](https://neuralensemble.org/elephant/)

## Challenges

### Data format

Currently, the algorithm reads data as a time series in Spike Data Format (SDF). Since the aim of the project is to be included within the Elephant Project, the format has to change to [Neo](https://neuralensemble.org/neo/) Data-structures. 

#### SDF

The SDF-Format describes a spike-train with multiple vectors where each vector represents a spike-time-series from one neuron.

### Code-Optimization

The original TSPE-Algorithm was written in MATLAB and uses a self implemented Fast-Cross-Correlation Algorithm as well as some other steps to optimize the code for speed.

For now the goal is to get it working in Python and then to think about code-optimization.

# TSPE

Total Spiking Probability Edges is a Cross-Correlation based method for eﬀective connectivity estimation of cortical spiking neurons.

## Background:
Connectivity is a relevant parameter for the information flow within neuronal networks. Network connectivity can be
reconstructed from recorded spike train data. Various methods have been developed to estimate connectivity from spike
trains.
## New method:
In this work, a novel effective connectivity estimation algorithm called Total Spiking Probability Edges (TSPE) is
proposed and evaluated. First, a cross-correlation between pairs of spike trains is calculated. Second, to distinguish
between excitatory and inhibitory connections, edge filters are applied on the resulting cross-correlogram.
## Results:
TSPE was evaluated with large scale in silico networks and enables almost perfect reconstructions (true positive rate of
approx. 99% at a false positive rate of 1% for low density random networks) depending on the network topology and the
spike train duration. A distinction between excitatory and inhibitory connections was possible. TSPE is computational
eﬀective and takes less than three minutes on a high-performance computer to estimate the connectivity of an one hour
dataset of 1000 spike trains.
