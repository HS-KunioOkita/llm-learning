# 位置符号の可視化

import japanize_matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 単語の最大長
K = 50
# 埋め込みの次元
D = 64

# 位置符号化行列を初期化
pos_enc = np.empty((K, D))

for i in range(K):
    for k in range(D // 2):
        theta = i / (10000 ** (2 * k / D))
        pos_enc[i, 2 * k] = np.sin(theta)
        pos_enc[i, 2 * k + 1] = np.cos(theta)

im = plt.imshow(pos_enc)
plt.xlabel("次元")
plt.ylabel("位置")
plt.colorbar(im)
plt.show()