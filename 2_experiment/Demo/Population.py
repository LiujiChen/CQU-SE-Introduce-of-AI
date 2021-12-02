import random
import cv2
import numpy

from copy import deepcopy
from numpy import *


# 用于初始化一个种群(生成个体的染色体)
def createPopulation(population_size, chromosome_length):
    population_chromosome = []
    for i in range(population_size):
        chromosome = []
        for j in range(chromosome_length):
            chromosome.append(random.randint(0, 2))
        population_chromosome.append(chromosome)
    return population_chromosome


# 解码: 染色体(基因型)->性状(表现型)
def decode(population_chromosome, chromosome_length):
    population_grey = []
    for i in range(len(population_chromosome)):
        grey = 0
        for j in range(chromosome_length):
            grey = grey + 2 ** (chromosome_length - j - 1) * population_chromosome[i][j]
        population_grey.append(grey)
    return population_grey


# 大津算法, 计算类间方差
def Otsu(grey, image):
    front = []
    background = []
    for i in image:
        for j in i:
            if j > grey:
                front.append(j)
            else:
                background.append(j)

    front = numpy.array(front)
    background = numpy.array(background)

    # 处理异常情况， 即thresh阈值极其不合理，将图片只分为一类
    if len(front) != 0:
        mean_front = mean(front)
    else:
        mean_front = 0
        front = image
    if len(background) != 0:
        mean_background = mean(background)
    else:
        mean_background = 0
        background = image

    # 试试看这样会不会计算溢出
    possibility_product = front.size * background.size / (image.size * image.size)
    means_square = (mean_front - mean_background) ** 2

    variance = possibility_product * means_square
    return variance


# 计算种群里，每个个体的适应度
def calculateFitness(population_chromosome, chromosome_length):
    # 读取灰度图片
    image = cv2.imread('../Data/data.png', cv2.IMREAD_GRAYSCALE)

    # 解码获得个体的表现型: 灰度
    population_grey = decode(population_chromosome, chromosome_length)

    population_fitness = []

    for i in population_grey:
        population_fitness.append(Otsu(i, image))

    return population_fitness


# 找到一代个体中，表现最优的个体
def bestGeneration(population_fitness, population_chromosome):
    fitness = deepcopy(population_fitness)
    fitness.sort(reverse=True)
    best_fitness = fitness[0]
    index = population_fitness.index(best_fitness)
    best_chromosome = population_chromosome[index]
    best_grey = 0
    for i in range(len(best_chromosome)):
        best_grey = best_grey + best_chromosome[i] * 2 ** (len(best_chromosome) - i - 1)
    return best_grey, best_chromosome, best_fitness


def creatRoulette(population_fitness):
    sum_fitness = 0
    for i in population_fitness:
        sum_fitness = sum_fitness + i
    fitness = population_fitness
    fitness.sort()
    roulette = [fitness[0] / sum_fitness]
    for i in range(1, len(population_fitness)):
        roulette.append(roulette[i - 1] + fitness[i] / sum_fitness)
    return roulette


# 自然选择作用
def select(population_chromosome, population_fitness):
    # 轮盘赌选择
    roulette = creatRoulette(population_fitness)

    # 生成轮盘赌的选择概率
    possibility_select = []
    for i in range(len(population_chromosome)):
        possibility_select.append(random.random())
    possibility_select.sort()

    leave = 0  # 留到下一代去的基因
    newin = 0  # 选择
    next_generation_chromosome = deepcopy(population_chromosome)

    while newin < len(population_chromosome):
        if possibility_select[newin] < roulette[leave]:
            next_generation_chromosome[newin] = population_chromosome[leave]
            newin = newin + 1
        else:
            leave = leave + 1
    return next_generation_chromosome


# 种群交配，产生下一代
def crossOver(population_chromosome, chromosome_length, crossover_possibility):
    crossover_chromosome = deepcopy(population_chromosome)
    for i in range(len(crossover_chromosome) - 1):
        if random.random() < crossover_possibility:
            crosspoint = random.randint(0, chromosome_length - 1)
            temp1_chromosome_length = []
            temp2_chromosome_length = []
            temp1_chromosome_length.extend(population_chromosome[i][0:crosspoint])
            temp1_chromosome_length.extend(population_chromosome[i + 1][crosspoint:chromosome_length])
            temp2_chromosome_length.extend(population_chromosome[i + 1][0:crosspoint])
            temp2_chromosome_length.extend(population_chromosome[i][crosspoint:chromosome_length])
            crossover_chromosome[i] = temp1_chromosome_length
            crossover_chromosome[i + 1] = temp2_chromosome_length
    return crossover_chromosome


# 以一定几率变异
def mutate(population_chromosome, chromosome_length, mutate_possibility):
    mutate_population = deepcopy(population_chromosome)
    for i in range(len(mutate_population)):
        if random.random() < mutate_possibility:
            mutate_point = random.randint(0, chromosome_length - 1)
            if mutate_population[i][mutate_point] == 1:
                mutate_population[i][mutate_point] = 0
            else:
                mutate_population[i][mutate_point] = 1
    return mutate_population


if __name__ == '__main__':
    populations_chromosome = createPopulation(10, 8)
    populations_grey = decode(populations_chromosome, 8)
    print('populations_chromosome:')
    print(populations_chromosome)
    print('populations_grey:')
    print(populations_grey)
    populations_fitness = calculateFitness(populations_chromosome, 8)
    print('populations_fitness:')
    print(populations_fitness)
    _best_grey, _best_chromosome, _best_fitness = bestGeneration(populations_fitness, populations_chromosome)
    print('best_grey, best_chromosome, best_fitness:')
    print(_best_grey, _best_chromosome, _best_fitness)
    print('validate:')
    _image = cv2.imread('../Data/data.png', cv2.IMREAD_GRAYSCALE)
    print(Otsu(_best_grey, _image))
    next_generations_chromosome = select(populations_chromosome, populations_fitness)
    print('next_generation_chromosome:')
    print(next_generations_chromosome)
    crossover_populations = crossOver(next_generations_chromosome, 8, 0.6)
    print('crossover_populations')
    print(crossover_populations)
    mutate_populations = mutate(crossover_populations, 8, 0.05)
    print('mutate_populations:')
    print(mutate_populations)
