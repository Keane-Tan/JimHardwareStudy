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
if len(pars) == 15:
    freq = pars[14] # in Gss
else:
    freq = 5.0
tfq = 1./freq

def triggerTime(trig_value_i):
    triTime = 0
    for j in range(len(trig_value_i)):
        if trig_value_i[j] > trigValue:
            triTime = j * tfq
            break
    return triTime

def sigPedVoltage(SiPM,triggerTime,wmin=sWinMin,wmax=sWinMax):
    wMin = triggerTime + wmin
    wMax = triggerTime + wmax
    return abs(np.mean(SiPM[int((wMin-10)/tfq):int((wMin)/tfq)]))

def signalPedestal(SiPM,triggerTime,wmin=sWinMin,wmax=sWinMax):
    wMin = triggerTime + wmin
    wMax = triggerTime + wmax
    return abs(np.mean(SiPM[int((wMin-10)/tfq):int((wMin)/tfq)])*(wMax-wMin))

def signalIntegral(SiPM_val_i,triggerTime,wmin=sWinMin,wmax=sWinMax):
    windowInt = 0
    for i in range(len(SiPM_val_i)):
        if (triggerTime + wmin < i*tfq < triggerTime + wmax):
            windowInt += SiPM_val_i[i]*tfq
    area = abs(windowInt) - signalPedestal(SiPM_val_i,triggerTime,wmin,wmax)
    if area < 0:
        return 0
    else:
        return area

# have to redefine the pedestal, because after smoothing the pedestal value also changes
def signalExist(SiPM_val_i,triggerTime,wmin=sWinMin,wmax=sWinMax,singlePE=False):
    windowValues = []
    windowIndices = []
    for i in range(len(SiPM_val_i)):
        if triggerTime + wmin < i*tfq < triggerTime + wmax: # this means there are only (27 - 18) x 5 = 45 data points within this window
            windowValues.append(SiPM_val_i[i])
            windowIndices.append(i)
    maxW = max(windowValues)
    minW = min(windowValues)

    windowInt = signalIntegral(SiPM_val_i,triggerTime,wmin=sWinMin,wmax=sWinMax)

    if singlePE: # the values for the difference came from looking at the distribution of the differences.
        ADCRequirement = windowInt > sPEADCMin and windowInt < sPEADCMax
    else:
        ADCRequirement = windowInt > pedADC # more than pedestal

    if (ADCRequirement) and (windowValues.index(maxW) < windowValues.index(minW)):
        return [windowValues,windowIndices]
    else:
        return False

def signalFilter(SiPM,win=31,pol=5): # 61, 3 seem to be the optimized values
    y = signal.savgol_filter(SiPM,
                           win, # window size used for filtering
                           pol), # order of fitted polynomial
    return y[0]

def midPointEdge(windowInfo,SiPM_val_i,percent=sPercent):
    windowValues = windowInfo[0]
    windowIndices = windowInfo[1]
    diff = (max(windowValues) - min(windowValues))
    mid = diff*percent + min(windowValues)
    mEdge = 0
    for i in windowIndices:
        if SiPM_val_i[i] < mid:
            mEdge = i*tfq
            break
    return mEdge

def GaussianFit(x, N, mu, sigma):
    return N * np.exp(-1.0 * (x - mu)**2 / (2 * sigma**2))

def ExponentialFit(x,N,l):
    return N*np.exp(-x*l)

def histplot(data,bins,color,label):
    binwidth = bins[1] - bins[0]
    print(len(bins))
    print(len(data))
    pbins = np.append(bins,bins[-1]+binwidth)
    pdata = np.append(data,data[-1])
    print(len(pbins))
    print(len(pdata))
    plt.step(pbins,pdata,where="post",color=color)
    plt.fill_between(pbins,pdata, step="post", color=color,label=label, alpha=1)

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
    fitFunction = GaussianFit
elif fitFunctionChoice == "Exp":
    fitFunction = ExponentialFit

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

        sf = signalFilter(SiPM_val_i)
        triggerEdge = triggerTime(trig_val_i)
        windowInfo = signalExist(sf,triggerEdge,sWinMin,sWinMax,singlePE)
    # trigger
        trigTimeList.append( triggerTime(trig_val_i) )
        pedV = sigPedVoltage(sf,triggerEdge)
    # signal
        if windowInfo:
            sigEdge = midPointEdge(windowInfo,sf)
            edgeTimeDiff.append(sigEdge - triggerEdge)
            sigEdgeList.append(sigEdge)
            trigEdgeList.append(triggerEdge)
            accEvent += 1
    # binning the results
    xlab = "Time Difference between Signal and Trigger"
    data_entries,bins = np.histogram(edgeTimeDiff, bins=bins)
    totalDataEntries += data_entries
    start += nSubEvents
np.savez("out.npz",sigEdge=sigEdgeList,trigEdge=trigEdgeList)
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
histplot(totalDataEntries,binscenters,'#2a77b4','Histogram entries')

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
