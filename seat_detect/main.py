import cv2
import numpy as np
from seat_detect import Color_detect as cd, grid as g


def main():
    image = cv2.imread('pcroom.jpg')
    cv2.imshow("image", image)
    matrix = [[0] * 12 for i in range(8)]

    cd.detect_seat(image)

    print(cd.detect_list)

    g.seat_collision(matrix, cd.detect_list)

    #g.fill_grid(image, matrix)
    g.draw_grid(image)

    for i in range(8):
        for j in range(12):
            value=matrix[i][j]
            print(value, end='   ')
        print()

    cv2.imshow('seat_analyze', image)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()

main()