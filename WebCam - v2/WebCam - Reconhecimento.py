import cv2
import numpy as np

webcam = cv2.VideoCapture(1)

if webcam.isOpened():
    print("Cam conect sucessuful!!")
    text = ""
    while True:
        
        _, pixels = webcam.read()
        offset = 122
        a,l,_ = pixels.shape
        
        gray = cv2.cvtColor(pixels, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        frames = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)[1]
        frames = cv2.dilate(frames, None, iterations=2)
        frames = cv2.bitwise_not(frames)
        
        #                  V            H      
        campo1 = frames[150:320, offset:l-offset]
        campo2 = frames[150:320, 80:110]
        campo3 = frames[150:320, 530:560]
        campo4 = frames[20:70, 320-40:320+40]
        campo5 = frames[130:350, 0:35]
        campo6 = frames[130:350, 605:640]
        cv2.rectangle(frames,(offset,150), (l-offset,320), (255,120,0), 2)
        cv2.rectangle(frames,(80,150), (110,320), (255,120,0), 2)
        cv2.rectangle(frames,(530,150), (560,320), (255,120,0), 2)
        cv2.rectangle(frames,(320-40,20), (320+40,70), (255,120,0), 2)
        cv2.rectangle(frames,(0,130), (35,350), (255,120,0), 2)
        cv2.rectangle(frames,(605,130), (640,350), (255,120,0), 2)

        media1 = np.average(campo1, axis=0)
        mediac1 = np.average(media1, axis=0)

        media2 = np.average(campo2, axis=0)
        mediac2 = np.average(media2, axis=0)

        media3 = np.average(campo3, axis=0)
        mediac3 = np.average(media3, axis=0)
        
        media4 = np.average(campo4, axis=0)
        mediac4 = np.average(media4, axis=0)

        media5 = np.average(campo5, axis=0)
        mediac5 = np.average(media5, axis=0)

        media6 = np.average(campo6, axis=0)
        mediac6 = np.average(media6, axis=0)

        r1,g1,b1 = int(mediac1[2]), int(mediac1[1]), int(mediac1[0])
        r2,g2,b2 = int(mediac2[2]), int(mediac2[1]), int(mediac2[0])
        r3,g3,b3 = int(mediac3[2]), int(mediac3[1]), int(mediac3[0])
        r4,g4,b4 = int(mediac4[2]), int(mediac4[1]), int(mediac4[0])
        r5,g5,b5 = int(mediac5[2]), int(mediac5[1]), int(mediac5[0])
        r6,g6,b6 = int(mediac6[2]), int(mediac6[1]), int(mediac6[0])

        cv2.putText(frames, "R:{} G:{} B:{}".format(r1, g1, b1), (250, 340), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (120,255,0), 1, cv2.LINE_AA)
        cv2.putText(frames, "R:{} G:{} B:{}".format(r2, g2, b2), (40, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (120,255,0), 1, cv2.LINE_AA)
        cv2.putText(frames, "R:{} G:{} B:{}".format(r3, g3, b3), (440, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (120,255,0), 1, cv2.LINE_AA)
        cv2.putText(frames, "R:{} G:{} B:{}".format(r4, g4, b4), (250, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (120,255,0), 1, cv2.LINE_AA)
        cv2.putText(frames, "{}".format(text), (150, 290), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2, cv2.LINE_AA)


        if (r1 <= 125 and g1 <= 130 and b1 <= 140):
            if (r2 >= 160 and g2 >= 165 and b2 >= 190) and (r3 >= 175 and g3 >= 165 and b3 >= 190):
               text = "Linha preta - Siga em Frente"
            elif ((r5 <= 170 and g5 <= 200 and b5 <= 235) or (r6 <= 170 and g6 <= 200 and b6 <= 235)) and (r4 < 190 and g4 < 210 and b4 < 240):
               text = "Desvio detectado - Seguir reto"
            elif (r5 <= 50 and g5 <= 40 and b5 <= 40) and (r4 >= 190 and g4 >= 200 and b4 >= 220):
               text = "Desvio detectado - Curva 90 Esquerda"
            elif (r6 <= 50 and g6 <= 40 and b6 <= 40) and (r4 >= 190 and g4 >= 200 and b4 >= 220):
               text = "Desvio detectado - Curva 90 Direita"
            elif r2  < 210 and g2 < 180 and b2 < 190:
               text = "Rota desvida - Correcao Direita"
            elif r3  < 210 and g3 < 180 and b3 < 190:
               text = "Rota desvida - Correcao Esquerda"
        else:
            text = "Rota Perdida!"

        print("R:{} G:{} B:{}".format(r5,g5,b5))        
        cv2.imshow("Video WEBCAM - Index 1", frames)
        
        key = cv2.waitKey(1)
        if key == 27:
            break

cv2.release()
cv2.destroyAllWindows()
