#coding=utf-8
import cv2
import numpy as np


cap = cv2.VideoCapture("VID_20181122_110326.mp4")
img_end = ".jpg"
img_start = 526
img_name = str(img_start) + img_end
print img_name
while True:
    # get a frame
    ret, frame = cap.read()
    #显示第几帧
    frames_num = cap.get(cv2.CAP_PROP_POS_FRAMES)
    #显示实时帧数
    FPS = cap.get(cv2.CAP_PROP_FPS)
    #总帧数
    total_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    # show a frame
    cv2.putText(frame, "FPS:"+str(FPS), (17, 13), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255))
    cv2.putText(frame, "NUM OF FRAME:"+str(frames_num), (222, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255))
    cv2.putText(frame, "TOTAL FRAME:" + str(total_frame), (504, 17), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255))
    cv2.imshow("capture", frame)
    #存储
    storage_path = ""
    if frames_num % 24 == 0:

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()