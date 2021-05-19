# sample command: python cosmicSignalExploration_lfilter.py -d cosmics_Mar_26_1p4fiber_61cm_5by2by20_one_hole_white_extrusion_1p2meter_long_5gss.root -r -p -s
import ROOT as rt
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from scipy.stats import norm
from scipy.signal import butter, lfilter, freqz
from scipy.optimize import curve_fit
from scipy import signal
import sys
import optparse
import os
from parameters import parameters
from utils import utility as ut
mpl.rc("font", family="serif", size=20)

parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-d', dest='filename', type='string', default='cosmics_Mar_8_1p4fiber_90cm_4by1by14_one_hole_white_extrusion_5p2meter_long.root', help="File name")
parser.add_option('-c', dest='channel', type='string', default='3', help="SiPM channel: 3 or 4.")
parser.add_option('-r', dest='rawPlot', action="store_true", help="Plotting raw triggers and signals")
parser.add_option('-p', dest='PEPlot', action="store_true", help="Plotting the PE peaks")
parser.add_option('-s', dest='smoothFit', action="store_true", help="Plotting smooth fit on the signals")
options, args = parser.parse_args()
filename = options.filename
rawPlot = options.rawPlot
PEPlot = options.PEPlot
smoothFit = options.smoothFit
channel = options.channel

outFolder = filename[:filename.find(".root")]
# parameters
if outFolder in parameters.keys():
    pars = parameters[outFolder]
else:
    pars = parameters["cosmics_Mar_8_1p4fiber_90cm_4by1by14_one_hole_white_extrusion_5p2meter_long"]

tpS = pars[0]
if channel == "3":
    pedADC = pars[1]
    sPEADCMin = pars[3][0]
    sPEADCMax = pars[3][1]
    sLEDWinMin = pars[5][0]
    sLEDWinMax = pars[5][1]
    sSiPMWinMin = pars[7][0]
    sSiPMWinMax = pars[7][1]
    zPEWinMin = pars[10][0]
    zPEWinMax = pars[10][1]
elif channel == "4":
    pedADC = pars[2]
    sPEADCMin = pars[4][0]
    sPEADCMax = pars[4][1]
    sLEDWinMin = pars[6][0]
    sLEDWinMax = pars[6][1]
    sSiPMWinMin = pars[8][0]
    sSiPMWinMax = pars[8][1]
    zPEWinMin = pars[11][0]
    zPEWinMax = pars[11][1]
zTWinMin = pars[9][0]
zTWinMax = pars[9][1]
# parameters for fitting savgol
fWinSize = pars[12][0]
fWinPoly = pars[12][1]
sPercent = pars[12][2]
# lowpass filter parameters
fs = pars[13][0]
cutoff = pars[13][1]
order = pars[13][2]
offset = pars[13][3]
# other parameters
trigValue = pars[18]


inputFolder = "dataFiles/"
tf = rt.TFile.Open(inputFolder + filename)
tr = tf.Get("T")
nEvents = tr.GetEntries()

# histogram details
trigTimeList = []
windowDiff_trigger = []
windowDiff_cosmic = []
windowInt_trigger = []
windowInt_cosmic = []
# for plotting raw signals and triggers
SiPM_50 = []
SiPM_1000 = []
SiPM_cosmic = []
SiPM_trigger = []
cosmic_50 = []
cosmic_1000 = []
cosmic_all = []
trigger_50 = []
trigger_1000 = []
trigger_all = []
# for plotting the smoothing fit
passedIndex = []
SiPM_smooth_50 = []
trigger_smooth_50 = []
lf_smooth_50 = []
window_smooth_50 = []
# making a histogram of the residual errors of the linear fit
rsList = []

eventCol = 0
print("Number of Events: {}".format(nEvents))
eRun = nEvents
# if run into memory issue, try uncommenting the following:
if nEvents > 40000:
    eRun = 40000
for count in range(0,eRun):
    # if count == 1000:
    #     break
    tr.GetEntry(count)
    trigger = tr.c2
    trigger_time = tr.t2
    cosmic = tr.c1
    cosmic_time = tr.t1

    if channel == "3":
        SiPM = tr.c3
        SiPM_time = tr.t3
    elif channel == "4":
        SiPM = tr.c4
        SiPM_time = tr.t4

    cos_val_i = []
    trig_val_i = []
    SiPM_val_i = []

    for i in range(len(SiPM)):
        trig_val_i.append( trigger[i] )
        cos_val_i.append( cosmic[i] )
        # making a hard cut off at SiPM ADC current > 0, because it should not be more than 0.
        if SiPM[i] > 0:
            SiPM_val_i.append(0)
        else:
            SiPM_val_i.append( SiPM[i] )
    triggerEdge = ut.pulseTime(trig_val_i,trigValue,tpS)
    cosmicEdge = ut.pulseTime(cos_val_i,trigValue,tpS)
    cosmic_all.append(cos_val_i)
    trigger_all.append(trig_val_i)

    if count < 1000:
        SiPM_1000.append(SiPM_val_i)
        trigger_1000.append(trig_val_i)
        cosmic_1000.append(cos_val_i)
    if count < 50:
        SiPM_50.append(SiPM_val_i)
        trigger_50.append(trig_val_i)
        cosmic_50.append(cos_val_i)

# separating cosmic events from LED events
    lf = ut.butter_lowpass_filter(SiPM_val_i,cutoff,fs,order)[offset:]
    if cosmicEdge > 0:
        eventPedADC = ut.signalPedestal(lf,sSiPMWinMin,tpS)
        lf = np.concatenate( (lf,[eventPedADC]*offset) )
        ADCInt = ut.signalIntegral(lf,sSiPMWinMin,sSiPMWinMax,tpS)
        SiPM_cosmic.append(SiPM_val_i)
        windowInt_cosmic.append(ADCInt)
    else:
        eventPedADC = ut.signalPedestal(lf,sLEDWinMin,tpS)
        lf = np.concatenate( (lf,[eventPedADC]*offset) )
        ADCInt = ut.signalIntegral(lf,sLEDWinMin,sLEDWinMax,tpS)
        SiPM_trigger.append(SiPM_val_i)
        windowInt_trigger.append(ADCInt)
    # this information is used for plotting the SiPM signals that pass requirement
    # to demonstrate how the fit for determining the time of the SiPM edge works.
    windowInfo = ut.signalExist(lf,cosmicEdge,pedADC,sSiPMWinMin,sSiPMWinMax,tpS)

# trigger
    trigTimeList.append( ut.pulseTime(trig_val_i,trigValue,tpS) )
# signal
    if windowInfo:
        eventCol += 1
        rs = ut.lineMatchEdge(lf,sSiPMWinMin,sSiPMWinMax,tpS,plot=False)[1]
        if rs < 0.005:
            rsList.append(rs)
        sigEdge = ut.midPointEdge(windowInfo,lf,tpS)
        if len(SiPM_smooth_50) < 50:
            passedIndex.append(count)
            SiPM_smooth_50.append(SiPM_val_i)
            trigger_smooth_50.append(trig_val_i)
            lf_smooth_50.append(lf)
            window_smooth_50.append(windowInfo)
print("Number of passed events: {}".format(eventCol))
print("SiPM_cosmic size: {}".format(len(SiPM_cosmic)))
print("SiPM_LED size: {}".format(len(SiPM_trigger)))
if rawPlot:
    if channel == "3":
        subfolder = "rawSignals_ch3"
    elif channel == "4":
        subfolder = "rawSignals_ch4"
    ut.plotNEvents(SiPM_50,subfolder,outFolder,10,0,1000*tpS)
    ut.plotNEvents(SiPM_1000,subfolder,outFolder,1000,0,1000*tpS)
    ut.plotNEvents(SiPM_cosmic,subfolder,outFolder,len(SiPM_cosmic),sSiPMWinMin,sSiPMWinMax)
    ut.plotNEvents(SiPM_trigger,subfolder,outFolder,len(SiPM_trigger),sLEDWinMin,sLEDWinMax)
    ut.plotNEvents(trigger_50,"rawTriggers",outFolder,10,zTWinMin,zTWinMax)
    ut.plotNEvents(trigger_1000,"rawTriggers",outFolder,1000,zTWinMin,zTWinMax)
    ut.plotNEvents(cosmic_50,"rawCosmics",outFolder,10,zTWinMin,zTWinMax)
    ut.plotNEvents(cosmic_1000,"rawCosmics",outFolder,1000,zTWinMin,zTWinMax)
    ut.plotNEvents(cosmic_all,"rawCosmics",outFolder,nEvents,zTWinMin,zTWinMax)
    ut.plotNEvents(trigger_all,"rawTriggers",outFolder,nEvents,zTWinMin,zTWinMax)

# histogram difference between ADC min vs ADC max in signal region
print("Making pedestal ADC plots...")
if channel == "3":
    folderName = "plots/pedADC_ch3/{}/".format(outFolder)
elif channel == "4":
    folderName = "plots/pedADC_ch4/{}/".format(outFolder)
ut.checkMakeDir(folderName)

if PEPlot:
    print("Number of events for LED signal area {}".format(len(windowInt_trigger)))
    print("Making PE peak plots using maximum and minimum ADC in signal region after smoothing signal...")
    if channel == "3":
        folderName = "plots/maxMinDiff_ch3/{}/".format(outFolder)
    elif channel == "4":
        folderName = "plots/maxMinDiff_ch4/{}/".format(outFolder)
    ut.checkMakeDir(folderName)
    plt.figure(figsize=(12,8))
    data_entries,bins = np.histogram(windowInt_trigger, bins=1000)
    binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
    ut.histplot(data_entries,binscenters,"blue","LED")
    # fitPEPeak(data_entries,binscenters,1.3,1.5,[100,1.4,1.0],"red")
    # fitPEPeak(data_entries,binscenters,1.0,1.3,[50,1.2,1.0],"green")
    plt.xlabel("Signal integral in signal window")
    plt.ylabel("Number of Events")
    # plt.xlim(0,1.0)
    # plt.xticks(np.arange(0,1.0,0.1))
    plt.grid()
    plt.legend()
    # plt.yscale("log")
    plt.savefig(folderName + "int.png")
    plt.xlim(zPEWinMin,zPEWinMax)
    plt.savefig(folderName + "int_zoom.png")
    plt.cla()
    plt.figure(figsize=(12,8))
    print(len(windowInt_cosmic))
    print(windowInt_cosmic[:10])
    data_entries,bins = np.histogram(windowInt_cosmic, bins=200)
    binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
    ut.histplot(data_entries,binscenters,"orange","Cosmic")
    # plt.xticks(np.arange(int(np.min(data_entries)),int(np.max(data_entries)),1))
    plt.grid()
    # plt.xlim(0,10)
    # plt.xticks(np.arange(0,10,0.5))
    # plt.hist(windowInt_cosmic,bins=np.arange(0,max(windowDiff_trigger)*1.01,0.01),color='#2a77b4',label="Cosmic")
    plt.savefig(folderName + "intCosmic.png")
    plt.grid()
    plt.xlim(0,10)
    plt.xticks(np.arange(0,10,0.5))
    # plt.hist(windowInt_cosmic,bins=np.arange(0,max(windowDiff_trigger)*1.01,0.01),color='#2a77b4',label="Cosmic")
    plt.savefig(folderName + "intCosmic_zoom.png")

# plot the smoothing fit
if smoothFit:
    print("Plotting smooth fit on the signals...")
    if channel == "3":
        folderName = "plots/signalFit_ch3/{}/".format(outFolder)
    elif channel == "4":
        folderName = "plots/signalFit_ch4/{}/".format(outFolder)
    ut.checkMakeDir(folderName)
    for i in range(len(SiPM_smooth_50)):
        SiPM_val_i = SiPM_smooth_50[i]
        trig_val_i = trigger_smooth_50[i]
        lf = lf_smooth_50[i]
        windowInfo = window_smooth_50[i]
        passedInd = passedIndex[i]
        triggerEdge = ut.pulseTime(trig_val_i,trigValue,tpS)
        wMin = int( (sSiPMWinMin)/tpS )
        wMax = int( (sSiPMWinMax)/tpS )
        base = ut.signalPedestal(lf,sSiPMWinMin,tpS)
        minSig = np.min(lf[wMin:wMax])
        ADC_5 = base - (abs(minSig-base)*0.05)
        ADC_30 = base - (abs(minSig-base)*0.30)
        ADC_85 = base - (abs(minSig-base)*0.85)
        area = ut.signalIntegral(lf,sSiPMWinMin,sSiPMWinMax,tpS)
        pedArea = ut.signalPedestalArea(lf,sSiPMWinMin,sSiPMWinMax,tpS)
        plt.figure(figsize=(12,8))
        axes = plt.gca()
        plt.plot(np.arange(0,len(SiPM_val_i))*tpS,SiPM_val_i,label="SiPM signal")
        plt.plot(np.arange(0,len(lf))*tpS,lf,label="Smoothed SiPM Signal",marker=".")
        # plt.vlines(midPointEdge(windowInfo,lf,tpS,0.55),min(SiPM_val_i),0,color="magenta",label="SiPM Signal Edge 55%")
        # plt.vlines(midPointEdge(windowInfo,lf,tpS),min(SiPM_val_i),0,color="red",label="SiPM Signal Edge 60%")
        # plt.vlines(midPointEdge(windowInfo,lf,tpS,0.7),min(SiPM_val_i),0,color="green",label="SiPM Signal Edge 70%")
        plt.vlines(sSiPMWinMin,min(SiPM_val_i),0,label="Time Window for Locating Signal",color="black")
        plt.vlines(sSiPMWinMax,min(SiPM_val_i),0,color="black")
        plt.hlines(base,sSiPMWinMin-10,sSiPMWinMax+10,color="red")
        plt.text(75,base,"0 %",color="red",fontsize=13)
        plt.hlines(ADC_5,sSiPMWinMin-10,sSiPMWinMax+10,color="red")
        plt.text(75,ADC_5,"5 %",color="red",fontsize=13)
        plt.hlines(ADC_30,sSiPMWinMin-10,sSiPMWinMax+10,color="red")
        plt.text(75,ADC_30,"30 %",color="red",fontsize=13)
        plt.hlines(ADC_85,sSiPMWinMin-10,sSiPMWinMax+10,color="red")
        plt.text(75,ADC_85,"85 %",color="red",fontsize=13)
        plt.hlines(minSig,sSiPMWinMin-10,sSiPMWinMax+10,color="red")
        plt.text(75,minSig,"100 %",color="red",fontsize=13)
        ut.lineMatchEdge(lf,sSiPMWinMin,sSiPMWinMax,tpS,plot=True)
        plt.ylabel("ADC Current")
        plt.xlabel("time (ns)")
        # plt.xlim(10,490)
        plt.ylim(min(SiPM_val_i)-0.001,0.001)
        plt.text(0,0,"Event {}".format(passedInd),transform = axes.transAxes)
        plt.text(0.65,0.75,"Trigger Time = {:.2f}".format(triggerEdge),transform = axes.transAxes)
        plt.text(0.65,0.85,"Signal Area = {:.2f}".format(area),transform = axes.transAxes)
        plt.text(0.65,0.65,"Pedestal Area = {:.2f}".format(pedArea),transform = axes.transAxes)
        plt.legend(fontsize=15,loc="lower right")
        plt.savefig(folderName + "passedEvent{}.png".format(passedInd))
        plt.cla()
    plt.figure(figsize=(12,8))
    plt.hist(rsList,bins=100)
    plt.yscale("log")
    plt.savefig(folderName + "normResidualErrors.png".format(passedInd))
