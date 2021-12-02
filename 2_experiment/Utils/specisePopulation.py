import random

from Utils.speciesIndividual import Individual


def creatRoulette(selectp):
    temp = selectp
    temp.sort()
    s = [1]
    s[0] = temp[0]
    for i in range(0, len(selectp)):
        if i > 0:
            s[i] = s[i - 1] + temp[i]
    return s


class Population:

    def __init__(self, popSize=50, pc=0.6, pm=0.01):
        self.popSize = popSize
        self.pops = self.InitPop()
        self.pcrossover = pc
        self.pmutate = pm
        self.generationbest = []

    def InitPop(self):
        pops = []
        for i in range(self.popSize):
            pops.append(Individual())
        return pops

    def Select(self):
        fits = 0
        for i in self.pops:
            fits = fits + i.fitness

        selectp = []
        for i in range(len(self.pops)):
            selectp.append(self.pops[i].fitness / fits)

        roulette = []
        roulette = creatRoulette(selectp)

        ms = []
        for i in range(len(self.pops)):
            ms.append(random.random())
        ms.sort()

        newpops = self.pops
        fitin = 0
        newin = 0
        while newin < len(self.pops):
            if (ms[newin] < roulette[fitin]):
                newpops[newin] = self.pops[fitin]
                newin = newin + 1
            else:
                fitin = fitin + 1

        self.pops = newpops
