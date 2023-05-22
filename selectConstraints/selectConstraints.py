import maya.cmds as cmds

selection= cmds.ls(sl=True)
cnList=[]

for i in selection:
    constraints= cmds.listConnections(i, type="constraint")
    try:
        cnList.append(constraints[0])
    except:
        pass
        
cmds.select(clear=True)
for i in cnList:
    cmds.select(i, add=True)
        
