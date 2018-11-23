# -*- coding: UTF-8 -*-
################################
################################
# 모듈명    : Color_detect
# 작성자    : 이현지
# 설명      : PC방 좌석의 배치도 이미지 상에서 색상을 통해 좌석 상황을 식별한다
################################
################################

import cv2
import numpy as np

# 전역 변수 선언 및 초기화
occupied_list=[]    # 이미 차지하고 있는 좌석을 인식한 개체 리스트
empty_list=[]       # 빈 좌석 개체 리스트

################################
# 함수명    : detect_seat
# 작성자    : 이현지
# 설명      : 좌석 배치도 상에서 빈 공간과 이미 차지된 좌석, 빈 좌석을 구분한다
# 리턴      : _
# 매개변수  : PC방 좌석 배치도 image
################################
def detect_seat(image):
    global detect_list

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 각 객체의 hsv 색상 범위 설정
    # bseat: 파랑 좌석, pseat: 보라 좌석, empty: 빈 좌석
    bseat_lower = np.array([101, 122, 49], np.uint8)
    bseat_upper = np.array([113, 208, 110], np.uint8)

    pseat_lower = np.array([126, 31, 54], np.uint8)
    pseat_upper = np.array([167, 180, 255], np.uint8)

    empty_lower = np.array([0, 79, 23], np.uint8)
    empty_upper = np.array([17, 255, 255], np.uint8)

    bseat = cv2.inRange(hsv, bseat_lower, bseat_upper)
    pseat = cv2.inRange(hsv, pseat_lower, pseat_upper)
    empty = cv2.inRange(hsv, empty_lower, empty_upper)

    kernel = np.ones((5, 5), "uint8")

    bseat = cv2.dilate(bseat, kernel)
    pseat = cv2.dilate(pseat, kernel)
    empty = cv2.dilate(empty, kernel)

    # 이미지 상에서 각 색상 판별하여 개체 리스트에 추가
    # 1. 파란색으로 표시된 좌석
    (_, contours, hierarchy) = cv2.findContours(bseat, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        # 파란색 영역이 700이상일 때, 좌석이라고 간주한다
        if (area > 700):
            x, y, w, h = cv2.boundingRect(contour)
            occupied_list.append((x, y, w, h, area))    # 이미 사용 중인 좌석의 개체 리스트에 추가
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)    #이미지에 해당 영역 사각형으로 표시

    # 2. 보라색으로 표시된 좌석
    (_, contours, hierarchy) = cv2.findContours(pseat, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 700):
            x, y, w, h = cv2.boundingRect(contour)
            occupied_list.append((x, y, w, h, area))
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 3. 빈 좌석
    (_, contours, hierarchy) = cv2.findContours(empty, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        # 빈 좌석을 표시하는 'X' 표식의 영역의 넓이를 개체로 인식한다
        if(area > 80):
            x, y, w, h = cv2.boundingRect(contour)
            empty_list.append((x, y, w, h, area))
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
