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

This repository provides the official implementation of  
**"DCT-Based Residual Network for NIR Image Colorization"**,  
published in **IEEE ICIP 2022**.

We introduce **DCT-RCAN**, a DCT-guided residual network that utilizes Discrete Cosine Transform (DCT) frequency priors to enhance the colorization of Near-Infrared (NIR) images. By integrating frequency-domain guidance into a channel attention framework, our model achieves high-fidelity RGB reconstruction with superior spatial and chromatic consistency.

---

## 🧠 Network Architecture

<p align="center"><strong>Network Architecture of DCT-RCAN</strong></p>
<p align="center">
  <img src="https://github.com/jianghongcheng/DCT-RCAN/blob/master/Figures/Network.png" width="800"/>
</p>

---

## 📊 Quantitative Results

<p align="center">
  <img src="https://github.com/jianghongcheng/DCT-RCAN/blob/master/Figures/Quantitative_Comparison.png" width="600"/>
</p>

<p align="center"><b>Table: Average PSNR (dB), SSIM, and Angular Error (AE in degrees) on the validation dataset.</b></p>

<div align="center">

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>PSNR (dB)</th>
      <th>SSIM</th>
      <th>AE (°)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>MFF</td>
      <td>17.39</td>
      <td>0.61</td>
      <td>4.69</td>
    </tr>
    <tr>
      <td>ATcycleGAN</td>
      <td>20.67</td>
      <td>0.68</td>
      <td>3.97</td>
    </tr>
    <tr>
      <td>SST</td>
      <td>14.26</td>
      <td>0.57</td>
      <td>5.61</td>
    </tr>
    <tr>
      <td>SPADE</td>
      <td>19.24</td>
      <td>0.59</td>
      <td>4.59</td>
    </tr>
    <tr>
      <td>NIR-GNN</td>
      <td>17.50</td>
      <td>0.60</td>
      <td>5.22</td>
    </tr>
    <tr>
      <td><b>Proposed Method</b></td>
      <td><b>22.15</b></td>
      <td><b>0.77</b></td>
      <td><b>3.40</b></td>
    </tr>
  </tbody>
</table>

</div>

---

## 🖼️ Visual Results

<p align="center"><strong>2D-DCT Visualization from a NIR Image</strong></p>
<p align="center">
  <img src="https://github.com/jianghongcheng/DCT-RCAN/blob/master/Figures/2d-DCT.png" width="800"/>
</p>

<p align="center"><strong>Comparison with State-of-the-Art Methods</strong></p>
<p align="center">
  <img src="https://github.com/jianghongcheng/DCT-RCAN/blob/master/Figures/Visual_Result.png" width="800"/>
</p>

---

## 📚 Citation

If you find this work helpful in your research, please cite:

```bibtex
@inproceedings{jiang2022dct,
  title={DCT-Based Residual Network for NIR Image Colorization},
  author={Jiang, Hongcheng and Maharjan, Paras and Li, Zhu and York, George},
  booktitle={2022 IEEE International Conference on Image Processing (ICIP)},
  pages={2926--2930},
  year={2022},
  organization={IEEE}
}



## 📬 Contact

If you have any questions, feedback, or collaboration ideas, feel free to reach out:

- 💻 Website: [jianghongcheng.github.io](https://jianghongcheng.github.io)
- 📧 Email: [hjq44@mail.umkc.edu](mailto:hjq44@mail.umkc.edu)
- 🏫 Affiliation: University of Missouri–Kansas City (UMKC)
