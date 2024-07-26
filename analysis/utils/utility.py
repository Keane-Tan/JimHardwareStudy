# sample command: python cosmicSignalExploration_lfilter.py -d cosmics_Mar_26_1p4fiber_61cm_5by2by20_one_hole_white_extrusion_1p2meter_long_5gss.root -r -p -s
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz
from scipy import signal
from scipy.optimize import curve_fit
import os
import ROOT as rt

mpl.rc("font", family="serif", size=20)

def checkMakeDir(folderName):
    if not os.path.isdir(folderName):
        os.system("mkdir {}".format(folderName))

def triggerTime(trig_value_i,trigValue,tfq,trig="pos"):
    triTime = 0
    for j in range(10,len(trig_value_i)-10):
        if trig_value_i[j] > trigValue and trig == "pos":
            triTime = j * tfq
            break
        elif trig_value_i[j] < trigValue and trig == "neg":
            triTime = j * tfq
            break
    return triTime

# return the index of the element in the list whose value is closest to val.
def indBasedVal(val,alist):
    clist = np.abs(np.array(alist) - val)
    return np.argmin(clist)

def sigPedVoltage(SiPM,triggerTime,tfq,wmin,wmax):
    wMin = triggerTime + wmin
    wMax = triggerTime + wmax
    return np.mean(SiPM[int((wMin-10)/tfq):int((wMin)/tfq)])

def signalPedestal(SiPM,triggerTime,tfq,wmin,wmax):
    wMin = triggerTime + wmin
    wMax = triggerTime + wmax
    return sigPedVoltage(SiPM,triggerTime,tfq,wmin,wmax)*(wMax-wMin)

def minPedDiff(SiPM,triggerTime,tfq,wmin,wmax):
    wMin = triggerTime + wmin
    wMax = triggerTime + wmax
    minADC = np.min(SiPM[int(wMin/tfq):int(wMax/tfq)])
    pedADC = sigPedVoltage(SiPM,triggerTime,tfq,wmin,wmax)
    return pedADC - minADC

def signalIntegral(SiPM_val_i,triggerTime,tfq,wmin,wmax):
    windowInt = 0
    for i in range(len(SiPM_val_i)):
        if (triggerTime + wmin < i*tfq < triggerTime + wmax):
            windowInt += SiPM_val_i[i]*tfq
    area = windowInt - signalPedestal(SiPM_val_i,triggerTime,tfq,wmin,wmax)
    if area > 0:
        return 0
    else:
        return abs(area)

# this is based on the difference between max ADC and min ADC
def signalExistThresholdmmD(SiPM_val_i,triggerTime,tfq,wmin,wmax):
    windowValues = []
    for i in range(len(SiPM_val_i)):
        if triggerTime + wmin < i*tfq < triggerTime + wmax:
            windowValues.append(SiPM_val_i[i])
    minW = min(windowValues)
    pedADC = sigPedVoltage(SiPM_val_i,triggerTime,tfq,wmin,wmax)
    return abs(minW - pedADC)

def signalExistThresholdMin(SiPM_val_i,triggerTime,tfq,wmin,wmax):
    windowValues = []
    for i in range(len(SiPM_val_i)):
        if triggerTime + wmin < i*tfq < triggerTime + wmax:
            windowValues.append(SiPM_val_i[i])
    minW = min(windowValues)
    return abs(minW)

# this is based on the area under graph for the signal
def signalExistThresholdArea(SiPM_val_i,triggerTime,tfq,wmin,wmax):
    return signalIntegral(SiPM_val_i,triggerTime,tfq,wmin,wmax)

# this is based on max min ADC diff
# def signalExist(SiPM_val_i,triggerTime,tfq,wmin,wmax,singlePE=False):
#     windowValues = []
#     windowIndices = []
#     for i in range(len(SiPM_val_i)):
#         if triggerTime + wmin < i*tfq < triggerTime + wmax: # this means there are only (27 - 18) x 5 = 45 data points within this window
#             windowValues.append(SiPM_val_i[i])
#             windowIndices.append(i)
#     maxW = max(windowValues)
#     minW = min(windowValues)
#     maxMinDiff = maxW - minW
#
#     if singlePE: # the values for the difference came from looking at the distribution of the differences.
#         ADCRequirement = maxMinDiff > sPEADCMin and maxMinDiff < sPEADCMax
#     else:
#         ADCRequirement = maxMinDiff > pedADC # more than pedestal
#
#     if (ADCRequirement) and (windowValues.index(maxW) < windowValues.index(minW)):
#         return [windowValues,windowIndices]
#     else:
#         return False

# this is based on signal integration
def signalExist(SiPM_val_i,triggerTime,tfq,pedADC,sPEADCMin,sPEADCMax,wmin,wmax,singlePE=False):
    windowValues = []
    windowIndices = []
    for i in range(len(SiPM_val_i)):
        if triggerTime + wmin < i*tfq < triggerTime + wmax: # this means there are only (27 - 18) x 5 = 45 data points within this window
            windowValues.append(SiPM_val_i[i])
            windowIndices.append(i)
    windowInt = signalIntegral(SiPM_val_i,triggerTime,tfq,wmin,wmax)

    if singlePE: # the values for the difference came from looking at the distribution of the differences.
        ADCRequirement = sPEADCMin < windowInt < sPEADCMax
    else:
        ADCRequirement = windowInt > pedADC # more than pedestal

    if ADCRequirement:
        return [windowValues,windowIndices]
    else:
        return False

def SiPMSig_NoiseRed(avgNoise,SiPM_val_i,sigWinMin,sigWinMax,tfq):
    avgNoiseMod = [0]*int(sigWinMin/tfq) + list(avgNoise)
    diff = len(SiPM_val_i)-len(avgNoiseMod)
    avgNoiseMod = avgNoiseMod + [0]*(len(SiPM_val_i)-len(avgNoiseMod))
    if len(SiPM_val_i) != len(avgNoiseMod):
        SiPM_NoiseRed = np.array(SiPM_val_i)
    else:
        SiPM_NoiseRed = np.array(SiPM_val_i) - np.array(avgNoiseMod)
    return SiPM_NoiseRed

def signalFilter(SiPM,win,pol): # 61, 3 seem to be the optimized values
    y = signal.savgol_filter(SiPM,
                           win, # window size used for filtering
                           pol), # order of fitted polynomial
    return y[0]

def butter_lowpass(cutoff, fs, order=6):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff=300, fs=5120, order=6):
    b, a = butter_lowpass(cutoff, fs, order)
    y = lfilter(b, a, data)
    return y

def filterOffset(trig_val_i,trigValue,trig): # match the locations of the trigger edge
    tf1 = butter_lowpass_filter(trig_val_i,300,5120,6)
    return abs(triggerTime(trig_val_i,trigValue,1,trig) - triggerTime(tf1,trigValue,1,trig))

def midPointEdge(windowInfo,SiPM_val_i,tfq,percent):
    windowValues = windowInfo[0]
    windowIndices = windowInfo[1]
    diff = (max(windowValues) - min(windowValues))
    mid = diff*percent + min(windowValues)
    mEdge = 0
    for i in windowIndices:
        if SiPM_val_i[i] < mid:
            mEdge = i*tfq
            break
    return mid,mEdge

def peFracEdge(SiPM_val_i,triggerTime,wmin,wmax,tfq,sPEADC,nPE = 1.0):
    edgeTime = -999
    sWinMin = triggerTime + wmin
    sWinMax = triggerTime + wmax
    for i in range(len(SiPM_val_i)):
        if int(sWinMin/tfq) < i < int(sWinMax/tfq):
            if SiPM_val_i[i] <= 0-sPEADC*nPE+sigPedVoltage(SiPM_val_i,triggerTime,tfq,wmin,wmax):
                edgeTime = i*tfq
                break
    return edgeTime

def minEdge(windowInfo,SiPM_val_i,tfq):
    windowIndices = windowInfo[1]
    return (windowIndices[0]+np.argmin(SiPM_val_i[windowIndices[0]:windowIndices[-1]]))*tfq


def GaussianFit(x, N, mu, sigma):
    return N * np.exp(-1.0 * (x - mu)**2 / (2 * sigma**2))

def ExponentialFit(x,N,l):
    return N*np.exp(-x*l)

def plotNEvents(events,subfolder,outfolder,nEvent,tfq,xlim=[0,200]):
    nDiv = int(len(events)/nEvent)
    st = 0

    folderName = "plots/{}/{}/".format(subfolder,outfolder)
    checkMakeDir(folderName)

    for i in range(nDiv):
        en = st + nEvent
        plt.figure(figsize=(12,8))
        for j in range(st,en):
            signal = events[j]
            plt.plot(np.arange(0,len(signal))*tfq,signal)
        print("Saving events {}-{} to {}...".format(st,en,folderName))
        plt.savefig(folderName + "Events_{}-{}.png".format(st,en))
        plt.figure(figsize=(12,8))
        for j in range(st,en):
            signal = events[j]
            for i in range(len(signal)):
                if i*tfq < xlim[0] or i*tfq > xlim[1]:
                    signal[i] = 0
            plt.plot(np.arange(0,len(signal))*tfq,signal)
        plt.xlim(xlim[0],xlim[1])
        # plt.ylim(-0.05,0.01)
        plt.savefig(folderName + "Events_ZoomedIn_{}-{}.png".format(st,en))
        plt.cla()
        st += nEvent

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
    print(len(bins))
    print(len(data))
    pbins = np.append(bins,bins[-1]+binwidth)
    pdata = np.append(data,data[-1])
    print(len(pbins))
    print(len(pdata))
    plt.step(pbins,pdata,where="post",color=color)
    plt.fill_between(pbins,pdata, step="post", color=color,label=label, alpha=1)

def convertToTHist(totalDataEntries,binscenters):
    binscenters = np.array(binscenters)
    binWidth = binscenters[1] - binscenters[0]
    bins = list(binscenters + binWidth)
    bins.append(bins[-1]+binWidth)
    h = rt.TH1F("h","h",len(binscenters),np.array(bins))
    for i in range(len(binscenters)):
        h.SetBinContent(i,totalDataEntries[i])
    return h