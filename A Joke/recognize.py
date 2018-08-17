import cv2
#读取本地照片进行人脸识别
image = cv2.imread('pic.jpg')
#灰度转换，降低计算强度
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#训练数据与代码放在同一文件夹下
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.1, 3)

##print ("发现{0}个人脸!".format(len(faces)))
###框出人脸
##for(x,y,w,h) in faces:
##    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
#显示检测结果
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
