#Import modules

import scipy
import numpy

def TSPE(sdf, d = 25, neg_wins = [3, 4, 5, 6, 7, 8], co_wins = 0, pos_wins = [2, 3, 4, 5, 6], FLAG_NORM = 0):
    # Parameters:
    #   sdf         - Time series in Spike Data Format (SDF)
    #   d           - Maximal delay time (default 25)
    #   neg_wins    - Windows for before and after area of interest (default [3, 4, 5, 6, 7, 8])
    #   co_wins     - Cross-over window size (default 0)
    #   pos_wins    - Sizes of area of interest (default [2, 3, 4, 5, 6])
    #   FLAG_NORM   - 0 - no usage of normalization (default)
    #               - 1 - usage of normalization
    #
    # Returns:
    #   CMres       - NxN matrix where N(i, j) is the total spiking probability edges (TSPE) i->j
    #   DMres       - NxN matrix where N(i, j) is the transmission time with highest TSPE Value i->j
    #
    # Wrote by Stefano De Blasi, UAS Aschaffenburg in 2018 ported to Python by Felician Richter in 2021

    # Generation of Sparse Matrisies / Data Input Formating from SDF
    # !! For now only normal matrisies -> Could use SciPy



    pass


    


