import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw =RandomWalk(50000)
    rw.fill_walk()
    num_p = list(range(rw.num_point))
    plt.scatter(rw.x,rw.y,s=1,c=num_p,cmap=plt.cm.Blues,edgecolors='none')
    plt.scatter(rw.x[0],rw.y[0],c='green',edgecolors='none',s=100)
    plt.scatter(rw.x[-1],rw.y[-1],c='red',edgecolors='none',s=100)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_run = input("make another walk?(y/n):")
    if keep_run=='n':
        break
