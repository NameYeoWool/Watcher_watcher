# -*- coding: UTF-8 -*-

################################
################################
# 모듈명    : grid
# 작성자    : 이현지
# 설명      : 색상 분석 결과를 image 상에 간결하게 격자로 표현한다
################################
################################

import cv2

# 전역 변수 선언 및 초기화
grid_w = 59     # 각 격자의 가로 길이
grid_h = 57     # 각 격자의 세로 길이

vertical_max, horizontal_max = 11, 6     # 격자는 총 가로 11칸, 세로 6칸
grid_x, grid_y = 10, 10                  # 격자의 시작 좌표. 변수 초기화

################################
# 함수명    : draw_grid
# 작성자    : 이현지
# 설명      : image(PC방 배치도)에 격자 무늬를 그린다
# 리턴      : 격자가 그려진 image
# 매개변수  : PC방 배치도 image
################################
def draw_grid(image):
    #가로선 그리기
    for ver in range(vertical_max + 1):
        cv2.line(image,
                 (grid_x + grid_w * ver, grid_y),
                 (grid_x + grid_w * ver, grid_y + grid_h * horizontal_max),
                 (255, 255, 255), 2, 1)

    # 그리드 세로선 그리기
    for hor in range(horizontal_max + 1):
        cv2.line(image,
                 (grid_x, grid_y + grid_h * hor),
                 (grid_x + grid_w * vertical_max + 1, grid_y + grid_h * hor),
                 (255, 255, 255), 2, 1)

    return image

################################
# 함수명    : occupied_in_grid
# 작성자    : 이현지
# 설명      : 해당 격자 칸 안에 색상 분석으로 식별한 '이미 차지된 좌석 개체'가 존재하는지 판단한다
#            해당 칸의 면적의 1/3 이상 차지할 때,
#            '이미 차지한 좌석 개체'가 칸 안에 존재한다고 판단한다.
# 매개변수  : int x, y 검사할 그리드의 시작좌표
#             int obj_x, obj_y 검사할 개체의 시작 좌표
#             int obj_w, obj_h 검사할 개체의 너비, 높이
# 리턴     : boolean 값
################################
def occupied_in_grid(x, y, obj_x, obj_y, obj_w, obj_h):
    # 검사할 grid의 좌표 범위
    x_range = set(range(x, x + grid_w + 1))
    y_range = set(range(y, y + grid_h + 1))
    # 검사할 개체의 좌표 범위
    obj_x_range = list(range(obj_x, obj_w))
    obj_y_range = list(range(obj_y, obj_h))
    # 격자 한 칸과 타겟의 x,y좌표 겹치는 것 찾기
    intersect_x = [value for value in obj_x_range if value in x_range]
    intersect_y = [value for value in obj_y_range if value in y_range]

    if len(intersect_x) >= grid_w/1.5 and len(intersect_y) >= grid_h/2:
        return True
    else:
        return False

################################
# 함수명    : emptyseat_in_grid
# 작성자    : 이현지
# 설명      : 해당 격자 칸 안에 색상 분석으로 식별한 '빈 좌석 개체'가 존재하는지 판단한다
#            해당 칸의 면적의 1/36 이상 차지할 때,
#            '빈 좌석 개체'가 칸 안에 존재한다고 판단한다.
# 매개변수  : int x, y 검사할 그리드의 시작좌표
#             int obj_x, obj_y 검사할 개체의 시작 좌표
#             int obj_w, obj_h 검사할 개체의 너비, 높이
# 리턴     : boolean 값
################################
def emptyseat_in_grid(x, y, obj_x, obj_y, obj_w, obj_h):
    # 검사할 그리드의 좌표 범위
    x_range = set(range(x, x + grid_w + 1))
    y_range = set(range(y, y + grid_h + 1))
    # 검사할 개체의 좌표 범위
    obj_x_range = list(range(obj_x, obj_w))
    obj_y_range = list(range(obj_y, obj_h))
    # 그리드 한 칸과 타겟의 x,y좌표 겹치는 것 찾기
    intersect_x = [value for value in obj_x_range if value in x_range]
    intersect_y = [value for value in obj_y_range if value in y_range]

    if len(intersect_x) >= grid_w/6 and len(intersect_y) >= grid_h/6:
        return True
    else:
        return False

################################
# 함수명    : seat_collision
# 작성자    : 이현지
# 설명      : 각 격자의 한 칸 마다 차지된 좌석이 존재하는지, 빈 좌석이 존재하는지 확인한다
# 리턴      : _
# 매개변수  : table matrix 현재 화면 그리드, current state matrix
#             int save_x, save_y 쿠키 시작 위치
#             int save_w, save_h 쿠키 너비, 높이
################################
def seat_collision(matrix, occupied_list, empty_list):
    for ver in range(vertical_max):
        for hor in range(horizontal_max):
            # 1. 차지된 좌석 개체 리스트를 검사한다
            for i in occupied_list:
                if occupied_in_grid(grid_x + ver * grid_w, grid_y + hor * grid_h, i[0], i[1], i[0] + i[2], i[1] + i[3]):
                    #해당 되는 좌표 위치에 matrix 값을 업데이트 한다
                    matrix[hor][ver] = 2    # 차지한 좌석
            # 2. 빈 좌석 개체 리스트를 검사한다
            for i in empty_list:
                if emptyseat_in_grid(grid_x + ver * grid_w, grid_y + hor * grid_h, i[0], i[1], i[0] + i[2], i[1] + i[3]):
                    matrix[hor][ver] = 1    # 빈 좌석

################################
# 함수명    : fill_grid
# 작성자    : 이현지
# 설명      : 각 격자 칸에 해당하는 속성에 따라 구분하여 색 칠하기
#            PC방 state 정보는 matrix에 축약되어 있고, 이 matrix 값을 기준으로 좌석 속성을 구분한다.
# 리턴      : _
# 매개변수  : PC방 배치도 image
#            PC방 좌석 state를 표현한 matrix
################################
def fill_grid(image, matrix):
    for ver in range(vertical_max):
        for hor in range(horizontal_max):
            if matrix[hor][ver] is 2:
                image[grid_y + grid_h * hor: grid_y + grid_h * (hor + 1),
                grid_x + grid_w * ver: grid_x + grid_w * (ver + 1)] = (150, 10, 10)
            elif matrix[hor][ver] is 1:
                image[grid_y + grid_h * hor: grid_y + grid_h * (hor + 1),
                grid_x + grid_w * ver: grid_x + grid_w * (ver + 1)] = (30, 30, 200)
            elif matrix[hor][ver] is 0:
                image[grid_y + grid_h * hor: grid_y + grid_h * (hor + 1),
                grid_x + grid_w * ver: grid_x + grid_w * (ver + 1)] = (100, 100, 100)
