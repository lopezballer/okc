import pandas as pd
import numpy as np

data = open("shots_data.csv", "r").read()
data = data.split("\n")
data.pop(0)


three_pts = []
two_pts = []

for i in range(len(data)):
    data[i] = data[i].split(",")

for pt in range(len(data)):
    for i in range(len(data[pt])):
        data[pt][i] = float(data[pt][i])


for data_pts in range(len(data)):
    x = data[data_pts][0]
    y = data[data_pts][1]
    z = data[data_pts][2]
    if (-22.0 <= x <= 22.0 and 0 <=  y <= 14.0) or (y > 14 and (x**2 + y**2)**0.5 < 23.75):
        two_pts.append(z)
    else:
        three_pts.append(z)



print("2 pointer fg:", (sum(two_pts)/len(two_pts)) * 100, " %")
print("3 pointer fg:", (sum(three_pts)/len(three_pts)) * 100, " %")