import json
import os

class Global:
    orc_folder = os.path.join(os.path.realpath("./"), "orc_folder")
    failed_folder = os.path.join(os.path.realpath(""), "failed_image")
    success_folder = os.path.join(os.path.realpath(""), "success_image")
    check_folder = os.path.join(os.path.realpath(""), "check_image")


class Config_Json:
    def __init__(self, file_path):
        self.file_path = file_path
        self.json = dict()
        self.path = []

    def at(self, key):
        self.path.append(key)

    def read(self, key):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            if key == "" or key is None:
                return data
            else:
                return data[key]

    def write(self, write_json):
        with open(self.file_path, 'w') as file:
            json.dump(write_json, file)

    def generate_default_json(self, generate_obj):
        self.json = generate_obj.get_default_json()
        with open(self.file_path, 'w') as file:
            json.dump(self.json, file)


class Key:
    class types:
        key = "types"

        class struct_datas:
            name_crop_info = "name_crop_info"
            phone_crop_info = "phone_crop_info"
            home_crop_info = "home_crop_info"
            check_crop_info = "check_crop_info"

    class folder:
        key = "folder"

        class failed_image:
            key = "failed_image"

        class orc_folder:
            key = "orc_folder"

    def get_default_json(self):
        data_json = dict()
        data_json[self.types.key] = []
        data_json[self.folder.key] = {}
        data_json[self.folder.key][self.folder.failed_image.key] = "failed_image"
        return data_json


if "__main__" == __name__:
    pass
    # config = Config_Json("json.json")
    # config.generate_default_json(Key())
    # data_json = config.read("")
    # print(data_json)
    #
    # # Type 1
    # types_dict = {Key.types.struct_datas.name_crop_info: (625, 145, 1020, 225),
    #               Key.types.struct_datas.phone_crop_info: (625, 380, 1020, 465),
    #               Key.types.struct_datas.home_crop_info: (270, 445, 1020, 520),
    #               Key.types.struct_datas.check_crop_info: (0, 0, 3500, 2400)}
    #
    # data_json[Key.types.key].append(types_dict)
    #
    # # Type 2
    # types_dict = {Key.types.struct_datas.name_crop_info: (625, 145, 1020, 225),
    #               Key.types.struct_datas.phone_crop_info: (625, 380, 1020, 465),
    #               Key.types.struct_datas.home_crop_info: (270, 445, 1020, 520),
    #               Key.types.struct_datas.check_crop_info: (0, 0, 3500, 2400)}
    #
    # data_json[Key.types.key].append(types_dict)
    #
    # print(data_json)
    # config.write(data_json)
    # print(config.read(Key.types.key))
