
# DCT-RCAN [![ICIP 2022](https://2022.ieeeicip.org/)]

### DCT-BASED RESIDUAL NETWORK FOR NIR IMAGE COLORIZATION [[Paper Link]](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9897373)
[Hongcheng Jiang](https://jianghongcheng.github.io/), [Paras Maharjan](https://p.web.umkc.edu/pmc4p/), [Zhu Li](https://l.web.umkc.edu/lizhu/) and [George York](https://ieeexplore.ieee.org/author/37420860700)




## Overview
<img src="https://github.com/jianghongcheng/DCT-RCAN/blob/master/Figures/Quantitative_Comparison.png" width="600"/>

**Average PSNR, SSIM, and AE for the validation dataset.**

| Model           | PSNR (dB) | SSIM  | AE (°) |
|-----------------|:---------:|:-----:|:------:|
| MFF             | 17.39     | 0.61  | 4.69   |
| ATcycleGAN      | 20.67     | 0.68  | 3.97   |
| SST             | 14.26     | 0.57  | 5.61   |
| SPADE           | 19.24     | 0.59  | 4.59   |
| NIR-GNN         | 17.50     | 0.60  | 5.22   |
| **Proposed Method** | **22.15** | **0.77** | **3.40** |


## Visual Results

**2D-DCT Visualization from a NIR Image**

<img src="https://github.com/jianghongcheng/DCT-RCAN/blob/master/Figures/2d-DCT.png" width="800"/>


**Comparison with State-of-the-Art Methods**

<img src="https://github.com/jianghongcheng/DCT-RCAN/blob/master/Figures/Visual_Result.png" width="800"/>

## Citations
#### BibTeX

@inproceedings{jiang2022dct,
  title={Dct-based residual network for nir image colorization},
  author={Jiang, Hongcheng and Maharjan, Paras and Li, Zhu and York, George},
  booktitle={2022 IEEE International Conference on Image Processing (ICIP)},
  pages={2926--2930},
  year={2022},
  organization={IEEE}
}


## Contact
If you have any question, please email hjq44@mail.umkc.edu.
