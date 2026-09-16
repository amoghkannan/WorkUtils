import os
from subprocess import run

controldict={}
flowdict={}
fvschemedict={}
res=[] #Values to get out, as final report compilation

controldict["CFL"]=["1.0"]
controldict["Adaptive CFL flag"]=["0"]
controldict["Restart level"]=["0"]
controldict["Maximum Iterations"]=["20000"]
controldict["Save Iterations"]=["2000"]
controldict["Output File format"]=["tecplot"]
controldict["Output Data format"]=["ASCII"]
controldict["Input File format"]=["tecplot"]
controldict["Input Data format"]=["ASCII"]
controldict["Write Precision"]=["10"]
controldict["Purge Write"]=["2"]
controldict["Residual write Interval"]=["5"]
controldict["Tolerance"]=["1e-18 Continuity_abs"]
controldict["Debug Level"]=["5"]

flowdict["Number of variables"]=["5"]
flowdict["Free Stream Density"]=["1.293"]
flowdict["Free Stream X-Speed"]=["2337.75673643"]
flowdict["Free Stream Y-Speed"]=["1349.741728431287"]
flowdict["Free Stream Z-Speed"]=["0.0"]
flowdict["Free Stream Pressure"]=["101325.0"]
flowdict["Free Stream Turbulence Intensity"]=["1.0"]
flowdict["Free Stream Viscosity Ratio"]=["10.0"]
flowdict["Free Stream Intermittency"]=["1.0"]
flowdict["Reference Viscosity"]=["0.0"]
flowdict["Viscosity law"]=["sutherland_law"]
flowdict["Reference Temperature"]=["273.0"]
flowdict["Sutherland Temperature"]=["110.5"]
flowdict["Prandtl numbers"]=["0.72 0.9"]
flowdict["Specific heat ratio"]=["1.4"]
flowdict["Gas constant"]=["287.0"]

fvschemedict["Inviscid Flux Scheme"]=["hlle"]
fvschemedict["Higher Order Method"]=["muscl","none"]
fvschemedict["Switch: Limiter - Pressure based switch"]=["1 1 1 0 0 0"]
fvschemedict["Turbulence Limiter Switch"]=["1 1 1"]
fvschemedict["Turbulence model"]=["none"]
fvschemedict["Transition model"]=["none"]
fvschemedict["Time Step"]=["l"]
fvschemedict["Time Integration Method"]=["RK4"]
fvschemedict["Higher Order Boundary Conditions"]=["0"]
fvschemedict["Effective Area"]=["0","1","2"]

res=["Mass_abs","Viscous_abs"]
