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

mpl.rc("font", family="serif", size=15)

parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-d', dest='filename', type='string', default='Blue_laser_Keane_low_light_test_trig_1_SIPM_2_delay_22ns_5Gss.root', help="File name")
parser.add_option('-r', dest='rawPlot', action="store_true", help="Plotting raw triggers and signals")
parser.add_option('-p', dest='PEPlot', action="store_true", help="Plotting the PE peaks")
parser.add_option('-s', dest='smoothFit', action="store_true", help="Plotting smooth fit on the signals")
parser.add_option('-t', dest='trigTimeD', action="store_true", help="Trigger time edge distribution")
parser.add_option('-a', dest='aveNoise', action="store_true", help="Average noise in the signal")
options, args = parser.parse_args()
filename = options.filename
rawPlot = options.rawPlot
PEPlot = options.PEPlot
smoothFit = options.smoothFit
trigTimeD = options.trigTimeD
aveNoise = options.aveNoise

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
freq = pars[14] # in Gss
trig = pars[15]

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
# for plotting average noise
noiseList = []
noiseWindow = []

for count in range(0,nEvents):
    tr.GetEntry(count)
    trigger = tr.c1
    SiPM = tr.c2
    trigger_time = tr.t1
    SiPM_time = tr.t2

    if count == 1000:
        break

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

    # sf = ut.signalFilter(SiPM_val_i,win=fWinSize,pol=fWinPoly)
    sf = ut.butter_lowpass_filter(SiPM_val_i,300,5120,6)
    offset = ut.filterOffset(trig_val_i,trigValue)
    sf = sf[offset:]
    eventPedADC = ut.signalPedestal(sf,ut.triggerTime(trig_val_i,trigValue,tfq,trig),tfq,wmin=sWinMin,wmax=sWinMax)
    sf = np.concatenate( (sf,[eventPedADC]*offset) )
    triggerEdge = ut.triggerTime(trig_val_i,trigValue,tfq,trig)
    sigArea = ut.signalIntegral(sf,triggerEdge,tfq,sWinMin,sWinMax)
    windowDiff.append(ut.signalExistThreshold(SiPM_val_i,triggerEdge,tfq,sWinMin,sWinMax))
    if ut.signalExistThreshold(SiPM_val_i,triggerEdge,tfq,sWinMin,sWinMax) < pedADC:
        noiseList.append(SiPM_val_i)
        noiseWindow.append([triggerEdge+sWinMin,triggerEdge+sWinMax])
    windowInfo = ut.signalExist(sf,triggerEdge,tfq,pedADC,sPEADCMin,sPEADCMax,sWinMin,sWinMax,True)
# trigger
    trigTimeList.append( ut.triggerTime(trig_val_i,trigValue,tfq,trig) )
# signal
    if windowInfo:
        sigEdge = ut.midPointEdge(windowInfo,sf,tfq,percent=sPercent)
        edgeTimeDiff.append(sigEdge - triggerEdge)
        if len(SiPM_smooth_50) < 50:
            passedIndex.append(count)
            SiPM_smooth_50.append(SiPM_val_i)
            trigger_smooth_50.append(trig_val_i)
            sf_smooth_50.append(sf)
            window_smooth_50.append(windowInfo)
        # break

np.savez("edgeTimeDiff",edgeTimeDiff)
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
    plt.xticks( np.arange(zPEWinMin,zPEWinMax,0.0005) , rotation=90)
    plt.xlim(zPEWinMin,zPEWinMax)
    plt.savefig(folderName + "mmD_zoomedIn.png")
    plt.cla()

if trigTimeD:
    folderName = "plots/triggerTimeDist/{}/".format(outFolder)
    ut.checkMakeDir(folderName)
    plt.figure(figsize=(12,8))
    plt.hist(trigTimeList)
    axes = plt.gca()
    plt.text(0.75,0.9,"Minimum trigger time = {:.2f}".format(np.amin(trigTimeList)),transform = axes.transAxes)
    plt.text(0.75,0.8,"Average = {:.2f}".format(np.mean(trigTimeList)),transform = axes.transAxes)
    plt.text(0.75,0.7,"Standard Dev. = {:.2f}".format(np.std(trigTimeList,ddof=1)),transform = axes.transAxes)
    plt.xlabel("Trigger Time Edge (ns)")
    plt.ylabel("Events")
    plt.savefig(folderName + "trigTime.png")
    plt.cla()

if aveNoise:
    folderName = "plots/aveNoise/{}/".format(outFolder)
    ut.checkMakeDir(folderName)
    plt.figure(figsize=(12,8))
    noiseInWindow = []
    for i in range(len(noiseList)):
        nWin = noiseWindow[i]
        nMin = int(nWin[0]/tfq)
        nMax = int(nWin[1]/tfq)
        noise = noiseList[i][nMin:nMax]
        noiseInWindow.append(noise)
        plt.plot(np.arange(0,len(noise))*tfq,noise)
    noiseInWindow = np.array(noiseInWindow)
    avgNoise = np.mean(noiseInWindow,axis=0)
    plt.plot(np.arange(0,len(avgNoise))*tfq,avgNoise,linewidth=3,color="silver",label="Average noise")
    plt.xlabel("Adjusted Time (ns)")
    plt.ylabel("ADC")
    plt.legend()
    plt.savefig(folderName + "aveNoise.png")
    plt.cla()
    np.savez(folderName + "avgNoise",avgNoise=avgNoise)

# plot the smoothing fit
if smoothFit:
    print("Plotting smooth fit on the signals...")
    folderName = "plots/signalFit/{}/".format(outFolder)
    ut.checkMakeDir(folderName)
    nf = np.load("plots/aveNoise/{}/".format(outFolder) + "avgNoise.npz")
    print(nf.files)
    avgNoise = nf["avgNoise"]
    for i in range(len(SiPM_smooth_50)):
        SiPM_val_i = SiPM_smooth_50[i]
        trig_val_i = trigger_smooth_50[i]
        sf = sf_smooth_50[i]
        windowInfo = window_smooth_50[i]
        passedInd = passedIndex[i]
        sigWinMin = ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMin
        sigWinMax = ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMax
        SiPM_NoiseRed = SiPMSig_NoiseRed(avgNoise,SiPM_val_i,sigWinMin,sigWinMax,tfq)
        plt.figure(figsize=(12,8))
        plt.plot(np.arange(0,len(SiPM_NoiseRed))*tfq,SiPM_NoiseRed,label="SiPM signal (Noise Cancelled)")
        plt.plot(np.arange(0,len(SiPM_val_i))*tfq,SiPM_val_i,label="SiPM signal")
        # plt.plot(np.arange(0,len(sf))*tfq,sf,label="Filtered SiPM Signal")
        plt.xticks(np.arange(zSWin[0],zSWin[1],10))
        bottom,top = plt.ylim()
        # plt.vlines(ut.midPointEdge(windowInfo,sf,tfq,0.55),bottom,top,color="magenta",label="SiPM Signal Edge 55%")
        # plt.vlines(ut.midPointEdge(windowInfo,sf,tfq,percent=sPercent),bottom,top,color="red",label="SiPM Signal Edge 60%")
        # plt.vlines(ut.midPointEdge(windowInfo,sf,tfq,0.7),bottom,top,color="green",label="SiPM Signal Edge 70%")
        # plt.vlines(ut.minEdge(windowInfo,sf,tfq),bottom,top,color="orange",label="SiPM Signal Edge (minimum)")
        plt.vlines(sigWinMin,bottom,top,label="Time Window for Signal ID")
        plt.vlines(sigWinMax,bottom,top)
        plt.ylabel("ADC Current")
        plt.xlabel("time (ns)")
        print("Event {}".format(passedInd))
        print(ut.triggerTime(trig_val_i,trigValue,tfq)+sWinMin,trig)
        # plt.xlim(ut.triggerTime(trig_val_i,trigValue,tfq,trig)+sWinMin,ut.triggerTime(trig_val_i,trigValue,tfq,trig)+sWinMax)
        plt.ylim(min(SiPM_val_i)-0.001,0.001)
        axes = plt.gca()
        plt.text(ut.triggerTime(trig_val_i,trigValue,tfq,trig)+sWinMin-10,0,"Event {}".format(passedInd))
        plt.text(0.2,0.1,"Signal Edge = {:.2f} ns".format(ut.minEdge(windowInfo,sf,tfq)),transform = axes.transAxes)
        plt.text(0.2,0.2,"Signal Area = {:.3f}".format(ut.signalIntegral(sf,ut.triggerTime(trig_val_i,trigValue,tfq,trig),tfq,wmin=sWinMin,wmax=sWinMax)),transform = axes.transAxes)
        plt.text(0.2,0.3,"Pedestal Area = {:.3f}".format(ut.signalPedestal(sf,ut.triggerTime(trig_val_i,trigValue,tfq,trig),tfq,wmin=sWinMin,wmax=sWinMax)),transform = axes.transAxes)
        plt.grid()
        plt.legend(fontsize=15,loc="lower right")
        plt.savefig(folderName + "passedEvent{}.png".format(passedInd))
        plt.cla()
