import os
from numpy import *
import numpy as np
import cv2

save_path = 'step5/'
u = 1433
v = 635
pts = loadtxt(save_path + "xy_alongWall.txt",dtype = int)
print(pts)
src_pts = pts[:,:2]
# print(tuple(src_pts[0]))
# print(src_pts[1])
dst_pts = pts[:,2:]
# print(dst_pts)
img = cv2.imread(save_path +"11fixedImg.jpg")
for i in range(0,12):
	# print(src_pts[i][0])
	src_u = u + (src_pts[i][0]-1) *80
	src_v = v + (src_pts[i][1]-1) *80
	dst_u = u + (dst_pts[i][0]-1) *80
	dst_v = v + (dst_pts[i][1]-1) *80
	print(src_u,src_v)
	worldXY = str((src_pts[i][0]-1) *80)+ ' ' + str((src_pts[i][1]-1) *80) + ' ' + str((dst_pts[i][0]-1) *80) + ' '+  str((dst_pts[i][1]-1) *80)
	print(worldXY)
	file = open(save_path +"worldXY_alongWall.txt","a")
	file.write(worldXY + '\n')
	file.close()
	img = cv2.line(img,(int(src_u),int(src_v)),(int(dst_u),int(dst_v)),(255,0,255),8)
	# cv2.namedWindow("change",cv2.WINDOW_NORMAL)
	# cv2.imshow("change", img)
	# cv2.waitKey(1000)
cv2.imwrite(save_path +"image_alongWall.jpg",img)