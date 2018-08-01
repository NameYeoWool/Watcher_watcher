import cv2
from seat_detect import Color_detect as cd

#전역변수 선언
unit = 60                               # 그리드 한 칸(정사각형)의 길이
unit2 = 55
vertical_max, horizontal_max = 12, 8   # 가로 12칸, 세로 8칸
grid_x, grid_y = 10, 0                  # 그리드의 시작지점. 변수 초기화

#그리드 그리는 함수
def draw_grid(image):
    global unit, unit2

    # 그리드 가로선 그리기
    for ver in range(vertical_max + 1):
        cv2.line(image,
                 (grid_x + unit * ver, grid_y),
                 (grid_x + unit * ver, grid_y + unit * horizontal_max),
                 (255, 0, 0), 2, 1)

    # 그리드 세로선 그리기
    for hor in range(horizontal_max + 1):
        cv2.line(image,
                 (grid_x, grid_y + unit2 * hor),
                 (grid_x + unit2 * vertical_max, grid_y + unit2 * hor),
                 (255, 0, 0), 2, 1)
    '''
    cv2.imshow("grid", image)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()
    '''
    return image

#이미지에서 색상 분석하기

#분석한 색상 결과를 바탕으로 그리드 칠하기

#입력된 그리드 안에 개체가 존재하는가 판단
#존재의 판단 기준-그리드 1/16
def in_grid(x, y, obj_x, obj_y, obj_w, obj_h):
    # 검사할 그리드의 좌표 범위
    x_range = set(range(x, x + unit + 1))
    y_range = set(range(y, y + unit2 + 1))
    # 검사할 개체의 좌표 범위
    obj_x_range = list(range(obj_x, obj_w))
    obj_y_range = list(range(obj_y, obj_h))
    # 그리드 한 칸과 타겟의 x,y좌표 겹치는 것 찾기
    intersect_x = [value for value in obj_x_range if value in x_range]
    intersect_y = [value for value in obj_y_range if value in y_range]

    if len(intersect_x) >= unit/4 and len(intersect_y) >= unit2/4:
        return True
    else:
        return False

def seat_collision(matrix, detect_list):
    # 그리드 한 칸마다 seat가 있는지 확인하기
    for ver in range(vertical_max):
        for hor in range(horizontal_max):
            for i in detect_list:
                if in_grid(grid_x + ver * unit, grid_y + hor * unit2, i[0], i[1], i[0] + i[2], i[1] + i[3]):
                    if(100< i[4] < 200):
                        matrix[hor][ver] = 0 # 좌석
                    elif(i[4]<2000):
                        matrix[hor][ver] = 1 # 차지한 좌석
                    else:
                        matrix[hor][ver] = 3

def fill_grid(image, matrix):
    for ver in range(vertical_max):
        for hor in range(horizontal_max):
            if matrix[hor][ver] is 0:
                image[grid_y + unit2 * hor: grid_y + unit2 * (hor + 1),
                grid_x + unit * ver: grid_x + unit * (ver + 1)] = (170, 100, 69)
            if matrix[hor][ver] is 1:
                image[grid_y + unit2 * hor: grid_y + unit2 * (hor + 1),
                grid_x + unit * ver: grid_x + unit * (ver + 1)] = (170, 69, 100)
            if matrix[hor][ver] is 3:
                image[grid_y + unit2 * hor: grid_y + unit2 * (hor + 1),
                grid_x + unit * ver: grid_x + unit * (ver + 1)] = (100, 170, 69)

'''
#해당 결과를 리스트로 표현하기
image=cv2.imread('pcroom.jpg')
matrix = [[0] * 12 for i in range(8)]

cd.detect_seat(image)
seat_collision(matrix, cd.detect_list)
for i in range(8):
    for j in range(12):
        value = matrix[i][j]
        print(value, end='   ')
    print()


draw_grid(image)
fill_grid(image, matrix)
'''