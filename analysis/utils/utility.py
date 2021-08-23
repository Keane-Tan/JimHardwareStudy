# sample command: python cosmicSignalExploration_lfilter.py -d cosmics_Mar_26_1p4fiber_61cm_5by2by20_one_hole_white_extrusion_1p2meter_long_5gss.root -r -p -s
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, lfilter, freqz
from scipy import signal
import os

mpl.rc("font", family="serif", size=20)

def checkMakeDir(folderName):
    if not os.path.isdir(folderName):
        os.system("mkdir {}".format(folderName))

def triggerTime(trig_value_i,trigValue,tfq):
    triTime = 0
    for j in range(len(trig_value_i)):
        if trig_value_i[j] > trigValue:
            triTime = j * tfq
            break
    return triTime

def sigPedVoltage(SiPM,triggerTime,tfq,wmin,wmax):
    wMin = triggerTime + wmin
    wMax = triggerTime + wmax
    return abs(np.mean(SiPM[int((wMin-10)/tfq):int((wMin)/tfq)]))

def signalPedestal(SiPM,triggerTime,tfq,wmin,wmax):
    wMin = triggerTime + wmin
    wMax = triggerTime + wmax
    return abs(np.mean(SiPM[int((wMin-10)/tfq):int((wMin)/tfq)])*(wMax-wMin))

def signalIntegral(SiPM_val_i,triggerTime,tfq,wmin,wmax):
    windowInt = 0
    for i in range(len(SiPM_val_i)):
        if (triggerTime + wmin < i*tfq < triggerTime + wmax):
            windowInt += SiPM_val_i[i]*tfq
    area = abs(windowInt) - signalPedestal(SiPM_val_i,triggerTime,tfq,wmin,wmax)
    if area < 0:
        return 0
    else:
        return area

# this is based on the difference between max ADC and min ADC
# def signalExistThreshold(SiPM_val_i,triggerTime,tfq,wmin,wmax):
#     windowValues = []
#     for i in range(len(SiPM_val_i)):
#         if triggerTime + wmin < i*tfq < triggerTime + wmax:
#             windowValues.append(SiPM_val_i[i])
#     maxW = max(windowValues)
#     minW = min(windowValues)
#
#     return maxW - minW

# this is based on the area under graph for the signal
def signalExistThreshold(SiPM_val_i,triggerTime,tfq,wmin,wmax):
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
    maxW = max(windowValues)
    minW = min(windowValues)

    windowInt = signalIntegral(SiPM_val_i,triggerTime,tfq,wmin,wmax)

    if singlePE: # the values for the difference came from looking at the distribution of the differences.
        ADCRequirement = windowInt > sPEADCMin and windowInt < sPEADCMax
    else:
        ADCRequirement = windowInt > pedADC # more than pedestal

    if (ADCRequirement) and (windowValues.index(maxW) < windowValues.index(minW)):
        return [windowValues,windowIndices]
    else:
        return False

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

def butter_lowpass_filter(data, cutoff=100, fs=2000, order=6):
    b, a = butter_lowpass(cutoff, fs, order)
    y = lfilter(b, a, data)
    return y

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
    return mEdge

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
