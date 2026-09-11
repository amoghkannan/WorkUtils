from automater.automaterFunctions import *
from automater.automaterAllowed import *
from automater.automaterConditions import *

currDir=os.getcwd()

os.chdir("../../build")
run(["make","clean"])
run(["make"])
run(["ctest"])
os.chdir("../tests")
run(["python3","Test.py","ausm", "muscl", "sst"])

os.chdir(currDir)
os.chdir("basefiles")

keysRepeated=[]
valsRepeated=[]

counter=0
for controlKey in controldict.keys():
        replaceEntry("system/control.md",counter,controldict[controlKey][0],controldictAllowed)
        if(len(controldict[controlKey])>1):
                keysRepeated.append(controlKey)
                valsRepeated.append(controldict[controlKey])
        counter=counter+1

counter=0
for flowKey in flowdict.keys():
        replaceEntry("system/flow.md",counter,flowdict[flowKey][0],flowdictAllowed)
        if(len(flowdict[flowKey])>1):
                keysRepeated.append(flowKey)
                valsRepeated.append(flowdict[flowKey])

        counter=counter+1

counter=0
for fvschemeKey in fvschemedict.keys():
        replaceEntry("system/fvscheme.md",counter,fvschemedict[fvschemeKey][0],fvschemedictAllowed)
        if(len(fvschemedict[fvschemeKey])>1):
                keysRepeated.append(fvschemeKey)
                valsRepeated.append(fvschemedict[fvschemeKey]) 
        counter=counter+1

os.chdir("..")
run(["rm","-rf","run_.part"])

generateCases(keysRepeated,valsRepeated,"")

os.chdir("..")
run(["rm","-rf","run_.part"])

