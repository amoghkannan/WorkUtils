program isentropicFlow
use iso_fortran_env, only:wp=>real64

implicit none

integer :: n
real(wp) :: MMin,MMax
real(wp) :: gm
real(wp) :: RGas
real(wp),dimension(:),allocatable :: M, TByT0, PByP0, AByAStar,nu 
integer :: i
real(wp) :: temmpp
real(wp) :: PI

PI=acos(-1.0)
RGas=287.0
gm=1.4
n=60
MMin=0.1
MMax=6.0
allocate(M(1:n))
allocate(TByT0(1:n))
allocate(PByP0(1:n))
allocate(AByAStar(1:n))
allocate(nu(1:n))

do i=1,n
        M(i)=MMin+(i-1)*(MMax-MMin)/(n-1)
        TByT0(i)=1.0/(1.0+0.5*(gm-1.0)*M(i)**2)
        PByP0(i)=(1.0/(1.0+0.5*(gm-1.0)*M(i)**2))**(gm/(gm-1.0))
        AByAStar(i)=(1.0/M(i))*((0.5*(1.0+gm))/(1+0.5*(gm-1.0)*M(i)**2))**(-0.5*(gm+1.0)/(gm-1.0))
        temmpp=(gm+1.0)/(gm-1.0)  
        nu(i)=sqrt(temmpp)*atan(sqrt((M(i)**2-1.0)/temmpp))-atan(sqrt(M(i)**2-1.0))
        nu(i)=nu(i)*180.0/PI
end do

open(11,file="isentropicFlow.tex")
write(11,*) "\begin{document}"
write(11,*) "\begin{multicols}{2}"

!write(11,*) "\begin{table}[h!]"
!write(11,*) "\centering"
write(11,*) "\begin{tabular}{|l|l|l|l|l|}"
write(11,*) "\hline"
write(11,*) "$M$ & $T/T_0$ & $P/P_0$ & $A/A^*$ & $\nu$ \\\hline"
do i=1,n/2
        if(M(i)>=1.0) then
                if(M(i) .eq. 1.0) nu(i)=0.0
                write(11,"(f6.4,'&',f6.4,'&',f6.4,'&',f7.4,'&',f6.3,'\\\hline')") M(i),TByT0(i),PByP0(i),AByAStar(i),nu(i)
        else
                write(11,"(f6.4,'&',f6.4,'&',f6.4,'&',f7.4,'&','-','\\\hline')") M(i),TByT0(i),PByP0(i),AByAStar(i)
        end if
end do
write(11,*) "\end{tabular}"
!write(11,*) "\end{table}"

!write(11,*) "\begin{table}[h!]"
!write(11,*) "\centering"
write(11,*) "\begin{tabular}{|l|l|l|l|l|}"
write(11,*) "\hline"
write(11,*) "$M$ & $T/T_0$ & $P/P_0$ & $A/A^*$ & $\nu$\\\hline"
do i=n/2+1,n
        if(M(i)>=1.0) then
                if(M(i) .eq. 1.0) nu(i)=0.0
                write(11,"(f6.4,'&',f6.4,'&',f6.4,'&',f7.4,'&',f6.3,'\\\hline')") M(i),TByT0(i),PByP0(i),AByAStar(i),nu(i)
        else
                write(11,"(f6.4,'&',f6.4,'&',f6.4,'&',f7.4,'&','-','\\\hline')") M(i),TByT0(i),PByP0(i),AByAStar(i)
        end if
end do
write(11,*) "\end{tabular}"
!write(11,*) "\end{table}"

write(11,*) "\end{multicols}"
write(11,*) "\end{document}"
close(11)





end program isentropicFlow
