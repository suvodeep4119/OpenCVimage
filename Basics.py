import cv2

img = cv2.imread("C:\\Users\\Suvodeep\\Pictures\\baleno.jpg", 1)
resize = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
print(img.shape)

cv2.imshow("photo", resize)

cv2.waitKey(0)

cv2.destroyAllWindows()

