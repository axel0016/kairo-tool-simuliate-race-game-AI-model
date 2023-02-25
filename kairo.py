import cv2
import numpy as np
from pynput.keyboard import Key, Controller
import pygame
keyboard = Controller()
# initialize pygame mixer
pygame.mixer.init()

# load the song

song1 = pygame.mixer.Sound("Message Ringtone SMS Tone iphone message tone new Ringtone.mp3")
song2 = pygame.mixer.Sound("Multi Tone Car Alarm Siren Sound Effect.mp3")
def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Mouse clicked at ({x}, {y})")
def victo(caylo,z):
    hsvImage = cv2.cvtColor(caylo, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    bbox = cv2.boundingRect(mask)
    if bbox is not None:
        x, y, w, h = bbox
        cv2.rectangle(caylo, (x, y), (x+w, y+h), (0, 255, 0), 5)
        
    return x,y,w,h
        
def get_limits(color):

    # here insert the bgr values which you want to convert to hsv
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit

yellow = [0, 255, 255]  # yellow in RGB colorspace
cap = cv2.VideoCapture(1)

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', on_click)


while True:
    try:
        ret, frame = cap.read()

        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lowerLimit, upperLimit = get_limits(color=yellow)

        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

        bbox = cv2.boundingRect(mask)

        cv2.rectangle(frame, (1, 64), (230, 235), (0, 0, 255), 3)
        cv2.rectangle(frame, (433, 64), (635, 228), (255, 0, 0), 5)
        cv2.rectangle(frame, (1, 350), (176, 417), (255, 94, 5), 3)
        cv2.rectangle(frame, (181, 350), (634, 417), (255, 191, 0), 5)
        cv2.rectangle(frame, (2, 240), (630, 342), (255, 2255, 255), 3)
        imgrect1 = frame[64:235, 1:230]
        imgrect2 = frame[64:228, 433:635]
        imgrect3 = frame[350:417, 1:176]
        imgrect4 = frame[350:417, 181:634]
        imgrect5 = frame[240:342, 2:630]
        x4,y4,w4,h4 = victo(imgrect1,1)
        if x4>0 and y4>0 and w4>0 and h4>0:
            keyboard.press(Key.left)
            song1.stop()
            song2.play()
        else:
            keyboard.release(Key.left)
        
        x,y,w,h = victo(imgrect2,2)
        if x>0 and y>0 and w>0 and h>0:
            keyboard.press(Key.right)
            song2.stop()
            song1.play()
        else:
            keyboard.release(Key.right)
        x1,y1,w1,h1 = victo(imgrect3,3)
        if x1>0 and y1>0 and w1>0 and h1>0:
            keyboard.press(Key.shift_l)
        else:
            keyboard.release(Key.shift_l)
        x2,y2,w2,h2 = victo(imgrect4,4)
        if x2>0 and y2>0 and w2>0 and h2>0:
            keyboard.press('z')
        else:    
            keyboard.release('z')
        x3,y3,w3,h3 = victo(imgrect5,5)
        if x3>0 and y3>0 and w3>0 and h3>0:
            keyboard.press('a')
        else:
            keyboard.release('a')
        
        

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        
    except Exception as e:
        print(f"An error occurred: {e}")
        break
cap.release()
cv2.destroyAllWindows()
pygame.quit()
   