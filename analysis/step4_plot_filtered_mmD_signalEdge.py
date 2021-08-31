import ROOT as rt
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import optparse
from parameters import parameters
from utils import utility as ut

mpl.rc("font", family="serif", size=15)

parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-d', dest='filename', type='string', default='Blue_laser_Keane_low_light_test_trig_1_SIPM_2_delay_22ns_5Gss.root', help="File name")
parser.add_option('-p', dest='PEPlot', action="store_true", help="Plotting the PE peaks")
parser.add_option('-s', dest='sigEdgeFit', action="store_true", help="Plotting filtered signals")
parser.add_option('-t', dest='timeDiff', action="store_true", help="Storing time difference between signal edge and trigger edge")
options, args = parser.parse_args()
filename = options.filename
PEPlot = options.PEPlot
sigEdgeFit = options.sigEdgeFit
timeDiff = options.timeDiff

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
sPercent = pars[5]
zSWin = pars[7]
trigValue = pars[11]
freq = pars[14] # in Gss
trig = pars[15]
zPEWinMin = pars[17][0]
zPEWinMax = pars[17][1]

print("sampling frequency: {} Gss".format(freq))
tfq = 1./freq
print("Time per bin: {} ns".format(tfq))

inputFolder = "dataFiles/"
tf = rt.TFile.Open(inputFolder + filename)
tr = tf.Get("T")
nEvents = tr.GetEntries()

# for plotting max min diff
windowDiff = []
# for plotting all filtered signals that pass the threshold
passedFilt = []
# loading noise-reduced signals
filSigs = np.load("processedData/{}/filtSig.npz".format(outFolder))
eventList = sorted(filSigs.files,key=int)

sfolderName = "plots/signalFit/{}/".format(outFolder)
ut.checkMakeDir(sfolderName)
sefCount = 0
midPointSigEdge = []
minSigEdge = []

for count in eventList:
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

    triggerEdge = ut.triggerTime(trig_val_i,trigValue,tfq,trig)
    if PEPlot:
        windowDiff.append(ut.signalExistThresholdArea(sf,triggerEdge,tfq,sWinMin,sWinMax))
    windowInfo = ut.signalExist(sf,triggerEdge,tfq,pedADC,sPEADCMin,sPEADCMax,sWinMin,sWinMax,True)
    if windowInfo:
        if timeDiff:
            midPointSigEdge.append(ut.midPointEdge(windowInfo,sf,tfq,percent=sPercent) - triggerEdge)
            minSigEdge.append(ut.minEdge(windowInfo,sf,tfq) - triggerEdge)
        if sigEdgeFit:
            passedFilt.append(sf)
            if sefCount < 50:
                sigWinMin = triggerEdge+sWinMin
                sigWinMax = triggerEdge+sWinMax
                plt.figure(figsize=(12,8))
                plt.plot(np.arange(0,len(SiPM_val_raw))*tfq,SiPM_val_raw,label="Raw SiPM signal")
                plt.plot(np.arange(0,len(sf))*tfq,sf,label="Filtered SiPM Signal")
                bottom,top = plt.ylim()
                plt.vlines(ut.midPointEdge(windowInfo,sf,tfq,percent=sPercent),bottom,top,color="red",label="SiPM Signal Edge 60%")
                plt.vlines(ut.minEdge(windowInfo,sf,tfq),bottom,top,color="orange",label="SiPM Signal Edge (minimum)")
                plt.vlines(sigWinMin,bottom,top,label="Time Window for Signal ID")
                plt.vlines(sigWinMax,bottom,top)
                plt.ylabel("ADC Current")
                plt.xlabel("time (ns)")
                plt.xticks(np.arange(zSWin[0],zSWin[1],10))
                plt.ylim(min(SiPM_val_raw[int(sigWinMin/tfq):int(sigWinMax/tfq)])-0.001,0.001)
                axes = plt.gca()
                plt.text(sigWinMin-10,0,"Event {}".format(count))
                plt.text(0.2,0.1,"Signal Edge = {:.2f} ns".format(ut.minEdge(windowInfo,sf,tfq)),transform = axes.transAxes)
                plt.text(0.2,0.2,"Signal Area = {:.3f}".format(ut.signalIntegral(sf,triggerEdge,tfq,wmin=sWinMin,wmax=sWinMax)),transform = axes.transAxes)
                plt.text(0.2,0.3,"Pedestal Area = {:.3f}".format(abs(ut.signalPedestal(sf,triggerEdge,tfq,wmin=sWinMin,wmax=sWinMax))),transform = axes.transAxes)
                plt.grid()
                plt.legend(fontsize=15,loc="lower right")
                plt.savefig(sfolderName + "passedEvent{}.png".format(count))
                plt.cla()
            sefCount += 1

if timeDiff:
    folderName = "processedData/{}".format(outFolder)
    ut.checkMakeDir(folderName)
    np.savez("{}/timeDifference".format(folderName),midPointSigEdge=midPointSigEdge,minSigEdge=minSigEdge)

# histogram difference between ADC min vs ADC max in signal region
if PEPlot:
    print("Making PE peak plots using maximum and minimum ADC in signal region after smoothing signal...")
    folderName = "plots/areaThreshold/{}/".format(outFolder)
    ut.checkMakeDir(folderName)
    plt.figure(figsize=(12,8))
    plt.hist(windowDiff,bins=np.linspace(0,max(windowDiff)*1.01,200))
    plt.xlabel("Signal Area (After Pedestal Subtraction)")
    plt.ylabel("Number of Events")
    plt.grid()
    plt.savefig(folderName + "mmD.png")
    ## zoomed in
    plt.xticks( np.arange(zPEWinMin,zPEWinMax,0.05) , rotation=90)
    plt.xlim(zPEWinMin,zPEWinMax)
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
