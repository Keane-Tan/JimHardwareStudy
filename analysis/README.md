# Steps to Analyze the Files
1. Store the files in the `dataFiles/` directory.
2. Run the following to get the "raw" signal and trigger plots:
`python signalExploration.py -d [filename].root -r`
3. Look at the plots in `plots/rawSignals/[filename]/` and `plots/rawTriggers/[filename]/`. `Events_0-1000.png` and `Events_ZoomedIn_0-1000.png` are the more useful plots to look at. If you do not see any bumps in `Events_ZoomedIn_0-1000.png`, you should add a dictionary entry in `parameters.py`. The entry's key should be `[filename]`, You can copy the parameters from another dictionary entry, but make sure to change the 7th and 8th parameters to the appropriate values so that you can see the bumps in `Events_ZoomedIn_0-1000.png` for both the `rawSignals` and `rawTriggers`. To make this change correctly, refer to `Events_0-1000.png` and estimate where the bumps are. After you have updated these values, rerun step 2 to see if things are working correctly.
4. Based on `Events_ZoomedIn_0-1000.png` for `rawSignals` and `rawTriggers`, you should set the correct value for the 2nd parameter value in `parameters.py`.
5. Run the following to get the distribution of (max - min ADC in signal window)
`python signalExploration.py -d [filename].root -p`
6. Look at the plots in `plots/maxMinDiff/[filename]/`. Change the 0th and 1st parameters in `parameters.py` based on the plots.
7. Run the following to get a sense of how well the algorithm is finding the signal's edge:
`python signalExploration.py -d [filename].root -s`
8. Look at the plots in `plots/signalFit/[filename]/`. If the algorithm seems to be identifying the signal's edge reasonably well in each plots, then proceed to the next step. Otherwise, you can try varying some of the parameters in `parameters.py` to get a better result.
9. To get the time difference distribution, run
`python timeDifference.py -d [filename].root`
using all the events that pass the pedestal requirement or
`python timeDifference.py -d [filename].root -s`
using only the single-PE events.
