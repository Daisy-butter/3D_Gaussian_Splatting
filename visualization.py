import os
import pandas as pd
import matplotlib.pyplot as plt

# 设置目录
csv_dir = 'RESULT_FIGURE/csv'
fig_dir = 'RESULT_FIGURE/figures'

# 创建图像输出目录
os.makedirs(fig_dir, exist_ok=True)

# 定义要绘图的指标文件及其信息
metrics = {
    'train_L1.csv': {
        'ylabel': 'L1 Loss',
        'title': 'Training L1 Loss',
        'output': 'l1_loss_curve.png'
    },
    'train_loss.csv': {
        'ylabel': 'Total Loss',
        'title': 'Training Total Loss',
        'output': 'total_loss_curve.png'
    },
    'train_loss_patches.csv': {
        'ylabel': 'Patches Loss',
        'title': 'Training Patches Loss',
        'output': 'patches_loss_curve.png'
    },
    'train_SSIM.csv': {
        'ylabel': 'SSIM',
        'title': 'Training SSIM',
        'output': 'ssim_curve.png'
    }
}

# 遍历绘制所有图像
for filename, info in metrics.items():
    path = os.path.join(csv_dir, filename)
    if not os.path.exists(path):
        print(f"❌ File not found: {path}")
        continue

    df = pd.read_csv(path)
    plt.figure(figsize=(8, 5))
    plt.plot(df['Step'], df['Value'], label=info['ylabel'])
    plt.xlabel('Iteration')
    plt.ylabel(info['ylabel'])
    plt.title(info['title'])
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    save_path = os.path.join(fig_dir, info['output'])
    plt.savefig(save_path, dpi=300)
    plt.close()
    print(f"✅ Saved: {save_path}")

print("🎉 All plots completed.")
