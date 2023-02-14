import matplotlib.pyplot as plt

def plot_update(x_axis,y_axis:list, sleep=1.0) -> None:
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1, = ax.plot(x_axis,y_axis[0],"b-")
    for i in range(len(y_axis)):
        line1.set_ydata(y[i])
        plt.pause(1)



if __name__ == "__main__":
    import numpy as np
    x = np.arange(-10,10,0.01)
    y = []
    for phase in np.linspace(0,10*np.pi,100):
        y.append([np.sin(i+phase) for i in x])
    plot_update(x,y,sleep=0.1)