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
parser.add_option('-s', dest='singlePE', action="store_true", help="Use only single PE signals")
parser.add_option('-q', dest='quick', action="store_true", help="Run over only the first 10000 events")
parser.add_option('-d', dest='filename', type='string', default='Blue_laser_Keane_low_light_test_trig_1_SIPM_2_delay_22ns_5Gss.root', help="File name")
options, args = parser.parse_args()

singlePE = options.singlePE
quick = options.quick
filename = options.filename

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
fitPars = pars[10]
trigValue = pars[11]
trigValue = pars[11]
fitFunctionChoice = pars[12]
binWidth = pars[13]
if len(pars) >= 15:
    freq = pars[14] # in Gss
else:
    freq = 5.0
if len(pars) >= 16:
    trig = pars[15]
tfq = 1./freq

inputFolder = "dataFiles/"
tf = rt.TFile.Open(inputFolder + filename)
tr = tf.Get("T")
nEvents = tr.GetEntries()

nDiv = 10 # how many sub datasets to divide the dataset into
nSubEvents = int(nEvents/nDiv)

if quick:
    nDiv = 1
    nSubEvents = 10000

# picking the right fit function
if fitFunctionChoice == "Gaus":
    fitFunction = ut.GaussianFit
elif fitFunctionChoice == "Exp":
    fitFunction = ut.ExponentialFit

# histogram details
bins=np.arange(tdhistXMin,tdhistXMax,binWidth)
binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
totalDataEntries = np.zeros(len(bins)-1)

sigEdgeList = []
trigEdgeList = []

start = 0
accEvent = 0
for i in range(nDiv):
    finish = start + nSubEvents
    print("Analyzing event {} to {}".format(start,finish))

    trigTimeList = []
    edgeTimeDiff = []

    if i == nDiv - 1:
        finish = nEvents

    for count in range(start,finish):
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

        # sf = ut.signalFilter(SiPM_val_i,win=fWinSize,pol=fWinPoly)
        sf = ut.butter_lowpass_filter(SiPM_val_i,300,5120,6)
        offset = ut.filterOffset(trig_val_i,trigValue)
        sf = sf[offset:]
        eventPedADC = ut.signalPedestal(sf,ut.triggerTime(trig_val_i,trigValue,tfq,trig),tfq,wmin=sWinMin,wmax=sWinMax)
        sf = np.concatenate( (sf,[eventPedADC]*offset) )
        triggerEdge = ut.triggerTime(trig_val_i,trigValue,tfq,trig)
        windowInfo = ut.signalExist(sf,triggerEdge,tfq,pedADC,sPEADCMin,sPEADCMax,sWinMin,sWinMax,singlePE)
    # trigger
        trigTimeList.append( ut.triggerTime(trig_val_i,trigValue,tfq,trig) )
        pedV = ut.sigPedVoltage(sf,triggerEdge,tfq,wmin=sWinMin,wmax=sWinMax)
    # signal
        if windowInfo:
            # sigEdge = ut.minEdge(windowInfo,sf,tfq)
            sigEdge = ut.midPointEdge(windowInfo,sf,tfq,percent=sPercent)
            edgeTimeDiff.append(sigEdge - triggerEdge)
            sigEdgeList.append(sigEdge)
            trigEdgeList.append(triggerEdge)
            accEvent += 1
    # binning the results
    xlab = "Time Difference between Signal and Trigger"
    data_entries,bins = np.histogram(edgeTimeDiff, bins=bins)
    totalDataEntries += data_entries
    start += nSubEvents
print("Number of single PE events: {}".format(accEvent))
print("Histogram for all {} events:".format(nEvents))
print(totalDataEntries)
# Generate enough x values to make the fit look smooth.
if fitFunctionChoice == "Gaus":
    xspace = np.linspace(tdhistXMin,tdhistXMax,100000)
    binscentersFit = binscenters
    totalDataEntriesFit = totalDataEntries
elif fitFunctionChoice == "Exp":
    xspace = np.linspace(binscenters[np.argmax(totalDataEntries)],tdhistXMax,100000)
    binscentersFit = binscenters[np.argmax(totalDataEntries):]
    totalDataEntriesFit = totalDataEntries[np.argmax(totalDataEntries):]

popt, pcov = curve_fit(fitFunction, xdata=binscentersFit, ydata=totalDataEntriesFit, p0=fitPars,maxfev = 10000)
perr = np.sqrt(np.diag(pcov))
print("Parameter errors:")
print(perr)
print("Number of Events Analyzed: {}".format(np.sum(totalDataEntriesFit)))
# Plot the histogram and the fitted function.
plt.figure(figsize=(12,8))
ut.histplot(totalDataEntries,binscenters,'#2a77b4','Histogram entries')

# fit function label
if fitFunctionChoice == "Gaus":
    fLabel = r'Fit function: $N e^{\frac{- (x-\mu)^2 }{2\sigma^2}}$'
    fParas = r"N={:.1f}$\pm${:.1f}; $\mu$={:.3f}$\pm${:.3f}; $\sigma$={:.3f}$\pm${:.3f}".format(popt[0],perr[0],popt[1],perr[1],abs(popt[2]),perr[2])
elif fitFunctionChoice == "Exp":
    fLabel = r'Fit function: $N e^{-x/\tau}$'
    f = 1/popt[1]
    errA = perr[1]
    A = popt[1]
    terr = abs(f*errA/A)
    fParas = r"N={:.1f}$\pm${:.1f}; $\tau$={:.3f}$\pm${:.3f}".format(popt[0],perr[0],1/popt[1],terr)
plt.plot(xspace+binWidth/2., fitFunction(xspace, *popt), color='darkorange', linewidth=2.5,
         label=fLabel)
plt.legend()
axes = plt.gca()
y_min, y_max = axes.get_ylim()
plt.text(0.5,0.75,fParas,fontsize=18,transform = axes.transAxes)
plt.text(0.5,0.7,"Events Analyse: {}".format(int(np.sum(totalDataEntriesFit))),fontsize=15,transform = axes.transAxes)
plt.ylabel("Events")
plt.xlabel("Time Difference between Signal and Trigger")
# naming the histogram
plotname = "timeDifference"
if quick:
    plotname += "_10000"
else:
    plotname += "_{}".format(nEvents)
if singlePE:
    plotname += "_1PE"

folderName = "plots/timeDiff/{}/".format(outFolder)
if not os.path.isdir(folderName):
    os.system("mkdir {}".format(folderName))
plt.savefig(folderName + plotname + ".png")
