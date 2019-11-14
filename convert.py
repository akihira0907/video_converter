import numpy as np
import cv2

cap = cv2.VideoCapture('video.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter("video.avi", int(fourcc), fps, (int(width), int(height)))

while(cap.isOpened()):
    try:
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;
    except:
        break

out.release()
cap.release()
cv2.destroyAllWindows()

