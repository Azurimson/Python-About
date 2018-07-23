import cv2
import win32gui,win32con, win32api
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')

##gameclassname = "MozillaWindowClass"
##gametitle = "python win32 简单操作 - 417小六 - 博客园 - Mozilla Firefox"
##workclassname = "TkTopLevel"
##worktitle = "*camera.py - D:\Download\1\camera.py (3.6.1)*"
gamehwnd=721986#win32gui.FindWindow(gameclassname, gametitle)
workhwnd=2032574#win32gui.FindWindow(workclassname, worktitle)
#句柄由按键精灵直接获得
print("game句柄：%s" % gamehwnd)
print("work句柄：%s" % workhwnd)

while(1):
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    if len(faces) > 0:
        win32gui.SetForegroundWindow(workhwnd)
        win32gui.SetBkMode(gamehwnd, win32con.TRANSPARENT)
        print ("发现{0}个人脸!".format(len(faces)))
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+w),(0,255,0),2)
    if len(faces) == 0:
        win32gui.SetForegroundWindow(gamehwnd)
        win32gui.SetBkMode(workhwnd, win32con.TRANSPARENT)
    cv2.imshow("capture", frame)
    #cv2.imwrite("d:/Download/1/1.jpg", frame)
    c = cv2.waitKey(10)
    if c & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

##import cv2
###控制摄像头拍摄每一帧存往本地，屏幕输入q结束
##cap = cv2.VideoCapture(0)
##face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')
##while(1):
##    ret, frame = cap.read()
##    if not ret:
##        break
##    cv2.imshow("capture", frame)
##    cv2.imwrite("d:/Download/1/1.jpg", frame)
##    #cv2.waitKey(1)
##    '''
##    cv2.waitKey(1) 1为参数，单位毫秒，表示间隔时间
##    ord(' ')将字符转化为对应的整数（ASCII码）
##    0xFF是十六进制常数，二进制值为11111111。
##    通过使用位和（和）这个常数，
##    它只留下原始的最后8位（在这种情况下，无论CV2.WaITKEY（0）是）
##    此处是防止BUG。
##    '''
##    if cv2.waitKey(1) & 0xFF == ord('q'):
##        break
##cap.release()
##cv2.destroyAllWindows()

##import win32gui,win32con, win32api
###设置窗口前台后台，类名与标题由按键精灵获得
##classname = "MozillaWindowClass"
##title = "python win32 简单操作 - 417小六 - 博客园 - Mozilla Firefox"
##hwnd=win32gui.FindWindow(classname, title)
##if int(hwnd) <= 0:
##    print("not find")
##print("句柄：%s" % hwnd)
##win32gui.SetForegroundWindow(hwnd)

##import cv2
###读取本地照片进行人脸识别
##image = cv2.imread('1.jpg')
###灰度转换，降低计算强度
##gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
###训练数据与代码放在同一文件夹下
##face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')
##faces = face_cascade.detectMultiScale(gray, 1.1, 3)
##
####print ("发现{0}个人脸!".format(len(faces)))
#####框出人脸
####for(x,y,w,h) in faces:
####    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
###显示检测结果
##cv2.imshow("image",image)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
