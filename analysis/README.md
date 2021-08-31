# Steps to Analyze the Files
1. Store the files in the `dataFiles/` directory.
2. Run
`python step1_plot_raw_noise_minMaxDiff.py -d [filename].root -r -p -t`
  * Look at `plots/rawSignals`
  * Look at `plots/rawTriggers`
  * Look at `plots/minThreshold`
3. Run
`python step1_plot_raw_noise_minMaxDiff.py -d July_16_260nm_s13360_1350_56V_LED_0_offset_extrusion_excites_SIPM_run1.root -a`
  * Look at `plots/aveNoise`
4. Run
`python step2_makeNoiseReducedSignals.py -d July_16_260nm_s13360_1350_56V_LED_0_offset_extrusion_excites_SIPM_run1.root`
  * Look at `plots/sigRedNoise`
5. Run
`python step3_makeFilteredSignal.py -d July_16_260nm_s13360_1350_56V_LED_0_offset_extrusion_excites_SIPM_run1.root`
  * Look at `plots/filtSig`
6. Run
`python step4_plot_filtered_mmD_signalEdge.py -d July_16_260nm_s13360_1350_56V_LED_0_offset_extrusion_excites_SIPM_run1.root -p`
  * Look at `plots/areaThreshold`
7. Run
`python step4_plot_filtered_mmD_signalEdge.py -d July_16_260nm_s13360_1350_56V_LED_0_offset_extrusion_excites_SIPM_run1.root -s -t`
  * Look at `plots/signalFit`
8. Run
`python step5_plotTimeDifference.py -d July_16_260nm_s13360_1350_56V_LED_0_offset_extrusion_excites_SIPM_run1.root`
  * Look at `plots/timeDiff`
