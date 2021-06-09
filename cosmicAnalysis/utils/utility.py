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

mpl.rc("font", family="serif", size=20)

def pulseTime(trig_value_i,trigValue,tpS):
    triTime = 0
    for j in range(len(trig_value_i)):
        if trig_value_i[j] < trigValue:
            triTime = j * tpS
            break
    return triTime

def signalPedestal(SiPM,sWinMin,tpS):
    if sWinMin - 10 < 0:
        return SiPM[int((sWinMin)/tpS)]
    else:
        return np.mean(SiPM[int((sWinMin-10)/tpS):int((sWinMin)/tpS)])

def minPedDiff(SiPM,sWinMin,sWinMax,tpS):
    minADC = np.min(SiPM[int(sWinMin/tpS):int(sWinMax/tpS)])
    pedADC = signalPedestal(SiPM,sWinMin,tpS)
    return pedADC - minADC

def checkMakeDir(folderName):
    if not os.path.isdir(folderName):
        os.system("mkdir {}".format(folderName))

def signalPedestalArea(SiPM,sWinMin,sWinMax,tpS):
    return abs(signalPedestal(SiPM,sWinMin,tpS))*(sWinMax-sWinMin)

def signalIntegralNoPSub(SiPM_val_i,sWinMin,sWinMax,tpS):
    windowInt = 0
    for i in range(len(SiPM_val_i)):
        if (sWinMin < i*tpS < sWinMax):
            windowInt += SiPM_val_i[i]*tpS
    area = abs(windowInt)
    if area < 0:
        return 0
    else:
        return area

def signalIntegral(SiPM_val_i,sWinMin,sWinMax,tpS):
    windowInt = 0
    for i in range(len(SiPM_val_i)):
        if (sWinMin < i*tpS < sWinMax):
            windowInt += SiPM_val_i[i]*tpS
    area = abs(windowInt) - signalPedestalArea(SiPM_val_i,sWinMin,sWinMax,tpS)
    if area < 0:
        return 0
    else:
        return area

def GaussianFit(x, N, mu, sigma):
    return N * np.exp(-1.0 * (x - mu)**2 / (2 * sigma**2))

# have to redefine the pedestal, because after smoothing the pedestal value also changes
def signalExist(SiPM_val_i,cosmicTime,gain,pedPE,sWinMin,sWinMax,tpS):
    windowValues = []
    windowIndices = []
    for i in range(len(SiPM_val_i)):
        if (sWinMin < i*tpS < sWinMax):
            windowValues.append(SiPM_val_i[i])
            windowIndices.append(i)
    windowInt = signalIntegral(SiPM_val_i,sWinMin,sWinMax,tpS)
    if gain <= 0:
        gain = 1
    ADCRequirement = windowInt/gain > pedPE # more than pedestal
    if (ADCRequirement) and (cosmicTime > 0):
        return [windowValues,windowIndices]
    else:
        return False

def butter_lowpass(cutoff, fs, order=6):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff=100, fs=2000, order=6):
    b, a = butter_lowpass(cutoff, fs, order)
    y = lfilter(b, a, data)
    return y

def minPedThreshEdge(SiPM_val_i,sWinMin,sWinMax,tpS,sPEADC,plot=False,nPE = 1.0):
    edgeTime = -999
    for i in range(len(SiPM_val_i)):
        if int(sWinMin/tpS) < i < int(sWinMax/tpS):
            if SiPM_val_i[i] <= 0-sPEADC*nPE+signalPedestal(SiPM_val_i,sWinMin,tpS):
                edgeTime = i*tpS
                break
    if plot:
        axes = plt.gca()
        plt.vlines(edgeTime,min(SiPM_val_i),0,color="orange")
        plt.hlines(0-sPEADC+signalPedestal(SiPM_val_i,sWinMin,tpS),sWinMin-10,sWinMax+10,color="orange")
        plt.text(0.65,0.5,"Signal edge (MPT) = {:.4f}".format(edgeTime),transform = axes.transAxes)
    return edgeTime

def midPointEdge(windowInfo,SiPM_val_i,tpS,percent=0.6):
    windowValues = windowInfo[0]
    windowIndices = windowInfo[1]
    diff = (max(windowValues) - min(windowValues))
    mid = diff*percent + min(windowValues)
    mEdge = 0
    for i in windowIndices:
        if SiPM_val_i[i] < mid:
            mEdge = i*tpS
            break
    return mEdge

def rsquared(obs,fit):
    return np.sum((obs-fit)**2)/np.mean(obs)

def linearFit(x,m,b):
    return m*x + b

def lineMatchEdge(SiPM_val_i,sWinMin,sWinMax,tpS,plot=False):
    base = signalPedestal(SiPM_val_i,sWinMin,tpS)
    minSig = np.min(SiPM_val_i[int(sWinMin/tpS):int(sWinMax/tpS)])
    ADC_5 = base - (abs(minSig-base)*0.05)
    ADC_85 = base - (abs(minSig-base)*0.3)
    data_5_85 = []
    time_5_85 = []
    for i in range(len(SiPM_val_i)):
        loopBreak = False
        if int(sWinMin/tpS) < i < int(sWinMax/tpS):
            if SiPM_val_i[i] <= ADC_5 and i > int(sWinMin/tpS):
                data_5_85.append(SiPM_val_i[i])
                time_5_85.append(i*tpS)
            if SiPM_val_i[i] < ADC_85:
                loopBreak = True
        if loopBreak:
            break
    if len(data_5_85) >= 2:
        data_5_85 = np.array(data_5_85)
        time_5_85 = np.array(time_5_85)
        xran = np.linspace(sWinMin*tpS,max(time_5_85),1000)
        popt, pcov = curve_fit(linearFit, xdata=time_5_85, ydata=data_5_85, p0=[2.0,2.0],maxfev = 10000)
        rs = rsquared(data_5_85,linearFit(time_5_85,popt[0],popt[1]))
        if plot:
            axes = plt.gca()
            plt.plot(time_5_85,data_5_85,color="orange")
            plt.plot(xran,linearFit(xran,popt[0],popt[1]),color="magenta")
            plt.vlines((base - popt[1])/popt[0],min(SiPM_val_i),0,color="#4294bd")
            plt.text(0.65,0.7,"Signal edge = {:.2f}".format((base - popt[1])/popt[0]),transform = axes.transAxes)
        return [(base - popt[1])/popt[0],abs(rs)]
    else:
        return [-999,np.Inf]

def fitPEPeak(data_entries,binscenters,xmin,xmax,p0List,color,fitFunc=GaussianFit):
    fitBins = []
    fitData = []
    for i in range(len(binscenters)):
        if xmin < binscenters[i] < xmax:
            fitBins.append(binscenters[i])
            fitData.append(data_entries[i])
    popt, pcov = curve_fit(fitFunc, xdata=fitBins, ydata=fitData, p0=p0List, maxfev = 10000)
    xspace = np.linspace(min(fitBins),max(fitBins),1000)
    plt.plot(xspace, fitFunc(xspace, *popt), color=color, linewidth=3,label="mean = {:.4f}".format(popt[1]))
    return popt[1]

def histplot(data,bins,color,label):
    binwidth = bins[1] - bins[0]
    pbins = np.append(bins,bins[-1]+binwidth)
    pdata = np.append(data,data[-1])
    plt.step(pbins,pdata,where="post",color=color)
    plt.fill_between(pbins,pdata, step="post", color=color,label=label, alpha=1)

def plotNEvents(events,subfolder,outfolder,nEvent,sWinMin,sWinMax,tpS,label=None):
    nDiv = int(len(events)/nEvent)
    st = 0

    folderName = "plots/{}/{}/".format(subfolder,outfolder)
    checkMakeDir(folderName)

    for i in range(nDiv):
        en = st + nEvent
        if label == "LED":
            plotName = "Events_{}-{}_trigger.png".format(st,en)
            zplotName = "Events_ZoomedIn_{}-{}_trigger.png".format(st,en)
        elif label == "cosmic":
            plotName = "Events_{}-{}_cosmic.png".format(st,en)
            zplotName = "Events_ZoomedIn_{}-{}_cosmic.png".format(st,en)
        else:
            plotName = "Events_{}-{}.png".format(st,en)
            zplotName = "Events_ZoomedIn_{}-{}.png".format(st,en)

        plt.figure(figsize=(12,8))
        for j in range(st,en):
            signal = events[j]
            plt.plot(np.arange(0,len(signal))*tpS,signal)
        plt.grid()
        print("Saving events {}-{} to {}...".format(st,en,folderName))
        plt.savefig(folderName + plotName)
        plt.figure(figsize=(12,8))
        for j in range(st,en):
            signal = events[j]
            for i in range(len(signal)):
                if i*tpS < sWinMin or i*tpS > sWinMax:
                    signal[i] = signalPedestal(signal,sWinMin,tpS)
            plt.plot(np.arange(0,len(signal))*tpS,signal)
        plt.xlim(sWinMin,sWinMax)
        # plt.ylim(-0.05,0.01)
        plt.grid()
        plt.savefig(folderName + zplotName)
        plt.cla()
        st += nEvent

def getSignal(SiPM,cosmicTime,gain,pedPE,sWinMin,sWinMax,tpS,cutoff,fs,order,offset):
    SiPM_val_i = []

    for i in range(len(SiPM)):
        # making a hard cut off at SiPM ADC current > 0, because it should not be more than 0.
        if SiPM[i] > 0:
            SiPM_val_i.append(0)
        else:
            SiPM_val_i.append( SiPM[i] )

    lf = butter_lowpass_filter(SiPM_val_i,cutoff,fs,order)[offset:]
    eventPedADC = signalPedestal(lf,sWinMin,tpS)
    lf = np.concatenate( (lf,[eventPedADC]*offset) )
    windowInfo = signalExist(lf,cosmicTime,gain,pedPE,sWinMin,sWinMax,tpS)
    return [windowInfo,lf]

def histoFill(edgeTimeDiff,totalDataEntries,bins):
    data_entries,bins = np.histogram(edgeTimeDiff, bins=bins)
    totalDataEntries += data_entries

def GaussianFit(x, N, mu, sigma):
    return N * np.exp(-1.0 * (x - mu)**2 / (2 * sigma**2))

def ExponentialFit(x,N,l):
    return N*np.exp(-x*l)

def fitAndPlot(totalDataEntries,binscentersFit,color,fitPars,fitFunction,xspace):
    totalDataEntriesFit = totalDataEntries
    mode = binscentersFit[np.argmax(totalDataEntries)]
    fitPars[1] = mode
    popt, pcov = curve_fit(fitFunction, xdata=binscentersFit, ydata=totalDataEntriesFit, p0=fitPars,maxfev = 10000)
    perr = np.sqrt(np.diag(pcov))
    fParas = r"$\mu$={:.2f}({:.2f}); $\sigma$={:.2f}({:.2f})".format(popt[1],perr[1],abs(popt[2]),perr[2])
    plt.plot(xspace, fitFunction(xspace, *popt), color=color, linewidth=3,label=fParas)
    print(fParas)
