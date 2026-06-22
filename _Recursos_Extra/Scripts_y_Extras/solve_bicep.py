import math

cap_height = 15.0
target_perimeter = 46.41

# Let's assume curve adds 15% to the straight line distance
curve_factor = 1.15

best_bicep = 0
min_diff = 999

for b in range(200, 400):
    bicep = b / 10.0
    cimera_half = (bicep / 4) + 1.5
    cimera_straight = math.sqrt(cimera_half**2 + cap_height**2) * 2
    bajera_width = (bicep / 2) - 3
    
    # Estimate perimeter with curves
    est_perimeter = (cimera_straight * curve_factor) + (bajera_width * 1.1)
    
    diff = abs(est_perimeter - target_perimeter)
    if diff < min_diff:
        min_diff = diff
        best_bicep = bicep

print(f"To achieve a ~46.41 cm sleeve cap perimeter, the Bicep width must be around: {best_bicep} cm")
