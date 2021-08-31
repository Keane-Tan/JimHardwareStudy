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
options, args = parser.parse_args()
filename = options.filename

outFolder = filename[:filename.find(".root")]
# parameters
if outFolder in parameters.keys():
    pars = parameters[outFolder]
else:
    pars = parameters["Blue_laser_Keane_low_light_test_trig_1_SIPM_2_delay_22ns_5Gss"]
sWinMin = pars[2][0]
sWinMax = pars[2][1]
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

# loading noise-reduced signals
sigRedNoise = np.load("processedData/{}/sigRedNoise.npz".format(outFolder))
eventList = sorted(sigRedNoise.files,key=int)
# for plotting and saving filtered signals
filSigs = {}
plotfolderName = "plots/filtSig/{}/".format(outFolder)
ut.checkMakeDir(plotfolderName)

for count in eventList:
    count = int(count)
    tr.GetEntry(count)
    trigger = tr.c1
    SiPM = tr.c2

    trig_val_i = []
    SiPM_val_raw = []

    for i in range(len(SiPM)):
        trig_val_i.append( trigger[i] )
        # making a hard cut off at SiPM ADC current > 0, because it should not be more than 0.
        if SiPM[i] > 0:
            SiPM_val_raw.append(0)
        else:
            SiPM_val_raw.append( SiPM[i] )

    triggerEdge = ut.triggerTime(trig_val_i,trigValue,tfq,trig)
    sigWinMin = triggerEdge+sWinMin
    sigWinMax = triggerEdge+sWinMax
    SiPM_val_i = sigRedNoise[str(count)]
    sf = ut.butter_lowpass_filter(SiPM_val_i,300,5120,6)
    offset = ut.filterOffset(trig_val_i,trigValue)
    sf = sf[offset:]
    eventPedADC = ut.signalPedestal(sf,triggerEdge,tfq,wmin=sWinMin,wmax=sWinMax)
    sf = np.concatenate( (sf,[eventPedADC]*offset) )
    filSigs[str(count)] = sf
    if len(filSigs) < 11:
        plt.figure(figsize=(12,8))
        plt.plot(np.arange(0,len(SiPM_val_raw))*tfq,SiPM_val_raw,label="Raw Signal")
        plt.plot(np.arange(0,len(SiPM_val_i))*tfq,SiPM_val_i,label="Noise Reduced Signal")
        plt.plot(np.arange(0,len(sf))*tfq,sf,linewidth=2,label="Filtered Signal")
        plt.legend(loc="lower left")
        plt.ylim(min(SiPM_val_i),max(SiPM_val_i))
        plt.xlabel("Time (ns)")
        plt.ylabel("ADC")
        plt.savefig(plotfolderName + "filteredSignal_{}.png".format(count))

np.savez("processedData/{}/filtSig".format(outFolder),**filSigs)
