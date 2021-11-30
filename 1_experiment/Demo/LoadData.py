import numpy as np
from numpy import loadtxt


def load_data(path="../Data/"):
    print("Loading Graph data....")

    # load data from files
    with open("{}Node.csv".format(path), 'rt', encoding='UTF-8')as node_data:
        name_x_y = loadtxt(node_data, delimiter=',',
                           dtype=np.dtype(str))
    with open("{}Egde.csv".format(path), 'rt', encoding='UTF-8')as edge_data:
        name_name_weight = loadtxt(edge_data, delimiter=',',
                                   dtype=np.dtype(str))
    # deal data
    name = []
    locations = []
    for i in name_x_y:
        name.append(i[0])
        locations.append(i[1:])
    name_dic = {}
    int_dic = {}
    for i in range(len(name)):
        name_dic[name[i]] = i
        int_dic[i] = name[i]

    adj = np.zeros((len(name),len(name)))
    for i in name_name_weight:
        adj[name_dic[i[0]]][name_dic[i[1]]] = int(i[2])
    adj = adj+adj.T
    return adj, locations, name_dic, int_dic
