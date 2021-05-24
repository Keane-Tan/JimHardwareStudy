parameters = {
"cosmics_Mar_8_1p4fiber_90cm_4by1by14_one_hole_white_extrusion_5p2meter_long":[
0.5,            # 0: time (ns) per sample
1.5,         # 1: pedestal PE for channel 3
1.0,         # 2: pedestal PE for channel 4
[0.15,0.35], # 3: single PE signal area minimum, maximum for channel 3
[0.15,0.35], # 4: single PE signal area minimum, maximum for channel 4
[180,480],        # 5: signal window LED for channel 3
[200,450],        # 6: signal window LED for channel 4
[100,350],        # 7: signal window SiPM for channel 3
[125,400],        # 8: signal window SiPM for channel 4
[75,175],        # 9: zoom window for raw triggers
[0.005,0.5],      # 10: zoom window for PE peak plots for channel 3
[0.005,0.5],      # 11: zoom window for PE peak plots for channel 4
[31,5,0.6],    # 12: savgol fit parameters [fit window size, polynomial, percent]
[2000,100,6,14], # 13: lowpass filter parameters: [fs,cutoff,order,offset]
[-60,40],      # 14: xmin and xmax for the time difference histogram
[100, -50, 1],    # 15: T3 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, -23, 1],    # 16: T4 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, 27, 1],    # 17: T43 fit parameters for gaussian: normalization constant, mean, standard deviation
-0.15,            # 18: trigger threshold
"Gaus",          # 19: fit function: Gaus, Exp
0.4,            # 20: bin width for the time difference histogram
[0,0,0],  # 21: local maxima for PE plots
0.05,            # 22: half width for the Gaussian fit to the PE plots
[0,0,0],  # 23: local maxima for PE plots Channel 4
0.1,            # 24: half width for the Gaussian fit to the PE plots Channel 4
0,           # 25: average gain Channel 3
0,           # 26: average gain Channel 4
],

"cosmics_Mar_10_1p4fiber_90cm_5by2by20_one_hole_white_extrusion_5p2meter_long":[
0.5,            # 0: time (ns) per sample
2.5,         # 1: pedestal PE for channel 3
2.5,         # 2: pedestal PE for channel 4
[0.15,0.35], # 3: single PE signal area minimum, maximum for channel 3
[0.15,0.35], # 4: single PE signal area minimum, maximum for channel 4
[180,480],        # 5: signal window LED for channel 3
[200,450],        # 6: signal window LED for channel 4
[75,400],        # 7: signal window SiPM for channel 3
[125,400],        # 8: signal window SiPM for channel 4
[75,175],        # 9: zoom window for raw triggers
[0.005,0.5],      # 10: zoom window for PE peak plots for channel 3
[0.005,0.5],      # 11: zoom window for PE peak plots for channel 4
[31,5,0.6],    # 12: savgol fit parameters [fit window size, polynomial, percent]
[2000,100,6,14], # 13: lowpass filter parameters: [fs,cutoff,order,offset]
[-60,40],      # 14: xmin and xmax for the time difference histogram
[100, -50, 1],    # 15: T3 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, -23, 1],    # 16: T4 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, 27, 1],    # 17: T43 fit parameters for gaussian: normalization constant, mean, standard deviation
-0.15,            # 18: trigger threshold
"Gaus",          # 19: fit function: Gaus, Exp
0.4,             # 20: bin width for the time difference histogram
[0,0,0],  # 21: local maxima for PE plots
0.05,            # 22: half width for the Gaussian fit to the PE plots
[0,0,0],  # 23: local maxima for PE plots Channel 4
0.1,            # 24: half width for the Gaussian fit to the PE plots Channel 4
0,           # 25: average gain Channel 3
0,           # 26: average gain Channel 4
],

"cosmics_Mar_11_1p4fiber_61cm_5by2by20_one_hole_white_extrusion_1p2meter_long":[
0.5,            # 0: time (ns) per sample
5.0,         # 1: pedestal PE for channel 3
6.0,         # 2: pedestal PE for channel 4
[0.15,0.35], # 3: single PE signal area minimum, maximum for channel 3
[0.15,0.35], # 4: single PE signal area minimum, maximum for channel 4
[180,480],        # 5: signal window LED for channel 3
[200,450],        # 6: signal window LED for channel 4
[75,400],        # 7: signal window SiPM for channel 3
[80,400],        # 8: signal window SiPM for channel 4
[75,175],        # 9: zoom window for raw triggers
[0.005,1.0],      # 10: zoom window for PE peak plots for channel 3
[0.005,1.0],      # 11: zoom window for PE peak plots for channel 4
[31,5,0.6],    # 12: savgol fit parameters [fit window size, polynomial, percent]
[2000,100,6,14], # 13: lowpass filter parameters: [fs,cutoff,order,offset]
[-60,40],      # 14: xmin and xmax for the time difference histogram
[100, -50, 1],    # 15: T3 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, -45, 1],    # 16: T4 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, 5, 1],    # 17: T43 fit parameters for gaussian: normalization constant, mean, standard deviation
-0.15,            # 18: trigger threshold
"Gaus",          # 19: fit function: Gaus, Exp
0.5,             # 20: bin width for the time difference histogram
[0.25,0.5,0.7],  # 21: local maxima for PE plots Channel 3
0.1,            # 22: half width for the Gaussian fit to the PE plots Channel 3
[0.28,0.52,0.8],  # 23: local maxima for PE plots Channel 4
0.1,            # 24: half width for the Gaussian fit to the PE plots Channel 4
0.26,           # 25: average gain Channel 3
0.23,           # 26: average gain Channel 4
[5,50],      # 27: zoom window for cosmic PE peak plots for channel 3
5,              # 28: zoom window width for cosmic PE peak plots for channel 3
[7,50],      # 29: zoom window for cosmic PE peak plots for channel 4
5,              # 30: zoom window width for cosmic PE peak plots for channel 4
[0.,0.01],      # 31: zoom window for minPedDiff plots for channel 3
[0.,0.01],      # 32: zoom window for minPedDiff plots for channel 4
0.0043,      # 33: single PE ADC for channel 3
0.0048,      # 34: single PE ADC for channel 4
0.001,    # 35: range to fit Gaussian to minPedDiff plots
0.001,    # 36: range to fit Gaussian to minPedDiff plots
22, # 37: mean PE for cosmic for channel 3
8,# 38: mean PE for cosmic for channel 4
20, # 39: half width to fit Gaussian for cosmic PE plots for channel 3
10,# 40: half width to fit Gaussian for cosmic PE plots for channel 4
],

"cosmics_Mar_26_1p4fiber_61cm_5by2by20_one_hole_white_extrusion_1p2meter_long_5gss":[
0.2,            # 0: time (ns) per sample
1.5,         # 1: pedestal PE for channel 3
0.5,         # 2: pedestal PE for channel 4
[0.15,0.35], # 3: single PE signal area minimum, maximum for channel 3
[0.15,0.35], # 4: single PE signal area minimum, maximum for channel 4
[125,200],        # 5: signal window LED for channel 3
[130,200],        # 6: signal window LED for channel 4
[25,200],        # 7: signal window SiPM for channel 3
[20,200],        # 8: signal window SiPM for channel 4
[75,175],        # 9: zoom window for raw triggers
[0.005,0.5],      # 10: zoom window for PE peak plots for channel 3
[0.005,0.5],      # 11: zoom window for PE peak plots for channel 4
[31,5,0.6],    # 12: savgol fit parameters [fit window size, polynomial, percent]
[2000,100,6,14], # 13: lowpass filter parameters: [fs,cutoff,order,offset]
[-70,20],      # 14: xmin and xmax for the time difference histogram
[100, -50, 1],    # 15: T3 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, -45, 1],    # 16: T4 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, 5, 1],    # 17: T43 fit parameters for gaussian: normalization constant, mean, standard deviation
-0.15,            # 18: trigger threshold
"Gaus",          # 19: fit function: Gaus, Exp
0.4,             # 20: bin width for the time difference histogram
[0,0,0],  # 21: local maxima for PE plots
0.05,            # 22: half width for the Gaussian fit to the PE plots
[0,0,0],  # 23: local maxima for PE plots Channel 4
0.1,            # 24: half width for the Gaussian fit to the PE plots Channel 4
0,           # 25: average gain Channel 3
0,           # 26: average gain Channel 4
],

"cosmics_May_4_1p4fiberKuraray_61cm_5by2by20_one_hole_white_extrusion_1p2meter_long_newS14160_5gss":[
0.2,            # 0: time (ns) per sample
3.0,         # 1: pedestal PE for channel 3
2.0,         # 2: pedestal PE for channel 4
[0.15,0.35], # 3: single PE signal area minimum, maximum for channel 3
[0.15,0.35], # 4: single PE signal area minimum, maximum for channel 4
[100,190],        # 5: signal window LED for channel 3
[105,190],        # 6: signal window LED for channel 4
[5,200],        # 7: signal window SiPM for channel 3
[5,200],        # 8: signal window SiPM for channel 4
[75,200],        # 9: zoom window for raw triggers
[0.005,0.5],      # 10: zoom window for PE peak plots for channel 3
[0.005,0.5],      # 11: zoom window for PE peak plots for channel 4
[31,5,0.6],    # 12: savgol fit parameters [fit window size, polynomial, percent]
[2000,100,6,14], # 13: lowpass filter parameters: [fs,cutoff,order,offset]
[-70,20],      # 14: xmin and xmax for the time difference histogram
[100, -50, 1],    # 15: T3 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, -45, 1],    # 16: T4 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, 5, 1],    # 17: T43 fit parameters for gaussian: normalization constant, mean, standard deviation
-0.15,            # 18: trigger threshold
"Gaus",          # 19: fit function: Gaus, Exp
0.4,             # 20: bin width for the time difference histogram
[0,0,0],  # 21: local maxima for PE plots
0.05,            # 22: half width for the Gaussian fit to the PE plots
[0,0,0],  # 23: local maxima for PE plots Channel 4
0.1,            # 24: half width for the Gaussian fit to the PE plots Channel 4
0,           # 25: average gain Channel 3
0,           # 26: average gain Channel 4
],

"cosmics_May_5_5by2by20_one_hole_white_extrusion_BCF92_1p5mm_250cm_500cm_long_newS14160_5gss":[
0.2,            # 0: time (ns) per sample
0.75,         # 1: pedestal PE for channel 3
0.5,         # 2: pedestal PE for channel 4
[0.15,0.35], # 3: single PE signal area minimum, maximum for channel 3
[0.15,0.35], # 4: single PE signal area minimum, maximum for channel 4
[105,190],        # 5: signal window LED for channel 3
[105,190],        # 6: signal window LED for channel 4
[5,190],        # 7: signal window SiPM for channel 3
[10,190],        # 8: signal window SiPM for channel 4
[75,200],        # 9: zoom window for raw triggers
[0.005,0.6],      # 10: zoom window for LED PE peak plots for channel 3
[0.005,0.6],      # 11: zoom window for LED PE peak plots for channel 4
[31,5,0.6],    # 12: savgol fit parameters [fit window size, polynomial, percent]
[2000,100,6,14], # 13: lowpass filter parameters: [fs,cutoff,order,offset]
[-70,20],      # 14: xmin and xmax for the time difference histogram
[100, -50, 1],    # 15: T3 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, -45, 1],    # 16: T4 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, 5, 1],    # 17: T43 fit parameters for gaussian: normalization constant, mean, standard deviation
-0.15,            # 18: trigger threshold
"Gaus",          # 19: fit function: Gaus, Exp
0.2,             # 20: bin width for the time difference histogram
[0.17,0.33,0.48],  # 21: local maxima for PE plots
0.05,            # 22: half width for the Gaussian fit to the PE plots
[0.17,0.33],  # 23: local maxima for PE plots Channel 4
0.05,            # 24: half width for the Gaussian fit to the PE plots Channel 4
0.16,           # 25: average gain Channel 3
0.17,           # 26: average gain Channel 4
[0,50],      # 27: zoom window for cosmic PE peak plots for channel 3
5,              # 28: zoom window width for cosmic PE peak plots for channel 3
[0,50],      # 29: zoom window for cosmic PE peak plots for channel 4
5,              # 30: zoom window width for cosmic PE peak plots for channel 4
[0.,0.015],      # 31: zoom window for minPedDiff plots for channel 3
[0.,0.01],      # 32: zoom window for minPedDiff plots for channel 4
0.0054,      # 33: single PE ADC for channel 3
0.0051,      # 34: single PE ADC for channel 4
0.0013,    # 35: range to fit Gaussian to minPedDiff plots
0.0013,    # 36: range to fit Gaussian to minPedDiff plots
22, # 37: mean PE for cosmic for channel 3
8,# 38: mean PE for cosmic for channel 4
20, # 39: half width to fit Gaussian for cosmic PE plots for channel 3
10,# 40: half width to fit Gaussian for cosmic PE plots for channel 4
],

"cosmics_May_6_5by2by20_one_hole_white_extrusion_BCF92_1p5mm_160cm_500cm_long_newS14160_5gss":[
0.2,            # 0: time (ns) per sample
0.1,         # 1: pedestal PE for channel 3
0.1,         # 2: pedestal PE for channel 4
[0.15,0.35], # 3: single PE signal area minimum, maximum for channel 3
[0.15,0.35], # 4: single PE signal area minimum, maximum for channel 4
[105,190],        # 5: signal window LED for channel 3
[120,190],        # 6: signal window LED for channel 4
[12,190],        # 7: signal window SiPM for channel 3
[12,190],        # 8: signal window SiPM for channel 4
[75,200],        # 9: zoom window for raw triggers
[0.005,0.5],      # 10: zoom window for PE peak plots for channel 3
[0.005,0.5],      # 11: zoom window for PE peak plots for channel 4
[31,5,0.6],    # 12: savgol fit parameters [fit window size, polynomial, percent]
[2000,100,6,14], # 13: lowpass filter parameters: [fs,cutoff,order,offset]
[-70,20],      # 14: xmin and xmax for the time difference histogram
[100, -50, 1],    # 15: T3 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, -45, 1],    # 16: T4 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, 5, 1],    # 17: T43 fit parameters for gaussian: normalization constant, mean, standard deviation
-0.15,            # 18: trigger threshold
"Gaus",          # 19: fit function: Gaus, Exp
0.4,             # 20: bin width for the time difference histogram
[0,0,0],  # 21: local maxima for PE plots
0.05,            # 22: half width for the Gaussian fit to the PE plots
[0,0,0],  # 23: local maxima for PE plots Channel 4
0.1,            # 24: half width for the Gaussian fit to the PE plots Channel 4
0,           # 25: average gain Channel 3
0,           # 26: average gain Channel 4
],

"cosmics_May_19_5by2by20_one_hole_white_extrusion_BCF92_1p5mm_160cm_500cm_long_newS14160_2gss":[
0.5,            # 0: time (ns) per sample
5.0,         # 1: pedestal PE for channel 3
6.0,         # 2: pedestal PE for channel 4
[0.15,0.35], # 3: single PE signal area minimum, maximum for channel 3
[0.15,0.35], # 4: single PE signal area minimum, maximum for channel 4
[175,480],        # 5: signal window LED for channel 3
[175,480],        # 6: signal window LED for channel 4
[75,380],        # 7: signal window SiPM for channel 3
[85,380],        # 8: signal window SiPM for channel 4
[75,175],        # 9: zoom window for raw triggers
[0.005,1.0],      # 10: zoom window for PE peak plots for channel 3
[0.005,1.0],      # 11: zoom window for PE peak plots for channel 4
[31,5,0.6],    # 12: savgol fit parameters [fit window size, polynomial, percent]
[2000,100,6,14], # 13: lowpass filter parameters: [fs,cutoff,order,offset]
[-60,40],      # 14: xmin and xmax for the time difference histogram
[100, -50, 1],    # 15: T3 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, -45, 1],    # 16: T4 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, 5, 1],    # 17: T43 fit parameters for gaussian: normalization constant, mean, standard deviation
-0.15,            # 18: trigger threshold
"Gaus",          # 19: fit function: Gaus, Exp
0.5,             # 20: bin width for the time difference histogram
[0.25,0.5,0.7],  # 21: local maxima for PE plots Channel 3
0.1,            # 22: half width for the Gaussian fit to the PE plots Channel 3
[0.28,0.52,0.8],  # 23: local maxima for PE plots Channel 4
0.1,            # 24: half width for the Gaussian fit to the PE plots Channel 4
0.24,           # 25: average gain Channel 3
0.26,           # 26: average gain Channel 4
[0,50],      # 27: zoom window for cosmic PE peak plots for channel 3
5,              # 28: zoom window width for cosmic PE peak plots for channel 3
[0,50],      # 29: zoom window for cosmic PE peak plots for channel 4
5,              # 30: zoom window width for cosmic PE peak plots for channel 4
[0.,0.015],      # 31: zoom window for minPedDiff plots for channel 3
[0.,0.015],      # 32: zoom window for minPedDiff plots for channel 4
0.0046,      # 33: single PE ADC for channel 3
0.0045,      # 34: single PE ADC for channel 4
0.001,    # 35: range to fit Gaussian to minPedDiff plots
0.001,    # 36: range to fit Gaussian to minPedDiff plots
22, # 37: mean PE for cosmic for channel 3
8,# 38: mean PE for cosmic for channel 4
20, # 39: half width to fit Gaussian for cosmic PE plots for channel 3
10,# 40: half width to fit Gaussian for cosmic PE plots for channel 4
],

"cosmics_May_20_5by2by20_one_hole_white_extrusion_BCF92_1p5mm_90cm_500cm_long_newS14160_2gss":[
0.5,            # 0: time (ns) per sample
8.0,         # 1: pedestal PE for channel 3
2.5,         # 2: pedestal PE for channel 4
[0.15,0.35], # 3: single PE signal area minimum, maximum for channel 3
[0.15,0.35], # 4: single PE signal area minimum, maximum for channel 4
[175,480],        # 5: signal window LED for channel 3
[200,450],        # 6: signal window LED for channel 4
[75,380],        # 7: signal window SiPM for channel 3
[100,380],        # 8: signal window SiPM for channel 4
[75,175],        # 9: zoom window for raw triggers
[1.2,3.0],      # 10: zoom window for PE peak plots for channel 3
[0.8,3.0],      # 11: zoom window for PE peak plots for channel 4
[31,5,0.6],    # 12: savgol fit parameters [fit window size, polynomial, percent]
[2000,100,6,14], # 13: lowpass filter parameters: [fs,cutoff,order,offset]
[-60,40],      # 14: xmin and xmax for the time difference histogram
[100, -50, 1],    # 15: T3 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, -45, 1],    # 16: T4 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, 5, 1],    # 17: T43 fit parameters for gaussian: normalization constant, mean, standard deviation
-0.15,            # 18: trigger threshold
"Gaus",          # 19: fit function: Gaus, Exp
0.5,             # 20: bin width for the time difference histogram
[1.55,1.8,2.05,2.25,2.5],  # 21: local maxima for PE plots Channel 3
0.1,            # 22: half width for the Gaussian fit to the PE plots Channel 3
[1.05,1.3,1.55,1.8],  # 23: local maxima for PE plots Channel 4
0.1,            # 24: half width for the Gaussian fit to the PE plots Channel 4
0.23,           # 25: average gain Channel 3
0.24,           # 26: average gain Channel 4
[0,75],      # 27: zoom window for cosmic PE peak plots for channel 3
5,              # 28: zoom window width for cosmic PE peak plots for channel 3
[0,26],      # 29: zoom window for cosmic PE peak plots for channel 4
2,              # 30: zoom window width for cosmic PE peak plots for channel 4
[0.,0.015],      # 31: zoom window for minPedDiff plots for channel 3
[0.,0.015],      # 32: zoom window for minPedDiff plots for channel 4
0.0045,      # 33: single PE ADC for channel 3
0.0042,      # 34: single PE ADC for channel 4
0.001,    # 35: range to fit Gaussian to minPedDiff plots
0.001,    # 36: range to fit Gaussian to minPedDiff plots
22, # 37: mean PE for cosmic for channel 3
8,# 38: mean PE for cosmic for channel 4
20, # 39: half width to fit Gaussian for cosmic PE plots for channel 3
10,# 40: half width to fit Gaussian for cosmic PE plots for channel 4
],
}
