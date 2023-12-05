import ROOT
import json
import sys

scale = 1
crossSectionArray = {
3000 : 0.000451036,
4000 : 4.7749E-5,
5000 : 5.34376E-6,
6000 : 5.45292E-7,
7000 : 5.2E-8, #extrapolated
}

#inputFolder = "./2DAlpha_CodeV46p3_1Dfrom2DNoExtrapol_ZPrimeTauPrime/"
#inputFolder = "./2DAlpha_CodeV46p2_1Dfrom2DNoExtrapol_ZPrimeTauPrimeWithSSM/"
inputFolder = "./2DAlpha_CodeV46p8_1Dfrom2DNoExtrapol_ZPrimeTauPrimeOfficial"

outputPoints = []

for ZPrimeMass in [3000,4000,5000,6000,7000]:
	scale = crossSectionArray[ZPrimeMass]
	for tauPrimeMass in [200,400,600,800,1000,1200,1400]:
		limitInfo = {}

		inputFileName = f"{inputFolder}/Signal_tauPrime2e-{tauPrimeMass}-ZPrime-{ZPrimeMass}-0x0_area/higgsCombineTest.AsymptoticLimits.mH120.root"
		inputFile = ROOT.TFile(inputFileName)
		inputTree = inputFile.Get("limit")

		tmpDict = {}
		tmpDict["m1"] = ZPrimeMass
		tmpDict["m2"] = tauPrimeMass
		tmpDict["dm"] = tmpDict["m1"]-tmpDict["m2"]

		# inputTree.Print()
		for entry in inputTree:
			# print(entry.)
			# print(entry.limit)
			# print(entry.quantileExpected)

			if entry.quantileExpected==-1:
				tmpDict["upperLimit"] = entry.limit*scale
			if entry.quantileExpected==0.02500000037252903:
				tmpDict["expectedUpperLimitMinus2Sig"] = entry.limit*scale
			elif entry.quantileExpected==0.1599999964237213:
				tmpDict["expectedUpperLimitMinus1Sig"] = entry.limit*scale
			elif entry.quantileExpected==0.5:
				tmpDict["expectedUpperLimit"] = entry.limit*scale
			elif entry.quantileExpected==0.8399999737739563:
				tmpDict["expectedUpperLimitPlus1Sig"] = entry.limit*scale
			elif entry.quantileExpected==0.9750000238418579:
				tmpDict["expectedUpperLimitPlus2Sig"] = entry.limit*scale

		outputPoints.append(tmpDict)

with open("ZPrimeLimits.json", 'w') as f:
    json.dump(outputPoints, f, indent=4)
