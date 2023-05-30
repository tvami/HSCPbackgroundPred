from time import time
from TwoDAlphabet import plot
from TwoDAlphabet.twoDalphabet import MakeCard, TwoDAlphabet
from TwoDAlphabet.alphawrap import BinnedDistribution, ParametricFunction
from TwoDAlphabet.helpers import make_env_tarball, cd, execute_cmd
from TwoDAlphabet.ftest import FstatCalc
import os,sys
import numpy as np
from optparse import OptionParser
parser = OptionParser(usage="Usage: python %prog workingArea config.json")

workingArea = sys.argv[1]
configJSON = sys.argv[2]

# Helper function to get region names
def _get_other_region_names(pass_reg_name):
    '''
    If passing e.g. "fail", will return ("fail", "pass")
    In HSCP analysis, we're just considering F/P regions
    '''
    return pass_reg_name, pass_reg_name.replace('fail','pass')

# Helper function to generate constraints for parametric Transfer Functions
# Change values as you see fit
def _generate_constraints(nparams):
    out = {}
    for i in range(nparams):
        if i == 0:
            out[i] = {"MIN":-30,"MAX":30}
        else:
            out[i] = {"MIN":-50,"MAX":50}
    return out

# Dict to store transfer function forms and constraints
_rpf_options = {
    '0x0': {
        'form': '0.1*(@0)',
        'constraints': _generate_constraints(1)
    },
    '1x0': {
        'form': '0.1*(@0+@1*x)',
        'constraints': _generate_constraints(2)
    },
    '0x1': {
        'form': '0.1*(@0+@1*y)',
        'constraints': _generate_constraints(2)
    },
    '1x1': {
        'form': '0.1*(@0+@1*x)*(1+@2*y)',
        'constraints': _generate_constraints(3)
    },
    '2x0': {
        'form': '0.1*(@0+@1*x+@2*x**2)*(@3)',
        'constraints': _generate_constraints(4)
    },
    '2x1': {
        'form': '0.1*(@0+@1*x+@2*x**2)*(1+@3*y)',
        'constraints': _generate_constraints(4)
    },
    '2x2': {
        'form': '0.1*(@0+@1*x+@2*x**2)*(1+@3*y+@4*y**2)',
        'constraints': _generate_constraints(4)
    }
}

# Helper function for selecting the signal from the ledger
def _select_signal(row, args):
    signame = args[0]
    poly_order = args[1]
    if row.process_type == 'SIGNAL':
        if signame in row.process:
            return True
        else:
            return False
    elif 'Background' in row.process:
        if row.process == 'Background_'+poly_order:
            return True
        elif row.process == 'Background':
            return True
        else:
            return False
    else:
        return True


# Make the workspace
def make_workspace():
  # Create the workspace directory, using info from the specified JSON file
  twoD = TwoDAlphabet(workingArea, configJSON, loadPrevious=False)

  # 2DAlphabet wasn't intended for an analysis like this, so the default function 
  # for Looping over all regions and for a given region's data histogram, subtracting
  # the list of background histograms, and returning a data-bkgList is called initQCDHists.
  # This is b/c QCD multijet is the main background we usually estimate via 2DAlphabe
  bkg_hists = twoD.InitQCDHists()
  #print('bkg_hists = {}'.format(bkg_hists))

  # Now, we loop over "pass" and "fail" regions and get the binnings
  for f, p in [_get_other_region_names(r) for r in twoD.ledger.GetRegions() if 'fail' in r]:
    #print(f, p)
    # get the binning for the fail region
    binning_f, _ = twoD.GetBinningFor(f)
    # you can change the name as you see fit 
    fail_name = 'Background_'+f
    # this is the actual binned distribution of the fail
    bkg_f = BinnedDistribution(fail_name, bkg_hists[f], binning_f, constant=False)
    # now we add it to the 2DAlphabet ledger
    twoD.AddAlphaObj('Background',f, bkg_f)

    # now construct all of the possible transfer functions, to be chosen and used later
    for opt_name, opt in _rpf_options.items():
           bkg_rpf = ParametricFunction(
               fail_name.replace('fail','rpf')+'_'+opt_name, # this is our pass/fail ratio
               binning_f,                                    # we use the binning from fail
               opt['form'],                                  # was _rpf_options['0x0']['form'],
               opt['constraints']                # was _rpf_options['0x0']['constraints'] 
           )

           # now define the bkg in pass as the bkg in fail multiplied by the transfer function (bkg_rpf)
           bkg_p = bkg_f.Multiply(fail_name.replace('fail','pass')+'_'+opt_name, bkg_rpf)

           # then add this to the 2DAlphabet ledger
           twoD.AddAlphaObj('Background_'+opt_name,p,bkg_p,title='Background')

    # and save it out
    twoD.Save()

def perform_fit(signal, tf, rMaxExt = 30, extra=''):
    '''
        signal [str] = 'Type-Mass'
        tf [str] = 0x0, 0x1, 1x0, 1x1, 1x2, 2x2
        extra (str) = any extra flags to pass to Combine when running the ML fit
    '''
    # this is the name of the directory created in the workspace function
    working_area = workingArea
    # we reuse the workspace from the last step.
    # The runConfig.json is copied from the origin JSON config file, 
    # and we must specify that we want to load the previous workspace
    twoD = TwoDAlphabet(working_area, '{}/runConfig.json'.format(working_area), loadPrevious=True)

    # Now we create a ledger and make a new area for it with a Combine card
    # this select() method uses lambda functions. Will explain later
    print("tf: " + str(tf))
    subset = twoD.ledger.select(_select_signal, '{}'.format(""), tf)
    twoD.MakeCard(subset, '{}-{}_area'.format("Signal_gluino-1800", tf))

    # perform fit
    print("perform fit")
    twoD.MLfit('{}-{}_area'.format(signal, tf), rMin=0, rMax=rMaxExt, verbosity=1, extra=extra)


def plot_fit(signal, tf):
    print("DoingTwoDAlphabet")
    twoD = TwoDAlphabet("2DAlpha_CodeV46p8_1Dfrom2DNoExtrapol_Glu1800Stau557", '2DAlpha_CodeV46p8_1Dfrom2DNoExtrapol_Glu1800Stau557/runConfig.json', loadPrevious=True)
    print("Doing twoD.ledger.select")
    subset = twoD.ledger.select(_select_signal, '{}'.format(""), tf) 
    #subset = twoD.ledger.select(_select_signal, '{}'.format(signal), tf)
    print("Doing twoD.StdPlots")
    twoD.StdPlots('Signal_gluino-1800-0x0_area', subset)

if __name__ == "__main__":
    #make_workspace()
    if (True) :
      fitPassed = False
      # If the fit failed iterate on rMax
      rMax = 30
      while not (fitPassed) :
        print("\n\n\nperform_fit with rMax = " + str(rMax))
        perform_fit("Signal_gluino-1800",'0x0',rMax,extra='--robustHesse 1')
        # Do fitting until the fit passes
        with open(workingArea + "/Signal_gluino-1800-0x0_area/FitDiagnostics.log", 'r') as file:
          content = file.read()
          if not "Fit failed" in content: fitPassed = True
          rMax = rMax / 10.
    plot_fit('','0x0')
