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

velocities = 0.01
strengths = 0.000005

field_points, angles = ap.define_arc(1000,180,dimensions = 2)

field_points = np.linspace(0.1,3,1000)

pressures = ap.pressure_field(positions_circle,
                            [2000],
                            field_points = field_points,
                            areas = areas_circle,
                            velocities = velocities,
                            strengths = strengths,
                            method = "Rayleigh")

plt.plot(field_points,np.abs(pressures))
plt.show()