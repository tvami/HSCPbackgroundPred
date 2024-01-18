void limits_combine_101fb_signals_tauPrime2e_v2_HSCPTauPrime2e()
{
//=========Macro generated from canvas: climits/climits
//=========  (Fri Jan 12 00:01:36 2024) by ROOT version 6.14/09
   TCanvas *climits = new TCanvas("climits", "climits",0,0,700,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   climits->SetHighLightColor(2);
   climits->Range(0.4015,-6.021442,2.9515,-1.218695);
   climits->SetFillColor(0);
   climits->SetBorderMode(0);
   climits->SetBorderSize(2);
   climits->SetLogy();
   climits->SetTickx(1);
   climits->SetTicky(1);
   climits->SetLeftMargin(0.15);
   climits->SetRightMargin(0.05);
   climits->SetBottomMargin(0.15);
   climits->SetFrameFillStyle(0);
   climits->SetFrameBorderMode(0);
   climits->SetFrameFillStyle(0);
   climits->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1[7] = {
   0.6,
   0.8,
   1,
   1.4,
   1.8,
   2.2,
   2.6};
   Double_t Graph0_fy1[7] = {
   3.715753e-05,
   4.747048e-05,
   5.903983e-05,
   9.130658e-05,
   0.0001485301,
   0.0002821932,
   0.0005680085};
   TGraph *graph = new TGraph(7,Graph0_fx1,Graph0_fy1);
   graph->SetName("Graph0");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   graph->SetMarkerStyle(7);
   
   TH1F *Graph_Graph01 = new TH1F("Graph_Graph01","",100,0.4,2.8);
   Graph_Graph01->SetMinimum(5e-06);
   Graph_Graph01->SetMaximum(0.02);
   Graph_Graph01->SetDirectory(0);
   Graph_Graph01->SetStats(0);
   Graph_Graph01->SetLineStyle(0);
   Graph_Graph01->GetXaxis()->SetTitle("m(#tau'^{2e}) [TeV]");
   Graph_Graph01->GetXaxis()->SetRange(17,101);
   Graph_Graph01->GetXaxis()->SetLabelFont(42);
   Graph_Graph01->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph01->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph01->GetXaxis()->SetTitleSize(0.055);
   Graph_Graph01->GetXaxis()->SetTitleOffset(1.25);
   Graph_Graph01->GetXaxis()->SetTitleFont(42);
   Graph_Graph01->GetYaxis()->SetTitle("Cross Section [pb]");
   Graph_Graph01->GetYaxis()->SetLabelFont(42);
   Graph_Graph01->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph01->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph01->GetYaxis()->SetTitleSize(0.05);
   Graph_Graph01->GetYaxis()->SetTitleOffset(1.5);
   Graph_Graph01->GetYaxis()->SetTitleFont(42);
   Graph_Graph01->GetZaxis()->SetLabelFont(42);
   Graph_Graph01->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph01->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph01->GetZaxis()->SetTitleSize(0.08);
   Graph_Graph01->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph01);
   
   graph->Draw("ap");
   
   Double_t Graph1_fx2[16] = {
   0.6,
   0.8,
   1,
   1.4,
   1.8,
   2.2,
   2.6,
   2.6,
   2.6,
   2.6,
   2.2,
   1.8,
   1.4,
   1,
   0.8,
   0.6};
   Double_t Graph1_fy2[16] = {
   6.623034e-05,
   9.711275e-05,
   0.0001222721,
   0.0001824741,
   0.0002882392,
   0.0005343373,
   0.001085773,
   0.001085773,
   3.426246e-05,
   3.426246e-05,
   2.167901e-05,
   1.522125e-05,
   1.198629e-05,
   9.764106e-06,
   9.0802e-06,
   8.572083e-06};
   graph = new TGraph(16,Graph1_fx2,Graph1_fy2);
   graph->SetName("Graph1");
   graph->SetTitle("Graph");

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#ffcc00");
   graph->SetFillColor(ci);
   graph->SetFillStyle(1000);
   graph->SetLineColor(0);
   
   TH1F *Graph_Graph12 = new TH1F("Graph_Graph12","Graph",100,0.4,2.8);
   Graph_Graph12->SetMinimum(7.714874e-06);
   Graph_Graph12->SetMaximum(0.001193493);
   Graph_Graph12->SetDirectory(0);
   Graph_Graph12->SetStats(0);
   Graph_Graph12->SetLineStyle(0);
   Graph_Graph12->GetXaxis()->SetLabelFont(42);
   Graph_Graph12->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph12->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph12->GetXaxis()->SetTitleSize(0.08);
   Graph_Graph12->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph12->GetXaxis()->SetTitleFont(42);
   Graph_Graph12->GetYaxis()->SetLabelFont(42);
   Graph_Graph12->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph12->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph12->GetYaxis()->SetTitleSize(0.08);
   Graph_Graph12->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph12->GetYaxis()->SetTitleFont(42);
   Graph_Graph12->GetZaxis()->SetLabelFont(42);
   Graph_Graph12->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph12->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph12->GetZaxis()->SetTitleSize(0.08);
   Graph_Graph12->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph12);
   
   graph->Draw("lf");
   
   Double_t Graph2_fx3[16] = {
   0.6,
   0.8,
   1,
   1.4,
   1.8,
   2.2,
   2.6,
   2.6,
   2.6,
   2.6,
   2.2,
   1.8,
   1.4,
   1,
   0.8,
   0.6};
   Double_t Graph2_fy3[16] = {
   4.326898e-05,
   6.420028e-05,
   8.113475e-05,
   0.0001210823,
   0.0001912637,
   0.0003545644,
   0.0007204744,
   0.0007204744,
   8.611228e-05,
   8.611228e-05,
   5.064889e-05,
   3.236981e-05,
   2.327852e-05,
   1.764085e-05,
   1.560659e-05,
   1.214378e-05};
   graph = new TGraph(16,Graph2_fx3,Graph2_fy3);
   graph->SetName("Graph2");
   graph->SetTitle("Graph");

   ci = TColor::GetColor("#00cc00");
   graph->SetFillColor(ci);
   graph->SetFillStyle(1000);
   graph->SetLineColor(0);
   
   TH1F *Graph_Graph23 = new TH1F("Graph_Graph23","Graph",100,0.4,2.8);
   Graph_Graph23->SetMinimum(1.092941e-05);
   Graph_Graph23->SetMaximum(0.0007913074);
   Graph_Graph23->SetDirectory(0);
   Graph_Graph23->SetStats(0);
   Graph_Graph23->SetLineStyle(0);
   Graph_Graph23->GetXaxis()->SetLabelFont(42);
   Graph_Graph23->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph23->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph23->GetXaxis()->SetTitleSize(0.08);
   Graph_Graph23->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph23->GetXaxis()->SetTitleFont(42);
   Graph_Graph23->GetYaxis()->SetLabelFont(42);
   Graph_Graph23->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph23->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph23->GetYaxis()->SetTitleSize(0.08);
   Graph_Graph23->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph23->GetYaxis()->SetTitleFont(42);
   Graph_Graph23->GetZaxis()->SetLabelFont(42);
   Graph_Graph23->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph23->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph23->GetZaxis()->SetTitleSize(0.08);
   Graph_Graph23->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph23);
   
   graph->Draw("lf");
   
   Double_t Graph3_fx4[7] = {
   0.6,
   0.8,
   1,
   1.4,
   1.8,
   2.2,
   2.6};
   Double_t Graph3_fy4[7] = {
   2.285889e-05,
   3.228516e-05,
   4.031631e-05,
   6.016648e-05,
   9.504e-05,
   0.000176185,
   0.0003580077};
   graph = new TGraph(7,Graph3_fx4,Graph3_fy4);
   graph->SetName("Graph3");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineStyle(2);
   graph->SetLineWidth(3);
   graph->SetMarkerStyle(21);
   graph->SetMarkerSize(0);
   
   TH1F *Graph_Graph34 = new TH1F("Graph_Graph34","",100,0.4,2.8);
   Graph_Graph34->SetMinimum(2.0573e-05);
   Graph_Graph34->SetMaximum(0.0003915226);
   Graph_Graph34->SetDirectory(0);
   Graph_Graph34->SetStats(0);
   Graph_Graph34->SetLineStyle(0);
   Graph_Graph34->GetXaxis()->SetLabelFont(42);
   Graph_Graph34->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph34->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph34->GetXaxis()->SetTitleSize(0.08);
   Graph_Graph34->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph34->GetXaxis()->SetTitleFont(42);
   Graph_Graph34->GetYaxis()->SetLabelFont(42);
   Graph_Graph34->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph34->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph34->GetYaxis()->SetTitleSize(0.08);
   Graph_Graph34->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph34->GetYaxis()->SetTitleFont(42);
   Graph_Graph34->GetZaxis()->SetLabelFont(42);
   Graph_Graph34->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph34->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph34->GetZaxis()->SetTitleSize(0.08);
   Graph_Graph34->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph34);
   
   graph->Draw("l");
   
   Double_t Graph0_fx5[7] = {
   0.6,
   0.8,
   1,
   1.4,
   1.8,
   2.2,
   2.6};
   Double_t Graph0_fy5[7] = {
   3.715753e-05,
   4.747048e-05,
   5.903983e-05,
   9.130658e-05,
   0.0001485301,
   0.0002821932,
   0.0005680085};
   graph = new TGraph(7,Graph0_fx5,Graph0_fy5);
   graph->SetName("Graph0");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   graph->SetMarkerStyle(7);
   
   TH1F *Graph_Graph_Graph015 = new TH1F("Graph_Graph_Graph015","",100,0.4,2.8);
   Graph_Graph_Graph015->SetMinimum(5e-06);
   Graph_Graph_Graph015->SetMaximum(0.02);
   Graph_Graph_Graph015->SetDirectory(0);
   Graph_Graph_Graph015->SetStats(0);
   Graph_Graph_Graph015->SetLineStyle(0);
   Graph_Graph_Graph015->GetXaxis()->SetTitle("m(#tau'^{2e}) [TeV]");
   Graph_Graph_Graph015->GetXaxis()->SetRange(17,101);
   Graph_Graph_Graph015->GetXaxis()->SetLabelFont(42);
   Graph_Graph_Graph015->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph015->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph015->GetXaxis()->SetTitleSize(0.055);
   Graph_Graph_Graph015->GetXaxis()->SetTitleOffset(1.25);
   Graph_Graph_Graph015->GetXaxis()->SetTitleFont(42);
   Graph_Graph_Graph015->GetYaxis()->SetTitle("Cross Section [pb]");
   Graph_Graph_Graph015->GetYaxis()->SetLabelFont(42);
   Graph_Graph_Graph015->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph015->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph015->GetYaxis()->SetTitleSize(0.05);
   Graph_Graph_Graph015->GetYaxis()->SetTitleOffset(1.5);
   Graph_Graph_Graph015->GetYaxis()->SetTitleFont(42);
   Graph_Graph_Graph015->GetZaxis()->SetLabelFont(42);
   Graph_Graph_Graph015->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph_Graph015->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph_Graph015->GetZaxis()->SetTitleSize(0.08);
   Graph_Graph_Graph015->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph_Graph015);
   
   graph->Draw("lp");
   
   Double_t _fx6[7] = {
   0.6,
   0.8,
   1,
   1.4,
   1.8,
   2.2,
   2.6};
   Double_t _fy6[7] = {
   0.009363,
   0.00228,
   0.0006553,
   7.477e-05,
   1.056e-05,
   1.67e-06,
   2.913e-07};
   graph = new TGraph(7,_fx6,_fy6);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineWidth(3);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(0.5);
   
   TH1F *Graph_Graph6 = new TH1F("Graph_Graph6","",100,0.4,2.8);
   Graph_Graph6->SetMinimum(0.0003);
   Graph_Graph6->SetMaximum(100);
   Graph_Graph6->SetDirectory(0);
   Graph_Graph6->SetStats(0);
   Graph_Graph6->SetLineStyle(0);
   Graph_Graph6->GetXaxis()->SetLabelFont(42);
   Graph_Graph6->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph6->GetXaxis()->SetTitleSize(0.08);
   Graph_Graph6->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph6->GetXaxis()->SetTitleFont(42);
   Graph_Graph6->GetYaxis()->SetLabelFont(42);
   Graph_Graph6->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph6->GetYaxis()->SetTitleSize(0.08);
   Graph_Graph6->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph6->GetYaxis()->SetTitleFont(42);
   Graph_Graph6->GetZaxis()->SetLabelFont(42);
   Graph_Graph6->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph6->GetZaxis()->SetTitleSize(0.08);
   Graph_Graph6->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph6);
   
   graph->Draw("l");
   
   Double_t _fx7[7] = {
   0.6,
   0.8,
   1,
   1.4,
   1.8,
   2.2,
   2.6};
   Double_t _fy7[7] = {
   0.0084267,
   0.002052,
   0.00058977,
   6.7293e-05,
   9.504e-06,
   1.503e-06,
   2.6217e-07};
   graph = new TGraph(7,_fx7,_fy7);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineStyle(2);
   graph->SetLineWidth(2);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(0.5);
   
   TH1F *Graph_Graph7 = new TH1F("Graph_Graph7","",100,0.4,2.8);
   Graph_Graph7->SetMinimum(2.35953e-07);
   Graph_Graph7->SetMaximum(0.009269344);
   Graph_Graph7->SetDirectory(0);
   Graph_Graph7->SetStats(0);
   Graph_Graph7->SetLineStyle(0);
   Graph_Graph7->GetXaxis()->SetLabelFont(42);
   Graph_Graph7->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph7->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph7->GetXaxis()->SetTitleSize(0.08);
   Graph_Graph7->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph7->GetXaxis()->SetTitleFont(42);
   Graph_Graph7->GetYaxis()->SetLabelFont(42);
   Graph_Graph7->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph7->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph7->GetYaxis()->SetTitleSize(0.08);
   Graph_Graph7->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph7->GetYaxis()->SetTitleFont(42);
   Graph_Graph7->GetZaxis()->SetLabelFont(42);
   Graph_Graph7->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph7->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph7->GetZaxis()->SetTitleSize(0.08);
   Graph_Graph7->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph7);
   
   graph->Draw("l");
   
   Double_t _fx8[7] = {
   0.6,
   0.8,
   1,
   1.4,
   1.8,
   2.2,
   2.6};
   Double_t _fy8[7] = {
   0.0102993,
   0.002508,
   0.00072083,
   8.2247e-05,
   1.1616e-05,
   1.837e-06,
   3.2043e-07};
   graph = new TGraph(7,_fx8,_fy8);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineStyle(2);
   graph->SetLineWidth(2);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(0.5);
   
   TH1F *Graph_Graph8 = new TH1F("Graph_Graph8","",100,0.4,2.8);
   Graph_Graph8->SetMinimum(2.88387e-07);
   Graph_Graph8->SetMaximum(0.0113292);
   Graph_Graph8->SetDirectory(0);
   Graph_Graph8->SetStats(0);
   Graph_Graph8->SetLineStyle(0);
   Graph_Graph8->GetXaxis()->SetLabelFont(42);
   Graph_Graph8->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph8->GetXaxis()->SetLabelSize(0.05);
   Graph_Graph8->GetXaxis()->SetTitleSize(0.08);
   Graph_Graph8->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph8->GetXaxis()->SetTitleFont(42);
   Graph_Graph8->GetYaxis()->SetLabelFont(42);
   Graph_Graph8->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph8->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph8->GetYaxis()->SetTitleSize(0.08);
   Graph_Graph8->GetYaxis()->SetTitleOffset(1.25);
   Graph_Graph8->GetYaxis()->SetTitleFont(42);
   Graph_Graph8->GetZaxis()->SetLabelFont(42);
   Graph_Graph8->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph8->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph8->GetZaxis()->SetTitleSize(0.08);
   Graph_Graph8->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph8);
   
   graph->Draw("l");
   TLine *line = new TLine(1.369339,-1111,1.369339,8.830547e-05);
   line->SetLineStyle(2);
   line->Draw();
   
   TLegend *leg = new TLegend(0.5,0.6,0.92,0.89,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextFont(62);
   leg->SetLineColor(0);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(0);
   TLegendEntry *entry=leg->AddEntry("NULL","95% CL Upper Limits","h");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph0","Observed Limit","l");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph1","Expected Limit #pm1#sigma, #pm2#sigma","f");

   ci = TColor::GetColor("#ffcc00");
   entry->SetFillColor(ci);
   entry->SetFillStyle(1000);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   entry=leg->AddEntry("","#sigma^{NNLO+NNLL}_{th}(pp#rightarrow#tau'^{2e}#tau'^{2e})#pm1#sigma","l");
   entry->SetLineColor(4);
   entry->SetLineStyle(1);
   entry->SetLineWidth(3);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   leg->Draw();
   line = new TLine(0.517,0.713,0.588,0.713);

   ci = TColor::GetColor("#00cc00");
   line->SetLineColor(ci);
   line->SetLineWidth(15);
   line->Draw();
   line = new TLine(0.517,0.713,0.588,0.713);
   line->SetLineStyle(2);
   line->SetLineWidth(3);
   line->Draw();
   line = new TLine(0.517,0.65,0.588,0.65);
   line->SetLineColor(4);
   line->SetLineStyle(2);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(0.517,0.625,0.588,0.625);
   line->SetLineColor(4);
   line->SetLineStyle(2);
   line->SetLineWidth(2);
   line->Draw();
   line = new TLine(1.435999,0,1.435999,6.269369e-05);

   ci = TColor::GetColor("#666666");
   line->SetLineColor(ci);
   line->SetLineStyle(2);
   line->Draw();
   TLatex *   tex = new TLatex(1.430999,0,"  1.44 TeV");

   ci = TColor::GetColor("#666666");
   tex->SetTextColor(ci);
   tex->SetTextFont(43);
   tex->SetTextSize(14);
   tex->SetTextAngle(90);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(1.364339,0,"  1.37 TeV");
   tex->SetTextFont(43);
   tex->SetTextSize(14);
   tex->SetTextAngle(90);
   tex->SetLineWidth(2);
   tex->Draw();
   
   TH1F *Graph_copy = new TH1F("Graph_copy","",100,0.4,2.8);
   Graph_copy->SetMinimum(5e-06);
   Graph_copy->SetMaximum(0.02);
   Graph_copy->SetDirectory(0);
   Graph_copy->SetStats(0);
   Graph_copy->SetLineStyle(0);
   Graph_copy->GetXaxis()->SetTitle("m(#tau'^{2e}) [TeV]");
   Graph_copy->GetXaxis()->SetRange(17,101);
   Graph_copy->GetXaxis()->SetLabelFont(42);
   Graph_copy->GetXaxis()->SetLabelOffset(0.007);
   Graph_copy->GetXaxis()->SetLabelSize(0.05);
   Graph_copy->GetXaxis()->SetTitleSize(0.055);
   Graph_copy->GetXaxis()->SetTitleOffset(1.25);
   Graph_copy->GetXaxis()->SetTitleFont(42);
   Graph_copy->GetYaxis()->SetTitle("Cross Section [pb]");
   Graph_copy->GetYaxis()->SetLabelFont(42);
   Graph_copy->GetYaxis()->SetLabelOffset(0.007);
   Graph_copy->GetYaxis()->SetLabelSize(0.05);
   Graph_copy->GetYaxis()->SetTitleSize(0.05);
   Graph_copy->GetYaxis()->SetTitleOffset(1.5);
   Graph_copy->GetYaxis()->SetTitleFont(42);
   Graph_copy->GetZaxis()->SetLabelFont(42);
   Graph_copy->GetZaxis()->SetLabelOffset(0.007);
   Graph_copy->GetZaxis()->SetLabelSize(0.05);
   Graph_copy->GetZaxis()->SetTitleSize(0.08);
   Graph_copy->GetZaxis()->SetTitleFont(42);
   Graph_copy->Draw("sameaxis");
      tex = new TLatex(0.95,0.915,"101 fb^{-1} (13 TeV)");
tex->SetNDC();
   tex->SetTextAlign(31);
   tex->SetTextFont(42);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.15,0.915,"CMS");
tex->SetNDC();
   tex->SetTextFont(61);
   tex->SetTextSize(0.08);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.3,0.96,"");
tex->SetNDC();
   tex->SetTextAlign(13);
   tex->SetTextFont(52);
   tex->SetTextSize(0.0608);
   tex->SetLineWidth(2);
   tex->Draw();
   climits->Modified();
   climits->cd();
   climits->SetSelected(climits);
}
