from csv import DictReader, DictWriter
from datetime import datetime
from os import listdir
from platform import system

VERSION=1.0
PSEUDO_PRIVACY_DISCLAIMER="SOME OF THE DATA ENTERED WILL BE SENT TO THE DEVS OF THIS PROGRAM ALONGSIDE WITH RELEVANT DATA COLLECTED FROM YOUR COMPUTER FOR THE SAKE OF IMPROVEMENT AND DEBUGGING. NO WORRIES WE WON'T INVADE YOUR PRIVACY. SEE THE TERMS AND CONDITIONS. YOU CAN ALSO OPT OUT."
FIRST_TIME_RUN_DISCLAIMER="THIS PROGRAM WILL GENERATE TWO FILES WHERE THE SETTINGS ARE GOING TO BE STORED FOR FUTURE USE. YOU CAN MODIFY THOSE FILES OR DELETE THEM TO RECONFIGURE. READ THE MANUAL CAREFULLY!"
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
            
