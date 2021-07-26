from cv2 import *
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    imshow("cam-test",img)
    waitKey(0)
    destroyWindow("cam-test")
    imwrite("BlankFrame.jpg",img) #save image

cap.release()
cv2.destroyAllWindows()
