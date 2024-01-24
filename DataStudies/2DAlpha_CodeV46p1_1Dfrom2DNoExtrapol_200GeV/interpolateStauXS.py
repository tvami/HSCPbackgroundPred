import matplotlib.pyplot as plt
import numpy as np
from array import array
import ROOT


## script to interpolate intermediate stau mass cross sections since the twiki doesn't have these masses
## https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVslepslep

## Interpolating the table at NLO+NLL precision using PDF4LHC15
## any single generation, sum of left- and right-handed sleptons

fig, ax = plt.subplots()

x,y,yup,ydown,yup_frac,ydown_frac = array("d"),array("d"),array("d"),array("d"),array("d"),array("d")

x.fromlist([50 , 80 , 100, 120, 125, 140, 150, 160, 175, 180, 200, 220, 225, 240, 250, 260, 275, 280, 300, 320, 340, 360, 380, 400, 440, 500, 600, 700, 800, 900, 1000])
'''
y.fromlist([
5.368    ,0.8014   ,0.3657   ,0.1928   ,0.1669   ,0.1116   ,0.08712  ,0.06896  ,0.04975  ,0.04485  ,0.03031  ,0.02115  ,0.01941  ,0.01514  ,0.01292  ,0.01108  ,0.008875 ,0.008259 ,0.006254 ,0.004802 ,0.003732 ,0.002931 ,0.002325 ,0.001859 ,0.001216 ,0.0006736,0.0002763,0.0001235,5.863e-05,2.918e-05,1.504e-05,
])
#Same for L-only
y.fromlist([
3.9906748000,0.5909244500,0.2678899700,0.1406291000,0.1216483300,0.0811408900,0.0632961040,0.0500452750,0.0360657630,0.0325025570,0.0219392150,0.0152887510,0.0140290420,0.0109371320,0.0093283983,0.0079963051,0.0064015765,0.0059558423,0.0045077309,0.0034592123,0.0026869113,0.0021095932,0.0016721666,0.0013368883,0.0008736890,0.0004835100,0.0001980417,0.0000883544,0.0000418944,0.0000208231,0.0000107156
])
'''

#Same for R-only
y.fromlist([
1.3770713000,0.2104129800,0.0978113150,0.0521521400,0.0452484250,0.0304104360,0.0238158970,0.0189132780,0.0136824980,0.0123470230,0.0083741187,0.0058590747,0.0053807607,0.0042047534,0.0035914049,0.0030828179,0.0024729013,0.0023024234,0.0017462546,0.0013426773,0.0010447821,0.0008216871,0.0006523448,0.0005222803,0.0003422616,0.0001901190,0.0000783113,0.0000351207,0.0000167406,0.0000083575,0.0000043273
])

yup_frac.fromlist([0.022,0.017,0.017,0.017,0.017,0.017,0.017,0.018,0.019,0.019,0.020,0.021,0.021,0.021,0.021,0.022,0.022,0.022,0.023,0.023,0.025,0.026,0.028,0.029,0.031,0.033,0.036,0.038,0.042,0.046,0.051,])


ydown_frac.fromlist([-3.9, -2.1, -1.8, -1.7, -1.7, -1.7, -1.7, -1.8, -1.9, -1.9, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.1, -2.1, -2.2, -2.3, -2.5, -2.6, -2.8, -3.0, -3.2, -3.6, -3.8, -4.2, -4.6, -5.2])


yup.fromlist([y[i]*(1+yup_frac[i]) for i in range(len(y))])
ydown.fromlist([y[i]*(1+ydown_frac[i]) for i in range(len(y))])


# x = np.array(x)
# y = np.array(y)
# yup = np.array(yup)
# ydown = np.array(ydown)

gr = ROOT.TGraph( len(x), x, y)

c = ROOT.TCanvas()
gr.SetMarkerStyle(22)
gr.Draw("ALP")

ROOT.gPad.SetLogy()


mymasses = [0.247,0.308, 0.432, 0.557, 0.651, 0.745, 0.871, 1.029]
mymasses = [x*1000 for x in mymasses]
myxs = []
for mymass in mymasses:
       print (mymass)
       #linear interpolation
       # myxs.append(gr.Eval(mymass) )
       myxs.append(gr.Eval(mymass,0,"S") )

print(mymasses)
print(myxs)

arrayx,arrayy = array("d"),array("d")
arrayx.fromlist(mymasses)
arrayy.fromlist(myxs)

mygr = ROOT.TGraph(len(arrayx),arrayx,arrayy)

mygr.SetMarkerStyle(23)
mygr.SetLineColor(ROOT.kRed)
mygr.SetMarkerColor(ROOT.kRed)
mygr.Draw("LP")

c.SaveAs("stauCrossections.pdf")



# x = [0.308, 0.432, 0.557, 0.651, 0.745, 0.871, 1.029]
# y = [0.0002321288143066406, 0.00015199648749999998, 0.00012412959375, 0.00011044920468750001, 0.00010260635175, 9.391863484375e-05, 8.742927384375e-05]



# y=[0.0048020183,
# 0.0012159719,
# 0.000389904,
# 0.0001234716,
# 5.8632201e-05,
# 2.9178605e-05,
# 1.50415955e-05,]

# ax.plot(x,y)

# # ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        # title='About as simple as it gets, folks')
# ax.grid()
# ax.set_yscale('log')
# fig.savefig("test.png")
# plt.show()
