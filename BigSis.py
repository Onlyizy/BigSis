from datetime import datetime
import os

VERSION=1.0
PSEUDO_PRIVACY_DISCLAIMER="disclaimer"

def logwriter()->None:
    first=True
    if "log.txt" in os.listdir(os.curdir):
        first=False
    f=open("log.txt","a+")
    f.writelines(VERSION, datetime.now)
    if first==True:
        runmode=input("Advanced or Minimal: ")
        f.write(runmode)

        Rlist=[]
        Clist=[]

        Rnum=int(input("How much Roommates?"))
        print(PSEUDO_PRIVACY_DISCLAIMER)
        Rlist=list(map(lambda a: input("Pseudo"),range(Rnum)))
        Cnum=int(input("How many chores? "))
        Clist=list(map(lambda a: input("Chores"),range(Cnum)))
        f.writelines(Rlist,Clist)
    f.close

def dispatcher(runmode: str)-> dict:
    

