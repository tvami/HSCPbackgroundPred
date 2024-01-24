import pickle
import ROOT


ROOT.gStyle.SetOptStat(0)
ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetPadTopMargin(0.07);
ROOT.gStyle.SetPadBottomMargin(0.1);
ROOT.gStyle.SetPadLeftMargin(0.13);
ROOT.gStyle.SetPadRightMargin(0.15);


#with open('output_BR100pct.root.expectedSurface.pkl', 'rb') as f:
with open('output_BR100pct.root.observedSurface.pkl', 'rb') as f:
    data = pickle.load(f)

xPoints = data["x"].flatten()
yPoints = data["y"].flatten()
zPoints = data["z"].flatten()

result = list(zip(xPoints, yPoints, zPoints))

tauPrimeMass = (200, 400, 600, 800, 1000, 1200, 1400)
ZPrimeMass = (3000, 4000, 5000, 6000, 7000)

graph = ROOT.TGraph2D()

for point in result:
    x, y, z = point
    graph.SetPoint(graph.GetN(), x, y, z)
    
graphOrig = ROOT.TGraph()
for x in tauPrimeMass :
  for y in ZPrimeMass :
    graphOrig.SetPoint(graphOrig.GetN(), x, y)
    
phenoContour = ROOT.TGraph("phenoContour.csv", "%lg,%lg")
#phenoContour.SetFillColorAlpha(ROOT.kBlue-2,0.2)
#phenoContour.SetFillColorAlpha(ROOT.kBlue,0.99)
phenoContour.SetFillColorAlpha(ROOT.kBlack,0.99)
#phenoContour.SetFillStyle(3005)
phenoContour.SetFillStyle(3004)
#phenoContour.SetLineColor(ROOT.kBlue)
phenoContour.SetLineColor(ROOT.kBlack)
#phenoContour.SetLineWidth(2)
phenoContour.SetLineWidth(1)
    
graph.SetMinimum(0.00001)
#graph.SetNpy(500);
#graph.SetNpx(500);
canvas = ROOT.TCanvas("canvas", "Graph;Ztuff", 800, 600)

canvas.SetLogz()

graph.Draw("colz")
phenoContour.Draw("LFSAME")
graph.SetTitle("")
graphOrig.SetMarkerColor(1)
graphOrig.SetMarkerStyle(ROOT.kCircle)
graphOrig.SetMarkerSize(0.75)
graphOrig.Draw("PSAME")
graph.GetXaxis().SetTitle("m(#tau'^{2e}) [GeV]")
graph.GetYaxis().SetTitle("m(Z') [GeV]")
graph.GetZaxis().SetTitle("Cross Section [pb]")
graph.GetZaxis().SetTitleOffset(1.25)

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


tex2 = ROOT.TLatex(0.14,0.94,"CMS");
#tex2 = ROOT.TLatex(0.20,0.94,"CMS");#if there is 10^x
tex2.SetNDC();
tex2.SetTextFont(61);
tex2.SetTextSize(0.0675);
tex2.SetLineWidth(2);

#tex3 = ROOT.TLatex(0.27,0.94,"Simulation"); # for square plots
#tex3 = ROOT.TLatex(0.28,0.94,"Work in Progress 2018"); #if there is 10^x
tex3 = ROOT.TLatex(0.65,0.94,"101 fb^{-1} (13 TeV)");
tex3.SetNDC();
tex3.SetTextFont(52);
tex3.SetTextSize(0.0485);
tex3.SetLineWidth(2);
tex2.Draw("SAME")
tex3.Draw("SAME")

canvas.Update()
ROOT.gPad.RedrawAxis()
canvas.SaveAs("ZPrimeVsTauPrimeExcludedObsXsection.pdf")
canvas.SaveAs("ZPrimeVsTauPrimeExcludedObsXsection.C")
