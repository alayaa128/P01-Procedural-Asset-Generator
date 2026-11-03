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
            height=self.door_height, width=self.door_width, depth=self.door_depth,
            subdivisionsX=(2*self.door_width), subdivisionsY=(2*self.door_height))

    def create_handle(self):
        pass

    def create_frame(self):
        self.frame_obj, self.frame_node = cmds.polyCube(name="frame",
        height=self.door_height, width=self.door_width, depth=self.frame_depth)
        cmds.delete('pCube4.f[1]')

door1 = Door()
door1.create()