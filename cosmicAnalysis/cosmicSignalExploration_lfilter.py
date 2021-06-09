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
mpl.rc("font", family="serif", size=15)

parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-d', dest='filename', type='string', default='cosmics_Mar_8_1p4fiber_90cm_4by1by14_one_hole_white_extrusion_5p2meter_long.root', help="File name")
parser.add_option('-c', dest='channel', type='string', default='3', help="SiPM channel: 3 or 4.")
parser.add_option('-r', dest='rawPlot', action="store_true", help="Plotting raw triggers and signals")
parser.add_option('-p', dest='PEPlot', action="store_true", help="Plotting the PE peaks")
parser.add_option('-m', dest='minPEDiff', action="store_true", help="Plotting the difference between minimum and Pedestal")
parser.add_option('-s', dest='smoothFit', action="store_true", help="Plotting smooth fit on the signals")
options, args = parser.parse_args()
filename = options.filename
rawPlot = options.rawPlot
minPEDiff = options.minPEDiff
PEPlot = options.PEPlot
smoothFit = options.smoothFit
channel = options.channel

outFolder = filename[:filename.find(".root")]
# parameters
if outFolder in parameters.keys():
    pars = parameters[outFolder]
else:
    pars = parameters["cosmics_Mar_8_1p4fiber_90cm_4by1by14_one_hole_white_extrusion_5p2meter_long"]

tpS = pars.tpS
if channel == "3":
    pedADC = pars.pedADC_c3
    sPEADCMin = pars.sPEADCMin_c3[0]
    sPEADCMax = pars.sPEADCMin_c3[1]
    sLEDWinMin = pars.sLEDWin_c3[0]
    sLEDWinMax = pars.sLEDWin_c3[1]
    sSiPMWinMin = pars.sSiPMWin_c3[0]
    sSiPMWinMax = pars.sSiPMWin_c3[1]
    zPEWinMin = pars.zPEWin_c3[0]
    zPEWinMax = pars.zPEWin_c3[1]
    zCoWinMin = pars.zCoWin_c3[0]
    zCoWinMax = pars.zCoWin_c3[1]
    zCoWidth = pars.zCoWidth_c3
    PEp0List = pars.PEp0List_c3
    hw = pars.hw_c3
    avgGain = pars.avgGain_c3
    zDWinMin = pars.zDWin_c3[0]
    zDWinMax = pars.zDWin_c3[1]
    pD0 = pars.pD0_c3
    hDw = pars.hDw_c3
    p0Cosmic = pars.p0Cosmic_c3
    hwCosmic = pars.hwCosmic_c3
elif channel == "4":
    pedADC = pars.pedADC_c4
    sPEADCMin = pars.sPEADCMin_c4[0]
    sPEADCMax = pars.sPEADCMin_c4[1]
    sLEDWinMin = pars.sLEDWin_c4[0]
    sLEDWinMax = pars.sLEDWin_c4[1]
    sSiPMWinMin = pars.sSiPMWin_c4[0]
    sSiPMWinMax = pars.sSiPMWin_c4[1]
    zPEWinMin = pars.zPEWin_c4[0]
    zPEWinMax = pars.zPEWin_c4[1]
    zCoWinMin = pars.zCoWin_c4[0]
    zCoWinMax = pars.zCoWin_c4[1]
    zCoWidth = pars.zCoWidth_c4
    PEp0List = pars.PEp0List_c4
    hw = pars.hw_c4
    avgGain = pars.avgGain_c4
    zDWinMin = pars.zDWin_c4[0]
    zDWinMax = pars.zDWin_c4[1]
    pD0 = pars.pD0_c4
    hDw = pars.hDw_c4
    p0Cosmic = pars.p0Cosmic_c4
    hwCosmic = pars.hwCosmic_c4
zTWinMin = pars.zTWin[0]
zTWinMax = pars.zTWin[1]
# parameters for fitting savgol
fWinSize = pars.savgolFit[0]
fWinPoly = pars.savgolFit[1]
sPercent = pars.savgolFit[2]
# lowpass filter parameters
fs = pars.lowpassFit[0]
cutoff = pars.lowpassFit[1]
order = pars.lowpassFit[2]
offset = pars.lowpassFit[3]
# other parameters
trigValue = pars.trigValue


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
minPedDiff_cosmic = []
minPedDiff_trigger = []
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
        minPedDiff = ut.minPedDiff(lf,sSiPMWinMin,sSiPMWinMax,tpS)
        SiPM_cosmic.append(SiPM_val_i)
        windowInt_cosmic.append(ADCInt)
        minPedDiff_cosmic.append(minPedDiff)
    else:
        eventPedADC = ut.signalPedestal(lf,sLEDWinMin,tpS)
        lf = np.concatenate( (lf,[eventPedADC]*offset) )
        ADCInt = ut.signalIntegral(lf,sLEDWinMin,sLEDWinMax,tpS)
        # ADCInt = ut.signalIntegralNoPSub(lf,sLEDWinMin,sLEDWinMax,tpS)
        minPedDiff = ut.minPedDiff(lf,sLEDWinMin,sLEDWinMax,tpS)
        SiPM_trigger.append(SiPM_val_i)
        windowInt_trigger.append(ADCInt)
        minPedDiff_trigger.append(minPedDiff)
    # this information is used for plotting the SiPM signals that pass requirement
    # to demonstrate how the fit for determining the time of the SiPM edge works.
    windowInfo = ut.signalExist(lf,cosmicEdge,avgGain,pedADC,sSiPMWinMin,sSiPMWinMax,tpS)

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
print("CH{}".format(channel))
if rawPlot:
    if channel == "3":
        subfolder = "rawSignals_ch3"
    elif channel == "4":
        subfolder = "rawSignals_ch4"
    ut.plotNEvents(SiPM_50,subfolder,outFolder,10,0,1000*tpS,tpS)
    ut.plotNEvents(SiPM_1000,subfolder,outFolder,1000,0,1000*tpS,tpS)
    ut.plotNEvents(SiPM_cosmic,subfolder,outFolder,len(SiPM_cosmic),sSiPMWinMin,sSiPMWinMax,tpS,"cosmic")
    ut.plotNEvents(SiPM_trigger,subfolder,outFolder,len(SiPM_trigger),sLEDWinMin,sLEDWinMax,tpS,"LED")
    ut.plotNEvents(trigger_50,"rawTriggers",outFolder,10,zTWinMin,zTWinMax,tpS)
    ut.plotNEvents(trigger_1000,"rawTriggers",outFolder,1000,zTWinMin,zTWinMax,tpS)
    ut.plotNEvents(cosmic_50,"rawCosmics",outFolder,10,zTWinMin,zTWinMax,tpS)
    ut.plotNEvents(cosmic_1000,"rawCosmics",outFolder,1000,zTWinMin,zTWinMax,tpS)
    ut.plotNEvents(cosmic_all,"rawCosmics",outFolder,nEvents,zTWinMin,zTWinMax,tpS)
    ut.plotNEvents(trigger_all,"rawTriggers",outFolder,nEvents,zTWinMin,zTWinMax,tpS)

# histogram difference between ADC min vs ADC max in signal region
print("Making pedestal ADC plots...")
if channel == "3":
    folderName = "plots/pedADC_ch3/{}/".format(outFolder)
elif channel == "4":
    folderName = "plots/pedADC_ch4/{}/".format(outFolder)
ut.checkMakeDir(folderName)

if minPEDiff:
    print("Making PE peak plots using maximum and minimum ADC in signal region after smoothing signal...")
    if channel == "3":
        folderName = "plots/minPedDiff_ch3/{}/".format(outFolder)
    elif channel == "4":
        folderName = "plots/minPedDiff_ch4/{}/".format(outFolder)
    ut.checkMakeDir(folderName)
    plt.figure(figsize=(12,8))
    data_entries,bins = np.histogram(minPedDiff_trigger, bins=1000)
    binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
    ut.histplot(data_entries,binscenters,"blue","LED")
    plt.xlabel("Difference between Minimum ADC and Pedestal")
    plt.ylabel("Number of Events")
    plt.grid()
    plt.legend()
    # plt.yscale("log")
    plt.xlabel("Difference between Minimum ADC and Pedestal")
    plt.ylabel("Event")
    plt.title("LED Ch{}: {}".format(channel,outFolder),y=1.02,fontsize=12)
    plt.savefig(folderName + "mpDLED.png")
    plt.xlim(zDWinMin,zDWinMax)
    print ut.fitPEPeak(data_entries,binscenters,pD0-hDw,pD0+hDw,[100,pD0,0.01],"red")
    plt.legend()
    plt.xlabel("Difference between Minimum ADC and Pedestal")
    plt.ylabel("Event")
    plt.title("LED Ch{}: {}".format(channel,outFolder),y=1.02,fontsize=12)
    plt.savefig(folderName + "mpDLED_zoom.png")
    plt.cla()
    plt.figure(figsize=(12,8))
    data_entries,bins = np.histogram(minPedDiff_cosmic, bins=200)
    binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
    ut.histplot(data_entries,binscenters,"orange","Cosmic")
    plt.grid()
    plt.xlabel("Difference between Minimum ADC and Pedestal")
    plt.ylabel("Event")
    plt.title("Cosmic Ch{}: {}".format(channel,outFolder),y=1.02,fontsize=12)
    plt.savefig(folderName + "mpDCosmic.png")

if PEPlot:
    print("Number of events for LED signal area {}".format(len(windowInt_trigger)))
    print("Making PE peak plots using signal area in signal region after smoothing signal...")
    if channel == "3":
        folderName = "plots/signalArea_ch3/{}/".format(outFolder)
    elif channel == "4":
        folderName = "plots/signalArea_ch4/{}/".format(outFolder)
    ut.checkMakeDir(folderName)
    plt.figure(figsize=(12,8))
    data_entries,bins = np.histogram(windowInt_trigger, bins=500)
    binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
    ut.histplot(data_entries,binscenters,"blue","LED")
    plt.xlabel("Signal integral in signal window")
    plt.ylabel("Number of Events")
    plt.grid()
    plt.legend()
    # plt.yscale("log")
    plt.title("LED Ch{}: {}".format(channel,outFolder),y=1.02,fontsize=12)
    plt.savefig(folderName + "int.png")
    if PEp0List != [0,0,0]:
        meanList = []
        for p0 in PEp0List:
            meanList.append(ut.fitPEPeak(data_entries,binscenters,p0-hw,p0+hw,[100,p0,0.1],"red"))
        gainList = []
        for i in range(len(meanList)-1):
            gainList.append(meanList[i+1]-meanList[i])
        axes = plt.gca()
        plt.text(0.65,0.5,"Average gain: {:.2f}".format(np.mean(gainList)),transform = axes.transAxes)
    plt.xlim(zPEWinMin,zPEWinMax)
    plt.xticks(np.arange(zPEWinMin,zPEWinMax,0.1))
    # plt.grid()
    plt.legend()
    plt.title("LED Ch{}: {}".format(channel,outFolder),y=1.02,fontsize=12)
    plt.savefig(folderName + "int_zoom.png")
    plt.cla()
    plt.figure(figsize=(12,8))
    if avgGain > 0:
        windowInt_cosmic = np.array(windowInt_cosmic)/avgGain
    data_entries,bins = np.histogram(windowInt_cosmic, bins=200)
    binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
    ut.histplot(data_entries,binscenters,"orange","Cosmic")
    # plt.xticks(np.arange(int(np.min(data_entries)),int(np.max(data_entries)),1))
    plt.grid()
    # plt.xlim(0,10)
    # plt.xticks(np.arange(0,10,0.5))
    # plt.hist(windowInt_cosmic,bins=np.arange(0,max(windowDiff_trigger)*1.01,0.01),color='#2a77b4',label="Cosmic")
    plt.title("Cosmic Ch{}: {}".format(channel,outFolder),y=1.02,fontsize=12)
    plt.savefig(folderName + "intCosmic.png")
    # fit Gaussian to cosmic PE distribution
    # ut.fitPEPeak(data_entries,binscenters,zCoWinMin,zCoWinMax,[100,p0Cosmic,hwCosmic],"red")
    plt.xlim(zCoWinMin,zCoWinMax)
    cutInd = 0
    avgCosPE = []
    for wInt in windowInt_cosmic:
        if wInt > pedADC:
            avgCosPE.append(wInt)
    for i in range(len(data_entries)):
        if binscenters[i] > zCoWinMin:
            cutInd = i
            break
    # print(avgCosPE)
    stdErr = np.std(avgCosPE,ddof=1)/np.sqrt(len(avgCosPE))
    axes = plt.gca()
    plt.text(0.6,0.65,"Avg. photoelectrons: {:.1f}({:.1f})".format(np.mean(avgCosPE),stdErr),transform = axes.transAxes)
    plt.ylim(0,np.amax(data_entries[cutInd:])*1.1)
    plt.xticks(np.arange(zCoWinMin,zCoWinMax,zCoWidth))
    plt.vlines(pedADC,0,np.amax(data_entries[cutInd:])*1.1,label="PE Threshold",color="red")
    plt.xlabel("Number of Photoelectrons")
    plt.ylabel("Event")
    plt.title("Cosmic Ch{}: {}".format(channel,outFolder),y=1.02,fontsize=12)
    # plt.yscale("log")
    # plt.hist(windowInt_cosmic,bins=np.arange(0,max(windowDiff_trigger)*1.01,0.01),color='#2a77b4',label="Cosmic")
    plt.legend()
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
        # plt.hlines(ADC_5,sSiPMWinMin-10,sSiPMWinMax+10,color="red")
        # plt.text(75,ADC_5,"5 %",color="red",fontsize=13)
        # plt.hlines(ADC_30,sSiPMWinMin-10,sSiPMWinMax+10,color="red")
        # plt.text(75,ADC_30,"30 %",color="red",fontsize=13)
        # plt.hlines(ADC_85,sSiPMWinMin-10,sSiPMWinMax+10,color="red")
        # plt.text(75,ADC_85,"85 %",color="red",fontsize=13)
        plt.hlines(minSig,sSiPMWinMin-10,sSiPMWinMax+10,color="red")
        plt.text(75,minSig,"100 %",color="red",fontsize=13)
        ut.lineMatchEdge(lf,sSiPMWinMin,sSiPMWinMax,tpS,plot=True)
        ut.minPedThreshEdge(lf,sSiPMWinMin,sSiPMWinMax,tpS,pD0,plot=True)
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
