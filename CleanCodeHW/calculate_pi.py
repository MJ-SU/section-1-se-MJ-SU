import random

# Constant settings
RADIUS = 1
NUM_POINTS = 1000000
AREA_FACTOR = 4
SQUARE_EXPONENT = 2
POINT_COUNT_INCREMENT = 1

inside_circle = 0

# Randomly generate points and count those inside the circle
for _ in range(1000000):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1**2:
        inside_circle += 1

# Estimate pi based on the number of points inside the circle
pi_estimate = (inside_circle / 1000000) * 4

print(f"Estimated value of pi is: {pi_estimate}")
