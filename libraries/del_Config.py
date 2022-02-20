import os
import json
import configparser


class ConfigInfo:

    def __init__(self) -> None:
        pass

    class Global:
        orc_folder = os.path.join(os.path.realpath("check_image"))
        failed_folder = "failed_image"
        success_folder = "success_image"
        check_image = "check_image"

        def __init__(self):
            path = os.path
            self.orc_folder = os.path.join(os.path.realpath(""), self.orc_folder)
            self.failed_folder = os.path.join(os.getcwd(), self.failed_folder)
            self.success_folder = os.path.join(os.getcwd(), self.success_folder)
            self.check_image = os.path.join(os.getcwd(), self.check_image)

    class Type_One_Image:
        section = "Type_One_Image"
        file_path = "setting.ini"

        class key:
            name_crop_site = "name-crop-info"
            phone_crop_site = "phone-crop-info"
            home_crop_site = "home-crop-info"
            check_crop_site = "check-crop-info"

        def create_default_config(self, file_path, config_obj):
            config_obj[self.section] = {}
            data = list()

            data = [625, 145, 1020, 225]
            config_obj[self.section][self.key.name_crop_site] = str(data)

            data = [625, 380, 1020, 465]
            config_obj[self.section][self.key.phone_crop_site] = str(data)

            data = [270, 445, 1020, 520]
            config_obj[self.section][self.key.home_crop_site] = str(data)

            data = [2830, 560, 2950, 670]
            config_obj[self.section][self.key.check_crop_site] = str(data)

            with open(file_path, 'w') as file:
                config_obj.write(file)

    class Type_Two_Image:
        section = "Type_One_Image"
        file_path = "setting.ini"

        class key:
            name_crop_site = "name-crop-info"
            phone_crop_site = "phone-crop-info"
            home_crop_site = "home-crop-info"
            check_crop_site = "check-crop-info"

        def create_default_config(self, file_path, config_obj):
            config_obj[self.section] = {}
            data = list()

            data = [500, 100, 650, 155]
            config_obj[self.section][self.key.name_crop_site] = str(data)

            data = [510, 305, 930, 360]
            config_obj[self.section][self.key.phone_crop_site] = str(data)

            data = [200, 350, 930, 415]
            config_obj[self.section][self.key.home_crop_site] = str(data)

            data = [2370, 640, 2650, 550]
            config_obj[self.section][self.key.check_crop_site] = str(data)

            with open(file_path, 'w') as file:
                config_obj.write(file)


class APP_Setting:
    def __init__(self, input_file_path, default_section, input_obj) -> None:
        self.default_section = default_section
        self.config_filepath = input_file_path
        self.config = configparser.ConfigParser()
        self.config.read(self.config_filepath, encoding='utf-8')
        self.default_obj = input_obj

        if not os.path.isfile(self.config_filepath):
            self.create_default_config()

    def read(self, key):
        return self.config[self.default_section][key]

    def create_default_config(self):
        self.default_obj.create_default_config(self.config_filepath, self.config)
        # user_setting = ConfigInfo.UserSetting()
        # self.config[user_setting.sections] = {}
        # self.config[user_setting.sections][user_setting.web_url] = "http://163.32.74.2/web_ap/student_allin/index.asp"
        # self.config[user_setting.sections][user_setting.username] = ""
        # self.config[user_setting.sections][user_setting.password] = ""
        # with open(ConfigInfo.setting_filename, 'w') as configfile:
        #     self.config.write(configfile)

# if __name__ == "__main__":
#     type_1 = APP_Setting("./test.ini", ConfigInfo.Type_One_Image.section, ConfigInfo.Type_One_Image())
