
import cv2
import mediapipe as mp
import controller as cnt

mpDraw=mp.solutions.drawing_utils
mpHand=mp.solutions.hands
handsType=[]
tips=[4,8,12,16,20]
tipsr=[5,16,12,8,20]
#tipsr=[4,20,16,12,8]
video=cv2.VideoCapture(0)

with mpHand.Hands(min_detection_confidence=0.5,
               min_tracking_confidence=0.5) as hands:
    while True:
        ret,image=video.read()
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable=False
        results=hands.process(image)
        image.flags.writeable=True
        image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        id_and_coordinates=[]
        if results.multi_hand_landmarks:
            for hand in results.multi_handedness:
                handType=hand.classification[0].label
                handsType.append(handType)
            for hand_landmark in results.multi_hand_landmarks:
                dHands=results.multi_hand_landmarks[0]
                for id, lm in enumerate(dHands.landmark):
                    h,w,c=image.shape
                    cx,cy= int(lm.x*w), int(lm.y*h)
                    id_and_coordinates.append([id,cx,cy])
                mpDraw.draw_landmarks(image, hand_landmark, mpHand.HAND_CONNECTIONS)
        numoffingers=[]
        if len(id_and_coordinates)!=0:
            if handType=='Left':
                if id_and_coordinates[tips[0]][1] > id_and_coordinates[tips[0]-1][1]:
                    numoffingers.append(1)
                else:
                    numoffingers.append(0)
                for id in range(1,5):
                    if id_and_coordinates[tips[id]][2] < id_and_coordinates[tips[id]-2][2]:
                        numoffingers.append(1)
                    else:
                        numoffingers.append(0)
                total=numoffingers.count(1)
                cnt.led(total);
                if total==0:
                    cv2.rectangle(image, (20, 300), (270, 425), (255, 0, 0), cv2.FILLED)
                    cv2.putText(image, "0", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 255), 5)
                    cv2.putText(image, "led", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 0), 5)
                elif total==1:
                    cv2.rectangle(image, (20, 300), (270, 425), (255, 0, 0), cv2.FILLED)
                    cv2.putText(image, "1", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 255), 5)
                    cv2.putText(image, "led", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 0), 5)
                elif total==2:
                    cv2.rectangle(image, (20, 300), (270, 425), (255, 0, 0), cv2.FILLED)
                    cv2.putText(image, "2", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 255), 5)
                    cv2.putText(image, "led", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 0), 5)
                elif total==3:
                    cv2.rectangle(image, (20, 300), (270, 425), (255, 0, 0), cv2.FILLED)
                    cv2.putText(image, "3", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 255), 5)
                    cv2.putText(image, "led", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 0), 5)
                elif total==4:
                    cv2.rectangle(image, (20, 300), (270, 425), (255, 0, 0), cv2.FILLED)
                    cv2.putText(image, "4", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 255), 5)
                    cv2.putText(image, "led", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 0), 5)
                elif total==5:
                    cv2.rectangle(image, (20, 300), (270, 425), (255, 0, 0), cv2.FILLED)
                    cv2.putText(image, "5", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 255), 5)
                    cv2.putText(image, "led", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 0), 5)
            elif handType=='Right':
                if id_and_coordinates[tipsr[0]][1] > id_and_coordinates[tipsr[0]-1][1]:
                    numoffingers.append(1)
                else:
                    numoffingers.append(0)
                for id in range(1,5):
                    if id_and_coordinates[tipsr[id]][2] < id_and_coordinates[tipsr[id]-2][2]:
                        numoffingers.append(1)
                    else:
                        numoffingers.append(0)
                total=numoffingers.count(1)
                cnt.led(total);
                if total==0:
                    cv2.rectangle(image, (20, 300), (270, 425), (255, 0, 0), cv2.FILLED)
                    cv2.putText(image, "0", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 255), 5)
                    cv2.putText(image, "led", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 0), 5)
                elif total==1:
                    cv2.rectangle(image, (20, 300), (270, 425), (255, 0, 0), cv2.FILLED)
                    cv2.putText(image, "1", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 255), 5)
                    cv2.putText(image, "led", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 0), 5)
                elif total==2:
                    cv2.rectangle(image, (20, 300), (270, 425), (255, 0, 0), cv2.FILLED)
                    cv2.putText(image, "2", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 255), 5)
                    cv2.putText(image, "led", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 0), 5)
                elif total==3:
                    cv2.rectangle(image, (20, 300), (270, 425), (255, 0, 0), cv2.FILLED)
                    cv2.putText(image, "3", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 255), 5)
                    cv2.putText(image, "led", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 0), 5)
                elif total==4:
                    cv2.rectangle(image, (20, 300), (270, 425), (255, 0, 0), cv2.FILLED)
                    cv2.putText(image, "4", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 255), 5)
                    cv2.putText(image, "led", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 0), 5)
                elif total==5:
                    cv2.rectangle(image, (20, 300), (270, 425), (255, 0, 0), cv2.FILLED)
                    cv2.putText(image, "5", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 255), 5)
                    cv2.putText(image, "led", (100, 375), cv2.FONT_HERSHEY_SIMPLEX,
                        2, (0, 0, 0), 5)

        cv2.imshow("Frame",image)
        k=cv2.waitKey(1)
        if k==ord('q'):
            break
video.release()
cv2.destroyAllWindows()
