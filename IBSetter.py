#Tool to generate IB lines for testing

import numpy as np
from matplotlib import pyplot as plt
from shapely.geometry import Point, Polygon, LineString

nx=20
ny=20

cell_type=np.zeros((nx-1,ny-1),dtype=np.int8)

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

polygon=Polygon(coords)

coords.append(coords[0])

nIB=len(coords)-1
outfile=open("files/mesh/ib.dat","w")

outfile.write(str(nIB)+"\n")

for i in range(0,nIB):
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

outfile=open("files/cell_class_00_test.txt","w")

for j in range(0,ny-1):
        for i in range(0,nx-1):
                outfile.write(str(i)+" "+str(j)+" "+str(1)+" ")
                point_cellcentre=Point(0.5*(x[i]+x[i+1]),0.5*(y[j]+y[j+1]))
                isInside=polygon.contains(point_cellcentre)
                if(isInside):
                        cell_type[i,j]=int(-1)
                else:
                        cell_type[i,j]=int(0)

                outfile.write(str(cell_type[i,j])+"\n")

outfile.close()

outfile=open("files/ea_x_test.txt","w")

for j in range(0,ny-1):
        for i in range(0,nx):
                line=LineString([(x[i],y[j]),(x[i],y[j+1])])
                intersection_pieces=line.intersection(polygon)
                intersection_length=intersection_pieces.length
                if(intersection_length==0.0 and polygon.contains(Point(x[i],y[j]))):
                        intersection_length=line.length
                non_intersection_length=line.length-intersection_length
                outfile.write("%25.15f\n" % non_intersection_length)

outfile.close()

outfile=open("files/ea_y_test.txt","w")

for j in range(0,ny):
        for i in range(0,nx-1):
                line=LineString([(x[i],y[j]),(x[i+1],y[j])])
                intersection_pieces=line.intersection(polygon)
                intersection_length=intersection_pieces.length
                if(intersection_length==0.0 and polygon.contains(Point(x[i],y[j]))):
                        intersection_length=line.length
                non_intersection_length=line.length-intersection_length
                outfile.write("%25.15f\n" % non_intersection_length)


outfile.close()
