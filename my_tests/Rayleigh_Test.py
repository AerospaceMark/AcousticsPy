import acousticspy as ap
import matplotlib.pyplot as plt

total_area = 0.2
num_elements = 20

positions_circle, areas_circle = ap.get_circle_elements(total_area,num_elements)
positions_square, areas_square = ap.get_square_elements(total_area,num_elements)

plt.figure()
plt.plot(positions_circle,areas_circle,marker = "o",label = "Circle")
plt.plot(positions_square,areas_square,marker = "o",label = "Square")
plt.grid()
plt.xlabel("Location (m)")
plt.ylabel("Element Area")
plt.title("Area Across Two Shapes")
plt.legend()

print("Total Circle Area = {:.5f} m^2".format(sum(areas_circle)))
print("Total Square Area = {:.5f} m^2".format(sum(areas_square)))