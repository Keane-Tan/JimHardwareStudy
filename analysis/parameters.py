class dataParameters:
    def __init__(self):
        self.pedADC = 0.0065 # 0: pedestal ADC
        self.sPEADC = [0.075,0.175] # 1: single PE ADC minimum, maximum
        self.sWin = [-20,100]        # 2: signal window minimum, maximum; original = [18,27]
        self.savgol =[31,5]             # 3: savgol fit parameters
        self.sPercent = 0.6            # 5: this percent should gives us a point around the center of the signal edge
        self.tdhistX = [-5,25]      # 6: xmin and xmax for the time difference histogram
        self.zSWin = [70,180]        # 7: zoom window for raw signals
        self.zTWin = [70,90]        # 8: zoom window for raw triggers
        self.zPEWin = [0,0.015]      # 9: zoom window for minThreshold plots
        self.fitPars = [1000, 0.2],   # 10: fit parameters for "Gaus"sian: normalization constant, mean, standard deviation
        self.trigValue = 0.06,           # 11: trigger threshold
        self.fitFunctionChoice = "Exp"          # 12: fit function: "Gaus", Exp
        self.binWidth = 1             # 13: bin width for the time difference histogram
        self.freq = 5.12            # 14: sampling rate in Gss
        self.trig = "pos",         # 15: polarity of trigger
        self.minTrigVal = 78.12          # 16: minimum trigger time edge
        self.aPEWin = [0,0.4]      # 17: zoom window for areaThreshold plots
        self.eSPE = [0.0068,0.002]      # 18: Estimated single PE peak ADC, and the distribution width for minPedDiff
        self.zDWin = [0,0.02,0.002] # 19: zoom window for minPedDiff
        self.fitRan = [3,20]
        self.aPEScan = "auto"
        self.GausTimeFit = False

Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss = dataParameters()
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss.pedADC = 0.0025
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss.sPEADC = [0.0025, 0.0055]
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss.sWin = [-4, 5]
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss.tdhistX = [-5.2, 7]
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss.zSWin = [70, 120]
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss.zTWin = [75, 90]
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss.zPEWin = [0, 0.006]
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss.fitPars = [1, 0, 2]
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss.trigValue = 0.15
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss.fitFunctionChoice = "Gaus"

Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p4V_5Gss = dataParameters()
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p4V_5Gss.pedADC = 0.0025
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p4V_5Gss.sPEADC = [0.0025, 0.0055]
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p4V_5Gss.sWin = [-4, 18]
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p4V_5Gss.tdhistX = [-5.2, 7]
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p4V_5Gss.zSWin = [70, 120]
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p4V_5Gss.zTWin = [75, 90]
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p4V_5Gss.zPEWin = [0, 0.006]
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p4V_5Gss.fitPars = [1, 0, 2]
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p4V_5Gss.trigValue = 0.15
Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p4V_5Gss.fitFunctionChoice = "Gaus"

Blue_laser_low_light_Feb_18_5p2V_5Gss = dataParameters()
Blue_laser_low_light_Feb_18_5p2V_5Gss.pedADC = 0.0019
Blue_laser_low_light_Feb_18_5p2V_5Gss.sPEADC = [0.0019, 0.0039]
Blue_laser_low_light_Feb_18_5p2V_5Gss.sWin = [-4, 18]
Blue_laser_low_light_Feb_18_5p2V_5Gss.tdhistX = [-5.2, 7]
Blue_laser_low_light_Feb_18_5p2V_5Gss.zSWin = [70, 120]
Blue_laser_low_light_Feb_18_5p2V_5Gss.zTWin = [75, 90]
Blue_laser_low_light_Feb_18_5p2V_5Gss.zPEWin = [0, 0.006]
Blue_laser_low_light_Feb_18_5p2V_5Gss.fitPars = [1, 0, 2]
Blue_laser_low_light_Feb_18_5p2V_5Gss.trigValue = 0.15
Blue_laser_low_light_Feb_18_5p2V_5Gss.fitFunctionChoice = "Gaus"

Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_1_try = dataParameters()
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_1_try.pedADC = 0.0016
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_1_try.sPEADC = [0.0016, 0.0036]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_1_try.sWin = [9, 31]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_1_try.tdhistX = [8.8, 21]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_1_try.zSWin = [90, 140]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_1_try.zTWin = [75, 90]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_1_try.zPEWin = [0, 0.006]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_1_try.fitPars = [1000, 14, 0.2]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_1_try.trigValue = 0.15
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_1_try.fitFunctionChoice = "Gaus"

Blue_laser_Feb_22_no_delay_5p2V_5Gss = dataParameters()
Blue_laser_Feb_22_no_delay_5p2V_5Gss.pedADC = 0.0019
Blue_laser_Feb_22_no_delay_5p2V_5Gss.sPEADC = [0.0019, 0.0039]
Blue_laser_Feb_22_no_delay_5p2V_5Gss.sWin = [-4, 18]
Blue_laser_Feb_22_no_delay_5p2V_5Gss.tdhistX = [-5.2, 7]
Blue_laser_Feb_22_no_delay_5p2V_5Gss.zSWin = [70, 120]
Blue_laser_Feb_22_no_delay_5p2V_5Gss.zTWin = [75, 90]
Blue_laser_Feb_22_no_delay_5p2V_5Gss.zPEWin = [0, 0.006]
Blue_laser_Feb_22_no_delay_5p2V_5Gss.fitPars = [1, 0, 2]
Blue_laser_Feb_22_no_delay_5p2V_5Gss.trigValue = 0.15
Blue_laser_Feb_22_no_delay_5p2V_5Gss.fitFunctionChoice = "Gaus"

Blue_laser_Feb_22_no_delay_5p2V_5Gss_2_try = dataParameters()
Blue_laser_Feb_22_no_delay_5p2V_5Gss_2_try.pedADC = 0.0018
Blue_laser_Feb_22_no_delay_5p2V_5Gss_2_try.sPEADC = [0.0018, 0.0038]
Blue_laser_Feb_22_no_delay_5p2V_5Gss_2_try.sWin = [-4, 18]
Blue_laser_Feb_22_no_delay_5p2V_5Gss_2_try.tdhistX = [-5.2, 7]
Blue_laser_Feb_22_no_delay_5p2V_5Gss_2_try.zSWin = [70, 120]
Blue_laser_Feb_22_no_delay_5p2V_5Gss_2_try.zTWin = [75, 90]
Blue_laser_Feb_22_no_delay_5p2V_5Gss_2_try.zPEWin = [0, 0.006]
Blue_laser_Feb_22_no_delay_5p2V_5Gss_2_try.fitPars = [1, 0, 2]
Blue_laser_Feb_22_no_delay_5p2V_5Gss_2_try.trigValue = 0.15
Blue_laser_Feb_22_no_delay_5p2V_5Gss_2_try.fitFunctionChoice = "Gaus"

Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_2_try_reduced_light = dataParameters()
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_2_try_reduced_light.pedADC = 0.0018
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_2_try_reduced_light.sPEADC = [0.0018, 0.0033]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_2_try_reduced_light.sWin = [9, 31]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_2_try_reduced_light.tdhistX = [8.8, 21]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_2_try_reduced_light.zSWin = [80, 130]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_2_try_reduced_light.zTWin = [75, 90]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_2_try_reduced_light.zPEWin = [0, 0.006]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_2_try_reduced_light.fitPars = [1000, 14, 0.2]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_2_try_reduced_light.trigValue = 0.15
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_2_try_reduced_light.fitFunctionChoice = "Gaus"

Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_3_try_somewhat_reduced_light = dataParameters()
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_3_try_somewhat_reduced_light.pedADC = 0.0017
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_3_try_somewhat_reduced_light.sPEADC = [0.0017, 0.0034]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_3_try_somewhat_reduced_light.sWin = [9, 31]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_3_try_somewhat_reduced_light.tdhistX = [8.8, 21]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_3_try_somewhat_reduced_light.zSWin = [80, 130]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_3_try_somewhat_reduced_light.zTWin = [75, 90]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_3_try_somewhat_reduced_light.zPEWin = [0, 0.006]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_3_try_somewhat_reduced_light.fitPars = [1000, 14, 0.2]
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_3_try_somewhat_reduced_light.trigValue = 0.15
Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_3_try_somewhat_reduced_light.fitFunctionChoice = "Gaus"

Feb_26_laser_SIPM_Pulser_neg_2p0V = dataParameters()
Feb_26_laser_SIPM_Pulser_neg_2p0V.pedADC = 0.0013
Feb_26_laser_SIPM_Pulser_neg_2p0V.sPEADC = [0.0013, 0.0032]
Feb_26_laser_SIPM_Pulser_neg_2p0V.sWin = [-9, 13]
Feb_26_laser_SIPM_Pulser_neg_2p0V.tdhistX = [-5.2, 7]
Feb_26_laser_SIPM_Pulser_neg_2p0V.zSWin = [65, 100]
Feb_26_laser_SIPM_Pulser_neg_2p0V.zTWin = [75, 90]
Feb_26_laser_SIPM_Pulser_neg_2p0V.zPEWin = [0, 0.006]
Feb_26_laser_SIPM_Pulser_neg_2p0V.fitPars = [1000, 0.1, 0.2]
Feb_26_laser_SIPM_Pulser_neg_2p0V.fitFunctionChoice = "Gaus"

Mar_1_K27_Sample_2_laser = dataParameters()
Mar_1_K27_Sample_2_laser.pedADC = 0.0016
Mar_1_K27_Sample_2_laser.sPEADC = [0.0016, 0.0033]
Mar_1_K27_Sample_2_laser.sWin = [-5, 45]
Mar_1_K27_Sample_2_laser.tdhistX = [-5.2, 35]
Mar_1_K27_Sample_2_laser.zSWin = [75, 130]
Mar_1_K27_Sample_2_laser.zTWin = [75, 90]
Mar_1_K27_Sample_2_laser.zPEWin = [0, 0.006]
Mar_1_K27_Sample_2_laser.binWidth = 5

Mar_1_K27_Sample_2_laser_reference_sampleoutofbeam = dataParameters()
Mar_1_K27_Sample_2_laser_reference_sampleoutofbeam.pedADC = 0.0016
Mar_1_K27_Sample_2_laser_reference_sampleoutofbeam.sPEADC = [0.0016, 0.0033]
Mar_1_K27_Sample_2_laser_reference_sampleoutofbeam.sWin = [-9, 13]
Mar_1_K27_Sample_2_laser_reference_sampleoutofbeam.tdhistX = [-5.2, 7]
Mar_1_K27_Sample_2_laser_reference_sampleoutofbeam.zSWin = [65, 100]
Mar_1_K27_Sample_2_laser_reference_sampleoutofbeam.zTWin = [75, 90]
Mar_1_K27_Sample_2_laser_reference_sampleoutofbeam.zPEWin = [0, 0.006]
Mar_1_K27_Sample_2_laser_reference_sampleoutofbeam.fitPars = [1000, 0.1, 0.2]
Mar_1_K27_Sample_2_laser_reference_sampleoutofbeam.fitFunctionChoice = "Gaus"

Mar_2_K27_Sample_3_laser = dataParameters()
Mar_2_K27_Sample_3_laser.pedADC = 0.0016
Mar_2_K27_Sample_3_laser.sPEADC = [0.0016, 0.0034]
Mar_2_K27_Sample_3_laser.sWin = [-5, 45]
Mar_2_K27_Sample_3_laser.tdhistX = [-5.2, 35]
Mar_2_K27_Sample_3_laser.zSWin = [75, 130]
Mar_2_K27_Sample_3_laser.zTWin = [75, 90]
Mar_2_K27_Sample_3_laser.zPEWin = [0, 0.006]
Mar_2_K27_Sample_3_laser.binWidth = 5

Mar_2_K27_Sample_4_laser = dataParameters()
Mar_2_K27_Sample_4_laser.pedADC = 0.0016
Mar_2_K27_Sample_4_laser.sPEADC = [0.0016, 0.0034]
Mar_2_K27_Sample_4_laser.sWin = [-5, 45]
Mar_2_K27_Sample_4_laser.tdhistX = [-5.2, 35]
Mar_2_K27_Sample_4_laser.zSWin = [75, 130]
Mar_2_K27_Sample_4_laser.zTWin = [75, 90]
Mar_2_K27_Sample_4_laser.zPEWin = [0, 0.006]
Mar_2_K27_Sample_4_laser.binWidth = 5

Mar_2_K27_Sample_5_laser_200hz = dataParameters()
Mar_2_K27_Sample_5_laser_200hz.pedADC = 0.0018
Mar_2_K27_Sample_5_laser_200hz.sPEADC = [0.0018, 0.0038]
Mar_2_K27_Sample_5_laser_200hz.sWin = [-10, 45]
Mar_2_K27_Sample_5_laser_200hz.tdhistX = [-5.2, 35]
Mar_2_K27_Sample_5_laser_200hz.zSWin = [65, 135]
Mar_2_K27_Sample_5_laser_200hz.zTWin = [75, 90]
Mar_2_K27_Sample_5_laser_200hz.zPEWin = [0, 0.006]
Mar_2_K27_Sample_5_laser_200hz.binWidth = 5

Mar_2_K27_Sample_6_laser_200hz = dataParameters()
Mar_2_K27_Sample_6_laser_200hz.pedADC = 0.0017
Mar_2_K27_Sample_6_laser_200hz.sPEADC = [0.0017, 0.0037]
Mar_2_K27_Sample_6_laser_200hz.sWin = [-10, 45]
Mar_2_K27_Sample_6_laser_200hz.tdhistX = [-5.2, 35]
Mar_2_K27_Sample_6_laser_200hz.zSWin = [65, 135]
Mar_2_K27_Sample_6_laser_200hz.zTWin = [75, 90]
Mar_2_K27_Sample_6_laser_200hz.zPEWin = [0, 0.006]
Mar_2_K27_Sample_6_laser_200hz.binWidth = 5

Mar_2_K27_Sample_3_laser_reference_sampleoutofbeam = dataParameters()
Mar_2_K27_Sample_3_laser_reference_sampleoutofbeam.pedADC = 0.0016
Mar_2_K27_Sample_3_laser_reference_sampleoutofbeam.sPEADC = [0.0016, 0.0034]
Mar_2_K27_Sample_3_laser_reference_sampleoutofbeam.sWin = [-9, 13]
Mar_2_K27_Sample_3_laser_reference_sampleoutofbeam.tdhistX = [-5.2, 7]
Mar_2_K27_Sample_3_laser_reference_sampleoutofbeam.zSWin = [65, 100]
Mar_2_K27_Sample_3_laser_reference_sampleoutofbeam.zTWin = [75, 90]
Mar_2_K27_Sample_3_laser_reference_sampleoutofbeam.zPEWin = [0, 0.006]
Mar_2_K27_Sample_3_laser_reference_sampleoutofbeam.fitPars = [1000, 0.1, 0.2]
Mar_2_K27_Sample_3_laser_reference_sampleoutofbeam.fitFunctionChoice = "Gaus"

Mar_2_K27_Sample_5_laser_reference_sampleoutofbeam_200hz = dataParameters()
Mar_2_K27_Sample_5_laser_reference_sampleoutofbeam_200hz.pedADC = 0.0018
Mar_2_K27_Sample_5_laser_reference_sampleoutofbeam_200hz.sPEADC = [0.0018, 0.0038]
Mar_2_K27_Sample_5_laser_reference_sampleoutofbeam_200hz.sWin = [-9, 13]
Mar_2_K27_Sample_5_laser_reference_sampleoutofbeam_200hz.tdhistX = [-5.2, 7]
Mar_2_K27_Sample_5_laser_reference_sampleoutofbeam_200hz.zSWin = [65, 100]
Mar_2_K27_Sample_5_laser_reference_sampleoutofbeam_200hz.zTWin = [75, 90]
Mar_2_K27_Sample_5_laser_reference_sampleoutofbeam_200hz.zPEWin = [0, 0.006]
Mar_2_K27_Sample_5_laser_reference_sampleoutofbeam_200hz.fitPars = [1000, 0.1, 0.2]
Mar_2_K27_Sample_5_laser_reference_sampleoutofbeam_200hz.fitFunctionChoice = "Gaus"

Mar_2_K27_Sample_6_laser_reference_sampleoutofbeam_200hz = dataParameters()
Mar_2_K27_Sample_6_laser_reference_sampleoutofbeam_200hz.pedADC = 0.0017
Mar_2_K27_Sample_6_laser_reference_sampleoutofbeam_200hz.sPEADC = [0.0017, 0.0037]
Mar_2_K27_Sample_6_laser_reference_sampleoutofbeam_200hz.sWin = [-9, 13]
Mar_2_K27_Sample_6_laser_reference_sampleoutofbeam_200hz.tdhistX = [-5.2, 7]
Mar_2_K27_Sample_6_laser_reference_sampleoutofbeam_200hz.zSWin = [65, 100]
Mar_2_K27_Sample_6_laser_reference_sampleoutofbeam_200hz.zTWin = [75, 90]
Mar_2_K27_Sample_6_laser_reference_sampleoutofbeam_200hz.zPEWin = [0, 0.006]
Mar_2_K27_Sample_6_laser_reference_sampleoutofbeam_200hz.fitPars = [1000, 0.1, 0.2]
Mar_2_K27_Sample_6_laser_reference_sampleoutofbeam_200hz.fitFunctionChoice = "Gaus"

Mar_3_laser_calib_new_hardware = dataParameters()
Mar_3_laser_calib_new_hardware.pedADC = 0.0017
Mar_3_laser_calib_new_hardware.sPEADC = [0.0017, 0.0036]
Mar_3_laser_calib_new_hardware.sWin = [-9, 13]
Mar_3_laser_calib_new_hardware.tdhistX = [-5.2, 7]
Mar_3_laser_calib_new_hardware.zSWin = [65, 100]
Mar_3_laser_calib_new_hardware.zTWin = [75, 90]
Mar_3_laser_calib_new_hardware.zPEWin = [0, 0.006]
Mar_3_laser_calib_new_hardware.fitPars = [1000, 0.1, 0.2]
Mar_3_laser_calib_new_hardware.fitFunctionChoice = "Gaus"

Mar_4_laser_calib_new_hardware_S13370_1173_56V = dataParameters()
Mar_4_laser_calib_new_hardware_S13370_1173_56V.pedADC = 0.005
Mar_4_laser_calib_new_hardware_S13370_1173_56V.sPEADC = [0.005, 0.0115]
Mar_4_laser_calib_new_hardware_S13370_1173_56V.sWin = [-9, 13]
Mar_4_laser_calib_new_hardware_S13370_1173_56V.tdhistX = [-5.2, 7]
Mar_4_laser_calib_new_hardware_S13370_1173_56V.zSWin = [65, 100]
Mar_4_laser_calib_new_hardware_S13370_1173_56V.zTWin = [75, 90]
Mar_4_laser_calib_new_hardware_S13370_1173_56V.zPEWin = [0, 0.02]
Mar_4_laser_calib_new_hardware_S13370_1173_56V.fitPars = [1000, 0.1, 0.2]
Mar_4_laser_calib_new_hardware_S13370_1173_56V.fitFunctionChoice = "Gaus"

Mar_4_260nm_LED_calib_new_hardware_S13370_1173_56V = dataParameters()
Mar_4_260nm_LED_calib_new_hardware_S13370_1173_56V.pedADC = 0.005
Mar_4_260nm_LED_calib_new_hardware_S13370_1173_56V.sPEADC = [0.005, 0.0115]
Mar_4_260nm_LED_calib_new_hardware_S13370_1173_56V.sWin = [-9, 13]
Mar_4_260nm_LED_calib_new_hardware_S13370_1173_56V.tdhistX = [-5.2, 7]
Mar_4_260nm_LED_calib_new_hardware_S13370_1173_56V.zSWin = [65, 100]
Mar_4_260nm_LED_calib_new_hardware_S13370_1173_56V.zTWin = [75, 90]
Mar_4_260nm_LED_calib_new_hardware_S13370_1173_56V.zPEWin = [0, 0.02]
Mar_4_260nm_LED_calib_new_hardware_S13370_1173_56V.fitPars = [1000, 0.1, 0.2]
Mar_4_260nm_LED_calib_new_hardware_S13370_1173_56V.fitFunctionChoice = "Gaus"

Mar_5_260nm_LED_S13370_1173_56V_0p0 = dataParameters()
Mar_5_260nm_LED_S13370_1173_56V_0p0.pedADC = 0.005
Mar_5_260nm_LED_S13370_1173_56V_0p0.sPEADC = [0.005, 0.0125]
Mar_5_260nm_LED_S13370_1173_56V_0p0.sWin = [-15, 88]
Mar_5_260nm_LED_S13370_1173_56V_0p0.tdhistX = [-5.2, 5]
Mar_5_260nm_LED_S13370_1173_56V_0p0.zSWin = [60, 170]
Mar_5_260nm_LED_S13370_1173_56V_0p0.zTWin = [75, 90]
Mar_5_260nm_LED_S13370_1173_56V_0p0.zPEWin = [0, 0.02]
Mar_5_260nm_LED_S13370_1173_56V_0p0.fitPars = [1000, 0.1, 0.2]
Mar_5_260nm_LED_S13370_1173_56V_0p0.fitFunctionChoice = "Gaus"
Mar_5_260nm_LED_S13370_1173_56V_0p0.binWidth = 2

Mar_5_260nm_LED_S13370_1173_56V_m0p5 = dataParameters()
Mar_5_260nm_LED_S13370_1173_56V_m0p5.pedADC = 0.006
Mar_5_260nm_LED_S13370_1173_56V_m0p5.sPEADC = [0.006, 0.013]
Mar_5_260nm_LED_S13370_1173_56V_m0p5.sWin = [-15, 88]
Mar_5_260nm_LED_S13370_1173_56V_m0p5.tdhistX = [-4, 2.5]
Mar_5_260nm_LED_S13370_1173_56V_m0p5.zSWin = [60, 170]
Mar_5_260nm_LED_S13370_1173_56V_m0p5.zTWin = [75, 90]
Mar_5_260nm_LED_S13370_1173_56V_m0p5.zPEWin = [0, 0.02]
Mar_5_260nm_LED_S13370_1173_56V_m0p5.fitPars = [1000, 0.1, 0.2]
Mar_5_260nm_LED_S13370_1173_56V_m0p5.fitFunctionChoice = "Gaus"
Mar_5_260nm_LED_S13370_1173_56V_m0p5.binWidth = 2

Mar_5_300nm_LED_S13370_1173_56V_0p0 = dataParameters()
Mar_5_300nm_LED_S13370_1173_56V_0p0.pedADC = 0.005
Mar_5_300nm_LED_S13370_1173_56V_0p0.sPEADC = [0.005, 0.0115]
Mar_5_300nm_LED_S13370_1173_56V_0p0.sWin = [-15, 88]
Mar_5_300nm_LED_S13370_1173_56V_0p0.tdhistX = [-5.2, 8]
Mar_5_300nm_LED_S13370_1173_56V_0p0.zSWin = [60, 170]
Mar_5_300nm_LED_S13370_1173_56V_0p0.zTWin = [75, 90]
Mar_5_300nm_LED_S13370_1173_56V_0p0.zPEWin = [0, 0.006]
Mar_5_300nm_LED_S13370_1173_56V_0p0.fitPars = [1000, 0.1, 0.2]
Mar_5_300nm_LED_S13370_1173_56V_0p0.fitFunctionChoice = "Gaus"
Mar_5_300nm_LED_S13370_1173_56V_0p0.binWidth = 2

Mar_8_laser_S13370_1173_56V_0p0 = dataParameters()
Mar_8_laser_S13370_1173_56V_0p0.pedADC = 0.005
Mar_8_laser_S13370_1173_56V_0p0.sPEADC = [0.005, 0.0125]
Mar_8_laser_S13370_1173_56V_0p0.sWin = [-15, 88]
Mar_8_laser_S13370_1173_56V_0p0.tdhistX = [-10.2, 0]
Mar_8_laser_S13370_1173_56V_0p0.zSWin = [60, 170]
Mar_8_laser_S13370_1173_56V_0p0.zTWin = [75, 90]
Mar_8_laser_S13370_1173_56V_0p0.zPEWin = [0, 0.02]
Mar_8_laser_S13370_1173_56V_0p0.fitPars = [1000, -6, 0.2]
Mar_8_laser_S13370_1173_56V_0p0.fitFunctionChoice = "Gaus"
Mar_8_laser_S13370_1173_56V_0p0.binWidth = 2

Mar_10_exp_test_LED260_m0p5V_S13370_56V_K27_with_Scint_in_front = dataParameters()
Mar_10_exp_test_LED260_m0p5V_S13370_56V_K27_with_Scint_in_front.pedADC = 0.005
Mar_10_exp_test_LED260_m0p5V_S13370_56V_K27_with_Scint_in_front.sPEADC = [0.005, 0.0125]
Mar_10_exp_test_LED260_m0p5V_S13370_56V_K27_with_Scint_in_front.sWin = [-15, 88]
Mar_10_exp_test_LED260_m0p5V_S13370_56V_K27_with_Scint_in_front.tdhistX = [-5, 40]
Mar_10_exp_test_LED260_m0p5V_S13370_56V_K27_with_Scint_in_front.zSWin = [60, 170]
Mar_10_exp_test_LED260_m0p5V_S13370_56V_K27_with_Scint_in_front.zTWin = [75, 90]
Mar_10_exp_test_LED260_m0p5V_S13370_56V_K27_with_Scint_in_front.zPEWin = [0, 0.02]
Mar_10_exp_test_LED260_m0p5V_S13370_56V_K27_with_Scint_in_front.binWidth = 2

Mar_10_exp_test_LED260_m1p0V_S13370_56V_K27_with_Scint_in_front = dataParameters()
Mar_10_exp_test_LED260_m1p0V_S13370_56V_K27_with_Scint_in_front.pedADC = 0.005
Mar_10_exp_test_LED260_m1p0V_S13370_56V_K27_with_Scint_in_front.sPEADC = [0.007, 0.01]
Mar_10_exp_test_LED260_m1p0V_S13370_56V_K27_with_Scint_in_front.sWin = [-15, 88]
Mar_10_exp_test_LED260_m1p0V_S13370_56V_K27_with_Scint_in_front.tdhistX = [-20, 80]
Mar_10_exp_test_LED260_m1p0V_S13370_56V_K27_with_Scint_in_front.zSWin = [60, 170]
Mar_10_exp_test_LED260_m1p0V_S13370_56V_K27_with_Scint_in_front.zTWin = [75, 90]
Mar_10_exp_test_LED260_m1p0V_S13370_56V_K27_with_Scint_in_front.zPEWin = [0, 0.02]
Mar_10_exp_test_LED260_m1p0V_S13370_56V_K27_with_Scint_in_front.fitPars = [1000, 10, 10]
Mar_10_exp_test_LED260_m1p0V_S13370_56V_K27_with_Scint_in_front.binWidth = 5

Apr_20_405nm_s13360_1350_54p6V_k27_0p1percent_in_toluene_freq200_offset_n0p5V = dataParameters()
Apr_20_405nm_s13360_1350_54p6V_k27_0p1percent_in_toluene_freq200_offset_n0p5V.pedADC = 0.05
Apr_20_405nm_s13360_1350_54p6V_k27_0p1percent_in_toluene_freq200_offset_n0p5V.sPEADC = [0.05, 0.14]
Apr_20_405nm_s13360_1350_54p6V_k27_0p1percent_in_toluene_freq200_offset_n0p5V.sWin = [-40, 100]
Apr_20_405nm_s13360_1350_54p6V_k27_0p1percent_in_toluene_freq200_offset_n0p5V.tdhistX = [-5, 30]
Apr_20_405nm_s13360_1350_54p6V_k27_0p1percent_in_toluene_freq200_offset_n0p5V.zSWin = [60, 170]
Apr_20_405nm_s13360_1350_54p6V_k27_0p1percent_in_toluene_freq200_offset_n0p5V.zTWin = [50, 75]
Apr_20_405nm_s13360_1350_54p6V_k27_0p1percent_in_toluene_freq200_offset_n0p5V.zPEWin = [0, 0.25]
Apr_20_405nm_s13360_1350_54p6V_k27_0p1percent_in_toluene_freq200_offset_n0p5V.binWidth = 5

Apr_20_405nm_s13360_1350_54p6V_Y11_sample_10_freq200_offset_n0p5V = dataParameters()
Apr_20_405nm_s13360_1350_54p6V_Y11_sample_10_freq200_offset_n0p5V.pedADC = 0.06
Apr_20_405nm_s13360_1350_54p6V_Y11_sample_10_freq200_offset_n0p5V.sPEADC = [0.06, 0.14]
Apr_20_405nm_s13360_1350_54p6V_Y11_sample_10_freq200_offset_n0p5V.sWin = [-10, 75]
Apr_20_405nm_s13360_1350_54p6V_Y11_sample_10_freq200_offset_n0p5V.tdhistX = [-10, 30]
Apr_20_405nm_s13360_1350_54p6V_Y11_sample_10_freq200_offset_n0p5V.zSWin = [60, 170]
Apr_20_405nm_s13360_1350_54p6V_Y11_sample_10_freq200_offset_n0p5V.zTWin = [75, 90]
Apr_20_405nm_s13360_1350_54p6V_Y11_sample_10_freq200_offset_n0p5V.zPEWin = [0, 0.25]
Apr_20_405nm_s13360_1350_54p6V_Y11_sample_10_freq200_offset_n0p5V.trigValue = -0.06
Apr_20_405nm_s13360_1350_54p6V_Y11_sample_10_freq200_offset_n0p5V.binWidth = 5

July_8_405nm_s13360_1350_56V_Kuraray_2MJ = dataParameters()
July_8_405nm_s13360_1350_56V_Kuraray_2MJ.pedADC = 0.18
July_8_405nm_s13360_1350_56V_Kuraray_2MJ.sPEADC = [0.18, 0.3]
July_8_405nm_s13360_1350_56V_Kuraray_2MJ.sWin = [-40, 100]
July_8_405nm_s13360_1350_56V_Kuraray_2MJ.tdhistX = [-5, 15]
July_8_405nm_s13360_1350_56V_Kuraray_2MJ.zSWin = [60, 170]
July_8_405nm_s13360_1350_56V_Kuraray_2MJ.zTWin = [55, 75]
July_8_405nm_s13360_1350_56V_Kuraray_2MJ.zPEWin = [0, 0.5]
July_8_405nm_s13360_1350_56V_Kuraray_2MJ.binWidth = 3

July_8_405nm_s13360_1350_56V_BCF92 = dataParameters()
July_8_405nm_s13360_1350_56V_BCF92.pedADC = 0.18
July_8_405nm_s13360_1350_56V_BCF92.sPEADC = [0.18, 0.3]
July_8_405nm_s13360_1350_56V_BCF92.sWin = [-40, 100]
July_8_405nm_s13360_1350_56V_BCF92.tdhistX = [-5, 15]
July_8_405nm_s13360_1350_56V_BCF92.zSWin = [60, 170]
July_8_405nm_s13360_1350_56V_BCF92.zTWin = [55, 75]
July_8_405nm_s13360_1350_56V_BCF92.zPEWin = [0, 0.5]
July_8_405nm_s13360_1350_56V_BCF92.binWidth = 2

July_8_405nm_s13360_1350_56V_Kuraray_1MJ = dataParameters()
July_8_405nm_s13360_1350_56V_Kuraray_1MJ.pedADC = 0.18
July_8_405nm_s13360_1350_56V_Kuraray_1MJ.sPEADC = [0.18, 0.3]
July_8_405nm_s13360_1350_56V_Kuraray_1MJ.sWin = [-40, 100]
July_8_405nm_s13360_1350_56V_Kuraray_1MJ.tdhistX = [-5, 15]
July_8_405nm_s13360_1350_56V_Kuraray_1MJ.zSWin = [60, 170]
July_8_405nm_s13360_1350_56V_Kuraray_1MJ.zTWin = [55, 75]
July_8_405nm_s13360_1350_56V_Kuraray_1MJ.zPEWin = [0, 0.5]
July_8_405nm_s13360_1350_56V_Kuraray_1MJ.binWidth = 3

July_8_405nm_s13360_1350_56V_KUR_Y11 = dataParameters()
July_8_405nm_s13360_1350_56V_KUR_Y11.pedADC = 0.18
July_8_405nm_s13360_1350_56V_KUR_Y11.sPEADC = [0.18, 0.3]
July_8_405nm_s13360_1350_56V_KUR_Y11.sWin = [-40, 100]
July_8_405nm_s13360_1350_56V_KUR_Y11.tdhistX = [-5, 15]
July_8_405nm_s13360_1350_56V_KUR_Y11.zSWin = [60, 170]
July_8_405nm_s13360_1350_56V_KUR_Y11.zTWin = [55, 75]
July_8_405nm_s13360_1350_56V_KUR_Y11.zPEWin = [0, 0.5]
July_8_405nm_s13360_1350_56V_KUR_Y11.binWidth = 3

July_11_405nm_s13360_1350_56V_Kuraray_1MJ = dataParameters()
July_11_405nm_s13360_1350_56V_Kuraray_1MJ.pedADC = 0.18
July_11_405nm_s13360_1350_56V_Kuraray_1MJ.sPEADC = [0.18, 0.3]
July_11_405nm_s13360_1350_56V_Kuraray_1MJ.tdhistX = [-5, 15]
July_11_405nm_s13360_1350_56V_Kuraray_1MJ.zPEWin = [0, 0.5]
July_11_405nm_s13360_1350_56V_Kuraray_1MJ.binWidth = 2

July_11_405nm_s13360_1350_56V_Kuraray_2MJ = dataParameters()
July_11_405nm_s13360_1350_56V_Kuraray_2MJ.pedADC = 0.18
July_11_405nm_s13360_1350_56V_Kuraray_2MJ.sPEADC = [0.18, 0.3]
July_11_405nm_s13360_1350_56V_Kuraray_2MJ.tdhistX = [-5, 15]
July_11_405nm_s13360_1350_56V_Kuraray_2MJ.zPEWin = [0, 0.5]
July_11_405nm_s13360_1350_56V_Kuraray_2MJ.binWidth = 2

July_15_405nm_s13360_1350_56V_BCF92 = dataParameters()
July_15_405nm_s13360_1350_56V_BCF92.pedADC = 0.18
July_15_405nm_s13360_1350_56V_BCF92.sPEADC = [0.18, 0.3]
July_15_405nm_s13360_1350_56V_BCF92.tdhistX = [-5, 15]
July_15_405nm_s13360_1350_56V_BCF92.zPEWin = [0, 0.5]
July_15_405nm_s13360_1350_56V_BCF92.binWidth = 2

July_15_405nm_s13360_1350_56V_KUR_Y11 = dataParameters()
July_15_405nm_s13360_1350_56V_KUR_Y11.pedADC = 0.18
July_15_405nm_s13360_1350_56V_KUR_Y11.sPEADC = [0.18, 0.3]
July_15_405nm_s13360_1350_56V_KUR_Y11.tdhistX = [-5, 15]
July_15_405nm_s13360_1350_56V_KUR_Y11.zPEWin = [0, 0.5]

Oct_28_cow_3_19_sample_6_1percentPPO_0p01percentPOPOP_260nm_to_small_sipm_56V = dataParameters()
Oct_28_cow_3_19_sample_6_1percentPPO_0p01percentPOPOP_260nm_to_small_sipm_56V.zSWin = [90,190]
Oct_28_cow_3_19_sample_6_1percentPPO_0p01percentPOPOP_260nm_to_small_sipm_56V.zTWin = [90,120]
Oct_28_cow_3_19_sample_6_1percentPPO_0p01percentPOPOP_260nm_to_small_sipm_56V.sWin = [-20,90]
Oct_28_cow_3_19_sample_6_1percentPPO_0p01percentPOPOP_260nm_to_small_sipm_56V.trigValue = -0.2
Oct_28_cow_3_19_sample_6_1percentPPO_0p01percentPOPOP_260nm_to_small_sipm_56V.trig = "neg"
Oct_28_cow_3_19_sample_6_1percentPPO_0p01percentPOPOP_260nm_to_small_sipm_56V.pedADC = 0.085
Oct_28_cow_3_19_sample_6_1percentPPO_0p01percentPOPOP_260nm_to_small_sipm_56V.sPEADC = [0.065,0.12]
Oct_28_cow_3_19_sample_6_1percentPPO_0p01percentPOPOP_260nm_to_small_sipm_56V.fitRan = [4,35]
Oct_28_cow_3_19_sample_6_1percentPPO_0p01percentPOPOP_260nm_to_small_sipm_56V.tdhistX = [-5,40]
Oct_28_cow_3_19_sample_6_1percentPPO_0p01percentPOPOP_260nm_to_small_sipm_56V.fitFunctionChoice = "Exp"
Oct_28_cow_3_19_sample_6_1percentPPO_0p01percentPOPOP_260nm_to_small_sipm_56V.fitPars = [1000, 0.2]

parameters = {
"Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss":Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss,
"Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p4V_5Gss":Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p4V_5Gss,
"Blue_laser_low_light_Feb_18_5p2V_5Gss":Blue_laser_low_light_Feb_18_5p2V_5Gss,
"Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_1_try":Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_1_try,
"Blue_laser_Feb_22_no_delay_5p2V_5Gss":Blue_laser_Feb_22_no_delay_5p2V_5Gss,
"Blue_laser_Feb_22_no_delay_5p2V_5Gss_2_try":Blue_laser_Feb_22_no_delay_5p2V_5Gss_2_try,
"Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_2_try_reduced_light":Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_2_try_reduced_light,
"Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_3_try_somewhat_reduced_light":Blue_laser_Feb_22_22ns_delay_5p2V_5Gss_3_try_somewhat_reduced_light,
"Feb_26_laser_SIPM_Pulser_neg_2p0V":Feb_26_laser_SIPM_Pulser_neg_2p0V,
"Mar_1_K27_Sample_2_laser":Mar_1_K27_Sample_2_laser,
"Mar_1_K27_Sample_2_laser_reference_sampleoutofbeam":Mar_1_K27_Sample_2_laser_reference_sampleoutofbeam,
"Mar_2_K27_Sample_3_laser":Mar_2_K27_Sample_3_laser,
"Mar_2_K27_Sample_4_laser":Mar_2_K27_Sample_4_laser,
"Mar_2_K27_Sample_5_laser_200hz":Mar_2_K27_Sample_5_laser_200hz,
"Mar_2_K27_Sample_6_laser_200hz":Mar_2_K27_Sample_6_laser_200hz,
"Mar_2_K27_Sample_3_laser_reference_sampleoutofbeam":Mar_2_K27_Sample_3_laser_reference_sampleoutofbeam,
"Mar_2_K27_Sample_5_laser_reference_sampleoutofbeam_200hz":Mar_2_K27_Sample_5_laser_reference_sampleoutofbeam_200hz,
"Mar_2_K27_Sample_6_laser_reference_sampleoutofbeam_200hz":Mar_2_K27_Sample_6_laser_reference_sampleoutofbeam_200hz,
"Mar_3_laser_calib_new_hardware":Mar_3_laser_calib_new_hardware,
"Mar_4_laser_calib_new_hardware_S13370_1173_56V":Mar_4_laser_calib_new_hardware_S13370_1173_56V,
"Mar_4_260nm_LED_calib_new_hardware_S13370_1173_56V":Mar_4_260nm_LED_calib_new_hardware_S13370_1173_56V,
"Mar_5_260nm_LED_S13370_1173_56V_0p0":Mar_5_260nm_LED_S13370_1173_56V_0p0,
"Mar_5_260nm_LED_S13370_1173_56V_m0p5":Mar_5_260nm_LED_S13370_1173_56V_m0p5,
"Mar_5_300nm_LED_S13370_1173_56V_0p0":Mar_5_300nm_LED_S13370_1173_56V_0p0,
"Mar_8_laser_S13370_1173_56V_0p0":Mar_8_laser_S13370_1173_56V_0p0,
"Mar_10_exp_test_LED260_m0p5V_S13370_56V_K27_with_Scint_in_front":Mar_10_exp_test_LED260_m0p5V_S13370_56V_K27_with_Scint_in_front,
"Mar_10_exp_test_LED260_m1p0V_S13370_56V_K27_with_Scint_in_front":Mar_10_exp_test_LED260_m1p0V_S13370_56V_K27_with_Scint_in_front,
"Apr_20_405nm_s13360_1350_54p6V_k27_0p1percent_in_toluene_freq200_offset_n0p5V":Apr_20_405nm_s13360_1350_54p6V_k27_0p1percent_in_toluene_freq200_offset_n0p5V,
"Apr_20_405nm_s13360_1350_54p6V_Y11_sample_10_freq200_offset_n0p5V":Apr_20_405nm_s13360_1350_54p6V_Y11_sample_10_freq200_offset_n0p5V,
"July_8_405nm_s13360_1350_56V_Kuraray_2MJ":July_8_405nm_s13360_1350_56V_Kuraray_2MJ,
"July_8_405nm_s13360_1350_56V_BCF92":July_8_405nm_s13360_1350_56V_BCF92,
"July_8_405nm_s13360_1350_56V_Kuraray_1MJ":July_8_405nm_s13360_1350_56V_Kuraray_1MJ,
"July_8_405nm_s13360_1350_56V_KUR_Y11":July_8_405nm_s13360_1350_56V_KUR_Y11,
"July_11_405nm_s13360_1350_56V_Kuraray_1MJ":July_11_405nm_s13360_1350_56V_Kuraray_1MJ,
"July_11_405nm_s13360_1350_56V_Kuraray_2MJ":July_11_405nm_s13360_1350_56V_Kuraray_2MJ,
"July_15_405nm_s13360_1350_56V_BCF92":July_15_405nm_s13360_1350_56V_BCF92,
"July_15_405nm_s13360_1350_56V_KUR_Y11":July_15_405nm_s13360_1350_56V_KUR_Y11,
"Oct_28_cow_3_19_sample_6_1percentPPO_0p01percentPOPOP_260nm_to_small_sipm_56V":Oct_28_cow_3_19_sample_6_1percentPPO_0p01percentPOPOP_260nm_to_small_sipm_56V,
}
