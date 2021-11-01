import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import optparse
from parameters import parameters
from utils import utility as ut

mpl.rc("font", family="serif", size=20)

parser = optparse.OptionParser("usage: %prog [options]\n")
parser.add_option('-d', dest='filename', type='string', default='Blue_laser_Keane_low_light_test_trig_1_SIPM_2_delay_22ns_5Gss.root', help="File name")
options, args = parser.parse_args()

filename = options.filename

outFolder = filename[:filename.find(".root")]
# parameters
if outFolder in parameters.keys():
    pars = parameters[outFolder]
else:
    pars = parameters["Blue_laser_Keane_low_light_test_trig_1_SIPM_2_delay_22ns_5Gss"]
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
    if key != "midPointSigEdge":
        continue
    edgeTimeDiff = timeDifference[key]
    totalDataEntries,bins = np.histogram(edgeTimeDiff, bins=bins)
    # Generate enough x values to make the fit look smooth.
    if fitFunctionChoice == "Gaus":
        xspace = np.linspace(tdhistXMin,tdhistXMax,100000)
        binscentersFit = binscenters
        totalDataEntriesFit = totalDataEntries
    elif fitFunctionChoice == "Exp":
        fitRanMin,fitRanMax = fitRan
        frmin = ut.indBasedVal(fitRanMin,binscenters)
        frmax = ut.indBasedVal(fitRanMax,binscenters)
        xspace = np.linspace(fitRanMin,fitRanMax,100000)
        binscentersFit = binscenters[frmin:frmax]
        totalDataEntriesFit = totalDataEntries[frmin:frmax]

    if fitFunctionChoice != None:
        print(key)
        print(totalDataEntriesFit)
        print(binscentersFit)
        popt, pcov = curve_fit(fitFunction, xdata=binscentersFit, ydata=totalDataEntriesFit, p0=fitPars,maxfev = 10000)
        perr = np.sqrt(np.diag(pcov))

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
        # fParas = r"N={:.1e}; $\tau$={:.3f}".format(popt[0],1/popt[1])
    if fitFunctionChoice != None:
        plt.plot(xspace+binWidth/2., fitFunction(xspace, *popt), color='darkorange', linewidth=2.5,
                 label=fLabel)
    axes = plt.gca()
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
        plt.plot(gxspace+binWidth/2., ut.GaussianFit(gxspace, *poptG), color='red', linewidth=2.5)
        plt.text(0.4,0.65,r"Gaus: N={:.1f}$\pm${:.1f}; $\mu$={:.3f}$\pm${:.3f}; $\sigma$={:.3f}$\pm${:.3f}".format(poptG[0],perrG[0],poptG[1],perrG[1],abs(poptG[2]),perrG[2]),fontsize=15,transform = axes.transAxes)
    plt.legend()
    y_min, y_max = axes.get_ylim()
    if fitFunctionChoice != None:
        plt.text(0.4,0.75,fParas,fontsize=18,transform = axes.transAxes)
        plt.text(0.5,0.7,"Events Analysed: {}".format(int(np.sum(totalDataEntriesFit))),fontsize=15,transform = axes.transAxes)
    else:
        plt.text(0.5,0.7,"Total Number of Events: {}".format(int(np.sum(totalDataEntries))),fontsize=15,transform = axes.transAxes)
        plt.text(0.5,0.75,"Std. Dev.: {:.2f}".format(np.std(edgeTimeDiff)),fontsize=18,transform = axes.transAxes)
    plt.ylabel("Events")
    plt.xlabel("Time Difference between Signal and Trigger")
    # naming the histogram
    plotname = "timeDifference_{}_{}".format(key,fitFunctionChoice)
    plt.savefig(folderName + plotname + ".png")
