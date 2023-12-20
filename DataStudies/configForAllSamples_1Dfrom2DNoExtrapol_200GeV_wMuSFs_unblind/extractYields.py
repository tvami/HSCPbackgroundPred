import ROOT, sys, os, time, re, array
import numpy as np
from ctypes import c_double as double
from optparse import OptionParser
parser = OptionParser(usage="Usage: python %prog fileName.root BinNumber")
(opt,args) = parser.parse_args()

ROOT.gROOT.SetStyle("Plain")
#ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPalette(1)
ROOT.gROOT.SetBatch(True)

ROOT.gStyle.SetPadTopMargin(0.07);
ROOT.gStyle.SetPadBottomMargin(0.1);
ROOT.gStyle.SetPadLeftMargin(0.15);
ROOT.gStyle.SetPadRightMargin(0.13);

fileName = sys.argv[1]
input_file = fileName

f = ROOT.TFile.Open(input_file)

dirs = []
for i in range(0, f.GetListOfKeys().GetEntries()):
  dirname = f.GetListOfKeys().At(i).GetName()
  curr_dir = f.GetDirectory(dirname)
  
  if any(condition in dirname for condition in ["fail", "prefit", "projx0", "projx1", "projy", "_2D", "Background_"]) :
    continue
  if not any(condition in dirname for condition in ["Signal"]) :
    continue

  objData = f.Get("data_obs_pass_postfit_projx2")
  objBkg = f.Get("TotalBkg_pass_postfit_projx2")
  objSig = f.Get(dirname)
  SigBin6 = round(objSig.GetBinContent(6),1)
  SigBin7 = round(objSig.GetBinContent(7),1)
  SigBin8 = round(objSig.GetBinContent(8),1)
  SigBin9 = round(objSig.GetBinContent(9),1)
  signalName = dirname[dirname.find("Signal_")+7:dirname.find("_pass_postfit")]

  with open('output.tex', 'a') as file:
    #file.write(f"{signalName} & {SigBin6} & {SigBin7} & {SigBin8} & {SigBin9} \\\\ \n\hline")
    file.write(str(signalName) + " GeV & " + str(SigBin6) + " & " + str(SigBin7) +  " & " + str(SigBin8) + " & " + str(SigBin9) + " \\\\ \n\hline\n")


