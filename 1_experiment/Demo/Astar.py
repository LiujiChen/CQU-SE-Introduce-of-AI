import heapq
import math
from queue import PriorityQueue

from Demo.LoadData import load_data


def showCurrentInfo(used, temp, node):
    print("***********************************************************************************************************")
    print("current node is {}".format(node))
    print("current close list :", end="")
    for i in used:
        print(i + " ", end="")
    print()
    print("current open list :", end="")
    for i in temp:
        print(i + " ", end="")
    print()


def h(locations, node, end, name_dic):
    node_x_y = locations[name_dic[node]]
    end_x_y = locations[name_dic[end]]
    _h = pow(int(end_x_y[0]) - int(node_x_y[0]), 2) + pow(int(end_x_y[1]) - int(node_x_y[1]), 2)
    return pow(_h, 0.5)


def Astar(start, end):
    adj, locations, name_dic, int_dic = load_data()
    print("find the shortest path connects {} and {} by Astar".format(start, end))
    frontier = PriorityQueue()
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    closelist = []
    openlist = []
    while len(frontier) > 0:
        _cur = heapq.heappop(frontier)
        cur = _cur[1]
        closelist.append(cur)
        if cur in openlist:
            openlist.remove(cur)
        showCurrentInfo(closelist, openlist, cur)
        if cur == end:
            break

        for i in range(len(adj[0])):
            if adj[name_dic[cur]][i] != 0:
                new_cost = cost_so_far[cur] + adj[name_dic[cur]][i]
                if (int_dic[i] not in cost_so_far) or (new_cost < cost_so_far[int_dic[i]]):
                    openlist.append(int_dic[i])
                    cost_so_far[int_dic[i]] = new_cost
                    heapq.heappush(frontier, (new_cost + h(locations, int_dic[i], end, name_dic), int_dic[i]))
                    came_from[int_dic[i]] = cur

    print("***********************************************************************************************************")
    if came_from[end] is None:
        print("there is no path can connect {} and {}".format(start, end))
        return

    node = end
    nodelist = [end]
    while came_from[node] is not None:
        node = came_from[node]
        nodelist.append(node)
    nodelist = nodelist[::-1]
    print("the shortest distance is {}".format(cost_so_far[end]))
    for i in range(len(nodelist)):
        if i != len(nodelist) - 1:
            print("{}->".format(nodelist[i]), end="")
        else:
            print("{}".format(nodelist[i]))

