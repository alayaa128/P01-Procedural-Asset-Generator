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

    def create(self):
        self.create_body()

        if self.create_frame_enabled:
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