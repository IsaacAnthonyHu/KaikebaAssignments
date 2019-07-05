# KaikebaAssignments

第一次写REAMME，不知道该怎么写，请见谅哈
作业里写了一个Image的类，拥有以下几个函数

## image_crop(self, width_range, height_range):
该函数对图像进行裁切，输入参数为小数形式的长宽百分比位置，例如：
Image.crop((0.1, 0.5), (0.1, 0.5))
则会裁切原图像长宽各位于原图10%至50%的部分

## color_shift(self):
该函数对图像进行随机的颜色偏移

## gamma_correction(self, gamma=2.2):
该函数对输入图像的gamma值进行校正，默认gamma值为2.2

## rotate（self, rotate_center, rotate_degree, scale_very):
将图片进行旋转
rotate_center 指定旋转中心小数形式百分比坐标，例：(0.5,0.5)为图像中心
rotate_degree 指定旋转角度
scale_vary 指定旋转后图片本身的缩放程度,例如：
Image.rotate((0.5, 0.5), 30, 1)

## random_affine_transform(self):
对图片进行随机的仿射变换

## random_perspective_transform(self):
对图片进行随机的透视变换
