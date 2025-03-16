import random

# 常數設定
RADIUS = 1  # 圓的半徑
NUM_POINTS = 1_000_000  # 隨機生成的點數
AREA_FACTOR = 4  # 區域因子

inside_circle = 0

# 隨機生成點並計算圓內的點數
for _ in range(NUM_POINTS):
    x = random.uniform(-RADIUS, RADIUS)
    y = random.uniform(-RADIUS, RADIUS)
    if x**2 + y**2 <= RADIUS**2:
        inside_circle += 1

# 根據圓內點數估算 π 值
pi_estimate = (inside_circle / NUM_POINTS) * AREA_FACTOR

print(f"Estimated value of pi is: {pi_estimate}")
