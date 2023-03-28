



import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# fig = plt.figure(figsize=(12, 10),dpi=80)
# ax = fig.add_subplot(111, projection='3d')


file = open("/home/star/Desktop/pose.txt")

points = []
cnt = 0
idx = []
for line in file:
    line = line.strip().split()
    if len(line) == 0:
        idx.append(cnt)
    if len(line) != 0:
        cnt = cnt+1
        if (float)(line[2]) < 300 or float(line[1]) > 55:
            points.append(line)

points = np.array(points,dtype=float)
idx = list(set(idx))
idx.sort()

# fig = plt.figure()
for i in range(len(idx)-1):

    X = points[idx[i]:idx[i + 1], 0]
    Y = points[idx[i]:idx[i + 1], 2]
    Z = points[idx[i]:idx[i + 1], 1]

    color = []
    for i in range(len(Z)):
        if float(Z[i]) > 60:
            color.append("red")
        else:
            color.append("green")

    # plt.ion()
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.view_init(elev=0)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_zlim(55, 200)
    ax.scatter(X, Y, Z, c=color)
    plt.show()
    # plt.pause(0.5)
