# DCT-RCAN [![ICIP 2022](https://img.shields.io/badge/ICIP-2022-blue)](https://2022.ieeeicip.org/)

### DCT-Based Residual Network for NIR Image Colorization  
[[📄 Paper Link (IEEE Xplore)]](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9897373)

**Authors:**  
[Hongcheng Jiang](https://jianghongcheng.github.io/),  
[Paras Maharjan](https://p.web.umkc.edu/pmc4p/),  
[Zhu Li](https://l.web.umkc.edu/lizhu/),  
[George York](https://ieeexplore.ieee.org/author/37420860700)

---

## 🔍 Overview

This repository contains the official implementation of the paper  
**"DCT-Based Residual Network for NIR Image Colorization"**  
published in **IEEE ICIP 2022**.

We propose a novel DCT-guided colorization framework that integrates Discrete Cosine Transform (DCT) frequency priors with a residual channel attention network (RCAN) to colorize Near-Infrared (NIR) images into RGB. The model achieves superior performance compared to existing methods on multiple benchmarks.

---

## 📊 Quantitative Results

<p align="center">
  <img src="https://github.com/jianghongcheng/DCT-RCAN/blob/master/Figures/Quantitative_Comparison.png" width="600"/>
</p>

**Table: Average PSNR (dB), SSIM, and Angular Error (AE in degrees) on the validation dataset.**

| Model             | PSNR (dB) | SSIM  | AE (°) |
|------------------|:---------:|:-----:|:------:|
| MFF              | 17.39     | 0.61  | 4.69   |
| ATcycleGAN       | 20.67     | 0.68  | 3.97   |
| SST              | 14.26     | 0.57  | 5.61   |
| SPADE            | 19.24     | 0.59  | 4.59   |
| NIR-GNN          | 17.50     | 0.60  | 5.22   |
| **Proposed Method** | **22.15** | **0.77** | **3.40** |

---

## 🖼️ Visual Results

### 2D-DCT Visualization from a NIR Image
<p align="center">
  <img src="https://github.com/jianghongcheng/DCT-RCAN/blob/master/Figures/2d-DCT.png" width="800"/>
</p>

### Comparison with State-of-the-Art Methods
<p align="center">
  <img src="https://github.com/jianghongcheng/DCT-RCAN/blob/master/Figures/Visual_Result.png" width="800"/>
</p>

---

## 📚 Citation

If you find this work useful in your research, please cite:

```bibtex
@inproceedings{jiang2022dct,
  title={DCT-based Residual Network for NIR Image Colorization},
  author={Jiang, Hongcheng and Maharjan, Paras and Li, Zhu and York, George},
  booktitle={2022 IEEE International Conference on Image Processing (ICIP)},
  pages={2926--2930},
  year={2022},
  organization={IEEE}
}
