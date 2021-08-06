import matplotlib.pyplot as plt
x = list(range(1,1001))
y= [i**2 for i in x]

plt.scatter(x,y,s =10,edgecolors='none',c=y,cmap=plt.cm.Blues)
plt.title("square number",fontsize = 24)
plt.xlabel("value",fontsize = 14)
plt.ylabel("square of value",fontsize = 14)

plt.tick_params(axis='both',which = 'major',labelsize =14)

plt.savefig('squares_plot.png',bbox_inches='tight')
plt.show()