import importlib



from PySide6 import QtWidgets, QtCore
from shiboken6 import wrapInstance

import maya.OpenMayaUI as omui
import maya.cmds as cmds


class Door():

    def __init__(self):
        self.door_height = 7
        self.door_width = 3
        self.door_depth = 0.3
        self.frame_depth = 0.5
        self.create_frame_enabled = True
        self.knob_radius = 0.06*self.door_width

    def create(self):
        self.create_body()
        self.create_front_knob()
        self.create_back_knob()
        self.create_knob_connector()
        self.create_lock()

        if self.create_frame_enabled:
            self.create_frame()

    def create_body(self):
        self.body_obj, self.body_node = cmds.polyCube(name="body",
            height=self.door_height, width=self.door_width, 
            depth=self.door_depth, subdivisionsX=(6), subdivisionsY=(14))

        body = self.body_obj

        #top left detail
        cmds.polyExtrudeFacet(f'{body}.f[67:68]', f'{body}.f[73:74]', 
        f'{body}.f[97:98]', f'{body}.f[103:104]', offset=(0.05))
        cmds.polyExtrudeFacet(f'{body}.f[67:68]', f'{body}.f[73:74]', 
        f'{body}.f[97:98]', f'{body}.f[103:104]', localTranslateZ=(-0.05))
        cmds.polyExtrudeFacet(f'{body}.f[67:68]', f'{body}.f[73:74]', 
        f'{body}.f[97:98]', f'{body}.f[103:104]', offset=(0.2))
        cmds.polyExtrudeFacet(f'{body}.f[67:68]', f'{body}.f[73:74]', 
        f'{body}.f[97:98]', f'{body}.f[103:104]', localTranslateZ=(0.05))

        #top right detail
        cmds.polyExtrudeFacet(f'{body}.f[69:70]', f'{body}.f[75:76]',
        f'{body}.f[99:100]', f'{body}.f[105:106]', offset=(0.05), )
        cmds.polyExtrudeFacet(f'{body}.f[69:70]', f'{body}.f[75:76]',
        f'{body}.f[99:100]', f'{body}.f[105:106]', localTranslateZ=(-0.05))
        cmds.polyExtrudeFacet(f'{body}.f[69:70]', f'{body}.f[75:76]',
        f'{body}.f[99:100]', f'{body}.f[105:106]', offset=(0.2))
        cmds.polyExtrudeFacet(f'{body}.f[69:70]', f'{body}.f[75:76]',
        f'{body}.f[99:100]', f'{body}.f[105:106]', localTranslateZ=(0.05))

        #middle left detail
        cmds.polyExtrudeFacet(f'{body}.f[37:38]', f'{body}.f[43:44]', 
        f'{body}.f[49:50]', f'{body}.f[55:56]', f'{body}.f[115:116]', f'{body}.f[121:122]', 
        f'{body}.f[127:128]', f'{body}.f[133:134]', offset=(0.05))
        cmds.polyExtrudeFacet(f'{body}.f[37:38]', f'{body}.f[43:44]', 
        f'{body}.f[49:50]', f'{body}.f[55:56]', f'{body}.f[115:116]', f'{body}.f[121:122]', 
        f'{body}.f[127:128]', f'{body}.f[133:134]', localTranslateZ=(-0.05))
        cmds.polyExtrudeFacet(f'{body}.f[37:38]', f'{body}.f[43:44]', 
        f'{body}.f[49:50]', f'{body}.f[55:56]', f'{body}.f[115:116]', f'{body}.f[121:122]', 
        f'{body}.f[127:128]', f'{body}.f[133:134]', offset=(0.2))
        cmds.polyExtrudeFacet(f'{body}.f[37:38]', f'{body}.f[43:44]', 
        f'{body}.f[49:50]', f'{body}.f[55:56]', f'{body}.f[115:116]', f'{body}.f[121:122]', 
        f'{body}.f[127:128]', f'{body}.f[133:134]', localTranslateZ=(0.05))

        #middle right detail
        cmds.polyExtrudeFacet(f'{body}.f[39:40]', f'{body}.f[45:46]', f'{body}.f[51:52]', 
        f'{body}.f[57:58]', f'{body}.f[117:118]', f'{body}.f[123:124]', 
        f'{body}.f[129:130]', f'{body}.f[135:136]', offset=(0.05))
        cmds.polyExtrudeFacet(f'{body}.f[39:40]', f'{body}.f[45:46]', f'{body}.f[51:52]', 
        f'{body}.f[57:58]', f'{body}.f[117:118]', f'{body}.f[123:124]', 
        f'{body}.f[129:130]', f'{body}.f[135:136]', localTranslateZ=(-0.05))
        cmds.polyExtrudeFacet(f'{body}.f[39:40]', f'{body}.f[45:46]', f'{body}.f[51:52]', 
        f'{body}.f[57:58]', f'{body}.f[117:118]', f'{body}.f[123:124]', 
        f'{body}.f[129:130]', f'{body}.f[135:136]', offset=(0.2))
        cmds.polyExtrudeFacet(f'{body}.f[39:40]', f'{body}.f[45:46]', f'{body}.f[51:52]', 
        f'{body}.f[57:58]', f'{body}.f[117:118]', f'{body}.f[123:124]', 
        f'{body}.f[129:130]', f'{body}.f[135:136]', localTranslateZ=(0.05))

        #bottom left detail
        cmds.polyExtrudeFacet(f'{body}.f[7:8]', f'{body}.f[13:14]', f'{body}.f[19:20]', 
        f'{body}.f[25:26]', f'{body}.f[145:146]', f'{body}.f[151:152]', 
        f'{body}.f[157:158]', f'{body}.f[163:164]', offset=(0.05))
        cmds.polyExtrudeFacet(f'{body}.f[7:8]', f'{body}.f[13:14]', f'{body}.f[19:20]', 
        f'{body}.f[25:26]', f'{body}.f[145:146]', f'{body}.f[151:152]', 
        f'{body}.f[157:158]', f'{body}.f[163:164]', localTranslateZ=(-0.05))
        cmds.polyExtrudeFacet(f'{body}.f[7:8]', f'{body}.f[13:14]', f'{body}.f[19:20]', 
        f'{body}.f[25:26]', f'{body}.f[145:146]', f'{body}.f[151:152]', 
        f'{body}.f[157:158]', f'{body}.f[163:164]', offset=(0.2))
        cmds.polyExtrudeFacet(f'{body}.f[7:8]', f'{body}.f[13:14]', f'{body}.f[19:20]', 
        f'{body}.f[25:26]', f'{body}.f[145:146]', f'{body}.f[151:152]', 
        f'{body}.f[157:158]', f'{body}.f[163:164]', localTranslateZ=(0.05))

        #bottom right detail
        cmds.polyExtrudeFacet(f'{body}.f[9:10]', f'{body}.f[15:16]', 
        f'{body}.f[21:22]', f'{body}.f[27:28]',
        f'{body}.f[147:148]', f'{body}.f[153:154]', f'{body}.f[159:160]', 
        f'{body}.f[165:166]', offset=(0.05))
        cmds.polyExtrudeFacet(f'{body}.f[9:10]', f'{body}.f[15:16]', 
        f'{body}.f[21:22]', f'{body}.f[27:28]',
        f'{body}.f[147:148]', f'{body}.f[153:154]', f'{body}.f[159:160]', 
        f'{body}.f[165:166]', localTranslateZ=(-0.05))
        cmds.polyExtrudeFacet(f'{body}.f[9:10]', f'{body}.f[15:16]', 
        f'{body}.f[21:22]', f'{body}.f[27:28]',
        f'{body}.f[147:148]', f'{body}.f[153:154]', f'{body}.f[159:160]', 
        f'{body}.f[165:166]', offset=(0.2))
        cmds.polyExtrudeFacet(f'{body}.f[9:10]', f'{body}.f[15:16]', 
        f'{body}.f[21:22]', f'{body}.f[27:28]',
        f'{body}.f[147:148]', f'{body}.f[153:154]', f'{body}.f[159:160]', 
        f'{body}.f[165:166]', localTranslateZ=(0.05))

    def create_front_knob(self):
        self.knob_obj, self.knob_node = cmds.polySphere(name="f_knob", 
        radius=(self.knob_radius))
        cmds.xform(translation=[0.4*self.door_width, -0.03*self.door_height, 1.3*self.door_depth])

    def create_back_knob(self):
        self.knob_obj, self.knob_node = cmds.polySphere(name="b_knob", 
        radius=(self.knob_radius))
        cmds.xform(translation=[0.4*self.door_width, -0.03*self.door_height, -1.3*self.door_depth])

    def create_knob_connector(self):
        self.knob_connector_obj, self.knob_connector_node = cmds.polyCylinder(name="Knob Connector", 
        radius=(0.5*self.knob_radius), height=(1.7*self.door_depth))
        cmds.xform(translation=[0.4*self.door_width, -0.03*self.door_height, 0],
        rotation=[90, 0, 0])

    def create_lock(self):
        self.lock_obj, self.lock_node, = cmds.polyCylinder(name="Door Lock",
        radius=(0.5*self.knob_radius),height=(1.2*self.door_depth))
        cmds.xform(translation=[0.4*self.door_width, 0.03*self.door_height, 0],
        rotation=[90, 0, 0])


    def create_frame(self):
        self.frame_obj, self.frame_node = cmds.polyCube(name="frame",
        height=self.door_height, width=self.door_width, depth=self.frame_depth)
        frame = self.frame_obj
        cmds.polyDelFacet(f'{frame}.f[0]', f'{frame}.f[2]', f'{frame}.f[3]')
        cmds.polyExtrudeFacet(f'{frame}.f[0]', f'{frame}.f[1]', f'{frame}.f[2]',
        scale=(1.15, 1.1, 1.15), keepFacesTogether=True)
        cmds.polyMoveEdge(f'{frame}.e[9]', translateY=((-0.55*self.door_height)+(0.5*self.door_height)))
        cmds.polyMoveEdge(f'{frame}.e[8]', translateY=((-0.55*self.door_height)+(0.5*self.door_height)))
        

def get_main_maya_win():
    main_win = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win), QtWidgets.QWidget)


class DoorGUI(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.door_generator = Door()
        self.setWindowTitle("Procedural Door")
        self.create_layout()
        self.create_connections()

    def create_layout(self):
        self.main_lay = QtWidgets.QVBoxLayout()
        self._form_ui()
        self.create_btn = QtWidgets.QPushButton("Create")
        self.main_lay.addWidget(self.create_btn)
        self.setLayout(self.main_lay)

    def _form_ui(self):
        self.form_lay = QtWidgets.QFormLayout()
        self.door_h_dspnbx = QtWidgets.QDoubleSpinBox()
        self.door_w_dspnbx = QtWidgets.QDoubleSpinBox()
        self.door_d_dspnbx = QtWidgets.QDoubleSpinBox()
        self.frame_d_dspnbx = QtWidgets.QDoubleSpinBox()
        self.frame_chk = QtWidgets.QCheckBox()
        self.frame_chk.setChecked(True)
        self.door_h_dspnbx.setValue(7.0)
        self.door_w_dspnbx.setValue(3.0)
        self.door_d_dspnbx.setValue(0.3)
        self.frame_d_dspnbx.setValue(0.5)
        self.form_lay.addRow("Door Height", self.door_h_dspnbx)
        self.form_lay.addRow("Door Width", self.door_w_dspnbx)
        self.form_lay.addRow("Door Depth", self.door_d_dspnbx)
        self.form_lay.addRow("Frame Depth", self.frame_d_dspnbx)
        self.form_lay.addRow("Create Door Frame", self.frame_chk)
        self.main_lay.addLayout(self.form_lay)

    def create_connections(self):
        self.create_btn.clicked.connect(self.create)

    @QtCore.Slot()
    def create(self):
        self.door_generator.door_height = self.door_h_dspnbx.value()
        self.door_generator.door_width = self.door_w_dspnbx.value()
        self.door_generator.door_depth = self.door_d_dspnbx.value()
        self.door_generator.frame_depth = self.frame_d_dspnbx.value()
        self.door_generator.create_frame_enabled = self.frame_chk.isChecked()
        self.door_generator.create()


door_gui = DoorGUI()
door_gui.show()