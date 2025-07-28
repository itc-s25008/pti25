import matplotlib.pyplot as plt
import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy

def imageToData(filename):
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8, 8), PIL.Image.Resampling.LANCZOS)
    numImage = numpy.asarray(grayImage, dtype=float)
    numImage = 16 - numpy.floor(17 * numImage / 256)
    return numImage  # flatten しない！

data = imageToData("1.png")
plt.imshow(data, cmap="Greys")
plt.show()

