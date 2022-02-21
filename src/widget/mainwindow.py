import sys
import os
import shutil
from PIL import ImageQt
from PySide6 import QtCore
from PySide6.QtGui import QPixmap

from libraries import School_Data_ORC
from libraries import Config

from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

from src.widget.ui.ui_mainwindow import Ui_MainWindow


class QtWindows(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.widget_init()

        # var
        self.now_image_path = str()

        # connect
        self.ui.pushButton_start.pressed.connect(self.start_orc)
        self.ui.pushButton_yes.pressed.connect(self.data_true)
        self.ui.pushButton_no.pressed.connect(self.data_false)

    def widget_init(self):
        self.ui.label_image_name.setScaledContents(True)
        self.ui.label_image_phone.setScaledContents(True)
        self.ui.label_image_home.setScaledContents(True)

    def data_true(self):

        # check file is exit
        if not os.path.exists(self.now_image_path):
            print("can't find file")
            return

        # move file to (success / failed) folder

        # noinspection PyBroadException
        try:
            shutil.move(self.now_image_path, Config.Global.success_folder)
        except Exception:
            os.remove(self.now_image_path)

        # clear app info
        self.clear_all_info()

    def data_false(self):
        # check file is exit
        if not os.path.exists(self.now_image_path):
            print("can't find file")
            return

        # move file to (success / failed) folder
        # noinspection PyBroadException
        try:
            shutil.move(self.now_image_path, Config.Global.failed_folder)
        except Exception:
            os.remove(self.now_image_path)

        # clear app info
        self.clear_all_info()

    def clear_all_info(self):
        self.ui.label_text_filename.setText("")
        self.ui.lineEdit_text_name.setText("")
        self.ui.lineEdit_text_phone.setText("")
        self.ui.lineEdit_text_home.setText("")
        self.ui.label_image_name.clear()
        self.ui.label_image_phone.clear()
        self.ui.label_image_home.clear()

    def start_orc(self):
        # load image file path
        all_file_name = os.listdir(Config.Global.orc_folder)

        if all_file_name is None:
            return

        image_path = all_file_name[0]

        # set now image path
        self.now_image_path = os.path.realpath(os.path.join(Config.Global.orc_folder, image_path))

        # set app file name info
        self.ui.label_text_filename.setText(image_path.split(".")[0])

        print("start orc")

        data_orc = School_Data_ORC.School_Data_ORC()
        datas = data_orc.get_orc_text(os.path.realpath(os.path.join(Config.Global.orc_folder, image_path)), False)
        data_text = datas[0]
        data_image = datas[1]
        self.ui.lineEdit_text_name.setText(data_text[0])
        self.ui.lineEdit_text_phone.setText(data_text[1])
        self.ui.lineEdit_text_home.setText(data_text[2])

        for index, image in enumerate(data_image):
            label_size = self.ui.label_image_name.size()
            q_map = QPixmap.fromImage(ImageQt.ImageQt(image))
            q_map = q_map.scaled(label_size.width(), label_size.height(), QtCore.Qt.KeepAspectRatio,
                                 QtCore.Qt.SmoothTransformation)
            data_image[index] = q_map

        self.ui.label_image_name.setPixmap(data_image[0])
        self.ui.label_image_phone.setPixmap(data_image[1])
        self.ui.label_image_home.setPixmap(data_image[2])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = QtWindows()
    windows.show()
    sys.exit(app.exec())
