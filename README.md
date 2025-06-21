<h1 align="center">3D Reconstruction via 3D Gaussian Splatting</h1>

---

This project explores real-time 3D object reconstruction and novel view synthesis using **3D Gaussian Splatting (3DGS)**. Unlike traditional volumetric NeRF-based methods, 3DGS represents the scene as a set of anisotropic 3D Gaussian primitives and leverages a differentiable splatting-based renderer for efficient optimization and interactive rendering.  
We apply this method to real-world data captured by smartphones, demonstrating high-quality view synthesis and significant performance improvements over NeRF and TensoRF.

## 📦 Dataset Access

The real-world dataset used in this project, along with COLMAP-processed poses and the resulting outputs, can be downloaded via the following link:

🔗 [Baidu Netdisk Download – Gaussian Splatting Dataset and Results](https://pan.baidu.com/s/1wkrH56RmCkV5-dXAMDY7iQ?pwd=5s6r) (extraction code: `5s6r`)

---

## 📌 Method Summary

3D Gaussian Splatting replaces neural field representations with explicit scene primitives—parameterized 3D Gaussians—which are projected onto the image plane using a differentiable rasterizer. This architecture supports:

- **Real-time rendering** without any neural network inference at test time.
- **Fast convergence** thanks to direct optimization of primitive parameters.
- **High-quality reconstruction**, even with sparse inputs.

Official codebase:  
🔗 https://github.com/graphdeco-inria/gaussian-splatting

---

