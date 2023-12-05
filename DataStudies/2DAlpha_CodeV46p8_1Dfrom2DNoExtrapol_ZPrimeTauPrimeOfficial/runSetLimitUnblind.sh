python set_limit.py -s signals_ZPrimePsi_TauAt600.txt -m ZPrime -p "Z'" -x "pp#rightarrow Z_{#psi}' #rightarrow #tau'^{2e}#tau'^{2e}" --unblind
python set_limit.py -s signals_ZPrimeSSM_TauAt600.txt -m ZPrime -p "Z'" -x "pp#rightarrow Z_{SSM}' #rightarrow #tau'^{2e}#tau'^{2e}" --unblind
python set_limit_noTheory.py -s signals_ZPrimeSSM_TauAt600.txt -m ZPrimeNoTheo -p "Z'" -x "pp#rightarrow Z_{SSM}' #rightarrow #tau'^{2e}#tau'^{2e}" --unblind

