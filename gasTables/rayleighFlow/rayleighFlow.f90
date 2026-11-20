program isentropicFlow
use iso_fortran_env, only:wp=>real64

implicit none

integer :: n
real(wp) :: MMin,MMax
real(wp) :: gm
real(wp) :: RGas
real(wp),dimension(:),allocatable :: M, TByTStar, PByPStar, TStagByTStagStar, PStagByPStagStar
integer :: i
real(wp) :: temmpp
real(wp) :: PI

PI=acos(-1.0)
RGas=287.0
gm=1.4
n=19
MMin=0.2
MMax=2.0
allocate(M(1:n))
allocate(TByTStar(1:n))
allocate(PByPStar(1:n))
allocate(TStagByTStagStar(1:n))
allocate(PStagByPStagStar(1:n))

do i=1,n
        M(i)=MMin+(i-1)*(MMax-MMin)/(n-1)
        TByTStar(i)=((1.0+gm)/(1.0+gm*M(i)*M(i)))**2*((M(i)*M(i))/1.0)
        PByPStar(i)=(1.0+gm)/(1.0+gm*M(i)*M(i))
        TStagByTStagStar(i)=((1.0+gm)/(1.0+gm*M(i)*M(i)))**2*(M(i)*M(i)/1.0)
        TStagByTStagStar(i)=TStagByTStagStar(i)*((1.0+0.5*(gm-1.0)*M(i)*M(i))/(0.5*(gm+1.0)))
        PStagByPStagStar(i)=((1.0+gm)/(1.0+gm*M(i)*M(i)))*((1+0.5*(gm-1.0)*M(i)*M(i))/(0.5*(gm+1.0)))**(gm/(gm-1.0))
end do

open(11,file="rayleighFlow.tex")
write(11,*) "\begin{document}"
write(11,*) "\begin{multicols}{2}"

!write(11,*) "\begin{table}[h!]"
!write(11,*) "\centering"
write(11,*) "\begin{tabular}{|l|l|l|l|l|}"
write(11,*) "\hline"
write(11,*) "$M$ & $T/T^*$ & $P/P^*$ & $T_0/T_0^*$ & $P_0/P_0^*$ \\\hline"
do i=1,n/2
        write(11,"(f6.4,'&',f6.4,'&',f6.4,'&',f7.4,'&',f7.4,'\\\hline')") M(i),TByTStar(i),PByPSTar(i),TStagByTStagStar(i),&
                                                                          PStagByPStagStar(i)
end do
write(11,*) "\end{tabular}"
!write(11,*) "\end{table}"

!write(11,*) "\begin{table}[h!]"
!write(11,*) "\centering"
write(11,*) "\begin{tabular}{|l|l|l|l|l|}"
write(11,*) "\hline"
write(11,*) "$M$ & $T/T^*$ & $P/P^*$ & $T_0/T_0^*$ & $P_0/P_0^*$ \\\hline"
do i=n/2+1,n
        write(11,"(f6.4,'&',f6.4,'&',f6.4,'&',f7.4,'&',f7.4,'\\\hline')") M(i),TByTStar(i),PByPSTar(i),TStagByTStagStar(i),&
                                                                          PStagByPStagStar(i)
end do
write(11,*) "\end{tabular}"
!write(11,*) "\end{table}"

write(11,*) "\end{multicols}"
write(11,*) "\end{document}"
close(11)





end program isentropicFlow
