import numpy
import cv2

image1 = cv2.imread("Dynalink Photos 2706 QRCode.jpg", -1)

nr, nc = image1.shape[:2]
pts1 = numpy.float32([
    [795, 350],
    [795, 690], 
    [1090, 720],
    [1090, 250]
])

pts2 = numpy.float32([
    [0, 0],
    [0, 500],
    [650, 500],
    [650, 0]
])

T = cv2.getPerspectiveTransform(pts1, pts2)

image2 = cv2.warpPerspective(image1, T, (650, 500))

cv2.imshow("Original Image", image1)
cv2.imshow("Perspective Transform", image2)
cv2.waitKey(0)