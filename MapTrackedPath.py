import numpy as np
import cv2
import re

img = cv2.imread('BlankFrame.jpg')

a_file = open("face.txt", "r")


list_of_lists = []

for line in a_file:

  stripped_line = line.strip()

  line_list = stripped_line.split()

  list_of_lists.append(line_list)


a_file.close()


print(list_of_lists)
for i in np.arange(1, len(list_of_lists)):
    pt1 = (int(tuple(list_of_lists[i - 1])[0]), int(tuple(list_of_lists[i - 1])[1]))
    pt2 = (int(tuple(list_of_lists[i])[0]), int(tuple(list_of_lists[i])[1]))
    cv2.line(img, pt1,pt2, (0, 0, 255), 2)
  
cv2.imshow('img',img)
cv2.imwrite("DrawnFrame.jpg",img) #save image
