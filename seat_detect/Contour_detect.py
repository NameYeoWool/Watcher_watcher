# -*- coding: UTF-8 -*-

import cv2



def seat_contour_detect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 그레이 스케일 화면으로 변환
    canny=cv2.Canny(gray, 100, 200, 3)
    ret, thr = cv2.threshold(canny, 127, 255, 0)

    object_list = []

    _, contours, hierarchy = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(hierarchy)

    #for i in range(len(contours)):
        #x, y, w, h= cv2.boundingRect(contours[i])


    cv2.drawContours(image, contours, -1, (0, 0, 255), 1)
    #cv2.imshow('thresh', thr)
    #cv2.imshow('contour', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    '''
    object_list = []

    # 모든 윤곽선 검출
    _, roi_contours, roi_hierarchy = cv2.findContours(map_canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print(roi_hierarchy)
    for i in range(len(roi_contours)):
        x, y, w, h = cv2.boundingRect(roi_contours[i])
        rect_area = w * h
        image = cv2.drawContours(image, roi_contours, -1, (0,255,0), 2)
        if roi_hierarchy[0][i][3] == -1:
            if rect_area >= 10:
                object_list.append([x, y, w, h, rect_area])

    cv2.imshow("drawcontours", image)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()
    print("object_list", object_list)
    #make_obstacle_list(object_list)

    empt_seat_list = []
    full_seat_list = []
    #jelly_list = []
    for i in range(len(object_list)):
        x, y, w, h, rect_area = object_list[i]
        if rect_area<300:
            empt_seat_list.append(object_list[i])
        elif rect_area<500:
            full_seat_list.append(object_list[i])
        #else:
            #jelly_list.append(object_list[i])

    return empt_seat_list, full_seat_list
'''
image=cv2.imread('pcroom.jpg')
print(seat_contour_detect(image))

