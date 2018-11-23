# -*- coding: UTF-8 -*-

import cv2
import numpy as np

def histogram(image, t, w, h):
    mhist = []

    #세로 -> 가로 히스토그램
    if(t == 0):
        # 90도 회전 - 가로, 세로 사이즈 반전 일어남
        img = np.rot90(image)

        #현재 img의 세로 size (for문 돌리기 위함)
        size = np.size(img, 0)
        #mhist = np.zeros((size, 1), dtype="uint8")


    #가로: 원본 이미지 -> 세로 히스토그램
    else:
        img = image
        size = np.size(img, 0)
        #mhist = np.zeros((size, 1), dtype="uint8")

    #count nonzero value
    max = -100
    for j in range(size):
        v = cv2.countNonZero(img[j])
        #mhist[j] = v
        mhist.append(v)
        if(v > max):
            max = v

    #원본 이미지의 경우: 세로 히스토그램 생성
    if(t == 1):
        width = max
        height = h
        histo = np.zeros((height, width, 1), dtype = "uint8")

        for i in range(height):
            data = mhist[i]
            for j in range(width):
                if(data == 0):
                    break
                else:
                    histo[i][j] = 255
                data -= 1

    #90도 회전 이미지의 경우: 가로 히스토그램 생성
    else:
        width = w
        height = max
        hist = np.zeros((height, width, 1), dtype="uint8")
        
        for j in range(width):
            data = mhist[j]
            for i in range(height-1, -1, -1):
                if(data == 0):
                    break
                else:
                    hist[i][j] = 255
                data -= 1

        histo = cv2.flip(hist, 1)
        mhist.reverse()

    return histo, mhist

'''
image = cv2.imread('pcroom2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
h, w = image.shape[:2]
cv2.line(image,
             (11, 0),
             (11, h),
             (255, 255, 255), 2, 1)
cv2.imshow("image", image)

ret, thresh = cv2.threshold(gray, 18, 255, cv2.THRESH_BINARY)

hist_w, mhist_w = histogram(thresh, 0, w, h) # height
hist_h, mhist_h = histogram(thresh, 1, w, h ) # width


cv2.imshow("image", image)
cv2.imshow("thresh", thresh)
cv2.imshow("hist1", hist_w)
cv2.imshow("hist2", hist_h)

print(mhist_w)
print(mhist_h)

key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
'''