import numpy as np
import matplotlib.pyplot as plt

# ステップ数
steps = 1000

# 初期位置
x, y = 0, 0

# パスを保存する配列
x_positions = [x]
y_positions = [y]

# ランダムウォークの実行
for _ in range(steps):
    angle = np.random.uniform(0, 2 * np.pi)  # 0から2πの範囲でランダムな角度
    x += np.cos(angle)  # X方向の移動
    y += np.sin(angle)  # Y方向の移動
    x_positions.append(x)
    y_positions.append(y)

# プロット設定
plt.figure(figsize=(10, 10))
plt.plot(x_positions, y_positions, color='blue')  # パスを青色でプロット
plt.title("Random Walk")
plt.axis('equal')
plt.axis('off')  # 軸の非表示
plt.show()
