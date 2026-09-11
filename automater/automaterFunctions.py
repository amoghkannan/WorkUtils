import os
from subprocess import run
from .automaterConditions import controldict, flowdict, fvschemedict

baseString=""" BEGIN{found=0}; found==0{print $0} found==1{print "placeholder1"; found=0} $0=="placeholder2"{found=1} """

def findEntry(fileName,keyInd):
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

def replaceEntry(fileName,keyInd,val,fileDictAllowed):
        (inline,inData)=findEntry(fileName,keyInd)
        localString=baseString.replace("placeholder2",inline.strip())
        localString=localString.replace("placeholder1",val)
        run(["awk","-i","inplace",localString,fileName])
        checkFile(fileName,fileDictAllowed)

def replaceEntryGeneric(key,val):
        
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

def generateCases(keysRepeated,valsRepeated,name):
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
               generateCases(keysRepeated[1:],valsRepeated[1:],name+"_"+keysRepeated[0]+"_"+val)


def checkFile(fileName, fileDict):
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

