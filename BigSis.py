from csv import DictReader, DictWriter
from datetime import datetime
from os import listdir
from platform import system

VERSION=1.0
PSEUDO_PRIVACY_DISCLAIMER="disclaimer"
FIRST_TIME_RUN_DISCLAIMER="disclaimer1"
params=["runmode","pseudo","chores"]

def config_file(disclamers,params):
    """Returns a tuple with relevant data for next operations in this order runmode, pseudo, chores"""
    FIRST_TIME_RUN_DISCLAIMER,PSEUDO_PRIVACY_DISCLAIMER=disclamers

    first=True

    if "config.csv" in listdir():

        first=False

    with open("config.csv","a+",newline='') as f:

        if first==True:

            print(FIRST_TIME_RUN_DISCLAIMER)
            runmode=input("(A)dvanced or (M)inimal: ")
            Rlist=[]
            Clist=[]
            Rnum=int(input("How much Roommates?"))
            print(PSEUDO_PRIVACY_DISCLAIMER)
            Rlist=set(map(lambda a: input("Pseudo"),range(Rnum)))
            Cnum=int(input("How many chores? "))
            Clist=set(map(lambda a: input("Chores"),range(Cnum)))
            DataWriter=DictWriter(f,fieldnames=params,extrasaction="raise",restval="")
            DataWriter.writeheader()
            DataWriter.writerow({"runmode":runmode, "pseudo":Rlist, "chores":Clist})
        
        DataReader=DictReader(f,restkey="",restval="")
        if 
        t=list(DataReader)[-1]["runmode"],list(DataReader)[-1]["pseudo"],list(DataReader)[-1]["chores"]
    return t

def logwriter()->None:
    """Write useful info about the program while running. intended to be useful for debugging
    """
    with open("log.txt","a+") as f:
        f.writelines([VERSION, datetime.now,system(),])
            
t=config_file((FIRST_TIME_RUN_DISCLAIMER, PSEUDO_PRIVACY_DISCLAIMER),params)
logwriter()
