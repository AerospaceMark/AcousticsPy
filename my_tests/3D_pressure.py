import acousticspy as ap
import numpy as np
import matplotlib.pyplot as plt

total_area = 0.2
num_elements = 100

positions_circle, areas_circle = ap.get_circle_elements(total_area,num_elements)
positions_square, areas_square = ap.get_square_elements(total_area,num_elements)

# plt.figure()
# plt.scatter(positions_circle[:,1],positions_circle[:,2],marker = "o",label = "Circle")
# plt.scatter(positions_square[:,1],positions_square[:,2],marker = "o",label = "Square")
# plt.grid()
# plt.xlabel("Y-Position")
# plt.ylabel("Z-Position")
# plt.title("Piston Shapes")
# plt.legend()
# plt.axis("equal")
#plt.show()

print("Total Circle Area = {0:.5f} m^2, number of elements is {1}".format(sum(areas_circle),len(areas_circle)))
print("Total Square Area = {0:.5f} m^2, number of elements is {1}".format(sum(areas_square),len(areas_square)))

velocities = 0.001
strengths = 0.000005

ap.pressure_field(positions_circle,
                  [2000],
                  areas = areas_circle,
                  velocities = velocities,
                  strengths = strengths,
                  x_range = [0,2],
                  y_range = [-1,1],
                  z_range = [-1,1],
                  pressure_limits = [-50,50],
                  method = "Rayleigh",
                  dimensions = 2,
                  point_density = 100,
                  show_plots = True)

plt.show()