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


#Get variables over which parameter sweep to be done
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

#Desired simulation figures of merit
resFile=open("system/res_control.md","w")
resFile.write("{\n")
for outcome in res:
        if(resAllowed.count(outcome)>0):
                resFile.write(outcome+"\n")
        else:
               res.remove(outcome) 
resFile.write("}")
resFile.close()

#Generate case files
os.chdir("..")
run(["rm","-rf","run_.part"])

generateCases(keysRepeated,valsRepeated,"")

os.chdir("..")
run(["rm","-rf","run_.part"])
run(["rm","results.csv"])

#Now run cases
fileList=os.listdir(".")

for fileName in fileList:
        if(fileName[0:3]=="run"):
                print("Running: ",fileName)
                os.chdir(fileName)
                run(["bash","run.sh"])
                os.chdir("..")

#Collect results
outfile=open("results.csv","w")
outfile.write("Case"+",")
for key in keysRepeated:
        outfile.write(key+",")

for i  in range(0,len(res)):
        outfile.write(res[i])
        if(i!=len(res)-1):
                outfile.write(",")
        else:
                outfile.write("\n")

outfile.close()
      
generateReport(keysRepeated,valsRepeated,"","",res)
