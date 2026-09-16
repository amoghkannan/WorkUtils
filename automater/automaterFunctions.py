import os
from subprocess import run
import subprocess
from .automaterConditions import controldict, flowdict, fvschemedict

baseString=""" BEGIN{found=0}; found==0{print $0} found==1{print "placeholder1"; found=0} $0=="placeholder2"{found=1} """

def findEntry(fileName,keyInd): #Value of a particular entry in an input file
        infile=open(fileName,"r")
        counter=-1
        while(counter<keyInd):
                inline=infile.readline()
                while(not ("#" in inline)):
                        inline=infile.readline()
                inData=infile.readline()
                counter=counter+1

        infile.close()

        return (inline,inData)

def replaceEntry(fileName,keyInd,val,fileDictAllowed): #First find the marker b4 the entry, then use awk script to replace
        (inline,inData)=findEntry(fileName,keyInd)
        localString=baseString.replace("placeholder2",inline.strip())
        localString=localString.replace("placeholder1",val)
        run(["awk","-i","inplace",localString,fileName])
        checkFile(fileName,fileDictAllowed)

def replaceEntryGeneric(key,val): #If we know what to replace but want to do in file-agnostic way
        
        found=False

        keys=list(controldict.keys())
        if(key in keys):
                found=True
                fileName="system/control.md"
                keyInd=keys.index(key)

        keys=list(flowdict.keys())
        if(key in keys):
                found=True
                fileName="system/flow.md"
                keyInd=keys.index(key)

        keys=list(fvschemedict.keys())
        if(key in keys):
                found=True
                fileName="system/fvscheme.md"
                keyInd=keys.index(key)

        if(found==False):
                print("Error, could not replace")
                return

        (inline,inData)=findEntry(fileName,keyInd)
        localString=baseString.replace("placeholder2",inline.strip())
        localString=localString.replace("placeholder1",val)
        run(["awk","-i","inplace",localString,fileName])

def generateCases(keysRepeated,valsRepeated,name): #Generate case files using repeated parameters; after setting non-repeating
       if(len(keysRepeated)==0 and name==""):
                return

       if(name==""):
                run(["cp","-r","basefiles","run_.part"])
                os.listdir(".")
                os.chdir("run_.part")
 
       if(len(keysRepeated)==0):
               os.chdir("..")
               name="run"+name
               run(["cp","-r","run_.part",name])
               os.chdir("run_.part")
               return

       for val in valsRepeated[0]:
               replaceEntryGeneric(keysRepeated[0],val)
               keyName=keysRepeated[0].replace(" ", "")
               valName=val.replace(".","")
               valName=valName.replace(" ","")
               generateCases(keysRepeated[1:],valsRepeated[1:],name+"_"+keyName+"_"+valName)


def checkFile(fileName, fileDict): #Check for invalid entries
        keys=fileDict.keys()

        n=len(keys)
        
        infile=open(fileName,"r")

        for key in keys:
                inline=infile.readline()
                while(not ("#" in inline)):
                       inline=infile.readline()

                inline=infile.readline().strip()
   
                if(fileDict[key][0]!="ANY"):
                       if(fileDict[key].count(inline)==0):
                                print("Error in file",fileName," for entry ",key," value: ",inline)

        infile.close()

def generateReport(keysRepeated,valsRepeated,name,outputString,res): #After running simulations, loop over files, get figure of merit 
       if(len(keysRepeated)==0 and name==""):
                return

       if(len(keysRepeated)==0):
               folderName="run"+name
               folderName=folderName.replace(" ","")
               folderName=folderName.replace(".","")
               print("Results from: ",folderName)
               os.chdir(folderName)
               outfile=open("../results.csv","a")
               outfile.write(folderName+",")
               outfile.write(outputString)
               for i in range(0,len(res)):
                       ans=checkForOutcome(res[i])
                       outfile.write(ans)
                       if(i!=len(res)-1):
                               outfile.write(",")
                       else:
                               outfile.write("\n")
               
               outfile.close()
               os.chdir("..")
               return

       for val in valsRepeated[0]:
               keyName=keysRepeated[0]
               valName=val
               generateReport(keysRepeated[1:],valsRepeated[1:],name+"_"+keyName+"_"+valName,outputString+valName+",",res)


def checkForOutcome(outcome): #Open resnorm, check whether entry present, return final value
        infile=open("time_directories/aux/resnorm","r")
        inline=infile.readline().strip().split()
        ans="N/A"
        counter=-1
        for item in inline:
                if(item==outcome):
                        break
                counter=counter+1

        if(counter!=-1):
               inlines=infile.readlines()
               inlineLast=inlines[-1].strip().split()
               ans=inlineLast[counter+1]

        return ans
