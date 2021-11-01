# Summary Steps to Analyze the Files
1. Store the files in the `dataFiles/` directory.
2. Run
`python step1_plot_raw_noise_minMaxDiff.py -d [filename].root -r -p -t`
  * Look at `plots/rawTriggers/[filename]/Events_0-1000.png` to update `zTWin`
  * Look at `plots/rawSignals/[filename]/Events_0-1000.png` to update `zSWin`, `sWin`
  * Look at `plots/minThreshold/[filename]/mmD.png` to update `zPEWin`, `zPEScan` (if can't see peak structure)
  * Look at `plots/minThreshold/[filename]/mmD_zoomedIn.png` to update `pedADC` (requires correct `zPEWin`) to reflect where the first peak ends.
3. Run
`python step1_plot_raw_noise_minMaxDiff.py -d [filename].root -a`
  * Look at `plots/aveNoise/[filename]/aveNoise.png` to make sure average noise is calculated properly.
4. Run
`python step2_makeNoiseReducedSignals.py -d [filename].root`
  * Look at `plots/sigRedNoise/[filename]` to make sure noise is reduced from each signal properly.
5. Run
`python step3_makeFilteredSignal.py -d [filename].root`
  * Look at `plots/filtSig/[filename]` to make sure the filtered signal looks smooth and reasonable.
6. Run
`python step4_plot_filtered_mmD_signalEdge.py -d [filename].root -p`
  * Look at `plots/areaThreshold/[filename]/mmD.png` to update `aPEWin`
  * Look at `plots/areaThreshold/[filename]/mmD_zoomedIn.png` to update `sPEADC` (requires correct `aPEWin`) to capture the first peak.
7. Run
`python step4_plot_filtered_mmD_signalEdge.py -d [filename].root -s -t`
  * Look at `plots/signalFit/[filename]` to make sure the signals selected by the algorithm look reasonable (mostly single PE events).
8. Run
`python step5_plotTimeDifference.py -d [filename].root`
  * Look at `plots/timeDiff/[filename]`. These are the final results. You can update `tdhistX` and `fitRan` to fit things better.
