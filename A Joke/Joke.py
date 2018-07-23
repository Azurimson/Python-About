import cv2
import win32gui,win32con, win32api
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(r'./haarcascade_frontalface_default.xml')

##gameclassname = "MozillaWindowClass"
##gametitle = "python win32 简单操作 - 417小六 - 博客园 - Mozilla Firefox"
##workclassname = "TkTopLevel"
##worktitle = "*camera.py - D:\Download\A joke\Joke.py (3.6.1)*"
gamehwnd=721986#win32gui.FindWindow(gameclassname, gametitle)
workhwnd=1181530#win32gui.FindWindow(workclassname, worktitle)
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
    #cv2.imwrite("d:/Download/A joke/pic.jpg", frame)
    c = cv2.waitKey(10)
    if c & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
