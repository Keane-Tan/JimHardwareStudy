parameters = {
"cosmics_Mar_8_1p4fiber_90cm_4by1by14_one_hole_white_extrusion_5p2meter_long":[
0.5,            # 0: time (ns) per sample
1.5,         # 1: pedestal signal area for channel 3
1.0,         # 2: pedestal signal area for channel 4
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
0.4             # 20: bin width for the time difference histogram
],

"cosmics_Mar_10_1p4fiber_90cm_5by2by20_one_hole_white_extrusion_5p2meter_long":[
0.5,            # 0: time (ns) per sample
2.5,         # 1: pedestal signal area for channel 3
2.5,         # 2: pedestal signal area for channel 4
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
0.4             # 20: bin width for the time difference histogram
],

"cosmics_Mar_11_1p4fiber_61cm_5by2by20_one_hole_white_extrusion_1p2meter_long":[
0.5,            # 0: time (ns) per sample
4.0,         # 1: pedestal signal area for channel 3
4.0,         # 2: pedestal signal area for channel 4
[0.15,0.35], # 3: single PE signal area minimum, maximum for channel 3
[0.15,0.35], # 4: single PE signal area minimum, maximum for channel 4
[180,480],        # 5: signal window LED for channel 3
[200,450],        # 6: signal window LED for channel 4
[75,400],        # 7: signal window SiPM for channel 3
[80,400],        # 8: signal window SiPM for channel 4
[75,175],        # 9: zoom window for raw triggers
[0.005,0.5],      # 10: zoom window for PE peak plots for channel 3
[0.005,0.5],      # 11: zoom window for PE peak plots for channel 4
[31,5,0.6],    # 12: savgol fit parameters [fit window size, polynomial, percent]
[2000,100,6,14], # 13: lowpass filter parameters: [fs,cutoff,order,offset]
[-60,40],      # 14: xmin and xmax for the time difference histogram
[100, -50, 1],    # 15: T3 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, -45, 1],    # 16: T4 fit parameters for gaussian: normalization constant, mean, standard deviation
[100, 5, 1],    # 17: T43 fit parameters for gaussian: normalization constant, mean, standard deviation
-0.15,            # 18: trigger threshold
"Gaus",          # 19: fit function: Gaus, Exp
0.4             # 20: bin width for the time difference histogram
],

"cosmics_Mar_26_1p4fiber_61cm_5by2by20_one_hole_white_extrusion_1p2meter_long_5gss":[
0.2,            # 0: time (ns) per sample
1.5,         # 1: pedestal signal area for channel 3
0.5,         # 2: pedestal signal area for channel 4
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
0.4             # 20: bin width for the time difference histogram
],

"cosmics_May_4_1p4fiberKuraray_61cm_5by2by20_one_hole_white_extrusion_1p2meter_long_newS14160_5gss":[
0.2,            # 0: time (ns) per sample
3.0,         # 1: pedestal signal area for channel 3
2.0,         # 2: pedestal signal area for channel 4
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
0.4             # 20: bin width for the time difference histogram
],

"cosmics_May_5_5by2by20_one_hole_white_extrusion_BCF92_1p5mm_250cm_500cm_long_newS14160_5gss":[
0.2,            # 0: time (ns) per sample
0.75,         # 1: pedestal signal area for channel 3
0.5,         # 2: pedestal signal area for channel 4
[0.15,0.35], # 3: single PE signal area minimum, maximum for channel 3
[0.15,0.35], # 4: single PE signal area minimum, maximum for channel 4
[105,190],        # 5: signal window LED for channel 3
[105,190],        # 6: signal window LED for channel 4
[5,190],        # 7: signal window SiPM for channel 3
[10,190],        # 8: signal window SiPM for channel 4
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
0.4             # 20: bin width for the time difference histogram
],

"cosmics_May_6_5by2by20_one_hole_white_extrusion_BCF92_1p5mm_160cm_500cm_long_newS14160_5gss":[
0.2,            # 0: time (ns) per sample
0.1,         # 1: pedestal signal area for channel 3
0.1,         # 2: pedestal signal area for channel 4
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
0.4             # 20: bin width for the time difference histogram
],
}
