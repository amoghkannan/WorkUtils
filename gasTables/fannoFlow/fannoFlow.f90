program isentropicFlow
use iso_fortran_env, only:wp=>real64

implicit none

integer :: n
real(wp) :: MMin,MMax
real(wp) :: gm
real(wp) :: RGas
real(wp),dimension(:),allocatable :: M, TByTStar, PByPStar, PStagByPStagStar, FourfLStarByD 
integer :: i
real(wp) :: temmpp
real(wp) :: PI

PI=acos(-1.0)
RGas=287.0
gm=1.4
n=31
MMin=1.0
MMax=4.0
allocate(M(1:n))
allocate(TByTStar(1:n))
allocate(PByPStar(1:n))
allocate(PStagByPStagStar(1:n))
allocate(FourfLStarByD(1:n))

do i=1,n
        M(i)=MMin+(i-1)*(MMax-MMin)/(n-1)
        TByTStar(i)=(0.5*(gm+1.0))/(1.0+0.5*(gm-1.0)*M(i)*M(i))
        PByPStar(i)=(1.0/M(i))*((0.5*(1.0+gm))/(1+0.5*(gm-1.0)*M(i)*M(i)))**0.5
        PStagByPStagStar(i)=(1.0/M(i))*((0.5*(1.0+gm))/(1+0.5*(gm-1.0)*M(i)*M(i)))**(-0.5*((gm+1.0)/(gm-1.0)))
        FourfLStarByD(i)=0.5*((gm+1.0)/gm)*log((0.5*(gm+1.0))/(1+0.5*(gm-1.0)*M(i)*M(i)))
        FourfLStarByD(i)=FourfLStarByD(i)-(1.0/gm)*(1.0-1.0/(M(i)*M(i)))
        FourfLStarByD(i)=FourfLStarByD(i)-0.5*((gm+1.0)/gm)*log(1.0/(M(i)*M(i)))
end do

open(11,file="fannoFlow.tex")
write(11,*) "\begin{document}"
write(11,*) "\begin{multicols}{2}"

!write(11,*) "\begin{table}[h!]"
!write(11,*) "\centering"
write(11,*) "\begin{tabular}{|l|l|l|l|l|}"
write(11,*) "\hline"
write(11,*) "$M$ & $T/T^*$ & $P/P^*$ & $P_0/P_0^*$ & $4fL^*/D$ \\\hline"
do i=1,n/2
        write(11,"(f6.4,'&',f6.4,'&',f6.4,'&',f7.4,'&',f6.4,'\\\hline')") M(i),TByTStar(i),PByPSTar(i),PStagByPStagStar(i),&
                                                                          FourfLStarByD(i)
end do
write(11,*) "\end{tabular}"
!write(11,*) "\end{table}"

!write(11,*) "\begin{table}[h!]"
!write(11,*) "\centering"
write(11,*) "\begin{tabular}{|l|l|l|l|l|}"
write(11,*) "\hline"
write(11,*) "$M$ & $T/T^*$ & $P/P^*$ & $P_0/P_0^*$ & $4fL^*/D$ \\\hline"
do i=n/2+1,n
        write(11,"(f6.4,'&',f6.4,'&',f6.4,'&',f7.4,'&',f6.4,'\\\hline')") M(i),TByTStar(i),PByPSTar(i),PStagByPStagStar(i),&
                                                                          FourfLStarByD(i)
end do
write(11,*) "\end{tabular}"
!write(11,*) "\end{table}"

write(11,*) "\end{multicols}"
write(11,*) "\end{document}"
close(11)





end program isentropicFlow
