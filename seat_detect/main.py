import cv2
from seat_detect import Color_detect as cd, grid as g

def main_():
    ################################
    # 분석할 이미지   : PC방의 좌석 배치도
    ################################

    # image 읽어들이기
    image = cv2.imread('pcroom.jpg')
    cv2.imshow("image", image)

    ################################
    # 이미지 분석 전 필요한 변수 초기화
    ################################

    # PC방 배치도의 state 표현하는 matrix 정의
    # 현재 예시 이미지의 경우 11*6 사이즈의 배열이다
    matrix = [[0] * 11 for i in range(6)]

    ################################
    # 이미지 색상 분석
    ################################
    cd.detect_seat(image)

    # (색상 분석으로 검출된 개체 리스트 출력)
    #print(cd.occupied_list)
    #print(cd.empty_list)

    ################################
    # 격자 내 개체 존재 여부 판별 및 격자 그리기
    ################################

    # 격자 칸 안에 개체 리스트가 존재하는지 확인
    g.seat_collision(matrix, cd.occupied_list, cd.empty_list)

    # 격자 그리기
    g.fill_grid(image, matrix)
    g.draw_grid(image)

    ################################
    # 격자 state 표현하는 matrix 출력
    ################################

    for i in range(g.horizontal_max):
        for j in range(g.vertical_max):
            value=matrix[i][j]
            print(value, end='   ')
        print()

    ################################
    # 최종 분석 결과 이미지 출력
    ################################

    cv2.imshow('seat_analyze', image)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()

main_()