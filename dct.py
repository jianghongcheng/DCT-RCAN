# Import functions and libraries
import numpy as np
from numpy import r_
import matplotlib.pyplot as plt
from scipy import fftpack
class ImageDCT():
    def __init__(self, dct_block=8):
        self.dct_block = dct_block
    def dct2(self, a):
        return fftpack.dct(fftpack.dct(a, axis=0, norm='ortho'), axis=1, norm='ortho')
    def idct2(self, a):
        return fftpack.idct(fftpack.idct(a, axis=0, norm='ortho'), axis=1, norm='ortho')
    def dct_2d(self, img):
        imsize = img.shape
        dct = np.zeros(imsize)
        # Do DCT on cjhannel 1
        for i in r_[:imsize[0]:self.dct_block]:
            for j in r_[:imsize[1]:self.dct_block]:
                if img.ndim == 2:
                    dct[i:(i+self.dct_block), j:(j+self.dct_block)] = self.dct2(img[i:(i+self.dct_block), j:(j+self.dct_block)])
                if img.ndim == 3:
                    for k in range(3):
                        dct[i:(i+self.dct_block), j:(j+self.dct_block), k] = self.dct2(img[i:(i+self.dct_block), j:(j+self.dct_block), k])
        return dct
    def idct_2d(self, img):
        imsize = img.shape
        idct = np.zeros(imsize)
        # Do DCT on cjhannel 1
        for i in r_[:imsize[0]:self.dct_block]:
            for j in r_[:imsize[1]:self.dct_block]:
                if img.ndim == 2:
                    idct[i:(i+self.dct_block), j:(j+self.dct_block)] = self.idct2(img[i:(i+self.dct_block), j:(j+self.dct_block)])
                if img.ndim == 3:
                    for k in range(3):
                        idct[i:(i+self.dct_block), j:(j+self.dct_block), k] = self.idct2(img[i:(i+self.dct_block), j:(j+self.dct_block), k])
        return idct
def test_gray():
    img = plt.imread("/home/max/Downloads/cameraman.tif")
    patch = 4
    #img = img[90:90+112, 950:950+112, :]
    plt.figure()
    plt.imshow(img)
    img = img[:, :, 0]
    print(img.max())
    dct_2d = ImageDCT(patch)
    dct = dct_2d.dct_2d(img)
    plt.figure()
    plt.imshow(dct, cmap='gray', vmax=np.max(dct)*0.01, vmin=0)
    plt.title("%dx%d DCTs of the image"%(patch,patch))
    plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(dct[::patch,::patch], cmap='gray', vmax=np.max(dct[::patch,::patch]), vmin=0)
    plt.title("DC component")
    histogram, bin_edges = np.histogram(dct[::patch,::patch], bins=256, range=(0, 1))
    plt.subplot(1,2,2)
    plt.title("Grayscale Histogram")
    plt.xlabel("grayscale value")
    plt.ylabel("pixels")
    plt.xlim([0.0, 1.0])  # <- named arguments do not work here
    plt.plot(bin_edges[0:-1], histogram)  # <- or here
    plt.grid()
    plt.show()
    plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(dct[::patch,1::patch], cmap='gray', vmax=np.max(dct[::patch,1::patch]), vmin=0)
    plt.title("AC01 component")
    histogram, bin_edges = np.histogram(dct[::patch,1::patch], bins=256, range=(-1, 1))
    plt.subplot(1,2,2)
    plt.title("Grayscale Histogram")
    plt.xlabel("grayscale value")
    plt.ylabel("pixels")
    plt.xlim([-1.0, 1.0])  # <- named arguments do not work here
    plt.plot(bin_edges[0:-1], histogram)  # <- or here
    plt.grid()
    plt.show()
    plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(dct[1::patch,::patch], cmap='gray', vmax=np.max(dct[1::patch,::patch]), vmin=0)
    plt.title("AC10 component")
    histogram, bin_edges = np.histogram(dct[1::patch,::patch], bins=256, range=(-1, 1))
    plt.subplot(1,2,2)
    plt.title("Grayscale Histogram")
    plt.xlabel("grayscale value")
    plt.ylabel("pixels")
    plt.xlim([-1.0, 1.0])  # <- named arguments do not work here
    plt.plot(bin_edges[0:-1], histogram)  # <- or here
    plt.grid()
    plt.show()
    plt.figure()
    plt.subplot(1,2,1)
    plt.imshow(dct[1::patch,1::patch], cmap='gray', vmax=np.max(dct[1::patch,1::patch]), vmin=0)
    plt.title("AC11 component")
    histogram, bin_edges = np.histogram(dct[1::patch,1::patch], bins=256, range=(-1, 1))
    plt.subplot(1,2,2)
    plt.title("Grayscale Histogram")
    plt.xlabel("grayscale value")
    plt.ylabel("pixels")
    plt.xlim([-1.0, 1.0])  # <- named arguments do not work here
    plt.plot(bin_edges[0:-1], histogram)  # <- or here
    plt.grid()
    plt.show()
    plt.show()
    print("Done...")
def test_rgb():
    img = plt.imread("./test_image/BlurJpeg_000_97.jpg")/255.0
    patch = 4
    #img = img[90:90+112, 950:950+112, :]
    plt.figure()
    plt.imshow(img)
    dct_2d = ImageDCT(patch)
    dct = dct_2d.dct_2d(img)
    dct = dct/dct.max()
    sharp_dc_ac_patch = dct[::patch, ::patch, :]
    for i in [(0,1),(0,2),(0,3),(1,0),(2,0),(3,0),(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]:
        sharp_dc_ac_patch = np.concatenate((sharp_dc_ac_patch, dct[i[0]::patch, i[1]::patch, :]), axis=2)
    out = np.zeros_like(img)
    for j, i in enumerate([(0,0),(0,1),(0,2),(0,3),(1,0),(2,0),(3,0),(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)]):
        out[i[0]::patch, i[1]::patch, :] = sharp_dc_ac_patch[:, :, j*3:j*3+3]
    plt.figure()
    plt.imshow(dct, vmax=1, vmin=0)
    plt.title("%dx%d DCTs of the image"%(patch,patch))
    plt.figure()
    plt.imshow(dct[::patch,::patch,:])
    plt.title("DC component")
    plt.figure()
    plt.imshow(dct[::patch,1::patch,:], vmax=np.max(dct[::patch,1::patch,:]), vmin=0)
    plt.title("AC01 component")
    plt.figure()
    plt.imshow(dct[1::patch,::patch,:], vmax=np.max(dct[1::patch,::patch,:]), vmin=0)
    plt.title("AC10 component")
    plt.figure()
    plt.imshow(dct[1::patch,1::patch,:], vmax=np.max(dct[1::patch,1::patch,:]), vmin=0)
    plt.title("AC11 component")
    plt.show()
    print("Done...")
if __name__ == '__main__':
    test_gray()