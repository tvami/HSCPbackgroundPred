python set_limit.py -s signals_gluino_v1.txt -p "#tilde{g}" -x "pp#rightarrow#tilde{g}#tilde{g}" -m HSCPgluino --unblind
python set_limit.py -s signals_ppStau.txt -p "#tilde{#tau}" -x "pp#rightarrow#tilde{#tau_{L/R}}#tilde{#tau_{L/R}}" -m ppStau --unblind
python set_limit.py -s signals_ppStau_L.txt -p "#tilde{#tau}" -x "pp#rightarrow#tilde{#tau_{L}}#tilde{#tau_{L}}" -m ppStauL --unblind
python set_limit.py -s signals_ppStau_R.txt -p "#tilde{#tau}" -x "pp#rightarrow#tilde{#tau_{R}}#tilde{#tau_{R}}" -m ppStauR --unblind
python set_limit.py -s signals_gmsbStau_v2.txt -p '#tilde{#tau}' -x 'pp#rightarrow#tilde{#tau}#tilde{#tau} (GMSB)' -m gmsbStau --unblind
python set_limit.py -s signals_stop_v1.txt -p '#tilde{t}' -x 'pp#rightarrow#tilde{t}#tilde{t}' -m HSCPstop --unblind
python set_limit.py -s signals_tauPrime1e_v2.txt -p "#tau'^{1e}" -x "pp#rightarrow#tau'^{1e}#tau'^{1e}" -m HSCPTauPrime1e --unblind
python set_limit.py -s signals_tauPrime2e_v2.txt -p "#tau'^{2e}" -x "pp#rightarrow#tau'^{2e}#tau'^{2e}" -m HSCPTauPrime2e --unblind
python set_limit.py -s signals_ZPrimePsi_TauAt600.txt -m ZPrime -p "Z'" -x "pp#rightarrow Z_{#psi}' #rightarrow #tau'^{2e}#tau'^{2e}" --unblind
python set_limit.py -s signals_ZPrimeSSM_TauAt600.txt -m ZPrime -p "Z'" -x "pp#rightarrow Z_{SSM}' #rightarrow #tau'^{2e}#tau'^{2e}" --unblind
