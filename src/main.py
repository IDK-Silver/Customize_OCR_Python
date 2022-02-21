import os
import shutil
from libraries import School_Data_ORC
from libraries import Config
from src.widget.mainwindow import QtWindows
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = QtWindows()
    windows.show()
    sys.exit(app.exec())
    # Data_ORC = School_Data_ORC.School_Data_ORC()
    # for image_path in os.listdir(Config.Global.orc_folder):
    #     if Data_ORC.get_orc_text(os.path.realpath(os.path.join(Config.Global.orc_folder, image_path)), True):
    #         try:
    #             shutil.move(os.path.join(Config.Global.orc_folder, image_path), Config.Global.success_folder)
    #         except:
    #             os.remove(os.path.join(Config.Global.orc_folder, image_path))
    #     else:
    #         try:
    #             shutil.move(os.path.join(Config.Global.orc_folder, image_path), Config.Global.failed_folder)
    #         except:
    #             os.remove(os.path.join(Config.Global.orc_folder, image_path))
