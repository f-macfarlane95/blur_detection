import cv2
import numpy as np
import blur_detection

I = blur_detection.get_blur_map("C:/Users/fm43842/Desktop/Data/202110_deep_blueberries/data/instancesegmentation/images/IMG_1023.jpg",50,20)

cv2.imshow('blur map', I)
cv2.waitKey(0) 
cv2.destroyAllWindows() 