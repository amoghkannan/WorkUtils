import numpy as np
from matplotlib import pyplot as plt

x=np.linspace(-1.0,1.0,num=20)
y=np.linspace(-1.0,1.0,num=20)

fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xticks(x)
ax.set_yticks(y)
ax.grid()
plt.xlim(-1.0,1.0)
plt.ylim(-1.0,1.0)
ax.tick_params(
    axis='both',       # Apply to both x and y axes
    which='both',      # Apply to major and minor ticks
    bottom=False,      # Turn off bottom ticks
    top=False,         # Turn off top ticks
    left=False,        # Turn off left ticks
    right=False,        # Turn off right ticks
    labelbottom=False,
    labelleft=False
)

coords=[]

def onclick(event):
        ix,iy=event.xdata,event.ydata
        print(ix,iy)
        global coords
        coords.append((ix,iy))
        if(len(coords)==1):
                ax.scatter(ix,iy)
        else:
                ax.plot([coords[-2][0],coords[-1][0]],[coords[-2][1],coords[-1][1]],"k")
        
        plt.show()

cid=fig.canvas.mpl_connect("button_press_event",onclick)
plt.show()
