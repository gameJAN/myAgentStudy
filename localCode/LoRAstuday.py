import matplotlib.pyplot as plt
import numpy as np

# 简化的2D示例，帮助你理解
def visualize_lora_concept():
    # 原始权重向量
    w_original = np.array([2.0, 1.0])
    
    # 低秩更新的方向（可以理解为A矩阵）
    update_direction = np.array([0.5, 0.8])
    
    # 更新幅度（可以理解为B矩阵）
    scale = 0.3
    
    # LoRA更新
    w_updated = w_original + scale * update_direction
    
    # 可视化
    plt.figure(figsize=(8, 6))
    plt.quiver(0, 0, w_original[0], w_original[1], 
               angles='xy', scale_units='xy', scale=1, 
               color='blue', label='原始权重向量')
    plt.quiver(w_original[0], w_original[1], 
               scale * update_direction[0], scale * update_direction[1],
               angles='xy', scale_units='xy', scale=1,
               color='red', label='LoRA更新')
    plt.quiver(0, 0, w_updated[0], w_updated[1],
               angles='xy', scale_units='xy', scale=1,
               color='green', label='更新后权重', alpha=0.7)
    
    plt.xlim(-1, 4)
    plt.ylim(-1, 3)
    plt.grid(True)
    plt.legend()
    plt.title('LoRA更新的向量理解')
    plt.show()

# visualize_lora_concept()