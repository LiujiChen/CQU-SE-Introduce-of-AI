import random
import cv2
import numpy

from numpy import *


def loadImage():
    img_src = cv2.imread('../Data/data.png')
    img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    return img_gray


class Individual:

    def __init__(self):
        # 随机获得个体的初始灰度
        self.grey = random.randint(0, 255)
        self.code = self.getCode()
        self.fitness = self.getFitness()

    def getFitness(self):
        # 获得灰度处理后的图片数组
        img = loadImage()

        front = []
        background = []

        for i in img:
            for j in i:
                if j < self.grey:
                    background.append(i)
                else:
                    front.append(i)

        front = numpy.array(front)
        background = numpy.array(background)

        mf = mean(front)
        mb = mean(background)

        fit = front.size * background.size * (mf - mb) * (mf - mb) / (img.size * img.size)
        return fit

    def getCode(self):
        code = [0, 0, 0, 0, 0, 0, 0, 0]
        grey = self.grey
        for i in range(8):
            code[7 - i] = int(grey % 2)
            grey = grey / 2
        return code

    def getGrey(self):
        grey = 0
        for i in range(len(self.code)):
            grey = grey + self.code[i]*2**(7-i)
        return grey

    def Mutation(self):
        # 使用均匀变异
        m = random.randint(0, 7)
        if self.code[m] == 1:
            self.code[m] = 0
        else:
            self.code[m] = 1
        self.grey = self.getGrey()
        self.fitness = self.getFitness()




