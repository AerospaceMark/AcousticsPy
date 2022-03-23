import acousticspy as ap
import numpy as np
import matplotlib.pyplot as plt

positions = [[-0.01,0],[0.01,0]]
strengths = [0.01,-0.01]
phases = [0,0]
velocities = [10,-10]
frequency = [1000,1000]

ap.pressure_field(positions,frequency,
                    strengths = strengths,
                    phases = phases,
                    velocities = velocities,
                    show_plots = True,
                    method = "Monopole Addition")

plt.tight_layout()
plt.show()