from PySide6 import QtWidgets, QtCore

from door import Door



class DoorGUI(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        self.door_generator = Door()
        self.setWindowTitle("Procedural Door")
        self.create_layout()
        self.create_connections()

    def create_layout(self):
        self.main_lay = QtWidgets.QFormLayout()
        self._form_ui()
        self.create_btn = QtWidgets.QDoubleSpinBox()
        self.main_lay.addWidget(self.create_btn)
        self.setLayout(self.main_lay)

    def _form_ui(self):
        self.form_lay = QtWidgets.QFormLayout()
        self.door_h_dspnbx = QtWidgets.QDoubleSpinBox()
        self.door_h_dspnbx.setValue(7.0)
        self.form_lay.addRow("Door Height", self.door_h_dspnbx)
        self.main_lay.addLayout(self.form_lay)

    def create_connections(self):
        self.create_btn.clicked.connect(self.create)

    @QtCore.Slot()
    def create(self):
        self.door_generator.door_height = self.door_h_dspnbx.value()
        self.door_generator.create()
