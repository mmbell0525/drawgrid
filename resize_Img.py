#1 加载缩放的图片
import cv2
img = cv2.imread('step6/fixedImg.jpg',1)

#2 获取图片信息
imgInfo = img.shape
print(imgInfo)#打印出图片的宽、高
# 图片的高、宽
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]

# 放大 缩小 / 等比例 非等比例
# 等比例缩小
# 乘的系数是相同的就是等比例的
dstHeight = int(height*20/15)
dstWidth = int(width*20/15)

# 最近临域插值 双线性插值 像素关系重采样 立方插值
# 3 调用resize方法?是上面哪种方法？
dst = cv2.resize(img,(dstWidth,dstHeight))

# 4 最终的效果图
# cv2.imshow('image',dst)
# cv2.waitKey(0)
cv2.imwrite('step6/11fixedImg.jpg',dst)

