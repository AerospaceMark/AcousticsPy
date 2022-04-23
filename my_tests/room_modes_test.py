import acousticspy as ap

modes = ap.calculate_room_modes(5,10,15,20, c = 343)

print(modes)