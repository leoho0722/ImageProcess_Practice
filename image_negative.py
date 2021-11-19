import numpy
import cv2

def image_negative(f):
    g = 255 - f
    return g

def main():
    image1 = cv2.imread("Dynalink Photos 2706 QRCode.jpg", -1)
    image2 = image_negative(image1)
    cv2.imshow("Original Image", image1)
    cv2.imshow("Image Negative", image2)
    cv2.waitKey(0)

main()