python set_limit.py -s signals_ZPrimePsi_TauAt600.txt -m ZPrime -p "Z'" -x "pp#rightarrow Z_{#psi}' #rightarrow #tau'^{2e}#tau'^{2e}" --unblind
python set_limit.py -s signals_ZPrimeSSM_TauAt600.txt -m ZPrime -p "Z'" -x "pp#rightarrow Z_{SSM}' #rightarrow #tau'^{2e}#tau'^{2e}" --unblind
python set_limit.py -s signals_gluino_v1.txt -p "#tilde{g}" -x "pp#rightarrow#tilde{g}#tilde{g}" -m HSCPgluino --unblind
python set_limit.py -s signals_ppStau.txt -p "#tilde{#tau}" -x "pp#rightarrow#tilde{#tau}#tilde{#tau}" -m ppStau --unblind


