import matplotlib.pyplot as pyplot
import matplotlib.animation as animation
import random as r

fig = pyplot.figure()
ax1 = fig.add_subplot(111)


def newData():
    f = open("data.txt", "w")
    for i in range(100):
        waarde = str(i)+","+str(r.randint(0, 1000)+"\n")
        f.write(waarde)


def refreshGraphData(i):
    print("Refreshing data...")
    graphData = open("data.txt", "r").read()
    lines = graphData.split("\n")
    xValues = []
    yValues = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(",")
            xValues.append(x)
            yValues.append(y)
    ax1.clear()
    ax1.plot(xValues, yValues)


ani = animation.FuncAnimation(fig, refreshGraphData, interval=1000)
pyplot.show()
