import cv2
import random
import numpy as np

class Image():

	def __init__(self, image_path, image_name='default'):
		"""
		image_path 为文件路径
		image_name 为文件名称
		"""
		self.name = image_name
		self.path = image_path
		self.image = cv2.imread(image_path)
		self.height = self.image.shape[0]
		self.width = self.image.shape[1]
	
	def image_crop(self, width_range, height_range):
		"""
		width_range 需裁切的宽度范围（小数），例如:(0.1,0.5)
		height_range 同上，需裁切的高度范围
		"""
		width_pixels = (np.array(width_range)*self.width).astype('int')
		height_pixels = (np.array(height_range)*self.height).astype('int')
		img_crop = self.image[height_pixels[0]:height_pixels[1], width_pixels[0]:width_pixels[1]]
		return img_crop

	def color_shift(self):
		"""
		颜色偏移
		"""
		random_shift = random.randint(-50,50)
		self.image = (self.image + random_shift).astype('uint8')
		self.image[self.image > 255] = 255
		self.image[self.image < 0] = 0
		return self.image

	def gamma_correction(self, gamma=2.2):
		"""
		将图片的客观灰度转化为人类观察的主观灰度
		主观灰度 = 客观灰度^(1/gamma)
		"""
		invert_gamma = 1/gamma
		table = [((i/255.0)**invert_gamma) * 255 for i in range(256)]
		# 将每个客观灰度转化为主观灰度对照表(值范围仍然不变，为256）
		table = np.array(table).astype('uint8')
		return cv2.LUT(self.image, table)
	
	def rotate(self, rotate_center, rotate_degree, scale_vary):
		"""
		将图片进行旋转
		rotate_center 指定旋转中心百分比坐标，例：(0.5,0.5)为图像中心
		rotate_degree 指定旋转角度
		scale_vary 指定旋转后图片本身的缩放程度
		after_shape 指定旋转后图片本身的大小，默认旋转前图片大小
		"""
		rotate_matrix = cv2.getRotationMatrix2D((int(rotate_center[0]*self.width),int(rotate_center[1]*self.height)), rotate_degree, scale_vary)
		image_rotated = cv2.warpAffine(self.image, rotate_matrix, (self.width,self.height))
		return image_rotated

	def random_affine_transform(self):
		"""
		随机仿射变换
		"""
		pts1 = np.float32([[0,0], [self.width-1, 0], [0, self.height-1]])
		pts2 = np.float32([[self.width*random.random(), self.height*random.random()], [self.width*random.random(), self.height*random.random()], [self.width*random.random(), self.height*random.random()]])
		affine_trans = cv2.getAffineTransform(pts1, pts2)
		
		dst = cv2.warpAffine(self.image, affine_trans, (self.width, self.height))
		return dst

	def random_perspective_transform(self):
		"""
		随机透视变换
		"""
		coord1 = [1,1]
		coord2 = [self.width-1, 1]
		coord3 = [self.width-1, self.height-1]
		coord4 = [1, self.height-1]
		
		random_delta = int(min(self.height,self.width)*0.3)

		coord5 = [random.randint(0,random_delta), random.randint(0, random_delta)]
		coord6 = [self.width-1-random.randint(0, random_delta), random.randint(0, random_delta)]
		coord7 = [self.width-1-random.randint(0, random_delta), self.height-1-random.randint(0, random_delta)]
		coord8 = [random.randint(0, random_delta), self.height-1-random.randint(0,random_delta)]

		pts1 = np.float32([coord1, coord2, coord3, coord4])
		pts2 = np.float32([coord5, coord6, coord7, coord8])

		M = cv2.getPerspectiveTransform(pts1, pts2)
		img_perspective_transform = cv2.warpPerspective(self.image, M, (self.width, self.height))
		return img_perspective_transform
