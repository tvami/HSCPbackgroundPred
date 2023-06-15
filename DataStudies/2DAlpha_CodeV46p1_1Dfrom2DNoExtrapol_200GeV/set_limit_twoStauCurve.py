from optparse import OptionParser
import subprocess
import array
from  array import array

import ROOT
from ROOT import *

import header
from header import WaitForJobs, make_smooth_graph, Inter
import tdrstyle, CMS_lumi

gStyle.SetOptStat(0)
gROOT.SetBatch(kTRUE)

parser = OptionParser()

# parser.add_option('-t', '--tag', metavar='FILE', type='string', action='store',
#                 default   =   'dataBsOff',
#                 dest      =   'tag',
#                 help      =   'Tag ran over')
parser.add_option('-s', '--signals', metavar='FILE', type='string', action='store',
                default   =   'bstar_signalsLH.txt',
                dest      =   'signals',
                help      =   'Text file containing the signal names and their corresponding cross sections')
parser.add_option('-P', '--plotOnly', action="store_true",
                default   =   False,
                dest      =   'plotOnly',
                help      =   'Only plots if True')
parser.add_option('--unblind', action="store_false",
                default   =   True,
                dest      =   'blind',
                help      =   'Only plot observed limit if false')
parser.add_option('--drawIntersection', action="store_true",
                default   =   False,
                dest      =   'drawIntersection',
                help      =   'Draw intersection values')
parser.add_option('-l', '--lumi', metavar='F', type='string', action='store',
                default       =       '101', #137.44
                dest          =       'lumi',
                help          =       'Luminosity option')
parser.add_option('-m', '--mod', metavar='F', type='string', action='store',
                default       =       '',
                dest          =       'mod',
                help          =       'Modification to limit title on y-axis. For example, different handedness of the signal')
parser.add_option('-p', '--particle', type='string', action='store',
                default       =       '#tilde{g}',
                dest          =       'particle',
                help          =       'Name of HSCP. e.g. #tilde{g}')
parser.add_option('-x', '--process', type='string', action='store',
                default       =       'pp#rightarrow#tilde{g}#tilde{g}',
                dest          =       'process',
                help          =       'Name of HSCP. e.g. pp#rightarrow#tilde{g}#tilde{g}')
parser.add_option('-o', '--xsorder', type='string', action='store',
                default       =       'NLO+NLL',
                dest          =       'xsorder',
                help          =       'Order of XS calculation. e.g. NLO+NLL')
parser.add_option('-d', '--debug', type='int',
                default       =       0,
                dest          =       'debug',
                help          =       'Debug level')

(options, args) = parser.parse_args()

debug = options.debug

# Open signal file
signal_file = open(options.signals,'r')
# Read in names of project spaces as a list of strings and strip whitespace
signal_names = signal_file.readline().split(',')
signal_names = [n.strip() for n in signal_names]
# Read in mass as a list of strings, strip whitespace, and convert to ints
signal_mass = signal_file.readline().split(',')
signal_mass = [float(m.strip())/1000 for m in signal_mass]
# Read in xsecs as a list of strings, strip whitespace, and convert to floats
theory_xsecs = signal_file.readline().split(',')
theory_xsecs = [float(x.strip()) for x in theory_xsecs]
# Read in xsecs used in the files
signal_xsecs = signal_file.readline().split(',')
signal_xsecs = [float(x.strip()) for x in signal_xsecs]
# Read in 2nd theo xsection line
theory_xsecs_v2 = signal_file.readline().split(',')
theory_xsecs_v2 = [float(x.strip()) for x in theory_xsecs_v2]

# Initialize arrays to eventually store the points on the TGraph
x_mass = array('d')
y_limit = array('d')
y_mclimit  = array('d')
y_mclimitlow68 = array('d')
y_mclimitup68 = array('d')
y_mclimitlow95 = array('d')
y_mclimitup95 = array('d')

tdrstyle.setTDRStyle()

# For each signal
for this_index, this_name in enumerate(signal_names):
    # Setup call for one of the signal
    this_xsec = signal_xsecs[this_index]
    this_mass = signal_mass[this_index]
    this_output = TFile.Open(this_name+'/higgsCombineTest.AsymptoticLimits.mH120.root')
    if not this_output: continue
    this_tree = this_output.Get('limit')

    # Set the mass (x axis)
    x_mass.append(this_mass)
    # Grab the cross section limits (y axis)
    for ievent in range(int(this_tree.GetEntries())):
        this_tree.GetEntry(ievent)

        # Nominal expected
        if this_tree.quantileExpected == 0.5:
            y_mclimit.append(this_tree.limit*this_xsec)
        # -1 sigma expected
        if round(this_tree.quantileExpected,2) == 0.16:
            y_mclimitlow68.append(this_tree.limit*this_xsec)
        # +1 sigma expected
        if round(this_tree.quantileExpected,2) == 0.84:
            y_mclimitup68.append(this_tree.limit*this_xsec)
        # -2 sigma expected
        if round(this_tree.quantileExpected,3) == 0.025:
            y_mclimitlow95.append(this_tree.limit*this_xsec)
        # +2 sigma expected
        if round(this_tree.quantileExpected,3) == 0.975:
            y_mclimitup95.append(this_tree.limit*this_xsec)
        if (debug > 0) : print("For " + str(this_mass) + " mc_limit is " +str(y_mclimit))
        # Observed (plot only if unblinded)
        if this_tree.quantileExpected == -1:
            if not options.blind:
                if (debug > 0) : print('DEBUG : appending to y_limit')
                if (debug > 0) : print('appending: {} to y_limit'.format(this_tree.limit*this_xsec))
                y_limit.append(this_tree.limit*this_xsec)
            else:
                y_limit.append(0.0)

# Make Canvas and TGraphs (mostly stolen from other code that formats well)
climits = TCanvas("climits", "climits",700, 600)
climits.SetLogy(True)
climits.SetLeftMargin(.15)
climits.SetBottomMargin(.15)
climits.SetTopMargin(0.1)
climits.SetRightMargin(0.05)

# NOT GENERIC
# if options.hand == 'LH':
#     cstr = 'L'
# elif options.hand == 'RH':
#     cstr = 'R'
# elif options.hand == 'VL':
#     cstr = 'LR'
# else:
#     cstr = ''
cstr = options.mod

gStyle.SetTextFont(42)
TPT = ROOT.TPaveText(.20, .22, .5, .27,"NDC")
TPT.AddText("All-Hadronic Channel") # NOT GENERIC
TPT.SetFillColor(0)
TPT.SetBorderSize(0)
TPT.SetTextAlign(12)

# Expected
if (debug > 0) : 
    print('---------DEBUG-----------')
    print('x_mass: {}'.format(x_mass))
    print('len x_mass: {}'.format(len(x_mass)))
    print('y_mclimit: {}'.format(y_mclimit))
g_mclimit = TGraph(len(x_mass), x_mass, y_mclimit)
g_mclimit.SetTitle("")
g_mclimit.SetMarkerStyle(21)
g_mclimit.SetMarkerColor(1)
g_mclimit.SetLineColor(1)
g_mclimit.SetLineStyle(2)
g_mclimit.SetLineWidth(3)
g_mclimit.SetMarkerSize(0.)

if (len(x_mass) != len(y_mclimit)) :
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Num of mass point not the same as the num of limit point")
    print("Check your input files, we exit now")
    exit()

# Observed
if not options.blind:
    print('Not blinded')
    print('---------------DEBUG---------------------')
    print('x_mass: {}'.format(x_mass))
    print('len x_mass: {}'.format(len(x_mass)))
    print('y_limit: {}'.format(y_limit))
    g_limit = TGraph(len(x_mass), x_mass, y_limit)
    g_limit.SetTitle("")
    g_limit.SetMarkerStyle(7)
    g_limit.SetMarkerColor(1)
    g_limit.SetLineColor(1)
    g_limit.SetLineWidth(2)
    g_limit.SetMarkerSize(1) #0.5
    if ("tau" in cstr) :
      g_limit.GetXaxis().SetRangeUser(0.1, 1.5)
      g_limit.SetMinimum(5e-6) #0.005
      g_limit.SetMaximum(0.02)
    #if ("Prime" in cstr) :
    #  g_limit.GetXaxis().SetRangeUser(0.8, 3.0)
    #  g_limit.SetMinimum(5e-6) #0.005
    #  g_limit.SetMaximum(0.02)
    else:
      g_limit.GetXaxis().SetRangeUser(0.8, 3.0)
      g_limit.SetMinimum(5e-5) #0.005
      g_limit.SetMaximum(0.2)
else:
    print('Blinded')
    g_mclimit.GetXaxis().SetTitle("m("+options.particle+") [TeV]")  # NOT GENERIC
    g_mclimit.GetYaxis().SetTitle("Cross Section [pb]") # NOT GENERIC
    if ("tau" in cstr) :
      g_mclimit.GetXaxis().SetRangeUser(0.1, 1.5)
      g_mclimit.SetMinimum(5e-6) #0.005
      g_mclimit.SetMaximum(0.02)
    #if ("Prime" in cstr) :
    #  g_mclimit.GetXaxis().SetRangeUser(0.2, 1.8)
    #  g_mclimit.SetMinimum(5e-6) #0.005
    #  g_mclimit.SetMaximum(0.2)
    else:
      g_mclimit.GetXaxis().SetRangeUser(0.8, 3.0)
      g_mclimit.SetMinimum(5e-5) #0.005
      g_mclimit.SetMaximum(0.2)
# Expected
# g_mclimit = TGraph(len(x_mass), x_mass, y_mclimit)
# g_mclimit.SetTitle("")
# g_mclimit.SetMarkerStyle(21)
# g_mclimit.SetMarkerColor(1)
# g_mclimit.SetLineColor(1)
# g_mclimit.SetLineStyle(2)
# g_mclimit.SetLineWidth(3)
# g_mclimit.SetMarkerSize(0.)
# g_mclimit.GetXaxis().SetTitle("M_{b*} (TeV/c^{2})")
# g_mclimit.GetYaxis().SetTitle("Upper Limit #sigma_{b*_{"+cstr+"}} #times b (pb)")
# g_mclimit.GetYaxis().SetTitleSize(0.03)
# g_mclimit.Draw("l")
# g_mclimit.GetYaxis().SetRangeUser(0., 80.)

# Will later be 1 and 2 sigma expected
g_mcplus = TGraph(len(x_mass), x_mass, y_mclimitup68)
g_mcminus = TGraph(len(x_mass), x_mass, y_mclimitlow68)

g_mc2plus = TGraph(len(x_mass), x_mass, y_mclimitup95)
g_mc2minus = TGraph(len(x_mass), x_mass, y_mclimitlow95)

# Theory line
graphWP = ROOT.TGraph()
graphWP.SetTitle("")
graphWP.SetMarkerStyle(23)
graphWP.SetMarkerColor(4)
graphWP.SetMarkerSize(0.5)
graphWP.GetYaxis().SetRangeUser(0., 80.)
graphWP.GetXaxis().SetRangeUser(1.0, 3.0)
graphWP.SetMinimum(0.3e-3) #0.005
graphWP.SetMaximum(100.)
graphWP.SetLineWidth(3)
graphWP.SetLineColor(4)

graphWP_v2 = ROOT.TGraph()
graphWP_v2.SetTitle("")
graphWP_v2.SetMarkerStyle(23)
graphWP_v2.SetMarkerColor(6)
graphWP_v2.SetMarkerSize(0.5)
graphWP_v2.GetYaxis().SetRangeUser(0., 80.)
graphWP_v2.GetXaxis().SetRangeUser(1.0, 3.0)
graphWP_v2.SetMinimum(0.3e-3) #0.005
graphWP_v2.SetMaximum(100.)
graphWP_v2.SetLineWidth(3)
graphWP_v2.SetLineColor(6)

xsecAt1800 = 0
for index,mass in enumerate(signal_mass):
    xsec = theory_xsecs[index]
    xsec_v2 = theory_xsecs_v2[index]
    graphWP.SetPoint(index,    mass,   xsec    )
    graphWP_v2.SetPoint(index,    mass,   xsec_v2 )
    if (mass == 1.8 ) : xsecAt1800 = theory_xsecs[index]

graphWPFixedAt1800  = ROOT.TGraph()
graphWPFixedAt1800.SetPoint(0, 1.799, xsecAt1800*0.99)
graphWPFixedAt1800.SetPoint(1, 1.8, xsecAt1800)
graphWPFixedAt1800.SetPoint(2, 1.801, xsecAt1800*1.01)


# Theory up and down unnecessary if not splitting PDF uncertainty into shape and norm
#
# # Theory up
graphWPup = ROOT.TGraph()
graphWPup.SetTitle("")
graphWPup.SetMarkerStyle(23)
graphWPup.SetMarkerColor(4)
graphWPup.SetLineColor(4)
graphWPup.SetLineWidth(2)
graphWPup.SetMarkerSize(0.5)

graphWPup_v2 = ROOT.TGraph()
graphWPup_v2.SetTitle("")
graphWPup_v2.SetMarkerStyle(23)
graphWPup_v2.SetMarkerColor(6)
graphWPup_v2.SetLineColor(6)
graphWPup_v2.SetLineWidth(2)
graphWPup_v2.SetMarkerSize(0.5)

q = 0
for index,mass in enumerate(signal_mass):
    rt_xsec = 1.1*theory_xsecs[index]
    rt_xsec_v2 = 1.1*theory_xsecs_v2[index]
    graphWPup.SetPoint(q,    mass ,   rt_xsec    )
    graphWPup_v2.SetPoint(q,    mass ,   rt_xsec_v2    )
    q+=1

# # Theory down
graphWPdown = ROOT.TGraph()
graphWPdown.SetTitle("")
graphWPdown.SetMarkerStyle(23)
graphWPdown.SetMarkerColor(4)
graphWPdown.SetLineColor(4)
graphWPdown.SetLineWidth(2)
graphWPdown.SetMarkerSize(0.5)

graphWPdown_v2 = ROOT.TGraph()
graphWPdown_v2.SetTitle("")
graphWPdown_v2.SetMarkerStyle(23)
graphWPdown_v2.SetMarkerColor(6)
graphWPdown_v2.SetLineColor(6)
graphWPdown_v2.SetLineWidth(2)
graphWPdown_v2.SetMarkerSize(0.5)

q = 0
for index,mass in enumerate(signal_mass):
    rt_xsec = 0.9*theory_xsecs[index]
    rt_xsec_v2 = 0.9*theory_xsecs_v2[index]
    graphWPdown.SetPoint(q,    mass ,   rt_xsec    )
    graphWPdown_v2.SetPoint(q,    mass ,   rt_xsec_v2    )
    q+=1

graphWPup.SetLineStyle(2)
graphWPdown.SetLineStyle(2)
graphWPup_v2.SetLineStyle(2)
graphWPdown_v2.SetLineStyle(2)
WPunc = make_smooth_graph(graphWPdown, graphWPup)
WPunc.SetFillColor(4)
WPunc.SetFillStyle(3004)
WPunc.SetLineColor(0)

# 2 sigma expected
g_error95 = make_smooth_graph(g_mc2minus, g_mc2plus)
g_error95.SetFillColor(kOrange)
g_error95.SetLineColor(0)

# 1 sigma expected
g_error = make_smooth_graph(g_mcminus, g_mcplus)
g_error.SetFillColor( kGreen+1)
g_error.SetLineColor(0)

if not options.blind:
    g_limit.GetXaxis().SetTitle("m("+options.particle+") [TeV]")  # NOT GENERIC
    g_limit.GetYaxis().SetTitle("Cross Section [pb]") # NOT GENERIC
    g_limit.GetXaxis().SetTitleSize(0.055)
    g_limit.GetYaxis().SetTitleSize(0.05)
    g_limit.Draw('ap')
    g_error95.Draw("lf")
    g_error.Draw("lf")
    g_mclimit.Draw("l")
    g_limit.Draw("lp")
    g_limit.GetYaxis().SetTitleOffset(1.5)
    g_limit.GetXaxis().SetTitleOffset(1.25)

else:
    g_mclimit.GetXaxis().SetTitle("m("+options.particle+") [TeV]")  # NOT GENERIC
    g_mclimit.GetYaxis().SetTitle("Cross Section [pb]") # NOT GENERIC
    g_mclimit.GetXaxis().SetTitleSize(0.055)
    g_mclimit.GetYaxis().SetTitleSize(0.05)
    g_mclimit.Draw("al")
    g_error95.Draw("lf")
    g_error.Draw("lf")
    g_mclimit.Draw("l")
    g_mclimit.GetYaxis().SetTitleOffset(1.5)
    g_mclimit.GetXaxis().SetTitleOffset(1.25)

graphWP.Draw("l")
graphWPdown.Draw("l")
graphWPup.Draw("l")
graphWP_v2.Draw("l")
graphWPdown_v2.Draw("l")
graphWPup_v2.Draw("l")
#graphWPFixedAt1800.SetMarkerStyle(29)
#graphWPFixedAt1800.Draw("samep")

# Finally calculate the intercept
expectedMassLimit,expectedCrossLimit = Inter(g_mclimit,graphWP) #if len(Inter(g_mclimit,graphWP)) > 0 else -1.0
expectedMassLimit_v2,expectedCrossLimit_v2 = Inter(g_mclimit,graphWP_v2)
upLimit,upXsectionLim = Inter(g_mcminus,graphWP) if len(Inter(g_mcminus,graphWP)) > 0 else -1.0
lowLimit,lowXsectionLim = Inter(g_mcplus,graphWP) if len(Inter(g_mcplus,graphWP)) > 0 else -1.0

a,expectedCrossLimitAt1800 = Inter(g_mclimit,graphWPFixedAt1800) #if len(Inter(g_mclimit,graphWPFixedAt1800)) > 0 else -1.0
a,upXsectionLimAt1800 = Inter(g_mcminus,graphWPFixedAt1800) if len(Inter(g_mcminus,graphWPFixedAt1800)) > 0 else -1.0
a,lowXsectionLimAt1800 = Inter(g_mcplus,graphWPFixedAt1800) if len(Inter(g_mcplus,graphWPFixedAt1800)) > 0 else -1.0


expLine = TLine(expectedMassLimit,g_mclimit.GetMinimum(),expectedMassLimit,expectedCrossLimit)
expLine.SetLineStyle(2)

#expLine.Draw()

if options.drawIntersection:
    expLineLabel = TPaveText(expectedMassLimit-300, expectedCrossLimit*2, expectedMassLimit+300, expectedCrossLimit*15, "NB")
    expLineLabel.SetFillColorAlpha(kWhite,0)
    expLineLabel.AddText(str(round(expectedMassLimit,2))+' TeV')
    expLineLabel.Draw()

print('Expected mass limit: '+str(round(expectedMassLimit,3)) + ' +'+str(round(upLimit-expectedMassLimit,3)) +' -'+str(round(expectedMassLimit-lowLimit,3)) + ' TeV')
print('Expected xsection limit at excluded mass: '+str(round(expectedCrossLimit,6)) + ' +'+str(round(expectedCrossLimit-upXsectionLim,6)) +' -'+str(round(lowXsectionLim-expectedCrossLimit,6)) + ' pb') 
print('Expected xsection limit @1800GeV: '+str(round(expectedCrossLimitAt1800,6)) + ' +'+str(round(expectedCrossLimitAt1800-upXsectionLimAt1800,6)) +' -'+str(round(lowXsectionLimAt1800-expectedCrossLimitAt1800,6)) + ' pb') 
print('Theory xsection limit @1800GeV: '+str(round(graphWP.Eval(1.8),6)) + ' pb')


if not options.blind:
    obsMassLimit,obsCrossLimit = Inter(g_limit,graphWP) if len(Inter(g_limit,graphWP)) > 0 else -1.0
    print('Observed limit: '+str(obsMassLimit) + ' TeV')

    obsLine = TLine(obsMassLimit,g_mclimit.GetMinimum(),obsMassLimit,obsCrossLimit)
    obsLine.SetLineStyle(2)
    obsLine.Draw()

# Legend and draw
gStyle.SetLegendFont(62)
legend = TLegend(0.5, 0.6, 0.92, 0.9, '')
legend.SetHeader("95% CL Upper Limits")
if not options.blind:
    legend.AddEntry(g_limit, "Observed Limit", "l")
legend.AddEntry(g_error95, "Expected Limit #pm1#sigma, #pm2#sigma","f")
# legend.AddEntry(g_error95, "#pm1#sigma, 2#sigma", "f")
# legend.AddEntry(g_error95, "#pm2#sigma", "f")
legend.AddEntry(graphWP, "#sigma^{"+options.xsorder+"}_{th}(pp#rightarrow#tilde{#tau}_{L}#tilde{#tau}_{L})#pm1#sigma", "l")
legend.AddEntry(graphWP_v2, "#sigma^{"+options.xsorder+"}_{th}(pp#rightarrow#tilde{#tau}_{R}#tilde{#tau}_{R})#pm1#sigma", "l") 

legend.SetBorderSize(0)
legend.SetFillStyle(0)
legend.SetLineColor(0)

legend.Draw("same")

# this is to fake the green+yellow band in the legend
tmpcolor = g_error.GetFillColor()
tmpline = ROOT.TLine()
tmpline.SetLineColor(tmpcolor)
tmLineWidth = 25  if options.blind else 20
tmpline.SetLineWidth(tmLineWidth)
tmpyposition = 0.785 if options.blind else 0.75
tmpline.DrawLineNDC(0.517,tmpyposition,0.588,tmpyposition)

# legend line for median point
tmpline.SetLineColor(1)
tmpline.SetLineWidth(3)
tmpline.SetLineStyle(2)
tmpline.DrawLineNDC(0.517,tmpyposition,0.588,tmpyposition)


# legend lines for theory
'''
tmpyposition = 0.66 if options.blind else 0.65
tmpline.SetLineColor(4)
tmpline.SetLineStyle(2)
tmpline.SetLineWidth(2)
tmpline.DrawLineNDC(0.517,tmpyposition,0.588,tmpyposition)

tmpyposition = 0.64 if options.blind else 0.625
tmpline.SetLineColor(4)
tmpline.SetLineStyle(2)
tmpline.SetLineWidth(2)
tmpline.DrawLineNDC(0.517,tmpyposition,0.588,tmpyposition)
'''

# intersection line
tmpline.SetLineColor(1)
tmpline.SetLineWidth(1)
tmpline.SetLineStyle(2)
tmpline.SetLineColor(ROOT.kGray+2)
tmpline.DrawLine(expectedMassLimit,0,expectedMassLimit,expectedCrossLimit)
tmpline.DrawLine(expectedMassLimit_v2,0,expectedMassLimit_v2,expectedCrossLimit_v2)

text1 = ROOT.TLatex()
# text1.SetNDC()
text1.SetTextFont(43)
text1.SetTextSize(14)
text1.SetTextColor(ROOT.kGray+2)
text1.SetTextAngle(90)
text1.DrawLatex(expectedMassLimit-0.005,0, "  %0.2f TeV"%(expectedMassLimit))
text1.DrawLatex(expectedMassLimit_v2-0.005,0, "  %0.2f TeV"%(expectedMassLimit_v2))

text2 = ROOT.TLatex()
# text2.SetNDC()
text2.SetTextFont(43)
text2.SetTextSize(14)
text2.SetTextColor(1)
text2.SetTextAngle(90)
if not options.blind:
    text2.DrawLatex(obsMassLimit-0.005,0, "  %0.2f TeV"%(obsMassLimit))


# text1 = ROOT.TLatex()
# text1.SetNDC()
# text1.SetTextFont(42)
# text1.DrawLatex(0.17,0.88, "#scale[1.0]{CMS, L = "+options.lumi+" fb^{-1} at  #sqrt{s} = 13 TeV}") # NOT GENERIC

# TPT.Draw()
climits.RedrawAxis()

CMS_lumi.extraText = 'Internal'
CMS_lumi.lumiTextSize     = 0.5

CMS_lumi.cmsTextSize      = 0.8
CMS_lumi.CMS_lumi(climits, 1, 11)

climits.SaveAs("limits_combine_"+options.lumi.replace('.','p')+"fb_"+options.signals[options.signals.find('/')+1:options.signals.find('.')]+'_'+cstr+".pdf")


