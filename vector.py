import numpy as np
import matplotlib.pyplot as plt

# ステップ数とウォーカーの数
steps = 500
num_walkers = 20

# 色のリスト
colors = plt.cm.viridis(np.linspace(0, 1, num_walkers))

# プロット設定
plt.figure(figsize=(10, 10))
plt.axis('off')  # 軸の非表示

# 複数のランダムウォークを生成して描画
for i in range(num_walkers):
    x, y = 0, 0  # 初期位置
    x_positions = [x]
    y_positions = [y]

    for _ in range(steps):
        angle = np.random.uniform(0, 2 * np.pi)  # 0から2πの範囲でランダムな角度
        x += np.cos(angle)  # X方向の移動
        y += np.sin(angle)  # Y方向の移動
        x_positions.append(x)
        y_positions.append(y)
    
    plt.plot(x_positions, y_positions, color=colors[i], alpha=0.6)  # パスを描画

plt.title("Multi-Layered Random Walks")
plt.show()
