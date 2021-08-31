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
tdhistXMin = pars[6][0]
tdhistXMax = pars[6][1]
fitPars = pars[10]
fitFunctionChoice = pars[12]
binWidth = pars[13]
freq = pars[14] # in Gss
trig = pars[15]
tfq = 1./freq
timeDifference = np.load("processedData/{}/timeDifference.npz".format(outFolder))
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
    edgeTimeDiff = timeDifference[key]
    totalDataEntries,bins = np.histogram(edgeTimeDiff, bins=bins)
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
    plotname = "timeDifference_{}_{}".format(key,int(np.sum(totalDataEntriesFit)))
    plt.savefig(folderName + plotname + ".png")
