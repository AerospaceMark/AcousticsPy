import acousticspy as ap
import matplotlib.pyplot as plt
import numpy as np

ap.moving_coil_loudspeaker(show_Analysis_Plots=True,show_TVC=True, f = np.logspace(0,4,10000),Mmd = 5)

plt.show()