import random
import numpy as np
from polymino import place,placeQ,remove,right_coord,status
n1,m1 = 4,6
grid =[ [0] * m1 for _ in range(n1) ]
base = [
    [[1]],[[1,1]],[[1,1,1]],[[1,1,1,1]],
    [[1],[1]],[[1],[1],[1]],[[1],[1],[1],[1]],
    [[1,1],[0,1]],[[0,1,0],[1,1,1]],[[1,0,0],[1,1,1]]
] #figures
all_points = [[i,j] for i in range(n1) for j in range(m1)]
print(all_points)
figs = []
ir=0

def right_crd(n,m,coords):
    for i in coords:
        if 0<=i[0]<n and 0<=i[1]<m:
            pass
        else:
            return False
    return True


while not status(grid):
    print("-----------------------------------------------")
    tmp_fig = random.choice(base)
    print("chosen figure")
    print(tmp_fig)
    place_points = []
    tmp = all_points[0]
    print("center")
    print(tmp)
    filled_pts = [np.array(tmp) + np.array([i, j]) for i in range(len(tmp_fig)) for j in range(len(tmp_fig[0]))]
    print("points recta")
    print(filled_pts)
    for ind in filled_pts:
        abs_pnt = np.array(ind) - np.array(tmp)
        # print(absolute_point)
        #print("ind")
        #print(ind)
        if tmp_fig[abs_pnt[0]][abs_pnt[1]] == 1:
            place_points.append(list(ind))

    print("znachimie points recta")
    print(place_points)
    if right_crd(n1,m1,place_points):
        print("enter")
        if placeQ(grid,place_points):
            grid = place(grid,place_points,1)

                #all_points = [i for i in all_points if i not in place_points]
            for i in place_points:
                all_points.remove(list(i))

            print("all centres after placa")
            print(all_points)
            figs.append(tmp_fig)

print("pole")
print(grid)
print(figs)


