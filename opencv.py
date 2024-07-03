import cv2
import math
import mediapipe as mp
import time

import serial
try :
    arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
except:
    pass
x_ax = 512
y_ax = 512
z_ax = 512
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
pam = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.5)

# pam = mpHands.Hands(1,0.8,0.5)
mpDraw = mp.solutions.drawing_utils # using mp draw for calling a class called "drawing utilities"
currenttime = 0
previoustime = 0

lmList = []
fing = []
count_time = 45
#
# cap.set(3,1920)
# cap.set(4,1080)
# #cap.set(15, 0.1)
def len():
    x_comp = x0 - x5
    y_comp = y0 - y5
    x = pow(x_comp, 2)
    y = pow(y_comp, 2)

    val = math.sqrt((x + y))
    return val
def lengh(k1,p1,k2,p2):   #9
    x_comp = k1 - k2
    y_comp = p1 - p2
    x_pow = pow(x_comp, 2)
    y_pow= pow(y_comp, 2)

    val = math.sqrt((x_pow + y_pow))
    return val


def send(num):
    arduino.write(bytes(num, 'utf-8'))




cap.set(3,1280)
cap.set(4,720)

while True:
    success , img = cap.read()
    img = cv2.flip(img, 2)
    imgRGB =  cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pam.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:         # results have the hand lms so to dram a  points we use draw land marks
        for handLms in results.multi_hand_landmarks:  #here hand lms value is is a variable cand be changed to required
            for id,lm in enumerate(handLms.landmark): # here also lm and id is a stroing variable name can be changed
                h,w,c = img.shape

                cx,cy = int(lm.x*w) , int(lm.y*h)
                if (id == 4):
                    x4, y4 = cx, cy
                    ######
                if (id == 8):
                    x8, y8 = cx, cy
                if (id == 12):
                    x12, y12 = cx, cy
                if (id == 20):
                    x20, y20 = cx, cy
                if (id == 16):
                    x16, y16 = cx, cy
                if (id == 0):
                    x0, y0 = cx, cy
                if (id == 1):
                    x1, y1 = cx, cy
                if (id == 2):
                    x2, y2 = cx, cy
                if (id == 3):
                    x3, y3 = cx, cy
                if (id == 5):
                    x5, y5 = cx, cy
                if (id == 6):
                    x6, y6 = cx, cy
                if (id == 7):
                    x7, x7 = cx, cy
                if (id == 9):
                    x9, y9 = cx, cy
                if (id == 10):
                    x10, y10 = cx, cy
                if (id == 11):
                    x11, y11 = cx, cy

                if (id == 13):
                    x13, y13 = cx, cy
                if (id == 14):
                    x14, y14 = cx, cy
                if (id == 15):
                    x15, y15 = cx, cy

                if (id == 17):
                    x17, y17 = cx, cy
                if (id == 19):
                    x19, y19 = cx, cy
                if (id == 18):
                    x18, y18 = cx,cy #-9 17 24 44
            # t_ind = ( x4 -   x8)
            # t_mid = (x4 -   x12)
            # t_ring = (x4 -  x16)
            # t_pinky = (x4 - x20)
            # lenght = len()
            # print(lenght)
            f48 = lengh(x4, y4, x8, y8)
            f412 = lengh(x4, y4, x12, y12)
            f128 = lengh(x8, y8, x12, y12)
            print(f"f48 {f48}    {f412}   {f128}")

            hndctrx,hndctry = int((x5 +x17)/2),int((y5+y17)/2)
            if (y8 > y5 and y12 > y9 and y16 > y13 and y20 > y17 and x5 >= x4 and x5 <= x9 and x9 <= x13 and y2 > y4):

                # (y8 <= y5 and y12 <= y9 and y16 <= y13 and y20 <= y17):
                cv2.putText(img, "left", (420, 240), cv2.FONT_ITALIC, 0.5, (250, 255, 0), 2)
                print("before 1")
                # arduino.write(bytes(1, 'utf-8'))
                send('x')
                x_ax = x_ax+10
                print(x_ax)
                print("after 1")
                # print(data)
            if (y8 > y5 and y12 > y9 and y16 > y13 and y20 > y17 and x5 <= x4 and  x5 >= x9 and x9 >= x13 and y4 > y17 ):
                # (y8 <= y5 and y12 <= y9 and y16 <= y13 and y20 <= y17):
                #arduino.write(bytes(2, 'utf-8'))
                cv2.putText(img, "right", (420, 240), cv2.FONT_ITALIC, 0.5, (250, 255, 0), 2)
                print("before 1")
                send('y')
                print("after 1")
                x_ax = x_ax-10
                print(x_ax)
                # data = arduino.readline()
                # print(data)
            if (x8 > x5 and x12 > x9 and x16 > x13 and x20 > x17 and y5 <= y4  and y17 <= y13 and y13 <= y9 and y9 <= y5  ):
                # (y8 <= y5 and y12 <= y9 and y16 <= y13 and y20 <= y17):
                #arduino.write(bytes(3, 'utf-8'))
                cv2.putText(img, "bottom", (420, 240), cv2.FONT_ITALIC, 0.5, (250, 255, 0), 2)
                send('d')
                # data = arduino.readline()
                # print(data)
            if (x8 > x6 and x12 > x10 and x16 > x14 and x20 > x18 and y5 >= y4 and y17 >= y13 and y13 >= y9 and y9 >= y5):
                # (y8 <= y5 and y12 <= y9 and y16 <= y13 and y20 <= y17):
                #arduino.write(bytes(4, 'utf-8'))
                cv2.putText(img, "top", (420, 240), cv2.FONT_ITALIC, 0.5, (250, 255, 0), 2)
                send('c')
                # data = arduino.readline()
                # print(data)
            # lenght between 5 and 20
            #print("lencht :",end="")
            #print(lengh(x5,y5,x20,y20))
            if(y12 > y9 and y16 < y13 and y8 < y5 and y20<y17):
                #print("forword")
                cv2.putText(img, "forward", (420, 240), cv2.FONT_ITALIC, 0.5, (250, 255, 0), 2)
                send('a')
            if (y12 < y9 and y16 > y13 and y8 < y5 and y20 < y17):
                # print("forword")
                cv2.putText(img, "backward", (420, 240), cv2.FONT_ITALIC, 0.5, (250, 255, 0), 2)
                send('b')
            if(f48 <= 60 and f128 <=60 and f412 <=60):
                cv2.putText(img, "relase", (420, 240), cv2.FONT_ITALIC, 0.5, (250, 255, 0), 2)
                send('p')
            if(f48 <= 120 and f412 >170):
                cv2.putText(img, "pick", (420, 240), cv2.FONT_ITALIC, 0.5, (250, 255, 0), 2)
                send('h')
                if (f412 <= 120 and f48 > 170):
                    cv2.putText(img, "hold", (420, 240), cv2.FONT_ITALIC, 0.5, (250, 255, 0), 2)

                # for i in range (1000000):
                #     val = i
                #     cv2.putText(img,f"val {val}", (620, 240), cv2.FONT_ITALIC, 0.5, (250, 255, 0), 2)


            # if (y20 > y17 and y16 > y13 and y8 < y5 and y12 < y9):
            #     #print("backward")
            #     cv2.putText(img, "backward", (420, 240), cv2.FONT_ITALIC, 0.5, (250, 255, 0), 2)
            #     send('b')













            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS )

    currenttime = time.time()
    fps =1/(currenttime - previoustime)
    previoustime = currenttime
    fps = int(fps)
    cv2.putText(img,f"frame rate {fps}",(10,450),cv2.FONT_ITALIC,0.5,(0,255,0),2)
    # cv2.rectangle(img, (475, 265), (800, 455), (255, 0, 0), 5, cv2.FILLED) #act center box for
    # #cv2.rectangle(img, (50, 25), (375, 215), (255, 0, 0), 5, cv2.FILLED) #top left
    # cv2.rectangle(img, (900, 240), (1230, 455), (255, 0, 0), 5, cv2.FILLED) #right
    # cv2.rectangle(img, (50, 265), (375, 455), (255, 0, 0), 5, cv2.FILLED)  # left
    # cv2.rectangle(img, (476, 0), (800, 215), (255, 0, 0), 5, cv2.FILLED)  # top
    # cv2.rectangle(img, (476, 505), (800, 695), (255, 0, 0), 5, cv2.FILLED)  # top
    cv2.imshow("hand tracking module" , img)
    #print(results.multi_hand_landmarks)

    cv2.waitKey(1)
