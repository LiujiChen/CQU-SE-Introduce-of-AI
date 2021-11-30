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

def DFS(start, end):
    adj, locations, name_dic, int_dic = load_data()
    print("find the shortest path connects {} and {} by DFS".format(start, end))
    distance = init_distance(start, name_dic)
    stack = [start]
    parent = {start: None}
    closelist = []

    while len(stack) > 0:
        cur = stack.pop()
        closelist.append(cur)
        for i in range(len(adj[0])):
            if adj[name_dic[cur]][i] != 0:
                if distance[cur]+adj[name_dic[cur]][i] < distance[int_dic[i]]:
                    stack.append(int_dic[i])
                    distance[int_dic[i]] = distance[cur]+adj[name_dic[cur]][i]
                    parent[int_dic[i]] = cur
        showCurrentInfo(closelist, stack, cur)

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