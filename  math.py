import numpy as np
import matplotlib.pyplot as plt

# パラメータ設定
a = 5
b = 4
delta = np.pi / 2  # 位相差
t = np.linspace(0, 2 * np.pi, 1000)  # パラメータtの範囲

# リサジュー図形の式
x = np.sin(a * t + delta)
y = np.sin(b * t)

# プロット設定
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_aspect('equal')  # アスペクト比を1に設定

# タイトルと軸の非表示
ax.set_title("Lissajous Curve")
plt.axis('off')  # 軸の非表示

# 背景色の設定
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
ax.plot(x, y, color='white')  # 線の色を白に設定

plt.show()
