import numpy as np
import matplotlib.pyplot as plt

# 角度の範囲を定義
theta = np.linspace(0, 4 * np.pi, 100)

# 螺旋の半径
r = theta**2

# 極座標におけるグラフの作成
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)

# グラフの装飾
ax.set_title("Spiral Pattern")
ax.set_facecolor('black')  # 背景色を黒に
ax.grid(True, color='white')  # グリッド線を白色に

plt.show()