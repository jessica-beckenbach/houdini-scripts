# inputToObjectMerge.py

#gets all inputs and connects them to an object merge instead
# to do:
# bool for make relative/absolute path?
# print to console, ui, or none at all
# destroy node if it's a null

import hou
node = hou.pwd()

def inputToObjectMerge():
    #get selected node
    selected = hou.selectedNodes()[0].path()
    
    #get its incoming streams
    n = hou.node(selected)
    incoming = n.inputs()
    parent = n.parent()
    
    # make the object merge nodes and set it to 
    # have the incoming streams as sources
    count = len(incoming)
    
    for i in range(0,count):    
        #make incoming node
        new = n.createInputNode(i,"object_merge",run_init_scripts=False)
        path = new.path()
        inc = new.relativePathTo(incoming[i])
        
        #set object path
        new.setParms({'objpath1':inc})
        
    #hou.ui.displayMessage('Replaced '+str(count)+' paths')
    
inputToObjectMerge()
