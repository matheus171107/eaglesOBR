import cv2
import numpy as np
import serial

webcam = cv2.VideoCapture(1)

def desenharRetangulos(frames, Cam1, Cam2, Cam3, Cam4, Cam5, Cam6):
	cv2.rectangle(frames,(200,50), (440,360), (120,255,0), 2)
	cv2.rectangle(frames,(150,50), (180,285), (120,255,0), 2)
	cv2.rectangle(frames,(460,50), (490,285), (120,255,0), 2)
	cv2.rectangle(frames,(320-40,0), (320+40,20), (120,255,0), 2)
	cv2.rectangle(frames,(0,30), (35,250), (120,255,0), 2)
	cv2.rectangle(frames,(605,30), (640,250), (120,255,0), 2)

	cv2.putText(frames, "W:{}".format(Cam1), (280, 340), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (120,255,0), 2, cv2.LINE_AA)
	cv2.putText(frames, "W:{}".format(Cam2), (100, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (120,255,0), 2, cv2.LINE_AA)
	cv2.putText(frames, "W:{}".format(Cam3), (500, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (120,255,0), 2, cv2.LINE_AA)
	cv2.putText(frames, "W:{}".format(Cam4), (300, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (120,255,0), 2, cv2.LINE_AA)
	cv2.putText(frames, "W:{}".format(Cam5), (0, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (120,255,0), 2, cv2.LINE_AA)
	cv2.putText(frames, "W:{}".format(Cam6), (590, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (120,255,0), 2, cv2.LINE_AA)

	

if webcam.isOpened():
    print("Cam conect sucessuful!!")
    text = ""
    
    cor_branca, cor_preta = 240, 10
    
    def analisador(c1, c2, c3, c4, c5, c6):
       if (c1 >= cor_branca ) and ((c2 < cor_preta) and (c3 < cor_preta)):
          return "Linha preta"
          

    while True:
        
        _, pixels = webcam.read()
        offset = 200
        a,l,_ = pixels.shape
        
        #Colocando filtros em escala cinza
        gray = cv2.cvtColor(pixels, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        frames = cv2.threshold(gray, 135, 255, cv2.THRESH_BINARY)[1]
        frames = cv2.dilate(frames, None, iterations=2)
        frames = cv2.bitwise_not(frames)
        img = frames.copy()
        
        #                  V            H      
        campo1 = img[50:360, offset:l-offset]
        campo2 = img[50:285, 150:180]
        campo3 = img[50:285, 460:490]
        campo4 = img[0:20, 320-40:320+40]
        campo5 = img[30:250, 0:35]
        campo6 = img[30:250, 605:640]

        Cam1 = int(np.average(np.average(campo1, axis=0)))
        Cam2 = int(np.average(np.average(campo2, axis=0)))
        Cam3 = int(np.average(np.average(campo3, axis=0)))
        Cam4 = int(np.average(np.average(campo4, axis=0)))
        Cam5 = int(np.average(np.average(campo5, axis=0)))
        Cam6 = int(np.average(np.average(campo6, axis=0)))

        desenharRetangulos(frames, Cam1, Cam2, Cam3, Cam4, Cam5, Cam6)
       
        cv2.imshow("Video WEBCAM - Index 1", frames)
        #cv2.imshow("Video", pixels)
        
        key = cv2.waitKey(1)
        if key == 27:
            break

cv2.release()
cv2.destroyAllWindows()
