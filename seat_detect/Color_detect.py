import cv2
import numpy as np

detect_list=[]

def detect_seat(image):
    global detect_list

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    seat_lower = np.array([0, 0, 61], np.uint8)
    seat_upper = np.array([179, 255, 255], np.uint8)

    kernel = np.ones((5, 5), "uint8")
    seat = cv2.inRange(hsv, seat_lower, seat_upper)
    seat = cv2.dilate(seat, kernel)
    #cv2.imshow("seat", seat)

    (_, contours, hierarchy) = cv2.findContours(seat, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        # Contour의 면적을 구하는 부분
        area = cv2.contourArea(contour)
        if (area > 100):
            #image=cv2.drawContours(image, contour, -1, (0,255,0), 3)
            x, y, w, h = cv2.boundingRect(contour)
            detect_list.append((x, y, w, h, area))
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

'''
    cv2.imshow("Color Tracking", image)

    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()

image=cv2.imread('pcroom.jpg')
detect_seat(image)
print(detect_list)
'''