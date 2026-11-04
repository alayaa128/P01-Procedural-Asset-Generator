import maya.cmds as cmds

class Door():

    def __init__(self):
        self.door_height = 7
        self.door_width = 3
        self.door_depth = 0.3
        self.frame_depth = 0.5

    def create(self):
        self.create_body()
        self.create_frame()

    def create_body(self):
        self.body_obj, self.body_node = cmds.polyCube(name="body",
            height=self.door_height, width=self.door_width, 
            depth=self.door_depth, subdivisionsX=(6), subdivisionsY=(14))
        
        #top left detail
        cmds.polyExtrudeFacet('body.f[67:68]','body.f[73:74]', 
        'body.f[97:98]', 'body.f[103:104]', offset=(0.05))
        cmds.polyExtrudeFacet('body.f[67:68]','body.f[73:74]', 
        'body.f[97:98]', 'body.f[103:104]', localTranslateZ=(-0.05))
        cmds.polyExtrudeFacet('body.f[67:68]', 'body.f[73:74]', 
        'body.f[97:98]', 'body.f[103:104]', offset=(0.2))
        cmds.polyExtrudeFacet('body.f[67:68]', 'body.f[73:74]',
         'body.f[97:98]', 'body.f[103:104]', localTranslateZ=(0.05))

        #top right detail
        cmds.polyExtrudeFacet('body.f[69:70]', 'body.f[75:76]',
        'body.f[99:100]', 'body.f[105:106]', offset=(0.05), )
        cmds.polyExtrudeFacet('body.f[69:70]', 'body.f[75:76]',
        'body.f[99:100]', 'body.f[105:106]', localTranslateZ=(-0.05))
        cmds.polyExtrudeFacet('body.f[69:70]', 'body.f[75:76]',
        'body.f[99:100]', 'body.f[105:106]', offset=(0.2))
        cmds.polyExtrudeFacet('body.f[69:70]', 'body.f[75:76]',
        'body.f[99:100]', 'body.f[105:106]', localTranslateZ=(0.05))

        #middle left detail
        cmds.polyExtrudeFacet('body.f[37:38]', 'body.f[43:44]', 
        'body.f[49:50]', 'body.f[55:56]', 'body.f[115:116]', 'body.f[121:122]', 
        'body.f[127:128]', 'body.f[133:134]', offset=(0.05))
        cmds.polyExtrudeFacet('body.f[37:38]', 'body.f[43:44]', 
        'body.f[49:50]', 'body.f[55:56]', 'body.f[115:116]', 'body.f[121:122]', 
        'body.f[127:128]', 'body.f[133:134]', localTranslateZ=(-0.05))
        cmds.polyExtrudeFacet('body.f[37:38]', 'body.f[43:44]', 
        'body.f[49:50]', 'body.f[55:56]', 'body.f[115:116]', 'body.f[121:122]', 
        'body.f[127:128]', 'body.f[133:134]', offset=(0.2))
        cmds.polyExtrudeFacet('body.f[37:38]', 'body.f[43:44]', 
        'body.f[49:50]', 'body.f[55:56]', 'body.f[115:116]', 'body.f[121:122]', 
        'body.f[127:128]', 'body.f[133:134]', localTranslateZ=(0.05))

        #middle right detail
        cmds.polyExtrudeFacet('body.f[39:40]', 'body.f[45:46]', 'body.f[51:52]', 
        'body.f[57:58]', 'body.f[117:118]', 'body.f[123:124]', 
        'body.f[129:130]', 'body.f[135:136]', offset=(0.05))
        cmds.polyExtrudeFacet('body.f[39:40]', 'body.f[45:46]', 'body.f[51:52]', 
        'body.f[57:58]', 'body.f[117:118]', 'body.f[123:124]', 
        'body.f[129:130]', 'body.f[135:136]', localTranslateZ=(-0.05))
        cmds.polyExtrudeFacet('body.f[39:40]', 'body.f[45:46]', 'body.f[51:52]', 
        'body.f[57:58]', 'body.f[117:118]', 'body.f[123:124]', 
        'body.f[129:130]', 'body.f[135:136]', offset=(0.2))
        cmds.polyExtrudeFacet('body.f[39:40]', 'body.f[45:46]', 'body.f[51:52]', 
        'body.f[57:58]', 'body.f[117:118]', 'body.f[123:124]', 
        'body.f[129:130]', 'body.f[135:136]', localTranslateZ=(0.05))

        #bottom left detail
        cmds.polyExtrudeFacet('body.f[7:8]', 'body.f[13:14]', 'body.f[19:20]', 
        'body.f[25:26]', 'body.f[145:146]', 'body.f[151:152]', 
        'body.f[157:158]', 'body.f[163:164]', offset=(0.05))
        cmds.polyExtrudeFacet('body.f[7:8]', 'body.f[13:14]', 'body.f[19:20]', 
        'body.f[25:26]', 'body.f[145:146]', 'body.f[151:152]', 
        'body.f[157:158]', 'body.f[163:164]', localTranslateZ=(-0.05))
        cmds.polyExtrudeFacet('body.f[7:8]', 'body.f[13:14]', 'body.f[19:20]', 
        'body.f[25:26]', 'body.f[145:146]', 'body.f[151:152]', 
        'body.f[157:158]', 'body.f[163:164]', offset=(0.2))
        cmds.polyExtrudeFacet('body.f[7:8]', 'body.f[13:14]', 'body.f[19:20]', 
        'body.f[25:26]', 'body.f[145:146]', 'body.f[151:152]', 
        'body.f[157:158]', 'body.f[163:164]', localTranslateZ=(0.05))

        #bottom right detail
        cmds.polyExtrudeFacet('body.f[9:10]', 'body.f[15:16]', 
        'body.f[21:22]', 'body.f[27:28]',
        'body.f[147:148]', 'body.f[153:154]', 'body.f[159:160]', 
        'body.f[165:166]', offset=(0.05))
        cmds.polyExtrudeFacet('body.f[9:10]', 'body.f[15:16]', 
        'body.f[21:22]', 'body.f[27:28]',
        'body.f[147:148]', 'body.f[153:154]', 'body.f[159:160]', 
        'body.f[165:166]', localTranslateZ=(-0.05))
        cmds.polyExtrudeFacet('body.f[9:10]', 'body.f[15:16]', 
        'body.f[21:22]', 'body.f[27:28]',
        'body.f[147:148]', 'body.f[153:154]', 'body.f[159:160]', 
        'body.f[165:166]', offset=(0.2))
        cmds.polyExtrudeFacet('body.f[9:10]', 'body.f[15:16]', 
        'body.f[21:22]', 'body.f[27:28]',
        'body.f[147:148]', 'body.f[153:154]', 'body.f[159:160]', 
        'body.f[165:166]', localTranslateZ=(0.05))

    def create_handle(self):
        pass

    def create_frame(self):
        self.frame_obj, self.frame_node = cmds.polyCube(name="frame",
        height=self.door_height, width=self.door_width, depth=self.frame_depth)
        cmds.polyDelFacet('frame.f[0]', 'frame.f[2]', 'frame.f[3]')
        cmds.polyExtrudeFacet('frame.f[0]', 'frame.f[1]', 'frame.f[2]',
            scale=(1.15, 1.1, 1.15), keepFacesTogether=True)
        cmds.polyMoveFacet('frame.f[11]', localRotateY=(-57.2))
        cmds.polyMoveFacet('frame.f[8]', localRotateY=(57.2))

door1 = Door()
door1.create()

door2 = Door()
door2.door_height = 5
door2.door_width = 2
door2.create()
