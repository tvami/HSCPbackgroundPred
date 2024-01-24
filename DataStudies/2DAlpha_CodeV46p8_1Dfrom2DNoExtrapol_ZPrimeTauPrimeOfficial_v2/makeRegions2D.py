import ROOT,sys,os
import numpy as np

from optparse import OptionParser
parser = OptionParser(usage="Usage: python %prog codeVersion")
from tqdm import tqdm

codeVersion = sys.argv[1]

def makeRegion(name, iHist, syst):
    f = ROOT.TFile.Open('HSCP_{}.root'.format(name),'UPDATE')

    # do it for fail
#    inputHistForFail = f.Get(iHist)
    hFailName = 'hfail{}'.format(syst)
    #iHist is PostS_ProbQNoL1VsIasVsPt
    hFail = ROOT.TH2D(hFailName,'GiVsPt;Gi;pT',iHist.GetNbinsY(),0.0,1.0,iHist.GetNbinsZ()+1,0.0,4025.0)
    # define fail as FiPixels < 0.9
    iHist.GetXaxis().SetRange(1,iHist.GetXaxis().FindBin(0.9)-1)
    hFailTEMP = iHist.Project3D("ZY")
    
    for xBin in range(1,hFailTEMP.GetNbinsX()+1):
      for yBin in  range(1,hFailTEMP.GetNbinsY()+2):
        binContent = hFailTEMP.GetBinContent(xBin,yBin)
        if (binContent==0 and "Signal" in name) : binContent = 0.0000001
        hFail.SetBinContent(xBin, yBin, binContent)
    
    # do it for pass
#    inputHistForPass = f.Get(iHist)
    # 2DAlphabet expects signal/blinding to be on X axis only so it has to be Gi vs pT
    hPassName = 'hpass{}'.format(syst)
    hPass = ROOT.TH2D(hPassName,'GiVsPt;Gi;pT',iHist.GetNbinsY(),0.0,1.0,iHist.GetNbinsZ()+1,0.0,4025.0)
    # define pass as FiPixels > 0.9
    iHist.GetXaxis().SetRange(iHist.GetXaxis().FindBin(0.9),iHist.GetNbinsX()+1)
    hPassTEMP = iHist.Project3D("ZY")
    
    for xBin in range(1,hPassTEMP.GetNbinsX()+1):
      for yBin in  range(1,hPassTEMP.GetNbinsY()+2):
        binContent = hPassTEMP.GetBinContent(xBin,yBin)
        if (binContent==0 and "Signal" in name) : binContent = 0.0000001
        hPass.SetBinContent(xBin, yBin, binContent)
    
    hFail.Write()
    hPass.Write()
    f.Close()

d = {
 'Signal_gluino-800-SR1': 'crab_Analysis_2018_HSCPgluino_M-800_CodeV'+codeVersion+'_v1.root',
 'Signal_gluino-1000-SR1': 'crab_Analysis_2018_HSCPgluino_M-1000_CodeV'+codeVersion+'_v1.root',
 'Signal_gluino-1400-SR1': 'crab_Analysis_2018_HSCPgluino_M-1400_CodeV'+codeVersion+'_v1.root',
 'Signal_gluino-1600-SR1': 'crab_Analysis_2018_HSCPgluino_M-1600_CodeV'+codeVersion+'_v1.root',
 'Signal_gluino-1800-SR1': 'crab_Analysis_2018_HSCPgluino_M-1800_CodeV'+codeVersion+'_v1.root',
 'Signal_gluino-2000-SR1': 'crab_Analysis_2018_HSCPgluino_M-2000_CodeV'+codeVersion+'_v1.root',
 'Signal_gluino-2200-SR1': 'crab_Analysis_2018_HSCPgluino_M-2200_CodeV'+codeVersion+'_v1.root',
 'Signal_gluino-2400-SR1': 'crab_Analysis_2018_HSCPgluino_M-2400_CodeV'+codeVersion+'_v1.root',
 'Signal_gluino-2600-SR1': 'crab_Analysis_2018_HSCPgluino_M-2600_CodeV'+codeVersion+'_v1.root',
 'Signal_ppStau-200-SR1': 'crab_Analysis_2018_HSCPpairStau_M-200_CodeV'+codeVersion+'_v1.root',
 'Signal_ppStau-247-SR1': 'crab_Analysis_2018_HSCPpairStau_M-247_CodeV'+codeVersion+'_v1.root',
 'Signal_ppStau-308-SR1': 'crab_Analysis_2018_HSCPpairStau_M-308_CodeV'+codeVersion+'_v1.root',
 'Signal_ppStau-432-SR1': 'crab_Analysis_2018_HSCPpairStau_M-432_CodeV'+codeVersion+'_v1.root',
 'Signal_ppStau-557-SR1': 'crab_Analysis_2018_HSCPpairStau_M-557_CodeV'+codeVersion+'_v1.root',
 'Signal_ppStau-651-SR1': 'crab_Analysis_2018_HSCPpairStau_M-651_CodeV'+codeVersion+'_v1.root',
 'Signal_ppStau-745-SR1': 'crab_Analysis_2018_HSCPpairStau_M-745_CodeV'+codeVersion+'_v1.root',
 'Signal_ppStau-871-SR1': 'crab_Analysis_2018_HSCPpairStau_M-871_CodeV'+codeVersion+'_v1.root',
 'Signal_ppStau-1029-SR1': 'crab_Analysis_2018_HSCPpairStau_M-1029_CodeV'+codeVersion+'_v1.root',
 'Signal_ppStau-1218-SR1': 'crab_Analysis_2018_HSCPpairStau_M-1218_CodeV'+codeVersion+'_v1.root',
 'Signal_gluinoCS-500-SR1' : 'crab_Analysis_2018_HSCPgluinoOnlyNeutral_M-500_CodeV'+codeVersion+'_v1.root',
 'Signal_gluinoCS-800-SR1' : 'crab_Analysis_2018_HSCPgluinoOnlyNeutral_M-800_CodeV'+codeVersion+'_v1.root',
 'Signal_gluinoCS-1000-SR1' : 'crab_Analysis_2018_HSCPgluinoOnlyNeutral_M-1000_CodeV'+codeVersion+'_v1.root',
 'Signal_gluinoCS-1200-SR1' : 'crab_Analysis_2018_HSCPgluinoOnlyNeutral_M-1200_CodeV'+codeVersion+'_v1.root',
 'Signal_gluinoCS-1400-SR1' : 'crab_Analysis_2018_HSCPgluinoOnlyNeutral_M-1400_CodeV'+codeVersion+'_v1.root',
 'Signal_gluinoCS-1600-SR1' : 'crab_Analysis_2018_HSCPgluinoOnlyNeutral_M-1600_CodeV'+codeVersion+'_v1.root',
 'Signal_gluinoCS-1800-SR1' : 'crab_Analysis_2018_HSCPgluinoOnlyNeutral_M-1800_CodeV'+codeVersion+'_v1.root',
 'Signal_gluinoCS-2000-SR1' : 'crab_Analysis_2018_HSCPgluinoOnlyNeutral_M-2000_CodeV'+codeVersion+'_v1.root',
 'Signal_gluinoCS-2200-SR1' : 'crab_Analysis_2018_HSCPgluinoOnlyNeutral_M-2200_CodeV'+codeVersion+'_v1.root',
 'Signal_gluinoCS-2400-SR1' : 'crab_Analysis_2018_HSCPgluinoOnlyNeutral_M-2400_CodeV'+codeVersion+'_v1.root',
 'Signal_gluinoCS-2600-SR1' : 'crab_Analysis_2018_HSCPgluinoOnlyNeutral_M-2600_CodeV'+codeVersion+'_v1.root',
 'Signal_gmsbStau-200-SR1' : 'crab_Analysis_2018_HSCPgmsbStau_M-200_CodeV'+codeVersion+'_v1.root',
 'Signal_gmsbStau-247-SR1' : 'crab_Analysis_2018_HSCPgmsbStau_M-247_CodeV'+codeVersion+'_v1.root',
 'Signal_gmsbStau-308-SR1' : 'crab_Analysis_2018_HSCPgmsbStau_M-308_CodeV'+codeVersion+'_v1.root',
 'Signal_gmsbStau-432-SR1' : 'crab_Analysis_2018_HSCPgmsbStau_M-432_CodeV'+codeVersion+'_v1.root',
 'Signal_gmsbStau-557-SR1' : 'crab_Analysis_2018_HSCPgmsbStau_M-557_CodeV'+codeVersion+'_v1.root',
 'Signal_gmsbStau-651-SR1' : 'crab_Analysis_2018_HSCPgmsbStau_M-651_CodeV'+codeVersion+'_v1.root',
 'Signal_gmsbStau-745-SR1' : 'crab_Analysis_2018_HSCPgmsbStau_M-745_CodeV'+codeVersion+'_v1.root',
 'Signal_gmsbStau-871-SR1' : 'crab_Analysis_2018_HSCPgmsbStau_M-871_CodeV'+codeVersion+'_v1.root',
 'Signal_gmsbStau-1029-SR1' : 'crab_Analysis_2018_HSCPgmsbStau_M-1029_CodeV'+codeVersion+'_v1.root',
 'Signal_gmsbStau-1218-SR1' : 'crab_Analysis_2018_HSCPgmsbStau_M-1218_CodeV'+codeVersion+'_v1.root',
 'Signal_gmsbStau-1409-SR1' : 'crab_Analysis_2018_HSCPgmsbStau_M-1409_CodeV'+codeVersion+'_v1.root',
 'Signal_gmsbStau-1599-SR1' : 'crab_Analysis_2018_HSCPgmsbStau_M-1599_CodeV'+codeVersion+'_v1.root',
 'Signal_stopCS-500-SR1' : 'crab_Analysis_2018_HSCPstopOnlyNeutral_M-500_CodeV'+codeVersion+'_v1.root',
 'Signal_stopCS-800-SR1' : 'crab_Analysis_2018_HSCPstopOnlyNeutral_M-800_CodeV'+codeVersion+'_v1.root',
 'Signal_stopCS-1000-SR1' : 'crab_Analysis_2018_HSCPstopOnlyNeutral_M-1000_CodeV'+codeVersion+'_v1.root',
 'Signal_stopCS-1200-SR1' : 'crab_Analysis_2018_HSCPstopOnlyNeutral_M-1200_CodeV'+codeVersion+'_v1.root',
 'Signal_stopCS-1400-SR1' : 'crab_Analysis_2018_HSCPstopOnlyNeutral_M-1400_CodeV'+codeVersion+'_v1.root',
 'Signal_stopCS-1600-SR1' : 'crab_Analysis_2018_HSCPstopOnlyNeutral_M-1600_CodeV'+codeVersion+'_v1.root',
 'Signal_stopCS-1800-SR1' : 'crab_Analysis_2018_HSCPstopOnlyNeutral_M-1800_CodeV'+codeVersion+'_v1.root',
 'Signal_stopCS-2000-SR1' : 'crab_Analysis_2018_HSCPstopOnlyNeutral_M-2000_CodeV'+codeVersion+'_v1.root',
 'Signal_stopCS-2200-SR1' : 'crab_Analysis_2018_HSCPstopOnlyNeutral_M-2200_CodeV'+codeVersion+'_v1.root',
 'Signal_stopCS-2400-SR1' : 'crab_Analysis_2018_HSCPstopOnlyNeutral_M-2400_CodeV'+codeVersion+'_v1.root',
 'Signal_stopCS-2600-SR1' : 'crab_Analysis_2018_HSCPstopOnlyNeutral_M-2600_CodeV'+codeVersion+'_v1.root',
 'Signal_stop-500-SR1' : 'crab_Analysis_2018_HSCPstop_M-500_CodeV'+codeVersion+'_v1.root',
 'Signal_stop-800-SR1' : 'crab_Analysis_2018_HSCPstop_M-800_CodeV'+codeVersion+'_v1.root',
 'Signal_stop-1000-SR1' : 'crab_Analysis_2018_HSCPstop_M-1000_CodeV'+codeVersion+'_v1.root',
 'Signal_stop-1200-SR1' : 'crab_Analysis_2018_HSCPstop_M-1200_CodeV'+codeVersion+'_v1.root',
 'Signal_stop-1400-SR1' : 'crab_Analysis_2018_HSCPstop_M-1400_CodeV'+codeVersion+'_v1.root',
 'Signal_stop-1600-SR1' : 'crab_Analysis_2018_HSCPstop_M-1600_CodeV'+codeVersion+'_v1.root',
 'Signal_stop-1800-SR1' : 'crab_Analysis_2018_HSCPstop_M-1800_CodeV'+codeVersion+'_v1.root',
 'Signal_stop-2000-SR1' : 'crab_Analysis_2018_HSCPstop_M-2000_CodeV'+codeVersion+'_v1.root',
 'Signal_stop-2200-SR1' : 'crab_Analysis_2018_HSCPstop_M-2200_CodeV'+codeVersion+'_v1.root',
 'Signal_stop-2400-SR1' : 'crab_Analysis_2018_HSCPstop_M-2400_CodeV'+codeVersion+'_v1.root',
 'Signal_stop-2600-SR1' : 'crab_Analysis_2018_HSCPstop_M-2600_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime1e-200-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge1e_M-200_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime1e-400-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge1e_M-400_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime1e-600-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge1e_M-600_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime1e-800-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge1e_M-800_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime1e-1000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge1e_M-1000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime1e-1400-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge1e_M-1400_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime1e-1800-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge1e_M-1800_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime1e-2200-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge1e_M-2200_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime1e-2600-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge1e_M-2600_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-200-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-200_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-400-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-400_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-600-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-600_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-800-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-800_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1400-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1400_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1800-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1800_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-2200-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-2200_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-2600-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-2600_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-200-ZPrime-3000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-200_ZPrime_M-3000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-200-ZPrime-4000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-200_ZPrime_M-4000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-200-ZPrime-5000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-200_ZPrime_M-5000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-200-ZPrime-6000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-200_ZPrime_M-6000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-200-ZPrime-7000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-200_ZPrime_M-7000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-400-ZPrime-3000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-400_ZPrime_M-3000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-400-ZPrime-4000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-400_ZPrime_M-4000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-400-ZPrime-5000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-400_ZPrime_M-5000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-400-ZPrime-6000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-400_ZPrime_M-6000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-400-ZPrime-7000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-400_ZPrime_M-7000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-600-ZPrime-3000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-600_ZPrime_M-3000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-600-ZPrime-4000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-600_ZPrime_M-4000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-600-ZPrime-5000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-600_ZPrime_M-5000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-600-ZPrime-6000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-600_ZPrime_M-6000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-600-ZPrime-7000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-600_ZPrime_M-7000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-800-ZPrime-3000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-800_ZPrime_M-3000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-800-ZPrime-4000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-800_ZPrime_M-4000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-800-ZPrime-5000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-800_ZPrime_M-5000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-800-ZPrime-6000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-800_ZPrime_M-6000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-800-ZPrime-7000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-800_ZPrime_M-7000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1000-ZPrime-3000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1000_ZPrime_M-3000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1000-ZPrime-4000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1000_ZPrime_M-4000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1000-ZPrime-5000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1000_ZPrime_M-5000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1000-ZPrime-6000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1000_ZPrime_M-6000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1000-ZPrime-7000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1000_ZPrime_M-7000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1200-ZPrime-3000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1200_ZPrime_M-3000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1200-ZPrime-4000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1200_ZPrime_M-4000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1200-ZPrime-5000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1200_ZPrime_M-5000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1200-ZPrime-6000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1200_ZPrime_M-6000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1200-ZPrime-7000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1200_ZPrime_M-7000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1400-ZPrime-3000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1400_ZPrime_M-3000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1400-ZPrime-4000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1400_ZPrime_M-4000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1400-ZPrime-5000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1400_ZPrime_M-5000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1400-ZPrime-6000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1400_ZPrime_M-6000_CodeV'+codeVersion+'_v1.root',
 'Signal_tauPrime2e-1400-ZPrime-7000-SR1' : 'crab_Analysis_2018_HSCPtauPrimeCharge2e_M-1400_ZPrime_M-7000_CodeV'+codeVersion+'_v1.root',
 'Data-SR1': 'crab_Analysis_SingleMuon_RunPhase1_CodeV'+codeVersion+'_v1.root'}
# 'Data': 'crab_Analysis_2018_AllBackground_CodeV42p3_v1.root'}

for name, fName in d.items():
    if not os.path.exists(fName): continue
    fTemp = ROOT.TFile.Open(fName)
    if ("Data" in name) :
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt'),'')
    if ("Signal" in name) :
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt'),'')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_Pileup_down'),'_PUsyst_down')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_Pileup_up'),'_PUsyst_up')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_ProbQNoL1_down'),'_Fsyst_down')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_ProbQNoL1_up'),'_Fsyst_up')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_Ias_down'),'_Gsyst_down')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_Ias_up'),'_Gsyst_up')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_Trigger_down'),'_Triggersyst_down')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_Trigger_up'),'_Triggersyst_up')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_Pt_down'),'_Ptsyst_down')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_Pt_up'),'_Ptsyst_up')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_MuonRecoSF_down'),'_MuonRecoSF_down')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_MuonRecoSF_up'),'_MuonRecoSF_up')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_MuonIDSF_down'),'_MuonIDSF_down')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_MuonIDSF_up'),'_MuonIDSF_up')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_MuonTriggerSF_down'),'_MuonTriggerSF_down')
      makeRegion(name, fTemp.Get('HSCParticleAnalyzer/BaseName/PostS_ProbQNoL1VsIasVsPt_MuonTriggerSF_up'),'_MuonTriggerSF_up')
    fTemp.Close()

print("scp HSCP_*root vami@ui3.kfki.hu:/data/vami/CMSSW_10_6_14/src/DataStudies/.")
