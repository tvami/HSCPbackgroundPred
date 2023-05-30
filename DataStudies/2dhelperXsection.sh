python3 limitPlotScripts/extractZPrimeXsecLimits.py

#python3 limitPlotScripts/harvestToContours.py --inputFile ZPrimeLimits.json  -x m2 -y m1 --useUpperLimit --debug --forbiddenFunction 2\*x --xMax 1100 -o output_BR100pct.root  --noSig --sigmax=1.
#python3 limitPlotScripts/harvestToContours.py --inputFile ZPrimeLimits.json  -x m2 -y m1 --useUpperLimit --debug --forbiddenFunction=none --xMax 1400 -o output_BR100pct.root  --noSig --sigmax=1.
python3 limitPlotScripts/harvestToContours.py --inputFile ZPrimeLimits.json -x m2 -y m1 --useUpperLimit --forbiddenFunction=none --xMax 1400 -o output_BR100pct.root --noSig --sigmax=1. --interpolationScheme=griddata --interpolation=linear

python3 limitPlotScripts/2dplot.py outputGraphs.root



