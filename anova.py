import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

no_electromagnets = [26.74, 26.43, 26.45, 26.55, 26.53]
two_electromagnets_top_050A = [23.74, 22.83, 22.63, 23.31, 23.36]
two_electromagnets_top_075A = [20.84, 20.33, 20.91, 19.47, 21.67]
two_electromagnets_top_100A = [17.58, 18.48, 17.57, 16.94, 18.37]
two_electromagnets_bottom_050A = [23.46, 22.39, 23.49, 21.32, 21.63]
two_electromagnets_bottom_075A = [19.18, 18.76, 18.40, 19.65, 19.01]
two_electromagnets_bottom_100A = [16.89, 16.14, 17.07, 16.71, 16.49]
four_electromagnets_050A = [21.16, 21.83, 20.16, 20.57, 21.20]
four_electromagnets_075A = [17.49, 17.09, 17.45, 17.03, 17.02]
four_electromagnets_100A = [14.61, 15.16, 15.48, 15.66, 14.24]

result = f_oneway(no_electromagnets,
                  two_electromagnets_top_050A,
                  two_electromagnets_top_075A,
                  two_electromagnets_top_100A,
                  two_electromagnets_bottom_050A,
                  two_electromagnets_bottom_075A,
                  two_electromagnets_bottom_100A,
                  four_electromagnets_050A,
                  four_electromagnets_075A,
                  four_electromagnets_100A)

print (result)

data_all = no_electromagnets +\
           two_electromagnets_top_050A +\
           two_electromagnets_top_075A +\
           two_electromagnets_top_100A + two_electromagnets_bottom_050A +\
           two_electromagnets_bottom_075A +\
           two_electromagnets_bottom_100A +\
           four_electromagnets_050A +\
           four_electromagnets_075A +\
           four_electromagnets_100A

df_electromagnet_configuration  = pd.DataFrame({"Value" : data_all,
                                     "Group" : np.repeat(["No Electromagnets",
                                                          "Two Electromagnets in Top Holes 0.50A",
                                                          "Two Electromagnets in Top Holes 0.75A",
                                                          "Two Electromagnets in Top Holes 1.00A",
                                                          "Two Electromagnets in Bottom Holes 1.00A",
                                                          "Two Electromagnets in Bottom Holes 1.00A",
                                                          "Two Electromagnets in Bottom Holes 1.00A",
                                                          "Four Electromagnets 0.50A",
                                                          "Four Electromagnets 0.75A",
                                                          "Four Electromagnets 1.00A"], repeats = 5)})

tukey = pairwise_tukeyhsd(endog = df_electromagnet_configuration["Value"],
                                     groups = df_electromagnet_configuration["Group"], alpha = 0.05)

print(tukey)

