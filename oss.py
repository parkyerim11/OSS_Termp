import cv2, numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('./family.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image', img)
cv2.imshow('Gray image', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

#원
COLOR = (255, 255, 0) #색
THICKNESS = 5 #두께

for (x, y, w, h) in faces:
    print(x, y, w, h)

    roi = img[y : y + h, x : x + w]
    cv2.imshow('cropped', roi)  # ROI 지정 영역을 새창으로 표시
    cv2.moveWindow('cropped', 0, 0) # 새창을 이동

    cv2.circle(img, (x + int(w/2), y + int(h / 2)), w, COLOR, THICKNESS, cv2.LINE_AA)

    cv2.imshow('img', img)
    cv2.waitKey()

x,y,w,h   = cv2.selectROI('img', img, False)
if w and h:
    roi = img[y:y+h, x:x+w]
    cv2.imshow('cropped2', roi)  # ROI 지정 영역을 새창으로 표시
    cv2.moveWindow('cropped2', x, 0) # 새창을 이동
    cv2.imwrite('./cropped2.jpg', roi)   # ROI 영역만 파일로 저장

cv2.waitKey(0)
cv2.destroyAllWindows()