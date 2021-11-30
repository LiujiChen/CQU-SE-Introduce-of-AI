import heapq
import math

from Demo.LoadData import load_data


def init_distance(start, name_dic):
    distance = {start: 0}
    for node in name_dic.keys():
        if node != start:
            distance[node] = math.inf
    return distance


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


def BFS(start, end):
    adj, locations, name_dic, int_dic = load_data()
    print("find the shortest path connects {} and {} by BFS".format(start, end))
    pq = []
    heapq.heappush(pq, (0, start))
    used = set()
    parent = {start: None}
    distance = init_distance(start, name_dic)
    while len(pq) > 0:
        pair = heapq.heappop(pq)
        dist = pair[0]
        node = pair[1]
        used.add(node)
        if node == end:
            break
        temp = []
        for i in range(len(adj[0])):
            if adj[name_dic[node]][i] != 0 and (int_dic[i] not in used):
                if (dist + adj[name_dic[node]][i]) < distance[int_dic[i]]:
                    temp.append(int_dic[i])
                    heapq.heappush(pq, (dist + adj[name_dic[node]][i], int_dic[i]))
                    parent[int_dic[i]] = node
                    distance[int_dic[i]] = dist + adj[name_dic[node]][i]
        showCurrentInfo(used, temp, node)
    print("***********************************************************************************************************")
    if parent[end] is None:
        print("there is no path can connect {} and {}".format(start, end))
        return
    print("the shortest distance is {}".format(distance[end]))
    nodelist = [end]
    cur = end
    while parent[cur] is not None:
        cur = parent[cur]
        nodelist.append(cur)
    nodelist = nodelist[::-1]
    for i in range(len(nodelist)):
        if i != len(nodelist) - 1:
            print("{}->".format(nodelist[i]), end="")
        else:
            print("{}".format(nodelist[i]))
