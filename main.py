import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utiels = mp . solutions.drawing_utils

index_x=0
index_y=0
flag = True
count=1

while True:
    _,frame =cap.read()
    frame = cv2.flip(frame,1)
    frame_height, frame_width, _ = frame.shape
    # frame_height*=1.1
    # frame_width*=1.1
    screen_widht,screen_height = pyautogui.size()
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    # print('screen',screen_widht,screen_height)
    # print('frame',frame_width,frame_height)

    if hands:
        for hand in hands:
            # drawing_utils.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for id , landmark in enumerate(landmarks):
                x= int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                # print ('landmark',x,y)
                # print ('index',index_x,index_y)

                if id == 5:
                    cv2.circle(img=frame,center=(x,y),radius=15,color=(0,255,255))
                    tracker_x=(screen_widht/frame_width) * x
                    tracker_y=(screen_height/frame_height) * y
                    pyautogui.moveTo(tracker_x,tracker_y)

                if id == 4:
                    cv2.circle(img=frame,center=(x,y),radius=15,color=(255,0,0))
                    index_x=(screen_widht/frame_width) * x
                    index_y=(screen_height/frame_height) * y

                if id == 8:
                    cv2.circle(img=frame,center=(x,y),radius=15,color=(255,0,0))
                    thumb_x=(screen_widht/frame_width) * x
                    thumb_y=(screen_height/frame_height) * y
                    # print ('index',index_y)
                    # print('thumb',thumb_y)
                    # print('distance','x',abs(thumb_x-index_x),'y',abs(thumb_y-index_y))
                    if abs(thumb_y-index_y)<32 and abs(thumb_x-index_x)<32 :
                        if flag==True and count:
                            print (count,'click')
                            count+=1
                            flag = False
                            pyautogui.click()
                    else :
                        flag=True


    # print (hands)
    cv2.imshow('Virtual Mouse',frame)
    cv2.waitKey(1)

