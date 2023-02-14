import acousticspy as ap
import numpy as np
import matplotlib.pyplot as plt

f = np.logspace(1,6,1000)

alpha = ap.absorption.get_alpha(f,1,20,0)

# Re-creates figure 8.6.2 in Kinsler and Frey "Fundamentals of Acoustics"
plt.figure()
plt.loglog(f,ap.absorption.get_alpha(f,1,20,0),label = "0 %")
plt.loglog(f,ap.absorption.get_alpha(f,1,20,10),label = "10 %")
plt.loglog(f,ap.absorption.get_alpha(f,1,20,100),label = "100 %")
plt.loglog(f,ap.absorption.get_alpha_classical(f),label = "Classical")
plt.xlim(1e1,1e6)
plt.ylim(1e-6,1e2)
plt.grid("on")
plt.legend(title = "Relative Humidity")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Absorption Coefficient (dB/m)")
plt.title("Atmospheric Absorption")
plt.show()