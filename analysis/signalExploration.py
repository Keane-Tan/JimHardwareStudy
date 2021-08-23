import ROOT as rt
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from scipy.stats import norm
from scipy.optimize import curve_fit
from scipy import signal
import sys
import optparse
import os
from parameters import parameters
from utils import utility as ut

mpl.rc("font", family="serif", size=20)

parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-d', dest='filename', type='string', default='Blue_laser_Keane_low_light_test_trig_1_SIPM_2_delay_22ns_5Gss.root', help="File name")
parser.add_option('-r', dest='rawPlot', action="store_true", help="Plotting raw triggers and signals")
parser.add_option('-p', dest='PEPlot', action="store_true", help="Plotting the PE peaks")
parser.add_option('-s', dest='smoothFit', action="store_true", help="Plotting smooth fit on the signals")
parser.add_option('-t', dest='testP', action="store_true", help="Testing things...")
options, args = parser.parse_args()
filename = options.filename
rawPlot = options.rawPlot
PEPlot = options.PEPlot
smoothFit = options.smoothFit
testP = options.testP

outFolder = filename[:filename.find(".root")]
# parameters
if outFolder in parameters.keys():
    pars = parameters[outFolder]
else:
    pars = parameters["Blue_laser_Keane_low_light_test_trig_1_SIPM_2_delay_22ns_5Gss"]
pedADC = pars[0]
sPEADCMin = pars[1][0]
sPEADCMax = pars[1][1]
sWinMin = pars[2][0]
sWinMax = pars[2][1]
fWinSize = pars[3]
fWinPoly = pars[4]
sPercent = pars[5]
tdhistXMin = pars[6][0]
tdhistXMax = pars[6][1]
zSWin = pars[7]
zTWin = pars[8]
zPEWinMin = pars[9][0]
zPEWinMax = pars[9][1]
trigValue = pars[11]
if len(pars) == 15:
    freq = pars[14] # in Gss
else:
    freq = 5.0
print("sampling frequency: {} Gss".format(freq))
tfq = 1./freq
print("Time per bin: {} ns".format(tfq))

inputFolder = "dataFiles/"
tf = rt.TFile.Open(inputFolder + filename)
tr = tf.Get("T")
nEvents = tr.GetEntries()

# histogram details
bins=np.arange(tdhistXMin,tdhistXMax,0.2)
binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
totalDataEntries = np.zeros(len(bins)-1)

trigTimeList = []
windowDiff = []
edgeTimeDiff = []
# for plotting raw signals and triggers
SiPM_50 = []
trigger_50 = []
SiPM_1000 = []
trigger_1000 = []
# for plotting the smoothing fit
passedIndex = []
SiPM_smooth_50 = []
trigger_smooth_50 = []
sf_smooth_50 = []
window_smooth_50 = []

# testing purpose
largetDiffEv = [
]
troubles_SiPM_smooth = []
troubles_trigger_smooth = []
troubles_sf_smooth = []
troubles_window_smooth = []
accEvent = 0
pedVList = []
highpVList = []

for count in range(0,nEvents):
    tr.GetEntry(count)

    trigger = tr.c1
    SiPM = tr.c2
    trigger_time = tr.t1
    SiPM_time = tr.t2

    trig_val_i = []
    SiPM_val_i = []

    for i in range(len(SiPM)):
        trig_val_i.append( trigger[i] )
        # making a hard cut off at SiPM ADC current > 0, because it should not be more than 0.
        if SiPM[i] > 0:
            SiPM_val_i.append(0)
        else:
            SiPM_val_i.append( SiPM[i] )

    if count < 1000:
        SiPM_1000.append(SiPM_val_i)
        trigger_1000.append(trig_val_i)
    if count < 50:
        SiPM_50.append(SiPM_val_i)
        trigger_50.append(trig_val_i)

    sf = ut.signalFilter(SiPM_val_i,win=fWinSize,pol=fWinPoly)
    triggerEdge = ut.triggerTime(trig_val_i,trigValue,tfq)
    windowDiff.append(ut.signalExistThreshold(sf,triggerEdge,tfq,sWinMin,sWinMax))
    windowInfo = ut.signalExist(sf,triggerEdge,tfq,pedADC,sPEADCMin,sPEADCMax,sWinMin,sWinMax,True)
    pedV = ut.sigPedVoltage(sf,triggerEdge,tfq,wmin=sWinMin,wmax=sWinMax)
    pedVList.append(pedV)
    if pedV > 0.0015:
        highpVList.append(sf)
# testing purpose
    if count in largetDiffEv:
        print("Recording event {}".format(count))
        troubles_SiPM_smooth.append(SiPM_val_i)
        troubles_trigger_smooth.append(trig_val_i)
        troubles_sf_smooth.append(sf)
        troubles_window_smooth.append(windowInfo)
# trigger
    trigTimeList.append( ut.triggerTime(trig_val_i,trigValue,tfq) )
# signal
    if windowInfo:
        accEvent += 1
        sigEdge = ut.midPointEdge(windowInfo,sf,tfq,percent=sPercent)
        edgeTimeDiff.append(sigEdge - triggerEdge)
        if len(SiPM_smooth_50) < 50:
            passedIndex.append(count)
            SiPM_smooth_50.append(SiPM_val_i)
            trigger_smooth_50.append(trig_val_i)
            sf_smooth_50.append(sf)
            window_smooth_50.append(windowInfo)
print("Number of single PE events: {}".format(accEvent))
pedVList = np.array(pedVList)
np.savez("pedVs",pedVList)
np.savez("hpEvents",*highpVList)
# plotting raw signals
if rawPlot:
    ut.plotNEvents(SiPM_50,"rawSignals",outFolder,10,tfq,zSWin)
    ut.plotNEvents(trigger_50,"rawTriggers",outFolder,10,tfq,zTWin)
    ut.plotNEvents(SiPM_1000,"rawSignals",outFolder,1000,tfq,zSWin)
    ut.plotNEvents(trigger_1000,"rawTriggers",outFolder,1000,tfq,zTWin)

# histogram difference between ADC min vs ADC max in signal region
if PEPlot:
    print("Making PE peak plots using maximum and minimum ADC in signal region after smoothing signal...")
    folderName = "plots/maxMinDiff/{}/".format(outFolder)
    ut.checkMakeDir(folderName)
    plt.figure(figsize=(12,8))
    plt.hist(windowDiff,bins=np.linspace(0,max(windowDiff)*1.01,200))
    plt.xlabel("Signal Area (After Pedestal Subtraction)")
    plt.ylabel("Number of Events")
    plt.grid()
    plt.savefig(folderName + "mmD.png")
    ## zoomed in
    plt.xticks( np.arange(zPEWinMin,zPEWinMax,0.02) , rotation=90)
    plt.xlim(zPEWinMin,zPEWinMax)
    plt.grid()
    plt.savefig(folderName + "mmD_zoomedIn.png")
    plt.cla()

# plot the smoothing fit
if smoothFit:
    print("Plotting smooth fit on the signals...")
    folderName = "plots/signalFit/{}/".format(outFolder)
    ut.checkMakeDir(folderName)
    for i in range(len(SiPM_smooth_50)):
        SiPM_val_i = SiPM_smooth_50[i]
        trig_val_i = trigger_smooth_50[i]
        sf = sf_smooth_50[i]
        windowInfo = window_smooth_50[i]
        passedInd = passedIndex[i]
        plt.figure(figsize=(12,8))
        plt.plot(np.arange(0,len(SiPM_val_i))*tfq,SiPM_val_i,label="SiPM signal")
        plt.plot(np.arange(0,len(sf))*tfq,sf,label="Smoothed SiPM Signal")
        plt.xticks(np.arange(zSWin[0],zSWin[1],5))
        plt.vlines(ut.midPointEdge(windowInfo,sf,tfq,0.55),min(SiPM_val_i),0,color="magenta",label="SiPM Signal Edge 55%")
        plt.vlines(ut.midPointEdge(windowInfo,sf,tfq,percent=sPercent),min(SiPM_val_i),0,color="red",label="SiPM Signal Edge 60%")
        plt.vlines(ut.midPointEdge(windowInfo,sf,tfq,0.7),min(SiPM_val_i),0,color="green",label="SiPM Signal Edge 70%")
        plt.vlines(ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMin,min(SiPM_val_i),0,label="Time Window for Signal ID")
        plt.vlines(ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMax,min(SiPM_val_i),0)
        plt.ylabel("ADC Current")
        plt.xlabel("time (ns)")
        print("Event {}".format(passedInd))
        print(ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMin)
        # plt.xlim(ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMin,ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMax)
        plt.ylim(min(SiPM_val_i)-0.001,0.001)
        axes = plt.gca()
        plt.text(ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMin-10,0,"Event {}".format(passedInd))
        plt.text(0.2,0.1,"Signal Edge = {:.2f} ns".format(ut.midPointEdge(windowInfo,sf,tfq,percent=sPercent)),transform = axes.transAxes)
        plt.text(0.2,0.2,"Signal Area = {:.3f}".format(ut.signalIntegral(sf,ut.triggerTime(trig_val_i,trigValue,tfq),tfq,wmin=sWinMin,wmax=sWinMax)),transform = axes.transAxes)
        plt.text(0.2,0.3,"Pedestal Area = {:.3f}".format(ut.signalPedestal(sf,ut.triggerTime(trig_val_i,trigValue,tfq),tfq,wmin=sWinMin,wmax=sWinMax)),transform = axes.transAxes)
        plt.grid()
        plt.legend(fontsize=15)
        plt.savefig(folderName + "passedEvent{}.png".format(passedInd))
        plt.cla()
# testing purpose
if testP:
    print("Plotting troubleshooting plots...")
    folderName = "plots/troubleShooting/{}/".format(outFolder)
    ut.checkMakeDir(folderName)
    for i in range(len(troubles_SiPM_smooth)):
        passedInd = largetDiffEv[i]
        SiPM_val_i = troubles_SiPM_smooth[i]
        trig_val_i = troubles_trigger_smooth[i]
        sf = troubles_sf_smooth[i]
        windowInfo = troubles_window_smooth[i]
        plt.figure(figsize=(12,8))
        plt.plot(np.arange(0,len(SiPM_val_i))*tfq,SiPM_val_i,label="SiPM signal")
        plt.plot(np.arange(0,len(sf))*tfq,sf,label="Smoothed SiPM Signal")
        plt.xticks(np.arange(zSWin[0],zSWin[1],5))
        plt.vlines(ut.midPointEdge(windowInfo,sf,tfq,0.55),min(SiPM_val_i),0,color="magenta",label="SiPM Signal Edge 55%")
        plt.vlines(ut.midPointEdge(windowInfo,sf,tfq,percent=sPercent),min(SiPM_val_i),0,color="red",label="SiPM Signal Edge 60%")
        plt.vlines(ut.midPointEdge(windowInfo,sf,tfq,0.7),min(SiPM_val_i),0,color="green",label="SiPM Signal Edge 70%")
        plt.vlines(ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMin,min(SiPM_val_i),0,label="Time Window for Signal ID")
        plt.vlines(ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMax,min(SiPM_val_i),0)
        plt.ylabel("ADC Current")
        plt.xlabel("time (ns)")
        plt.xlim(ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMin,ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMax)
        plt.ylim(min(SiPM_val_i)-0.001,0.001)
        plt.text(ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMin-10,0,"Event {}".format(passedInd))
        plt.grid()
        plt.legend(fontsize=15)
        plt.savefig(folderName + "passedEvent{}.png".format(passedInd))
        plt.cla()
    plt.figure(figsize=(12,8))
    for i in range(len(troubles_SiPM_smooth)):
        SiPM_val_i = troubles_SiPM_smooth[i]
        trig_val_i = troubles_trigger_smooth[i]
        for i in range(len(SiPM_val_i)):
            if i*tfq < zSWin[0] or i*tfq > zSWin[1]:
                SiPM_val_i[i] = 0
        plt.plot(np.arange(0,len(SiPM_val_i))*tfq,SiPM_val_i,label="SiPM signal")
        plt.vlines(ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMin,min(SiPM_val_i),0,label="Time Window for Signal ID")
        plt.vlines(ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMax,min(SiPM_val_i),0)
        plt.xticks(np.arange(zSWin[0],zSWin[1],5))
        plt.xlim(zSWin[0],zSWin[1])
    plt.savefig(folderName + "rawEvent.png")
    plt.cla()
