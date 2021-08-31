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
parser.add_option('-r', dest='rawPlot', action="store_true", help="Plotting raw triggers and signals")
parser.add_option('-p', dest='PEPlot', action="store_true", help="Plotting the PE peaks")
parser.add_option('-t', dest='trigTimeD', action="store_true", help="Trigger time edge distribution")
parser.add_option('-a', dest='aveNoise', action="store_true", help="Average noise in the signal")
options, args = parser.parse_args()
filename = options.filename
rawPlot = options.rawPlot
PEPlot = options.PEPlot
trigTimeD = options.trigTimeD
aveNoise = options.aveNoise

outFolder = filename[:filename.find(".root")]
# parameters
if outFolder in parameters.keys():
    pars = parameters[outFolder]
else:
    pars = parameters["Blue_laser_Keane_low_light_test_trig_1_SIPM_2_delay_22ns_5Gss"]
pedADC = pars[0]
sWinMin = pars[2][0]
sWinMax = pars[2][1]
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

# for plotting raw signals and triggers
SiPM_50 = []
trigger_50 = []
SiPM_1000 = []
trigger_1000 = []
# for plotting min max diff
windowDiff = []
# for plotting trigger edge time distribution
trigTimeList = []
# for plotting average noise
noiseList = []
noiseWindow = []

for count in range(0,nEvents):
    tr.GetEntry(count)
    trigger = tr.c1
    SiPM = tr.c2

    if count % 10000 == 0:
        print(count)

    # if count == 1000:
    #     break

    trig_val_i = []
    SiPM_val_i = []

    for i in range(len(SiPM)):
        trig_val_i.append( trigger[i] )
        if SiPM[i] > 0:
            SiPM_val_i.append(0)
        else:
            SiPM_val_i.append( SiPM[i] )
    triggerEdge = ut.triggerTime(trig_val_i,trigValue,tfq,trig)
    sigWinMin = triggerEdge+sWinMin
    sigWinMax = triggerEdge+sWinMax
    if rawPlot:
        if count < 1000:
            SiPM_1000.append(SiPM_val_i)
            trigger_1000.append(trig_val_i)
        if count < 50:
            SiPM_50.append(SiPM_val_i)
            trigger_50.append(trig_val_i)
    if PEPlot:
        windowDiff.append(ut.signalExistThresholdMin(SiPM_val_i,triggerEdge,tfq,sWinMin,sWinMax))
    if trigTimeD:
        trigTimeList.append( ut.triggerTime(trig_val_i,trigValue,tfq,trig) )
    if aveNoise:
        if ut.signalExistThresholdMin(SiPM_val_i,triggerEdge,tfq,sWinMin,sWinMax) < pedADC:
            noiseList.append(SiPM_val_i)
            noiseWindow.append([sigWinMin,sigWinMax])

# plotting raw signals
if rawPlot:
    ut.plotNEvents(SiPM_50,"rawSignals",outFolder,10,tfq,zSWin)
    ut.plotNEvents(trigger_50,"rawTriggers",outFolder,10,tfq,zTWin)
    ut.plotNEvents(SiPM_1000,"rawSignals",outFolder,1000,tfq,zSWin)
    ut.plotNEvents(trigger_1000,"rawTriggers",outFolder,1000,tfq,zTWin)

# histogram difference between ADC min vs ADC max in signal region
if PEPlot:
    print("Making PE peak plots using maximum and minimum ADC in signal region using raw signals...")
    folderName = "plots/minThreshold/{}/".format(outFolder)
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
