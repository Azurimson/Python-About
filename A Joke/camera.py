import cv2
#控制摄像头拍摄每一帧存往本地，屏幕输入q结束
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')
while(1):
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("capture", frame)
    cv2.imwrite("d:/Download/A joke/pic.jpg", frame)
    #cv2.waitKey(1)
    '''
    cv2.waitKey(1) 1为参数，单位毫秒，表示间隔时间
    ord(' ')将字符转化为对应的整数（ASCII码）
    0xFF是十六进制常数，二进制值为11111111。
    通过使用位和（和）这个常数，
    它只留下原始的最后8位（在这种情况下，无论CV2.WaITKEY（0）是）
    此处是防止BUG。
    '''
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
