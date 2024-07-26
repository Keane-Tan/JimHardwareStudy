import ROOT as rt
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import optparse
from parameters import parameters
from utils import utility as ut
import os

mpl.rc("font", family="serif", size=15)

parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-d', dest='filename', type='string', default='Blue_laser_Keane_low_light_test_trig_1_SIPM_2_delay_22ns_5Gss.root', help="File name")
parser.add_option('-p', dest='PEPlot', action="store_true", help="Plotting the PE peaks")
parser.add_option('-s', dest='sigEdgeFit', action="store_true", help="Plotting filtered signals")
parser.add_option('-m', dest='minPEDiff', action="store_true", help="Plotting the difference between minimum and Pedestal")
parser.add_option('-t', dest='timeDiff', action="store_true", help="Storing time difference between signal edge and trigger edge")
options, args = parser.parse_args()
filename = options.filename
PEPlot = options.PEPlot
minPEDiff = options.minPEDiff
sigEdgeFit = options.sigEdgeFit
timeDiff = options.timeDiff

outFolder = filename[:filename.find(".root")]
# parameters
pars = parameters[outFolder]
pedADC = pars.pedADC
sPEADCMin,sPEADCMax = pars.sPEADC
sWinMin,sWinMax = pars.sWin
sPercent = pars.sPercent
zSWin = pars.zSWin
trigValue = pars.trigValue
freq = pars.freq # in Gss
trigPol = pars.trigPol
aPEWinMin,aPEWinMax,aPEWidth = pars.aPEWin
pD0,hDw = pars.eSPE
zDWinMin,zDWinMax,zDWinWidth = pars.zDWin
aPEScan = pars.aPEScan

print("sampling frequency: {} Gss".format(freq))
tfq = 1./freq
print("Time per bin: {} ns".format(tfq))

inputFolder = "root://cmseos.fnal.gov//store/user/keanet/Hardware/analysis/dataFiles/"
tf = rt.TFile.Open(inputFolder + filename)
tr = tf.Get("T")
nEvents = tr.GetEntries()

minPedDiff = []
# for plotting max min diff
windowDiff = []
# for plotting all filtered signals that pass the threshold
passedFilt = []
# delete noise reduced signals
if os.path.isfile("processedData/{}/sigRedNoise.npz".format(outFolder)):
    os.system("rm processedData/{}/sigRedNoise.npz".format(outFolder))
# loading filtered signals
filSigs = np.load("/eos/uscms/store/user/keanet/Hardware/analysis/processedData/{}/filtSig.npz".format(outFolder))
eventList = sorted(filSigs.files,key=int)

sfolderName = "plots/signalFit/{}/".format(outFolder)
ut.checkMakeDir(sfolderName)
sefCount = 0
midPointSigEdge = []
minSigEdge = []
minPedEdge_0p5 = []
minPedEdge_0p75 = []
minPedEdge = []

print("Number of events to process: {}".format(len(eventList)))
evC = 0
for count in eventList:
    if evC % 1000 == 0:
        print(evC)
    evC += 1
    # if evC == 1000:
    #     break
    sf = filSigs[count]
    count = int(count)
    tr.GetEntry(count)
    trigger = tr.c1
    SiPM = tr.c2

    trig_val_i = list(trigger)
    SiPM_val_raw = []

    for i in range(len(SiPM)):
        if SiPM[i] > 0:
            SiPM_val_raw.append(0)
        else:
            SiPM_val_raw.append( SiPM[i] )

    triggerEdge = ut.triggerTime(trig_val_i,trigValue,tfq,trigPol)
    sigWinMin = triggerEdge+sWinMin
    sigWinMax = triggerEdge+sWinMax
    if minPEDiff:
        minPedDiff.append(ut.minPedDiff(sf,triggerEdge,tfq,sWinMin,sWinMax))
    if PEPlot:
        windowDiff.append(ut.signalExistThresholdArea(sf,triggerEdge,tfq,sWinMin,sWinMax))
    windowInfo = ut.signalExist(sf,triggerEdge,tfq,pedADC,sPEADCMin,sPEADCMax,sWinMin,sWinMax,True)
    if windowInfo:
        if timeDiff:
            midADC,mpSE = ut.midPointEdge(windowInfo,sf,tfq,percent=sPercent)
            midPointSigEdge.append(mpSE - triggerEdge)
            minSigEdge.append(ut.minEdge(windowInfo,sf,tfq) - triggerEdge)
            minPedEdge_0p5.append(ut.peFracEdge(sf,triggerEdge,sWinMin,sWinMax,tfq,pD0,nPE = 0.5) - triggerEdge)
            minPedEdge_0p75.append(ut.peFracEdge(sf,triggerEdge,sWinMin,sWinMax,tfq,pD0,nPE = 0.75) - triggerEdge)
            minPedEdge.append(ut.peFracEdge(sf,triggerEdge,sWinMin,sWinMax,tfq,pD0,nPE = 1.0) - triggerEdge)
        if sigEdgeFit:
            passedFilt.append(sf)
            if sefCount < 50:
                midADC,mpSE = ut.midPointEdge(windowInfo,sf,tfq,percent=sPercent)
                plt.figure(figsize=(12,8))
                plt.plot(np.arange(0,len(SiPM_val_raw))*tfq,SiPM_val_raw,label="Raw SiPM signal")
                plt.plot(np.arange(0,len(sf))*tfq,sf,label="Filtered SiPM Signal")
                bottom,top = plt.ylim()
                plt.vlines(mpSE,bottom,top,color="red",label="Signal Edge")
                plt.hlines(midADC,sigWinMin,sigWinMax,color="red",linestyle=":",linewidth=3,label="60% between Max and Min ADC")
                # plt.vlines(ut.minEdge(windowInfo,sf,tfq),bottom,top,color="orange",label="SiPM Signal Edge (minimum)")
                # if ut.peFracEdge(sf,triggerEdge,sWinMin,sWinMax,tfq,pD0,nPE = 1.0) != -999:
                #     plt.vlines(ut.peFracEdge(sf,triggerEdge,sWinMin,sWinMax,tfq,pD0,nPE = 1.0),bottom,top,color="magenta",label="SiPM Signal Edge (1 PE)")
                # plt.vlines(sigWinMin,bottom,top,label="Time Window for Signal ID")
                # plt.vlines(sigWinMax,bottom,top)
                plt.ylabel("ADC Current")
                plt.xlabel("time (ns)")
                plt.xticks(np.arange(zSWin[0],zSWin[1],10))
                if len(SiPM_val_raw[int(sigWinMin/tfq):int(sigWinMax/tfq)]) > 0:
                    plt.ylim(min(SiPM_val_raw[int(sigWinMin/tfq):int(sigWinMax/tfq)])-0.001,0.001)
                axes = plt.gca()
                # plt.text(sigWinMin-10,0,"Event {}".format(count))
                plt.text(0.7,0.25,"Signal Edge = {:.2f} ns".format(ut.minEdge(windowInfo,sf,tfq)),transform = axes.transAxes)
                plt.text(0.7,0.30,"Signal Area = {:.3f}".format(ut.signalIntegral(sf,triggerEdge,tfq,wmin=sWinMin,wmax=sWinMax)),transform = axes.transAxes)
                plt.text(0.7,0.35,"Pedestal Area = {:.3f}".format(abs(ut.signalPedestal(sf,triggerEdge,tfq,wmin=sWinMin,wmax=sWinMax))),transform = axes.transAxes)
                plt.xlim(sigWinMin,sigWinMax)
                plt.grid()
                plt.legend(fontsize=15,loc="lower right")
                plt.savefig(sfolderName + "passedEvent{}.png".format(count))
                plt.cla()
            sefCount += 1

if timeDiff:
    localOutFolder = "processedData/{}".format(outFolder)
    fullOutFolder = "root://cmseos.fnal.gov//store/user/keanet/Hardware/analysis/processedData/{}".format(outFolder)
    np.savez("{}/timeDifference".format(localOutFolder),midPointSigEdge=midPointSigEdge,minSigEdge=minSigEdge,minPedEdge_0p5=minPedEdge_0p5,minPedEdge_0p75=minPedEdge_0p75,minPedEdge=minPedEdge)
    os.system("xrdcp -f {}/timeDifference.npz {}/timeDifference.npz".format(localOutFolder,fullOutFolder))
    os.system("rm {}/timeDifference.npz".format(localOutFolder))


if minPEDiff:
    folderName = "plots/minPedDiff/{}/".format(outFolder)
    ut.checkMakeDir(folderName)
    plt.figure(figsize=(12,8))
    data_entries,bins = np.histogram(minPedDiff, bins=1000)
    binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
    ut.histplot(data_entries,binscenters,"blue","Data")
    plt.xlabel("Difference between Minimum ADC and Pedestal")
    plt.ylabel("Number of Events")
    plt.grid()
    plt.savefig(folderName + "mpD.png")
    ## zoomed in
    plt.xticks( np.arange(zDWinMin,zDWinMax,zDWinWidth) , rotation=90)
    plt.xlim(zDWinMin,zDWinMax)
    ut.fitPEPeak(data_entries,binscenters,pD0-hDw,pD0+hDw,[max(data_entries),pD0,0.01],"red")
    plt.legend()
    plt.savefig(folderName + "mpD_zoomedIn.png")
    plt.cla()

# histogram difference between ADC min vs ADC max in signal region
if PEPlot:
    print("Making PE peak plots using maximum and minimum ADC in signal region after smoothing signal...")
    folderName = "plots/areaThreshold/{}/".format(outFolder)
    ut.checkMakeDir(folderName)
    windowDiff = np.array(windowDiff)
    windowDiff = windowDiff[np.logical_not(np.isnan(windowDiff))]
    plt.figure(figsize=(12,8))
    if aPEScan == "auto":
        plt.hist(windowDiff,bins=np.linspace(0,np.nanmax(windowDiff)*1.01,200))
    else:
        plt.hist(windowDiff,bins=np.linspace(aPEScan[0],aPEScan[1],200))
    plt.xlabel("Signal Area (After Pedestal Subtraction)")
    plt.ylabel("Number of Events")
    plt.grid()
    plt.savefig(folderName + "mmD.png")
    ## zoomed in
    plt.xticks( np.arange(aPEWinMin,aPEWinMax,aPEWidth) , rotation=90)
    plt.xlim(aPEWinMin,aPEWinMax)
    plt.savefig(folderName + "mmD_zoomedIn.png")
    plt.cla()

if sigEdgeFit:
    plt.figure(figsize=(12,8))
    sfMin = []
    for sf in passedFilt:
        sfMin.append(min(SiPM_val_raw[10:-10]))
        plt.plot(np.arange(0,len(sf))*tfq,sf)
    plt.ylim(min(sfMin)-0.001,0.001)
    plt.savefig(sfolderName + "allPassedEvent.png")
