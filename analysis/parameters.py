parameters = {
"Blue_laser_Keane_low_light_test_trig_1_SIPM_2_delay_22ns_5Gss":[
0.0025,         # 0: pedestal ADC
[0.003,0.0055], # 1: single PE ADC minimum, maximum
[18,40],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[17.8,27],      # 6: xmin and xmax for the time difference histogram
[50,100],        # 7: zoom window for raw signals
[30,50],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1, 22, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.15,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p4V_5Gss":[
0.0025,         # 0: pedestal ADC
[0.0025,0.0055], # 1: single PE ADC minimum, maximum
[-4,18],         # 2: signal window minimum, maximum
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,7],      # 6: xmin and xmax for the time difference histogram
[70,120],       # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1, 0, 2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.15,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss":[
0.0025,         # 0: pedestal ADC
[0.0025,0.0055], # 1: single PE ADC minimum, maximum
[-4,5],         # 2: signal window minimum, maximum
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,7],      # 6: xmin and xmax for the time difference histogram
[70,120],       # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1, 0, 2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.15,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Blue_laser_low_light_Feb_18_5p2V_5Gss":[
0.0019,         # 0: pedestal ADC
[0.0019,0.0039], # 1: single PE ADC minimum, maximum
[-4,18],         # 2: signal window minimum, maximum
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,7],      # 6: xmin and xmax for the time difference histogram
[70,120],       # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1, 0, 2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.15,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Blue_laser_Feb_22_no_delay_5p2V_5Gss":[
0.0019,         # 0: pedestal ADC
[0.0019,0.0039], # 1: single PE ADC minimum, maximum
[-4,18],         # 2: signal window minimum, maximum
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,7],      # 6: xmin and xmax for the time difference histogram
[70,120],       # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1, 0, 2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.15,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Blue_laser_Feb_22_no_delay_5p2V_5Gss_2_try":[
0.0018,         # 0: pedestal ADC
[0.0018,0.0038], # 1: single PE ADC minimum, maximum
[-4,18],         # 2: signal window minimum, maximum
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,7],      # 6: xmin and xmax for the time difference histogram
[70,120],       # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1, 0, 2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.15,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_1_try":[
0.0016,         # 0: pedestal ADC
[0.0016,0.0036], # 1: single PE ADC minimum, maximum
[9,31],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[8.8,21],      # 6: xmin and xmax for the time difference histogram
[90,140],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1000, 14, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.15,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_2_try_reduced_light":[
0.0018,         # 0: pedestal ADC
[0.0018,0.0033], # 1: single PE ADC minimum, maximum
[9,31],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[8.8,21],      # 6: xmin and xmax for the time difference histogram
[80,130],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1000, 14, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.15,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_3_try_somewhat_reduced_light":[
0.0017,         # 0: pedestal ADC
[0.0017,0.0034], # 1: single PE ADC minimum, maximum
[9,31],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[8.8,21],      # 6: xmin and xmax for the time difference histogram
[80,130],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1000, 14, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.15,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Feb_26_laser_SIPM_Pulser_neg_2p0V":[
0.0013,         # 0: pedestal ADC
[0.0013,0.0032], # 1: single PE ADC minimum, maximum
[-9,13],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,7],      # 6: xmin and xmax for the time difference histogram
[65,100],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1000, 0.1, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Mar_1_K27_Sample_2_laser_reference_sampleoutofbeam":[
0.0016,         # 0: pedestal ADC
[0.0016,0.0033], # 1: single PE ADC minimum, maximum
[-9,13],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,7],      # 6: xmin and xmax for the time difference histogram
[65,100],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1000, 0.1, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Mar_1_K27_Sample_2_laser":[
0.0016,         # 0: pedestal ADC
[0.0016,0.0033], # 1: single PE ADC minimum, maximum
[-5,45],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,35],      # 6: xmin and xmax for the time difference histogram
[75,130],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
1.             # 13: bin width for the time difference histogram
],

"Mar_2_K27_Sample_3_laser_reference_sampleoutofbeam":[
0.0016,         # 0: pedestal ADC
[0.0016,0.0034], # 1: single PE ADC minimum, maximum
[-9,13],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,7],      # 6: xmin and xmax for the time difference histogram
[65,100],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1000, 0.1, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Mar_2_K27_Sample_3_laser":[
0.0016,         # 0: pedestal ADC
[0.0016,0.0034], # 1: single PE ADC minimum, maximum
[-5,45],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,35],      # 6: xmin and xmax for the time difference histogram
[75,130],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
1.             # 13: bin width for the time difference histogram
],

"Mar_2_K27_Sample_4_laser":[
0.0016,         # 0: pedestal ADC
[0.0016,0.0034], # 1: single PE ADC minimum, maximum
[-5,45],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,35],      # 6: xmin and xmax for the time difference histogram
[75,130],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
1.             # 13: bin width for the time difference histogram
],

"Mar_2_K27_Sample_5_laser_reference_sampleoutofbeam_200hz":[
0.0018,         # 0: pedestal ADC
[0.0018,0.0038], # 1: single PE ADC minimum, maximum
[-9,13],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,7],      # 6: xmin and xmax for the time difference histogram
[65,100],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1000, 0.1, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Mar_2_K27_Sample_5_laser_200hz":[
0.0018,         # 0: pedestal ADC
[0.0018,0.0038], # 1: single PE ADC minimum, maximum
[-10,45],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,35],      # 6: xmin and xmax for the time difference histogram
[65,135],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
1.             # 13: bin width for the time difference histogram
],

"Mar_2_K27_Sample_6_laser_reference_sampleoutofbeam_200hz":[
0.0017,         # 0: pedestal ADC
[0.0017,0.0037], # 1: single PE ADC minimum, maximum
[-9,13],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,7],      # 6: xmin and xmax for the time difference histogram
[65,100],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1000, 0.1, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Mar_2_K27_Sample_6_laser_200hz":[
0.0017,         # 0: pedestal ADC
[0.0017,0.0037], # 1: single PE ADC minimum, maximum
[-10,45],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,35],      # 6: xmin and xmax for the time difference histogram
[65,135],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
1.             # 13: bin width for the time difference histogram
],

"Mar_3_laser_calib_new_hardware":[
0.0017,         # 0: pedestal ADC
[0.0017,0.0036], # 1: single PE ADC minimum, maximum
[-9,13],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,7],      # 6: xmin and xmax for the time difference histogram
[65,100],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1000, 0.1, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Mar_4_laser_calib_new_hardware_S13370_1173_56V":[
0.005,         # 0: pedestal ADC
[0.005,0.0115], # 1: single PE ADC minimum, maximum
[-9,13],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,7],      # 6: xmin and xmax for the time difference histogram
[65,100],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.02],      # 9: zoom window for PE peak plots
[1000, 0.1, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Mar_4_260nm_LED_calib_new_hardware_S13370_1173_56V":[
0.005,         # 0: pedestal ADC
[0.005,0.0115], # 1: single PE ADC minimum, maximum
[-9,13],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,7],      # 6: xmin and xmax for the time difference histogram
[65,100],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.02],      # 9: zoom window for PE peak plots
[1000, 0.1, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.2             # 13: bin width for the time difference histogram
],

"Mar_5_300nm_LED_S13370_1173_56V_0p0":[
0.005,         # 0: pedestal ADC
[0.005,0.0115], # 1: single PE ADC minimum, maximum
[-15,88],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,8],      # 6: xmin and xmax for the time difference histogram
[60,170],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.006],      # 9: zoom window for PE peak plots
[1000, 0.1, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.3             # 13: bin width for the time difference histogram
],

"Mar_5_260nm_LED_S13370_1173_56V_m0p5":[
0.006,         # 0: pedestal ADC
[0.006,0.013], # 1: single PE ADC minimum, maximum
[-15,88],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-4,2.5],      # 6: xmin and xmax for the time difference histogram
[60,170],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.02],      # 9: zoom window for PE peak plots
[1000, 0.1, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.3             # 13: bin width for the time difference histogram
],

"Mar_5_260nm_LED_S13370_1173_56V_0p0":[
0.005,         # 0: pedestal ADC
[0.005,0.0125], # 1: single PE ADC minimum, maximum
[-15,88],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5.2,5],      # 6: xmin and xmax for the time difference histogram
[60,170],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.02],      # 9: zoom window for PE peak plots
[1000, 0.1, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.3             # 13: bin width for the time difference histogram
],

"Mar_8_laser_S13370_1173_56V_0p0":[
0.005,         # 0: pedestal ADC
[0.005,0.0125], # 1: single PE ADC minimum, maximum
[-15,88],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-10.2,0],      # 6: xmin and xmax for the time difference histogram
[60,170],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.02],      # 9: zoom window for PE peak plots
[1000, -6, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Gaus",          # 12: fit function: Gaus, Exp
0.3             # 13: bin width for the time difference histogram
],

"Mar_10_exp_test_LED260_m1p0V_S13370_56V_K27_with_Scint_in_front":[
0.005,         # 0: pedestal ADC
[0.007,0.010], # 1: single PE ADC minimum, maximum
[-15,88],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-20,80],      # 6: xmin and xmax for the time difference histogram
[60,170],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.02],      # 9: zoom window for PE peak plots
[1000, 10,10],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
1             # 13: bin width for the time difference histogram
],

"Mar_10_exp_test_LED260_m0p5V_S13370_56V_K27_with_Scint_in_front":[
0.005,         # 0: pedestal ADC
[0.005,0.0125], # 1: single PE ADC minimum, maximum
[-15,88],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,40],      # 6: xmin and xmax for the time difference histogram
[60,170],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.02],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
2             # 13: bin width for the time difference histogram
],

"Apr_20_405nm_s13360_1350_54p6V_Y11_sample_10_freq200_offset_n0p5V":[
0.06,         # 0: pedestal ADC
[0.06,0.14], # 1: single PE ADC minimum, maximum
[-10,75],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-10,30],      # 6: xmin and xmax for the time difference histogram
[60,170],        # 7: zoom window for raw signals
[75,90],        # 8: zoom window for raw triggers
[0,0.25],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
-0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
1.0             # 13: bin width for the time difference histogram
],

"Apr_20_405nm_s13360_1350_54p6V_k27_0p1percent_in_toluene_freq200_offset_n0p5V":[
0.05,         # 0: pedestal ADC
[0.05,0.14], # 1: single PE ADC minimum, maximum
[-40,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,30],      # 6: xmin and xmax for the time difference histogram
[60,170],        # 7: zoom window for raw signals
[50,75],        # 8: zoom window for raw triggers
[0,0.25],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
1.0             # 13: bin width for the time difference histogram
],

"July_8_405nm_s13360_1350_56V_BCF92":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-40,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[60,170],        # 7: zoom window for raw signals
[55,75],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.4             # 13: bin width for the time difference histogram
],

"July_8_405nm_s13360_1350_56V_Kuraray_2MJ":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-40,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[60,170],        # 7: zoom window for raw signals
[55,75],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.6             # 13: bin width for the time difference histogram
],

"July_8_405nm_s13360_1350_56V_KUR_Y11":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-40,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[60,170],        # 7: zoom window for raw signals
[55,75],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.6             # 13: bin width for the time difference histogram
],

"July_8_405nm_s13360_1350_56V_Kuraray_1MJ":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-40,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[60,170],        # 7: zoom window for raw signals
[55,75],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.6             # 13: bin width for the time difference histogram
],

"July_11_405nm_s13360_1350_56V_Kuraray_1MJ":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-20,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[70,180],        # 7: zoom window for raw signals
[70,90],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.4,             # 13: bin width for the time difference histogram
5.12            # 14: sampling rate in Gss
],

"July_11_405nm_s13360_1350_56V_Kuraray_2MJ":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-20,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[70,180],        # 7: zoom window for raw signals
[70,90],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.4,             # 13: bin width for the time difference histogram
5.12            # 14: sampling rate in Gss
],

"July_15_405nm_s13360_1350_56V_BCF92":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-20,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[70,180],        # 7: zoom window for raw signals
[70,90],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.4,             # 13: bin width for the time difference histogram
5.12            # 14: sampling rate in Gss
],

"July_15_405nm_s13360_1350_56V_KUR_Y11":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-20,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[70,180],        # 7: zoom window for raw signals
[70,90],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.2,             # 13: bin width for the time difference histogram
5.12            # 14: sampling rate in Gss
],

"July_16_260nm_s13360_1350_56V_LED_0_offset_extrusion_excites_BCF92_excites_SIPM_run1":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-20,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[70,180],        # 7: zoom window for raw signals
[70,90],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.2,             # 13: bin width for the time difference histogram
5.12            # 14: sampling rate in Gss
],

"July_16_260nm_s13360_1350_56V_LED_0_offset_extrusion_excites_SIPM_run1":[
0.0065,         # 0: pedestal ADC
[0.23,0.25], # 1: single PE ADC minimum, maximum
[-20,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[70,180],        # 7: zoom window for raw signals
[70,90],        # 8: zoom window for raw triggers
[0,0.015],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.2,             # 13: bin width for the time difference histogram
5.12,            # 14: sampling rate in Gss
"pos",          # 15: polarity of trigger
78.12,          # 16: minimum trigger time edge
],

"July_16_260nm_s13360_1350_56V_LED_0_offset_extrusion_excites_Y11_excites_SIPM_run1":[
0.18,         # 0: pedestal ADC
[0.21,0.25], # 1: single PE ADC minimum, maximum
[-20,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,50],      # 6: xmin and xmax for the time difference histogram
[70,180],        # 7: zoom window for raw signals
[70,90],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.6,             # 13: bin width for the time difference histogram
5.12            # 14: sampling rate in Gss
],

"July_16_260nm_s13360_1350_56V_LED_0_offset_straight_to_SIPM":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-20,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-2,5],      # 6: xmin and xmax for the time difference histogram
[70,180],        # 7: zoom window for raw signals
[70,90],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.2,             # 13: bin width for the time difference histogram
5.12            # 14: sampling rate in Gss
],

"July_19_Bi207_triggerChan1_S13360_1350_56V_source_excites_extrusion_excites_BCF92_excites_SIPM":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-20,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[70,180],        # 7: zoom window for raw signals
[70,90],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.2,             # 13: bin width for the time difference histogram
5.12            # 14: sampling rate in Gss
],

"July_22_260nm_s13360_3050_56V_triggerSIPM_extrusion_excites_1MJ_excites_SIPM_1350_run1":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-10,65],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[105,180],        # 7: zoom window for raw signals
[85,200],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.2,             # 13: bin width for the time difference histogram
5.12,            # 14: sampling rate in Gss
"neg",          # 15: trigger polarity
],

"July_22_260nm_s13360_3050_56V_triggerSIPM_extrusion_excites_2MJ_excites_SIPM_1350_run1":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-20,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[70,180],        # 7: zoom window for raw signals
[70,90],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.2,             # 13: bin width for the time difference histogram
5.12,            # 14: sampling rate in Gss
"neg",          # 15: trigger polarity
],

"July_22_260nm_s13360_3050_56V_triggerSIPM_extrusion_excites_BCF92_excites_SIPM_1350_run1":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-20,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[70,180],        # 7: zoom window for raw signals
[70,90],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.2,             # 13: bin width for the time difference histogram
5.12,            # 14: sampling rate in Gss
"neg",          # 15: trigger polarity
],

"July_22_260nm_s13360_3050_56V_triggerSIPM_extrusion_excites_Y11_excites_SIPM_1350_run1":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-20,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[70,180],        # 7: zoom window for raw signals
[70,90],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.2,             # 13: bin width for the time difference histogram
5.12,            # 14: sampling rate in Gss
"neg",          # 15: trigger polarity
],

"July_23_Bi207_s13360_3050_56V_triggerSIPM_extrusion_excites_1MJ_blue_fiber_excites_SIPM_1350_run1":[
0.18,         # 0: pedestal ADC
[0.18,0.3], # 1: single PE ADC minimum, maximum
[-20,100],        # 2: signal window minimum, maximum; original = [18,27]
31,             # 3: fit window size, should be at least smaller than signal window size * 5
5,              # 4: fit polynomial
0.6,            # 5: this percent should gives us a point around the center of the signal edge
[-5,15],      # 6: xmin and xmax for the time difference histogram
[70,180],        # 7: zoom window for raw signals
[70,90],        # 8: zoom window for raw triggers
[0,0.5],      # 9: zoom window for PE peak plots
[1000, 0.2],    # 10: fit parameters for gaussian: normalization constant, mean, standard deviation
0.06,            # 11: trigger threshold
"Exp",          # 12: fit function: Gaus, Exp
0.2,             # 13: bin width for the time difference histogram
5.12            # 14: sampling rate in Gss
],
}
# 2Gss is really 1.98Gss
# 5Gss is 5.12Gss
