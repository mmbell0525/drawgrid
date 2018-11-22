import os
from numpy import *
import numpy as np
import cv2
# from sys import argv

# a,b,c = argv
save_path = 'step3/'
u = 943
v = 39
pts = loadtxt(save_path + "xy_grid.txt",dtype = int)
print(len(pts))
src_pts = pts[:,:2]
# print(tuple(src_pts[0]))
# print(src_pts[1])
dst_pts = pts[:,2:]
# print(dst_pts)
# img = cv2.imread(save_path + "image.png")
img = cv2.imread(save_path + "image_alongWall.png")
for i in range(0,len(pts)):
	# print(src_pts[i][0])
	src_u = u + (src_pts[i][0]-1) *80
	src_v = v + (src_pts[i][1]-1) *80
	dst_u = u + (dst_pts[i][0]-1) *80
	dst_v = v + (dst_pts[i][1]-1) *80
	worldXY = str((src_pts[i][0]-1) *80)+ ' ' + str((src_pts[i][1]-1) *80) + ' ' + str((dst_pts[i][0]-1) *80) + ' '+  str((dst_pts[i][1]-1) *80)
	print(worldXY)
	file = open(save_path + "worldXY_grid.txt","a")
	file.write(worldXY + '\n')
	file.close()
	img = cv2.line(img,(int(src_u),int(src_v)),(int(dst_u),int(dst_v)),(255,0,255),2)
	# cv2.namedWindow("change",cv2.WINDOW_NORMAL)
	# cv2.imshow("change", img)
	# cv2.waitKey(1000)
cv2.imwrite(save_path + "11image_grid.png",img)