import math

# Cimera
w_c = 10.0
h_c = 15.0
d_c = math.sqrt(w_c**2 + h_c**2)  # 18.02

# Standard bezier length approximation for 90 degree turn with ratio 0.55
# It's roughly 1.15 * diagonal
c_len = d_c * 1.15
total_cimera = c_len * 2
print(f"Cimera standard length: {total_cimera:.2f} cm")

# Bajera
w_b = 14.0
h_b = 0.0 # mostly flat

# Bajera curve with small control points (e.g. 2.5)
b_len = 14.5
print(f"Bajera standard length: {b_len:.2f} cm")
print(f"Total sleeve cap: {total_cimera + b_len:.2f} cm")

print(f"Bodice armhole: 43.41 cm")
print(f"Excess ease: {total_cimera + b_len - 43.41:.2f} cm")
