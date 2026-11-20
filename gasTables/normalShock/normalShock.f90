program normalShock
use iso_fortran_env,only: wp=>real64

implicit none

integer :: n
real(wp) :: MMin,MMax
real(wp) :: gm
real(wp) :: RGas
real(wp),dimension(:),allocatable :: M1,M2,pRat,tRat,pStagRat
integer :: i
real(wp) :: temmpp

RGas=287.0
gm=1.4
n=21
MMin=1.0
MMax=3.0

allocate(M1(1:n))
allocate(M2(1:n))
allocate(pRat(1:n))
allocate(tRat(1:n))
allocate(pStagRat(1:n))

do i=1,n
        M1(i)=MMin+(i-1)*(MMax-MMin)/(n-1)
        M2(i)=sqrt((1.0+0.5*(gm-1.0)*M1(i)**2)/(gm*M1(i)**2-0.5*(gm-1.0)))
        pRat(i)=1.0+2.0*gm*(M1(i)**2-1.0)/(gm+1.0)
        temmpp=(gm+1.0)*M1(i)**2/(2.0+(gm-1.0)*M1(i)**2)
        tRat(i)=pRat(i)/temmpp
        pStagRat(i)=((gm+1.0)*M1(i)**2/(2.0+(gm-1.0)*M1(i)**2))**(gm/(gm-1.0)) * &
                    ((gm+1.0)/(2.0*gm*M1(i)**2-(gm-1.0)))**(1.0/(gm-1.0))
end do

open(11,file="normalShock.tex")
write(11,*) "\begin{document}"
write(11,*) "\begin{multicols}{2}"

!write(11,*) "\begin{table}[h!]"
!write(11,*) "\centering"
write(11,*) "\begin{tabular}{|l|l|l|l|l|}"
write(11,*) "\hline"
write(11,*) "$M_1$ & $M_2$ & $T_2/T_1$ & $P_2/P_1$ & $P_{02}/P_{01}$ \\\hline"
do i=1,n/2
        write(11,"(f4.2,'&',f6.4,'&',f6.4,'&',f7.4,'&',f6.4,'\\\hline')") M1(i),M2(i),tRat(i),pRat(i),pStagRat(i)
end do
write(11,*) "\end{tabular}"
!write(11,*) "\end{table}"

!write(11,*) "\begin{table}[h!]"
!write(11,*) "\centering"
write(11,*) "\begin{tabular}{|l|l|l|l|l|}"
write(11,*) "\hline"
write(11,*) "$M_1$ & $M_2$ & $T_2/T_1$ & $P_2/P_1$ & $P_{02}/P_{01}$ \\\hline"
do i=n/2+1,n
        write(11,"(f4.2,'&',f6.4,'&',f6.4,'&',f7.4,'&',f6.4,'\\\hline')") M1(i),M2(i),tRat(i),pRat(i),pStagRat(i)
end do
write(11,*) "\end{tabular}"
!write(11,*) "\end{table}"

write(11,*) "\end{multicols}"
write(11,*) "\end{document}"
close(11)












end program normalShock
