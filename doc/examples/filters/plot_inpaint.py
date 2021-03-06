"""
===========
Inpainting
===========
Inpainting [1]_ is the process of reconstructing lost or deteriorated
parts of images and videos.

The reconstruction is supposed to be performed in fully automatic way by
exploiting the information presented in non-damaged regions.

In this example, we show how the masked pixels get inpainted by
inpainting algorithm based on 'biharmonic equation'-assumption [2]_ [3]_.

.. [1]  Wikipedia. Inpainting
        https://en.wikipedia.org/wiki/Inpainting
.. [2]  Wikipedia. Biharmonic equation
        https://en.wikipedia.org/wiki/Biharmonic_equation
.. [3]  N.S.Hoang, S.B.Damelin, "On surface completion and image
        inpainting by biharmonic functions: numerical aspects",
        http://www.ima.umn.edu/~damelin/biharmonic
"""

import numpy as np
import matplotlib.pyplot as plt

from skimage import data, color
from skimage.restoration import inpaint

image_orig = data.astronaut()

# Create mask with three defect regions: left, middle, right respectively
mask = np.zeros(image_orig.shape[:-1])
mask[20:60, 0:20] = 1
mask[200:300, 150:170] = 1
mask[50:100, 400:430] = 1

# Defect image over the same region in each color channel
image_defect = image_orig.copy()
for layer in range(image_defect.shape[-1]):
    image_defect[np.where(mask)] = 0

image_result = inpaint.inpaint_biharmonic(image_defect, mask, multichannel=True)

fig, axes = plt.subplots(ncols=2, nrows=2)
ax0, ax1, ax2, ax3 = axes.ravel()

ax0.set_title('Original image')
ax0.imshow(image_orig)
ax0.axis('off')

ax1.set_title('Mask')
ax1.imshow(mask, cmap=plt.cm.gray)
ax1.axis('off')

ax2.set_title('Defected image')
ax2.imshow(image_defect)
ax2.axis('off')

ax3.set_title('Inpainted image')
ax3.imshow(image_result)
ax3.axis('off')

plt.tight_layout()
plt.show()
