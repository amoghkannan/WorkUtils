import numpy as np
import scipy as sc

theta=np.linspace(2.0,44.0,num=22)
M=np.linspace(1.5,2.5,num=11)

outfile=open("obliqueShock.tex","w")
outfile.write("\\begin{tabular}{|l|l|l|l|l|l|l|l|l|l|l|}\n")
outfile.write("\hline\n")
outfile.write("\\makecell{$\\theta(^\circ)\\to$\\\$M\downarrow$}")

for t in theta:
        outfile.write("&"+str(t))

outfile.write("\\\\\hline\n")

betaPrev=np.pi/4.0
for m in M:
        outfile.write(str(m))
        for t in theta:
                def func(beta):
                        return 2.0*((m*m*np.sin(beta)*np.sin(beta)-1.0)/
                                    (m*m*(1.4+np.cos(2.0*beta))+2.0))/np.tan(beta)-np.tan(t*np.pi/180.0)

                root,infodict,ierr,mesg=sc.optimize.fsolve(func,35*np.pi/180.0,full_output=True,xtol=1e-12,maxfev=10000) 
                if(ierr==1 and root>0.0 and root<0.5*np.pi):
                        betaPrev=np.min(root)
                        outfile.write("&"+"{:.2f}".format(np.min(root)*180.0/np.pi))
                else:
                        outfile.write("&"+"-")

        outfile.write("\\\\\hline\n")

outfile.write("\end{tabular}\n")

outfile.close()
