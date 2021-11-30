import argparse

from Demo.Astar import Astar
from Demo.BFS import BFS
from Demo.DFS import DFS


def parse_args():
    parser = argparse.ArgumentParser(description='Find the shortest path')
    parser.add_argument('-m', '--method', type=str, default="Astar", help='method name:(DFS, BFS, Astar)')
    parser.add_argument('-s', '--start', type=str, default="Arad", help='start city')
    parser.add_argument('-e', '--end', type=str, default="Bucharest", help='end city')
    return parser.parse_args()


if __name__ == '__main__':
    p_args = parse_args()
    print("choose the run model: A:args, B:input")
    model = input()
    if model == 'A':
        if p_args.method == "DFS":
            DFS(p_args.start, p_args.end)
        elif p_args.method == "BFS":
            BFS(p_args.start, p_args.end)
        elif p_args.method == "Astar":
            Astar(p_args.start, p_args.end)
        else:
            raise ValueError("Unrecognized method {}".format(p_args.task))
    elif model == 'B':
        print("please input the method that find the shortest path (DFS, BFS, Astar)")
        method = input()
        print("please input the start city")
        start = input()
        print("please input the goal city")
        end = input()
        if method == "DFS":
            DFS(start, end)
        elif method == "BFS":
            BFS(start, end)
        elif method == "Astar":
            Astar(start, end)
        else:
            raise ValueError("Unrecognized method {}".format(method))