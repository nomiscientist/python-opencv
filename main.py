import cv2
import numpy as np
import matplotlib.pyplot as plt

img  = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("new.jpg",img)

# plt.imshow(img,cmap='gray',interpolation='bicubic')
# plt.plot([30,50],[20, 100],'c',linewidth=5)
# plt.show()





# print("Hello Pakistan!")