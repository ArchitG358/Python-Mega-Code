import cv2


face_cascade = cv2.CascadeClassifier(r"C:\Users\ASUS\Desktop\IMPORTANT\Python_mega_course\Applications\Image Processing\haarcascade_frontalface_default.xml")

img = cv2.imread(r"C:\Users\ASUS\Desktop\IMPORTANT\Python_mega_course\Applications\Image Processing\photo.jpg")
gray_img = cv2.imread(r"C:\Users\ASUS\Desktop\IMPORTANT\Python_mega_course\Applications\Image Processing\photo.jpg",0)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,250),3)

resized_img = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("Gray",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
