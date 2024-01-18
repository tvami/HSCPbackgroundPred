void limits_combine_101fb_signals_stop_v1_HSCPstop()
{
//=========Macro generated from canvas: climits/climits
//=========  (Fri Jan 12 00:01:04 2024) by ROOT version 6.14/09
   TCanvas *climits = new TCanvas("climits", "climits",0,0,700,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   climits->SetHighLightColor(2);
   climits->Range(0.4536,-5.021442,2.9016,-0.2186953);
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
   
   Double_t Graph0_fx1[9] = {
   1,
   1.2,
   1.4,
   1.6,
   1.8,
   2,
   2.2,
   2.4,
   2.6};
   Double_t Graph0_fy1[9] = {
   0.0004789789,
   0.0004610552,
   0.0004645231,
   0.0004938505,
   0.0005189575,
   0.0005255584,
   0.000530566,
   0.0005109394,
   0.0004456098};
   TGraph *graph = new TGraph(9,Graph0_fx1,Graph0_fy1);
   graph->SetName("Graph0");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   graph->SetMarkerStyle(7);
   
   TH1F *Graph_Graph01 = new TH1F("Graph_Graph01","",100,0.84,2.76);
   Graph_Graph01->SetMinimum(5e-05);
   Graph_Graph01->SetMaximum(0.2);
   Graph_Graph01->SetDirectory(0);
   Graph_Graph01->SetStats(0);
   Graph_Graph01->SetLineStyle(0);
   Graph_Graph01->GetXaxis()->SetTitle("m(#tilde{t}) [TeV]");
   Graph_Graph01->GetXaxis()->SetRange(0,101);
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
   
   Double_t Graph1_fx2[20] = {
   1,
   1.2,
   1.4,
   1.6,
   1.8,
   2,
   2.2,
   2.4,
   2.6,
   2.6,
   2.6,
   2.6,
   2.4,
   2.2,
   2,
   1.8,
   1.6,
   1.4,
   1.2,
   1};
   Double_t Graph1_fy2[20] = {
   0.00111091,
   0.001068857,
   0.001066483,
   0.001145646,
   0.001205099,
   0.001208749,
   0.001226889,
   0.001184136,
   0.001030481,
   0.001030481,
   0.0001359397,
   0.0001359397,
   0.0001536328,
   0.0001591797,
   0.0001568164,
   0.0001563525,
   0.0001486389,
   0.0001406889,
   0.0001414764,
   0.0001474939};
   graph = new TGraph(20,Graph1_fx2,Graph1_fy2);
   graph->SetName("Graph1");
   graph->SetTitle("Graph");

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#ffcc00");
   graph->SetFillColor(ci);
   graph->SetFillStyle(1000);
   graph->SetLineColor(0);
   
   TH1F *Graph_Graph12 = new TH1F("Graph_Graph12","Graph",100,0.84,2.76);
   Graph_Graph12->SetMinimum(2.684471e-05);
   Graph_Graph12->SetMaximum(0.001335984);
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
   
   Double_t Graph2_fx3[20] = {
   1,
   1.2,
   1.4,
   1.6,
   1.8,
   2,
   2.2,
   2.4,
   2.6,
   2.6,
   2.6,
   2.6,
   2.4,
   2.2,
   2,
   1.8,
   1.6,
   1.4,
   1.2,
   1};
   Double_t Graph2_fy3[20] = {
   0.0006534874,
   0.000630174,
   0.0006266662,
   0.0006686984,
   0.0007034006,
   0.0007086878,
   0.0007161194,
   0.000691165,
   0.0006055118,
   0.0006055118,
   0.0002060231,
   0.0002060231,
   0.000234146,
   0.0002425998,
   0.000238998,
   0.000238291,
   0.000226535,
   0.0002132208,
   0.0002144143,
   0.0002223027};
   graph = new TGraph(20,Graph2_fx3,Graph2_fy3);
   graph->SetName("Graph2");
   graph->SetTitle("Graph");

   ci = TColor::GetColor("#00cc00");
   graph->SetFillColor(ci);
   graph->SetFillStyle(1000);
   graph->SetLineColor(0);
   
   TH1F *Graph_Graph23 = new TH1F("Graph_Graph23","Graph",100,0.84,2.76);
   Graph_Graph23->SetMinimum(0.0001550134);
   Graph_Graph23->SetMaximum(0.000767129);
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
   
   Double_t Graph3_fx4[9] = {
   1,
   1.2,
   1.4,
   1.6,
   1.8,
   2,
   2.2,
   2.4,
   2.6};
   Double_t Graph3_fy4[9] = {
   0.0003701807,
   0.0003585937,
   0.0003565977,
   0.0003805156,
   0.0004002625,
   0.00040145,
   0.0004075,
   0.0003933,
   0.00034456};
   graph = new TGraph(9,Graph3_fx4,Graph3_fy4);
   graph->SetName("Graph3");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineStyle(2);
   graph->SetLineWidth(3);
   graph->SetMarkerStyle(21);
   graph->SetMarkerSize(0);
   
   TH1F *Graph_Graph34 = new TH1F("Graph_Graph34","",100,0.84,2.76);
   Graph_Graph34->SetMinimum(0.000338266);
   Graph_Graph34->SetMaximum(0.000413794);
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
   
   Double_t Graph0_fx5[9] = {
   1,
   1.2,
   1.4,
   1.6,
   1.8,
   2,
   2.2,
   2.4,
   2.6};
   Double_t Graph0_fy5[9] = {
   0.0004789789,
   0.0004610552,
   0.0004645231,
   0.0004938505,
   0.0005189575,
   0.0005255584,
   0.000530566,
   0.0005109394,
   0.0004456098};
   graph = new TGraph(9,Graph0_fx5,Graph0_fy5);
   graph->SetName("Graph0");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineWidth(2);
   graph->SetMarkerStyle(7);
   
   TH1F *Graph_Graph_Graph015 = new TH1F("Graph_Graph_Graph015","",100,0.84,2.76);
   Graph_Graph_Graph015->SetMinimum(5e-05);
   Graph_Graph_Graph015->SetMaximum(0.2);
   Graph_Graph_Graph015->SetDirectory(0);
   Graph_Graph_Graph015->SetStats(0);
   Graph_Graph_Graph015->SetLineStyle(0);
   Graph_Graph_Graph015->GetXaxis()->SetTitle("m(#tilde{t}) [TeV]");
   Graph_Graph_Graph015->GetXaxis()->SetRange(0,101);
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
   
   Double_t _fx6[9] = {
   1,
   1.2,
   1.4,
   1.6,
   1.8,
   2,
   2.2,
   2.4,
   2.6};
   Double_t _fy6[9] = {
   0.00683,
   0.0017,
   0.000473,
   0.000142,
   4.51e-05,
   1.48e-05,
   5e-06,
   1.71e-06,
   5.9e-07};
   graph = new TGraph(9,_fx6,_fy6);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineWidth(3);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(0.5);
   
   TH1F *Graph_Graph6 = new TH1F("Graph_Graph6","",100,0.84,2.76);
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
   
   Double_t _fx7[9] = {
   1,
   1.2,
   1.4,
   1.6,
   1.8,
   2,
   2.2,
   2.4,
   2.6};
   Double_t _fy7[9] = {
   0.006147,
   0.00153,
   0.0004257,
   0.0001278,
   4.059e-05,
   1.332e-05,
   4.5e-06,
   1.539e-06,
   5.31e-07};
   graph = new TGraph(9,_fx7,_fy7);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineStyle(2);
   graph->SetLineWidth(2);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(0.5);
   
   TH1F *Graph_Graph7 = new TH1F("Graph_Graph7","",100,0.84,2.76);
   Graph_Graph7->SetMinimum(4.779e-07);
   Graph_Graph7->SetMaximum(0.006761647);
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
   
   Double_t _fx8[9] = {
   1,
   1.2,
   1.4,
   1.6,
   1.8,
   2,
   2.2,
   2.4,
   2.6};
   Double_t _fy8[9] = {
   0.007513,
   0.00187,
   0.0005203,
   0.0001562,
   4.961e-05,
   1.628e-05,
   5.5e-06,
   1.881e-06,
   6.49e-07};
   graph = new TGraph(9,_fx8,_fy8);
   graph->SetName("");
   graph->SetTitle("");
   graph->SetFillStyle(1000);
   graph->SetLineColor(4);
   graph->SetLineStyle(2);
   graph->SetLineWidth(2);
   graph->SetMarkerColor(4);
   graph->SetMarkerStyle(23);
   graph->SetMarkerSize(0.5);
   
   TH1F *Graph_Graph8 = new TH1F("Graph_Graph8","",100,0.84,2.76);
   Graph_Graph8->SetMinimum(5.841e-07);
   Graph_Graph8->SetMaximum(0.008264235);
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
   TLine *line = new TLine(1.40286,-1111,1.40286,0.00046493);
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
   entry=leg->AddEntry("","#sigma^{NNLO+NNLL}_{th}(pp#rightarrow#tilde{t}#tilde{t})#pm1#sigma","l");
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
   line = new TLine(1.44455,0,1.44455,0.0003617918);

   ci = TColor::GetColor("#666666");
   line->SetLineColor(ci);
   line->SetLineStyle(2);
   line->Draw();
   TLatex *   tex = new TLatex(1.43955,0,"  1.44 TeV");

   ci = TColor::GetColor("#666666");
   tex->SetTextColor(ci);
   tex->SetTextFont(43);
   tex->SetTextSize(14);
   tex->SetTextAngle(90);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(1.39786,0,"  1.40 TeV");
   tex->SetTextFont(43);
   tex->SetTextSize(14);
   tex->SetTextAngle(90);
   tex->SetLineWidth(2);
   tex->Draw();
   
   TH1F *Graph_copy = new TH1F("Graph_copy","",100,0.84,2.76);
   Graph_copy->SetMinimum(5e-05);
   Graph_copy->SetMaximum(0.2);
   Graph_copy->SetDirectory(0);
   Graph_copy->SetStats(0);
   Graph_copy->SetLineStyle(0);
   Graph_copy->GetXaxis()->SetTitle("m(#tilde{t}) [TeV]");
   Graph_copy->GetXaxis()->SetRange(0,101);
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
