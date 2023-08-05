import maya.cmds as cmds


def setRGBColor(ctrl, color = (1,1,1)):
    
    rgb = ("R","G","B")
    
    cmds.setAttr(ctrl + ".overrideEnabled",1)
    cmds.setAttr(ctrl + ".overrideRGBColors",1)
    
    for channel, color in zip(rgb, color):
        
        cmds.setAttr(ctrl + ".overrideColor%s" %channel, color)


selection = cmds.ls(orderedSelection = True);

for i in selection:
    n= cmds.listRelatives(i, shapes=True)
    print n
    for i in n:
        setRGBColor(i, color = (102/255,1,1))


