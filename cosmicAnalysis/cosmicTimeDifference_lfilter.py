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
from utils import utility as ut

mpl.rc("font", family="serif", size=10)
rt.gStyle.SetOptStat(0)
rt.gStyle.SetOptTitle(0)

# colorblind safe palettes (Okabe and Ito) (see https://www.nceas.ucsb.edu/sites/default/files/2022-06/Colorblind%20Safe%20Color%20Schemes.pdf)
black = rt.TColor.GetColor(0., 0., 0.)
green = rt.TColor.GetColor(0., 158./255., 115./255.)
darkBlue = rt.TColor.GetColor(0., 114./255., 178./255.)
lightBlue = rt.TColor.GetColor(86./255., 180./255., 233./255.)
yellow = rt.TColor.GetColor(240./255., 228./255., 66./255.)
orange = rt.TColor.GetColor(230./255., 159./255., 0.)
darkOrange = rt.TColor.GetColor(213./255., 94./255., 0.)
pink = rt.TColor.GetColor(204./255., 121./255., 167./255.)

parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-s', dest='singlePE', action="store_true", help="Use only single PE signals")
parser.add_option('-q', dest='quick', action="store_true", help="Run over only the first 10000 events")
parser.add_option('-m', dest='minPedThresh', action="store_true", help="Use the minimum-pedestal difference threshold algorithm to determine signal edge")
parser.add_option('-d', dest='filename', type='string', default='cosmics_Mar_8_1p4fiber_90cm_4by1by14_one_hole_white_extrusion_5p2meter_long.root', help="File name")
options, args = parser.parse_args()

singlePE = options.singlePE
quick = options.quick
filename = options.filename
minPedThresh = options.minPedThresh

outFolder = filename[:filename.find(".root")]
# parameters
if outFolder in parameters.keys():
    pars = parameters[outFolder]
else:
    pars = parameters["cosmics_Mar_8_1p4fiber_90cm_4by1by14_one_hole_white_extrusion_5p2meter_long"]
tpS = pars.tpS
pedPE_ch3 = pars.pedADC_c3
sPEADCMin_ch3 = pars.sPEADCMin_c3[0]
sPEADCMax_ch3 = pars.sPEADCMin_c3[1]
sSiPMWinMin_ch3 = pars.sSiPMWin_c3[0]
sSiPMWinMax_ch3 = pars.sSiPMWin_c3[1]
pedPE_ch4 = pars.pedADC_c4
sPEADCMin_ch4 = pars.sPEADCMin_c4[0]
sPEADCMax_ch4 = pars.sPEADCMin_c4[1]
sSiPMWinMin_ch4 = pars.sSiPMWin_c4[0]
sSiPMWinMax_ch4 = pars.sSiPMWin_c4[1]
fWinSize = pars.savgolFit[0]
fWinPoly = pars.savgolFit[1]
sPercent = pars.savgolFit[2]
tdhistXMin = pars.tdhistX[0]
tdhistXMax = pars.tdhistX[1]
fitPars_T3 = pars.fitPars_T3
fitPars_T4 = pars.fitPars_T4
fitPars_T43 = pars.fitPars_T43
trigValue = pars.trigValue
fitFunctionChoice = pars.fitFunctionChoice
binWidth = pars.tdBinWidth
# lowpass filter parameters
fs = pars.lowpassFit[0]
cutoff = pars.lowpassFit[1]
order = pars.lowpassFit[2]
offset = pars.lowpassFit[3]
gain_ch3 = pars.avgGain_c3
gain_ch4 = pars.avgGain_c4
pD0_ch3 = pars.pD0_c3
pD0_ch4 = pars.pD0_c4

# have to redefine the pedestal, because after smoothing the pedestal value also changes
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
fitFunction = ut.GaussianFit
# histogram details
bins=np.arange(tdhistXMin,tdhistXMax,binWidth)
binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])
totalDataEntries_T3 = np.zeros(len(bins)-1)
totalDataEntries_T4 = np.zeros(len(bins)-1)
totalDataEntries_T43 = np.zeros(len(bins)-1)
start = 0

T3_all = []
T4_all = []
T43_all = []

T3_count = 0
T4_count = 0
T43_count = 0

T3_raw_100 = []
T4_raw_100 = []

for i in range(nDiv):
    finish = start + nSubEvents
    # print("Analyzing event {} to {}".format(start,finish))

    trigEdgeList = []
    T3 = []
    T4 = []
    T43 = []

    for count in range(start,finish):
        tr.GetEntry(count)

        trigger = tr.c2
        trigger_time = tr.t2
        cosmic = tr.c1
        cosmic_time = tr.t1
        SiPM_ch3 = tr.c3
        SiPM_time_ch3 = tr.t3
        SiPM_ch4 = tr.c4
        SiPM_time_ch4 = tr.t4

        triggerEdge = ut.pulseTime(trigger,trigValue,tpS)
        cosmicEdge = ut.pulseTime(cosmic,trigValue,tpS)
        info3 = ut.getSignal(SiPM_ch3,cosmicEdge,gain_ch3,pedPE_ch3,sSiPMWinMin_ch3,sSiPMWinMax_ch3,tpS,cutoff,fs,order,offset)
        info4 = ut.getSignal(SiPM_ch4,cosmicEdge,gain_ch4,pedPE_ch4,sSiPMWinMin_ch4,sSiPMWinMax_ch4,tpS,cutoff,fs,order,offset)
        windowInfo_ch3 = info3[0]
        windowInfo_ch4 = info4[0]
        lf_ch3 = info3[1]
        lf_ch4 = info4[1]
        # signal
        rsCut = 9999
        if windowInfo_ch3:
            # sigEdge_ch3 = midPointEdge(windowInfo_ch3,lf_ch3)
            sigEdge_ch3 = ut.lineMatchEdge(lf_ch3,sSiPMWinMin_ch3,sSiPMWinMax_ch3,tpS)
            T3_count += 1
            # if count < 5000:
                # print("event {}".format(count))
                # print("signal edge: {}".format(sigEdge_ch3[0]))
                # print("trigger edge: {}".format(triggerEdge))
            if sigEdge_ch3[1] < rsCut:
                ch3_Time = sigEdge_ch3[0] - triggerEdge
                if minPedThresh:
                    ch3_Time = ut.minPedThreshEdge(lf_ch3,sSiPMWinMin_ch3,sSiPMWinMax_ch3,tpS,pD0_ch3,plot=False,nPE = 1.0)[0] - triggerEdge
                T3.append(ch3_Time)
                T3_all.append(ch3_Time)
                if len(T3_raw_100) < 100:
                    sigEdge3 = ut.minPedThreshEdge(lf_ch3,sSiPMWinMin_ch3,sSiPMWinMax_ch3,tpS,pD0_ch3,plot=False,nPE = 1.0)[0]
                    T3_raw_100.append(lf_ch3[int(sigEdge3/tpS)-50:])
                    # T3_raw_100.append(lf_ch3)
        if windowInfo_ch4:
            T4_count += 1
            # sigEdge_ch4 = midPointEdge(windowInfo_ch4,lf_ch4)
            sigEdge_ch4 = ut.lineMatchEdge(lf_ch4,sSiPMWinMin_ch4,sSiPMWinMax_ch4,tpS)
            if sigEdge_ch4[1] < rsCut:
                ch4_Time = sigEdge_ch4[0] - triggerEdge
                if minPedThresh:
                    ch4_Time = ut.minPedThreshEdge(lf_ch4,sSiPMWinMin_ch4,sSiPMWinMax_ch4,tpS,pD0_ch4,plot=False,nPE = 1.0)[0] - triggerEdge
                T4.append(ch4_Time)
                T4_all.append(ch4_Time)
                if len(T4_raw_100) < 100:
                    sigEdge4 = ut.minPedThreshEdge(lf_ch4,sSiPMWinMin_ch4,sSiPMWinMax_ch4,tpS,pD0_ch4,plot=False,nPE = 1.0)[0]
                    T4_raw_100.append(lf_ch4[int(sigEdge4/tpS)-50:])
                    # T4_raw_100.append(lf_ch4)
        if windowInfo_ch3 and windowInfo_ch4:
            T43_count += 1
            if sigEdge_ch3[1] < rsCut and sigEdge_ch4[1] < rsCut:
                ch43_time = (sigEdge_ch4[0] - sigEdge_ch3[0])/2.
                if minPedThresh:
                    ch43_time = (ut.minPedThreshEdge(lf_ch4,sSiPMWinMin_ch4,sSiPMWinMax_ch4,tpS,pD0_ch4,plot=False,nPE = 1.0)[0] - ut.minPedThreshEdge(lf_ch3,sSiPMWinMin_ch3,sSiPMWinMax_ch3,tpS,pD0_ch3,plot=False,nPE = 1.0)[0])/2.
                T43.append(ch43_time)
                T43_all.append(ch43_time)
    # print("Number of data in ch3: {}".format(len(T3)))
    # print("Number of data in ch4: {}".format(len(T4)))
    # binning the results
    ut.histoFill(T3,totalDataEntries_T3,bins)
    ut.histoFill(T4,totalDataEntries_T4,bins)
    ut.histoFill(T43,totalDataEntries_T43,bins)
    # print("Number of data still kept in ch3: {}".format(np.sum(totalDataEntries_T3)))
    # print("Number of data still kept in ch4: {}".format(np.sum(totalDataEntries_T4)))
    start += nSubEvents
print("T3_count: {}".format(T3_count))
print("T4_count: {}".format(T4_count))
print("T43_count: {}".format(T43_count))
# print("Histogram for all T3 {} events:".format(np.sum(totalDataEntries_T3)))
# print(totalDataEntries_T3)
# print("Histogram for all T4 {} events:".format(np.sum(totalDataEntries_T4)))
# print(totalDataEntries_T4)
# print("Histogram for all T43 {} events:".format(np.sum(totalDataEntries_T43)))
# print(totalDataEntries_T43)
if minPedThresh:
    folderName = "plots/timeDiff_ADCThresh/{}/".format(outFolder)
else:
    folderName = "plots/timeDiff_lineMatch/{}/".format(outFolder)
if not os.path.isdir(folderName):
    os.system("mkdir {}".format(folderName))
if not os.path.isdir("plots/signal_100/{}/".format(outFolder)):
    os.system("mkdir {}".format("plots/signal_100/{}/".format(outFolder)))
plotname = "T3_T4_T43"

xspace = np.linspace(tdhistXMin,tdhistXMax,100000)
binscentersFit = binscenters

plt.figure(figsize=(12,8))

ut.histplot(totalDataEntries_T3,binscenters,color='#2ca02c',label="T3")
popt3, perr3 = ut.fitAndPlot(totalDataEntries_T3,binscentersFit,'#d62728',fitPars_T3,fitFunction,xspace)
ut.histplot(totalDataEntries_T4,binscenters,color='#2a77b4',label="T4")
popt4, perr4 = ut.fitAndPlot(totalDataEntries_T4,binscentersFit,'#9467bd',fitPars_T4,fitFunction,xspace)
ut.histplot(totalDataEntries_T43,binscenters,color='#ff7f0e',label="(T4-T3)/2")
popt43, perr43 = ut.fitAndPlot(totalDataEntries_T43,binscentersFit,'#17becf',fitPars_T43,fitFunction,xspace)
axes = plt.gca()
# plt.text(0.6,0.6,"Number of T3 events = %i"%(T3_count),transform = axes.transAxes)
# plt.text(0.6,0.55,"Number of T4 events = %i"%(T4_count),transform = axes.transAxes)
plt.text(0.6,1.05,"Number of T3,T4 events = %i"%(T43_count),transform = axes.transAxes)
plt.xticks(np.arange(tdhistXMin,tdhistXMax,10))
plt.grid()
plt.legend(loc="best")
plt.xlabel("Time (ns)")
plt.ylabel("Events")
plt.ylim(0)
plt.savefig(folderName + plotname + ".png")

# ROOT plotting
c = rt.TCanvas("c_1", "canvas_1", 1200, 800)
c.SetLeftMargin(0.15)
## plot histogram
rootHist3 = ut.convertToTHist(totalDataEntries_T3,binscenters)
rootHist4 = ut.convertToTHist(totalDataEntries_T4,binscenters)
rootHist43 = ut.convertToTHist(totalDataEntries_T43,binscenters)
rootHist43.Draw()
rootHist43.SetFillColor(darkOrange)
rootHist43.GetYaxis().SetRangeUser(0,np.amax(totalDataEntries_T43[5:])*1.1)
rootHist43.GetYaxis().SetTitle("Events")
rootHist43.GetXaxis().SetTitle("Time Difference between Signal and Trigger")
rootHist3.Draw("SAME")
rootHist3.SetFillColor(green)
rootHist4.Draw("SAME")
rootHist4.SetFillColor(darkBlue)

## plot fits
xspace, 
gr_smooth3 = rt.TGraph(len(xspace),xspace,fitFunction(xspace, *popt3))
gr_smooth3.Draw("L")
gr_smooth3.SetLineWidth(2)
gr_smooth3.SetLineColor(pink)
gr_smooth4 = rt.TGraph(len(xspace),xspace,fitFunction(xspace, *popt4))
gr_smooth4.Draw("L")
gr_smooth4.SetLineWidth(2)
gr_smooth4.SetLineColor(yellow)
gr_smooth43 = rt.TGraph(len(xspace),xspace,fitFunction(xspace, *popt43))
gr_smooth43.Draw("L")
gr_smooth43.SetLineWidth(2)
gr_smooth43.SetLineColor(lightBlue)


legend = rt.TLegend(0.15,0.6,0.7,0.9)
legend.SetNColumns(2)
legend.AddEntry(rootHist3, "T1", "f")
legend.AddEntry(gr_smooth3, ut.getFitInfoROOT(popt3, perr3), "l")
legend.AddEntry(rootHist4, "T2", "f")
legend.AddEntry(gr_smooth4, ut.getFitInfoROOT(popt4, perr4), "l")
legend.AddEntry(rootHist43, "(T2-T1)/2", "f")
legend.AddEntry(gr_smooth43, ut.getFitInfoROOT(popt43, perr43), "l")
legend.Draw()
c.SaveAs(folderName + plotname + ".pdf")

plt.figure(figsize=(12,8))
for i in range(100):
    plt.plot(np.arange(0,len(T3_raw_100[i]))*tpS,T3_raw_100[i])
plt.savefig("plots/signal_100/{}/T3100.png".format(outFolder))
plt.xlim(20,60)
# plt.ylim(-0.008,0)
plt.savefig("plots/signal_100/{}/T3100_zoom.png".format(outFolder))

plt.figure(figsize=(12,8))
for i in range(100):
    plt.plot(np.arange(0,len(T4_raw_100[i]))*tpS,T4_raw_100[i])
plt.savefig("plots/signal_100/{}/T4100.png".format(outFolder))
plt.xlim(20,60)
# plt.ylim(-0.008,0)
plt.savefig("plots/signal_100/{}/T4100_zoom.png".format(outFolder))