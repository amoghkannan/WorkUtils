#Tool to generate IB lines for testing

import numpy as np
from matplotlib import pyplot as plt

nx=20
ny=20

x=np.linspace(-1.0,1.0,num=nx)
y=np.linspace(-1.0,1.0,num=ny)

fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_xticks(x)
ax.set_yticks(y)
ax.grid()
plt.xlim(-1.0,1.0)
plt.ylim(-1.0,1.0)
ax.set_aspect("equal")
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

coords.append(coords[0])

nIB=len(coords)
outfile=open("files/mesh/ib.dat","w")

outfile.write(str(nIB)+"\n")

for i in range(0,nIB-1):
        currCoord1=coords[i]
        currCoord2=coords[i+1]
        normal=np.array([currCoord2[1]-currCoord1[1],currCoord1[0]-currCoord2[0]])
        normal=normal/np.sqrt(normal[0]**2+normal[1]**2)
        outfile.write("%25.15f " % currCoord1[0])
        outfile.write("%25.15f " % currCoord1[1])
        outfile.write("%25.15f " % currCoord2[0])
        outfile.write("%25.15f " % currCoord2[1])
        outfile.write("%25.15f " % normal[0])
        outfile.write("%25.15f\n" % normal[1])

outfile.close()

outfile=open("files/mesh/gridfiles/grid_00.txt","w")
outfile.write(str(nx)+" "+str(ny)+" "+str(2)+"\n")

for k in range(0,2):
        for j in range(0,ny):
                for i in range(0,nx):
                        outfile.write("%25.15f " % x[i])
                        outfile.write("%25.15f " % y[j])
                        outfile.write("%25.15f\n" % k)

outfile.close()
