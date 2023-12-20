#!/bin/sh
ulimit -s unlimited
set -e
cd /data/vami/CMSSW_10_6_14/src
export SCRAM_ARCH=slc7_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /data/vami/CMSSW_10_6_14/src/DataStudies/2DAlpha_CodeV46p9_1Dfrom2DNoExtrapol_200GeV_Gluino1800/Signal_gluino-1800-0x0_area

if [ $1 -eq 0 ]; then
  combine -M MultiDimFit -n _paramFit_t1_Background_fail_LOW_bin_1-1 --algo impact --redefineSignalPOIs r -P Background_fail_LOW_bin_1-1 --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 1 ]; then
  combine -M MultiDimFit -n _paramFit_t1_Background_fail_LOW_bin_2-1 --algo impact --redefineSignalPOIs r -P Background_fail_LOW_bin_2-1 --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 2 ]; then
  combine -M MultiDimFit -n _paramFit_t1_Background_fail_LOW_bin_3-1 --algo impact --redefineSignalPOIs r -P Background_fail_LOW_bin_3-1 --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 3 ]; then
  combine -M MultiDimFit -n _paramFit_t1_Background_fail_LOW_bin_4-1 --algo impact --redefineSignalPOIs r -P Background_fail_LOW_bin_4-1 --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 4 ]; then
  combine -M MultiDimFit -n _paramFit_t1_Background_fail_LOW_bin_5-1 --algo impact --redefineSignalPOIs r -P Background_fail_LOW_bin_5-1 --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 5 ]; then
  combine -M MultiDimFit -n _paramFit_t1_Background_fail_SIG_bin_1-1 --algo impact --redefineSignalPOIs r -P Background_fail_SIG_bin_1-1 --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 6 ]; then
  combine -M MultiDimFit -n _paramFit_t1_Background_fail_SIG_bin_2-1 --algo impact --redefineSignalPOIs r -P Background_fail_SIG_bin_2-1 --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 7 ]; then
  combine -M MultiDimFit -n _paramFit_t1_Background_fail_SIG_bin_3-1 --algo impact --redefineSignalPOIs r -P Background_fail_SIG_bin_3-1 --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 8 ]; then
  combine -M MultiDimFit -n _paramFit_t1_Background_fail_SIG_bin_4-1 --algo impact --redefineSignalPOIs r -P Background_fail_SIG_bin_4-1 --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 9 ]; then
  combine -M MultiDimFit -n _paramFit_t1_Background_rpf_0x0_par0 --algo impact --redefineSignalPOIs r -P Background_rpf_0x0_par0 --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 10 ]; then
  combine -M MultiDimFit -n _paramFit_t1_lumi --algo impact --redefineSignalPOIs r -P lumi --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 11 ]; then
  combine -M MultiDimFit -n _paramFit_t1_pileup --algo impact --redefineSignalPOIs r -P pileup --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 12 ]; then
  combine -M MultiDimFit -n _paramFit_t1_systOnF --algo impact --redefineSignalPOIs r -P systOnF --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 13 ]; then
  combine -M MultiDimFit -n _paramFit_t1_systOnG --algo impact --redefineSignalPOIs r -P systOnG --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 14 ]; then
  combine -M MultiDimFit -n _paramFit_t1_systOnMuID --algo impact --redefineSignalPOIs r -P systOnMuID --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 15 ]; then
  combine -M MultiDimFit -n _paramFit_t1_systOnMuReco --algo impact --redefineSignalPOIs r -P systOnMuReco --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 16 ]; then
  combine -M MultiDimFit -n _paramFit_t1_systOnMuTrigger --algo impact --redefineSignalPOIs r -P systOnMuTrigger --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 17 ]; then
  combine -M MultiDimFit -n _paramFit_t1_systOnPt --algo impact --redefineSignalPOIs r -P systOnPt --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi
if [ $1 -eq 18 ]; then
  combine -M MultiDimFit -n _paramFit_t1_systOnTrigger --algo impact --redefineSignalPOIs r -P systOnTrigger --floatOtherPOIs 1 --saveInactivePOI 1 -t -1 --expectSignal 1 --rMin -10 -m 1 -d card.root
fi