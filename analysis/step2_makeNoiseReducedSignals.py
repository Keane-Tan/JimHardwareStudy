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
pedADC = pars[0]
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

# for plotting and saving signals with reduced noise
rawSignals = []
sigNoisReds = {}
plotfolderName = "plots/sigRedNoise/{}/".format(outFolder)
ut.checkMakeDir(plotfolderName)

for count in range(0,nEvents):
    tr.GetEntry(count)
    trigger = tr.c1
    SiPM = tr.c2

    if count % 10000 == 0:
        print(count)

    # if count == 1000:
    #     break

    trig_val_i = []
    SiPM_val_i = []

    for i in range(len(SiPM)):
        trig_val_i.append( trigger[i] )
        # making a hard cut off at SiPM ADC current > 0, because it should not be more than 0.
        if SiPM[i] > 0:
            SiPM_val_i.append(0)
        else:
            SiPM_val_i.append( SiPM[i] )

    triggerEdge = ut.triggerTime(trig_val_i,trigValue,tfq,trig)
    sigWinMin = triggerEdge+sWinMin
    sigWinMax = triggerEdge+sWinMax
    if ut.signalExistThresholdMin(SiPM_val_i,triggerEdge,tfq,sWinMin,sWinMax) > pedADC:
        nf = np.load("plots/aveNoise/{}/".format(outFolder) + "avgNoise.npz")
        avgNoise = nf["avgNoise"]
        sigNoisRed = ut.SiPMSig_NoiseRed(avgNoise,SiPM_val_i,sigWinMin,sigWinMax,tfq)
        sigNoisReds[str(count)] = sigNoisRed
        if len(sigNoisReds) < 11:
            plt.figure(figsize=(12,8))
            plt.plot(np.arange(0,len(sigNoisRed))*tfq,sigNoisRed,label="Noise Reduced Signal")
            plt.plot(np.arange(0,len(SiPM_val_i))*tfq,SiPM_val_i,label="Raw Signal")
            plt.legend()
            plt.xlabel("Time (ns)")
            plt.ylabel("ADC")
            plt.savefig(plotfolderName + "noiseRedSignal_{}.png".format(count))

folderName = "processedData/{}".format(outFolder)
ut.checkMakeDir(folderName)
np.savez("{}/sigRedNoise".format(folderName),**sigNoisReds)
