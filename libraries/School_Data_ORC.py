import os
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import cv2
from paddleocr import PaddleOCR, draw_ocr
from opencc import OpenCC
import shutil
import libraries.Config
import libraries.Image_Similarity
import numpy
from libraries import Config, Image_Similarity


class Data:
    class Json_Key:
        name_crop_info = "name_crop_info"
        phone_crop_info = "phone_crop_info"
        home_crop_info = "home_crop_info"
        check_crop_info = "check_crop_info"

    name_crop_info = ()
    phone_crop_info = ()
    home_crop_info = ()
    check_crop_info = ()


def clear_console():
    for i in range(50):
        print()


class School_Data_ORC:

    def __init__(self):
        pass

    def ocr_image(self, input_image):
        ocr = PaddleOCR(use_angle_cls=True, lang="chinese_cht")
        result = ocr.ocr(input_image, cls=True)
        return result

    # def set_orc_image(self, input_image):
    #     ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    #     result = ocr.ocr(input_image, cls=True)
    #     return result

    def get_orc_text(self, image_path):
        # config
        config = Config.Config_Json("json.json")
        config_types = config.read(Config.Key.types.key)

        # read image
        cv2_input_image = cv2.imread(image_path)

        # conversion cv2 format to pil
        pil_image = Image.fromarray(cv2.cvtColor(cv2_input_image, cv2.COLOR_BGR2RGB))

        # rotary image
        (w, h) = pil_image.size
        if w < h:
            print("rotary image")
            pil_image = pil_image.transpose(Image.ROTATE_90)

        image_type = 0

        for index, check_type in enumerate(config_types):
            print(Config.Global.check_folder + "/" + str(index) + ".TIF")
            sensitive_pic = pil_image.crop(check_type[Config.Key.types.struct_datas.check_crop_info])
            # plt.imshow(sensitive_pic)
            # plt.show()
            print(Config.Global.check_folder)
            target_pic = Image.open(Config.Global.check_folder + "/" + str(index) + ".png")
            if Image_Similarity.is_imgs_similar(sensitive_pic, target_pic):
                image_type = index
                break
        print(image_type)

        # crop name part image
        image_name = pil_image.crop(config_types[image_type][Config.Key.types.struct_datas.name_crop_info])
        # (w, h) = image_name.size
        # image_name = image_name.resize((w * 5, h * 5))
        # image_name = image_name.filter(ImageFilter.BLUR)

        # crop phone part image
        image_phone = pil_image.crop(config_types[image_type][Config.Key.types.struct_datas.phone_crop_info])
        # (w, h) = image_phone.size
        # image_phone = image_phone.resize((w * 5, h * 5))

        # crop home part image
        image_home = pil_image.crop(config_types[image_type][Config.Key.types.struct_datas.home_crop_info])
        # (w, h) = image_home.size
        # image_home = image_home.resize((w * 30, h * 30))
        # image_home = image_home.filter(ImageFilter.BLUR)
        # image_home = image_home.convert('1')

        # show original image
        # plt.imshow(pil_image)
        # plt.show()
        #
        # show name part image
        plt.imshow(image_name)
        plt.show()
        #
        # # show phone part image
        # plt.imshow(image_phone)
        # plt.show()
        # #
        # show home part image
        plt.imshow(image_home)
        plt.show()

        ocr_part = list()
        img_binary = \
            cv2.threshold(cv2.cvtColor(numpy.asarray(image_name), cv2.COLOR_RGB2BGR), 128, 255, cv2.THRESH_BINARY)[1]
        ocr_part.append(self.ocr_image(cv2.cvtColor(numpy.asarray(img_binary), cv2.COLOR_RGB2BGR)))

        img_binary = \
            cv2.threshold(cv2.cvtColor(numpy.asarray(image_phone), cv2.COLOR_RGB2BGR), 128, 255, cv2.THRESH_BINARY)[1]
        ocr_part.append(self.ocr_image(cv2.cvtColor(numpy.array(img_binary), cv2.COLOR_RGB2BGR)))

        img_binary = \
            cv2.threshold(cv2.cvtColor(numpy.asarray(image_home), cv2.COLOR_RGB2BGR), 200, 255, cv2.THRESH_BINARY)[1]
        ocr_part.append(self.ocr_image(img_binary))

        # print(ocr_image(cv2.cvtColor(numpy.array(image_name), cv2.COLOR_RGB2BGR)))
        # print(ocr_image(cv2.cvtColor(numpy.array(image_phone), cv2.COLOR_RGB2BGR)))
        # print(ocr_image(cv2.cvtColor(numpy.array(image_home), cv2.COLOR_RGB2BGR)))

        clear_console()

        print("圖片名稱：%s" % image_path.split(".")[0])

        # for text in ocr_part:
        #     print([line[1][0] for line in text])

        data = list()
        for text in ocr_part:
            text_list = [line[1][0] for line in text]
            for line in text_list:
                data.append(OpenCC("s2tw").convert(line))
                # print(OpenCC("s2tw").convert(line))
        print("姓名   ：%s" % data[0])
        print("電話   ：%s" % data[1])
        print("住址   ：%s" % data[2])

        ans = input("輸入是否正確(Y/N)　：").lower()
        while ans != "y" and ans != "n":
            print("輸入錯誤！")
            ans = input("輸入是否正確(Y/N)　：").lower()

        if ans == "y":
            return True
        else:
            return False
