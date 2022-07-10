#from typing import Dict
import handler
import random

disclaimers = handler.PSEUDO_PRIVACY_DISCLAIMER,handler.FIRST_TIME_RUN_DISCLAIMER
params=handler.params

settings=handler.config_file(disclaimers,params)
runmode,pseudo,chores=settings

switch={"A": advanced_dispatcher(pseudo,chores),"M":minimal_dipatcher(pseudo,chores)}

def minimal_dipatcher(roomates:list,tasks:list)->dict:
    """associate each roomate to a specific task without making use of the spam bot"""
    d=map(lambda a (r,t): return d.setdefault(r,t) ,roomates,tasks)    
    return None

def advanced_dispatcher(roomates:list,tasks:list)-> dict:
    """ associate each roomate with a specific chore for a given time and make uses of the spam bot to encourage them doing their chore
    """
    pass
    return None



r=switch.get(runmode,"Please update your setting see manual.")
#r is whatever is returned by the dispatcher it can be an error message defined higher


#put all the input statement in the UI module
