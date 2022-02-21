import os
import shutil
from libraries import School_Data_ORC
from libraries import Config

if __name__ == '__main__':
    Data_ORC = School_Data_ORC.School_Data_ORC()
    for image_path in os.listdir(Config.Global.orc_folder):
        if Data_ORC.get_orc_text(os.path.realpath(os.path.join(Config.Global.orc_folder, image_path)), True):
            try:
                shutil.move(os.path.join(Config.Global.orc_folder, image_path), Config.Global.success_folder)
            except:
                os.remove(os.path.join(Config.Global.orc_folder, image_path))
        else:
            try:
                shutil.move(os.path.join(Config.Global.orc_folder, image_path), Config.Global.failed_folder)
            except:
                os.remove(os.path.join(Config.Global.orc_folder, image_path))
