from copy import deepcopy

import cv2
import numpy

from Demo.Population import createPopulation, calculateFitness, bestGeneration, select, crossOver, mutate


def GeneticAlgorithm(_population_size=16, _mutate_possibility=0.05, _crossover_possibility=0.6, _generations=10):
    population_size = _population_size  # 种群大小
    chromosome_length = 8  # 染色体长度, [0, 255], 所以八位二进制就够了
    mutate_possibility = _mutate_possibility  # 变异概率
    crossover_possibility = _crossover_possibility  # 交配概率
    generations = _generations  # 种群进化代数
    generations_best = []  # 每一代中的最优个体
    population_fitness = []  # 适应度

    # 初始化种群
    population_chromosome = createPopulation(population_size, chromosome_length)

    # 遗传进化
    for i in range(generations):
        print('current generation is {}'.format(i))
        print('current population_chromosome is:')
        print(population_chromosome)
        print('-----------------------------------------------------------------------------------------')
        population_fitness = calculateFitness(population_chromosome, chromosome_length)
        best_grey, best_chromosome, best_fitness = bestGeneration(population_fitness, population_chromosome)
        generations_best.append([best_fitness, best_grey, best_chromosome])
        population_chromosome = select(population_chromosome, population_fitness)
        population_chromosome = crossOver(population_chromosome, chromosome_length, crossover_possibility)
        population_chromosome = mutate(population_chromosome, chromosome_length, mutate_possibility)

    print('-----------------------------------------------------------------------------------------')
    generations_best.sort(reverse=True)
    print('the best individual is:')
    print(generations_best[0])
    return generations_best[0][1]


def binaryzation(image, grey):
    images = []
    for i in image:
        temp = []
        for j in i:
            if j < grey:
                temp.append(0)
            else:
                temp.append(255)
        images.append(temp)
    return numpy.array(images, dtype=numpy.uint8)


if __name__ == '__main__':
    best_grey = GeneticAlgorithm()
    image = cv2.imread('../Data/data.png')
    image_grey = cv2.imread('../Data/data.png', cv2.IMREAD_GRAYSCALE)
    print(image_grey)
    image_binary = binaryzation(image_grey, 103)
    print(image_binary)
    cv2.imshow('binary', image_binary)
    cv2.imshow('origin', image)
    cv2.waitKey()
