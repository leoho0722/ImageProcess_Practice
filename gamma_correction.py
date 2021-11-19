import numpy
import cv2

def gamma_correction(f, gamma = 2.0):
    g = f.copy()
    nr, nc = f.shape[:2]
    c = 255.0 / (255.0 ** gamma)
    table = numpy.zeros(256)
    for i in range(256):
        table[i] = round(i ** gamma * c, 0)
    if (f.ndim != 3):
        for x in range(nr):
            for y in range(nc):
                g[x, y] = table[f[x, y]]
    else:
        for x in range(nr):
            for y in range(nc):
                for k in range(3):
                    g[x, y, k] = table[f[x, y, k]]
    
    return g


def main():
    image = cv2.imread("Dynalink Photos 2706 QRCode.jpg", -1)
    image1 = gamma_correction(image, 0.1)
    image2 = gamma_correction(image, 0.5)
    cv2.imshow("Original Image", image)
    cv2.imshow("Gamma = 0.1", image1)
    cv2.imshow("Gamma = 0.5", image2)
    cv2.waitKey(0)

main()