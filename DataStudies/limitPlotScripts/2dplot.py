import ROOT
import sys


#######################
#######################
#######################
#######################
#######################
#######################
#  To add:
#  Change color scale to be excluded XS
#  Show contour at XS excluded XS from ATLAS
#  Show contour at XS expected from ATLAS


outputFile = ROOT.TFile("output_BR100pct.root")
#outputFile10 = ROOT.TFile("output_BR10pct.root")
#outputFile1 = ROOT.TFile("output_BR1pct.root")

canvas = ROOT.TCanvas("FinalCurves","FinalCurves")


#setup
dummy = ROOT.TH2D("dummy",";m(#tau'^{#pm#pm}) [GeV];m(Z') [GeV];thing",10,200,1400,10,3000,7000)
dummy.Draw("axis")
outputFile.Get("expectedUpperLimit_gr").Draw("colz same")
#outputFile.Get("upperLimit_gr").Draw("colz same")
dummy.SetMinimum(1e-5)
dummy.SetMaximum(1e+2)
ROOT.gPad.SetLogz()
ROOT.gPad.SetRightMargin(0.15)
ROOT.gStyle.SetOptStat(0)


phenoContour = ROOT.TGraph("limitPlotScripts/phenoContour.csv", "%lg,%lg")
phenoContour.Draw("LF")
phenoContour.SetFillColorAlpha(ROOT.kBlue-2,0.2)
phenoContour.SetLineColor(ROOT.kBlue-2)
phenoContour.SetLineWidth(2)

if outputFile.Get("Band_1s_0"):
    for iGraph in range(3):
        try:
            outputFile.Get("Band_1s_%d"%iGraph).Draw("L")
        except:
            pass

for iGraph in range(3 ):
    try:
        outputFile.Get("Exp_%d"%iGraph).Draw("L")
        # outputFile10.Get("Exp_%d"%iGraph).Draw("L")
        # outputFile1.Get("Exp_%d"%iGraph).Draw("L")

    except:
        pass


'''
for iGraph in range(3 ):
    try:
        outputFile.Get("Obs_%d"%iGraph).Draw("L")
    except:
        pass
'''

marker = ROOT.TGraph()
marker.SetPoint(0,650,5200)
marker.SetMarkerStyle(29)
marker.SetMarkerSize(2)
marker.SetMarkerColor(ROOT.kBlack)
marker.Draw("P")

latex = ROOT.TLatex()
latex.SetTextFont(63)
latex.SetTextSize(14)
latex.DrawLatex(650,5200,"    Best fit from\n [2205.04473]")



ROOT.gPad.RedrawAxis()
canvas.SaveAs("test.pdf")


