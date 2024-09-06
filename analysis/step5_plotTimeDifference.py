import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import optparse
from parameters import parameters
from utils import utility as ut
import ROOT as rt 

rt.gStyle.SetOptStat(0)
rt.gStyle.SetOptTitle(0)
mpl.rc("font", family="serif", size=20)

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
parser.add_option('-d', dest='filename', type='string', default='Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss.root', help="File name")
parser.add_option('--pythonPlot',help='Use python plotting style instead of ROOT.', dest='pythonPlot', default=False, action='store_true')
options, args = parser.parse_args()
pythonPlot = options.pythonPlot
filename = options.filename

outFolder = filename[:filename.find(".root")]
# parameters
if outFolder in parameters.keys():
    pars = parameters[outFolder]
else:
    print("Using Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss")
    pars = parameters["Blue_laser_Keane_low_light_test_trig_1_SIPM_2_4p6V_5Gss"]
tdhistXMin,tdhistXMax = pars.tdhistX
fitPars = pars.fitPars
fitFunctionChoice = pars.fitFunctionChoice
freq = pars.freq
fitRan = pars.fitRan
tfq = 1./freq
binWidth = pars.binWidth * tfq
GausTimeFit = pars.GausTimeFit

timeDifference = np.load("/eos/uscms/store/user/keanet/Hardware/analysis/processedData/{}/timeDifference.npz".format(outFolder))
folderName = "plots/timeDiff/{}/".format(outFolder)
ut.checkMakeDir(folderName)

# picking the right fit function
if fitFunctionChoice == "Gaus":
    fitFunction = ut.GaussianFit
elif fitFunctionChoice == "Exp":
    fitFunction = ut.ExponentialFit

# histogram details
bins=np.arange(tdhistXMin,tdhistXMax,binWidth)
binscenters = np.array([0.5 * (bins[i] + bins[i+1]) for i in range(len(bins)-1)])

for key,item in timeDifference.items():
    plotname = "timeDifference_{}_{}".format(key,fitFunctionChoice)
    if key != "midPointSigEdge":
        continue
    edgeTimeDiff = timeDifference[key]
    totalDataEntries,bins = np.histogram(edgeTimeDiff, bins=bins)
    fitRanMin,fitRanMax = fitRan
    frmin = ut.indBasedVal(fitRanMin,binscenters)
    frmax = ut.indBasedVal(fitRanMax,binscenters)
    if fitFunctionChoice == "Gaus":
        xspace = np.linspace(fitRanMin,fitRanMax,100000)
        binscentersFit = binscenters[frmin:frmax]
        totalDataEntriesFit = totalDataEntries[frmin:frmax]
    elif fitFunctionChoice == "Exp":
        xspace = np.linspace(fitRanMin,fitRanMax,100000)
        binscentersFit = binscenters[frmin:frmax]
        totalDataEntriesFit = totalDataEntries[frmin:frmax]
    rootHist = ut.convertToTHist(totalDataEntries,binscenters)

    if fitFunctionChoice != None:
        print(key)
        print(totalDataEntriesFit)
        print(binscentersFit)
        popt, pcov = curve_fit(fitFunction, xdata=binscentersFit, ydata=totalDataEntriesFit, p0=fitPars,maxfev = 10000)
        perr = np.sqrt(np.diag(pcov))

    # Plot the histogram and the fitted function.
    if pythonPlot:
        plt.figure(figsize=(12,8))
        ut.histplot(totalDataEntries,binscenters,'#2a77b4','Histogram entries')
    else:
        c = rt.TCanvas("c_1", "canvas_1", 800, 800)
        c.SetLeftMargin(0.15)
        rootHist.Draw()
        rootHist.SetFillColor(darkBlue)
        rootHist.GetYaxis().SetTitle("Events")
        rootHist.GetXaxis().SetTitle("Time Difference between Signal and Trigger")
    if fitFunctionChoice != None:
        if pythonPlot:
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
                # fParas = r"N={:.1e}; $\tau$={:.3f}".format(popt[0],1/popt[1])
            plt.plot(xspace+binWidth/2., fitFunction(xspace, *popt), color='darkorange', linewidth=2.5,
                 label=fLabel)
            axes = plt.gca()
        else:
            gr = rt.TGraph(len(xspace),xspace+binWidth/2.,fitFunction(xspace, *popt))
            gr.Draw("L SAME")
            gr.SetLineWidth(3)
            gr.SetLineColor(darkOrange)
            if fitFunctionChoice == "Gaus":
                fitFunctionLeg = "Fit: N exp #left[ #frac{- (x-#mu)^{2} }{2#sigma^{2}} #right]"
                nVals = "N = {:.1f} ({:.1f})".format(popt[0],perr[0])
                muVals = "#mu = {:.3f} ({:.3f})".format(popt[1],perr[1])
                sigVals = "#sigma = {:.3f} ({:.3f})".format(abs(popt[2]),perr[2])
                fParas = "#scale[0.7]{#splitline{#splitline{"+nVals+"}{"+muVals+"}}{"+sigVals+"}}"
            elif fitFunctionChoice == "Exp":
                fitFunctionLeg = "Fit: N exp #left[ -x/#tau #right]"
                nVals = "N = {:.1f} ({:.1f})".format(popt[0],perr[0])
                f = 1/popt[1]
                errA = perr[1]
                A = popt[1]
                terr = abs(f*errA/A)
                tauVals = "#tau = {:.3f} ({:.3f})".format(1/popt[1],terr)
                fParas = "#scale[0.7]{#splitline{"+nVals+"}{"+tauVals+"}}"
            legend = rt.TLegend(0.5,0.7,0.9,0.9)
            legend.AddEntry(rootHist, "Single PE Data", "f")
            legend.AddEntry(gr, fitFunctionLeg, "l")
            legend.Draw()

            # fParas = "N={:.1f} ({:.1f}) #mu={:.3f} ({:.3f}); #sigma={:.3f} ({:.3f})".format(popt[0],perr[0],popt[1],perr[1],abs(popt[2]),perr[2])
            # fParas = "#scale[0.5]{"+fParas+"}"
            extraInfo = rt.TLatex(0.5,0.6,fParas)
            extraInfo.SetNDC() # so that the position for TText can be in the range [0,1]
            extraInfo.Draw()
            nEvents = "Events Analysed: {}".format(int(np.sum(totalDataEntriesFit)))
            extraInfo2 = rt.TLatex(0.5,0.4,"#scale[0.7]{"+nEvents+"}")
            extraInfo2.SetNDC() # so that the position for TText can be in the range [0,1]
            extraInfo2.Draw()

            c.SaveAs(folderName + plotname + "_ROOT.pdf")
    if GausTimeFit != False:
        gfitRanMin = GausTimeFit[0]
        gfitRanMax = GausTimeFit[2]
        fgmin = ut.indBasedVal(gfitRanMin,binscenters)
        fgmax = ut.indBasedVal(gfitRanMax,binscenters)
        binscentersGFit = binscenters[fgmin:fgmax]
        totalDataEntriesGFit = totalDataEntries[fgmin:fgmax]
        gxspace = np.linspace(gfitRanMin,gfitRanMax,100000)

        poptG, pcovG = curve_fit(ut.GaussianFit, xdata=binscentersGFit, ydata=totalDataEntriesGFit, p0=[100,GausTimeFit[1],10],maxfev = 10000)
        perrG = np.sqrt(np.diag(pcovG))
        if pythonPlot:
            plt.plot(gxspace+binWidth/2., ut.GaussianFit(gxspace, *poptG), color='red', linewidth=2.5)
            plt.text(0.4,0.65,r"Gaus: N={:.1f}$\pm${:.1f}; $\mu$={:.3f}$\pm${:.3f}; $\sigma$={:.3f}$\pm${:.3f}".format(poptG[0],perrG[0],poptG[1],perrG[1],abs(poptG[2]),perrG[2]),fontsize=15,transform = axes.transAxes)
    if pythonPlot:
        if fitFunctionChoice != None:
            plt.text(0.4,0.75,fParas,fontsize=18,transform = axes.transAxes)
            plt.text(0.5,0.7,"Events Analysed: {}".format(int(np.sum(totalDataEntriesFit))),fontsize=15,transform = axes.transAxes)
        else:
            plt.text(0.5,0.7,"Total Number of Events: {}".format(int(np.sum(totalDataEntries))),fontsize=15,transform = axes.transAxes)
            plt.text(0.5,0.75,"Std. Dev.: {:.2f}".format(np.std(edgeTimeDiff)),fontsize=18,transform = axes.transAxes)
        plt.legend()
        plt.ylabel("Events")
        plt.xlabel("Time Difference between Signal and Trigger")
        plt.savefig(folderName + plotname + ".png")
