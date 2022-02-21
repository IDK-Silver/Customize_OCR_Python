from functools import reduce
from PIL import Image


# 計算圖片的局部哈希值--pHash
def phash(img):
    """
    :param img: 圖片
    :return: 返回圖片的局部hash值
    """
    img = img.resize((8, 8), Image.ANTIALIAS).convert('L')
    avg = reduce(lambda x, y: x + y, img.getdata()) / 64.
    hash_value = reduce(lambda x, y: x | (y[1] << y[0]), enumerate(map(lambda i: 0 if i < avg else 1, img.getdata())),
                        0)
    print("Check Image Hash：%d" % hash_value)
    return hash_value


# 計算漢明距離:
def hamming_distance(a, b):
    """
    :param a: 圖片1的hash值
    :param b: 圖片2的hash值
    :return: 返回兩個圖片hash值的漢明距離
    """
    hm_distance = bin(a ^ b).count('1')
    print("hamming_distance：%d" % hm_distance)
    return hm_distance


# 計算兩個圖片是否相似:
def is_imgs_similar(img1, img2):
    """
    :param img1: 圖片1
    :param img2: 圖片2
    :return:  True 圖片相似  False 圖片不相似
    """
    return True if hamming_distance(phash(img1), phash(img2)) <= 10 else False


if __name__ == '__main__':
    pass
    # config = Config.Config_Json("json.json")
    #
    #
    # image = cv2.imread("Type_2.TIF")
    # # conversion cv2 format to pil
    # pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    #
    # plt.imshow(pil_image)
    # plt.show()
    #
    # config_types = config.read(Config.Key.types.key)
    # image_check = pil_image.crop(config_types[1][Config.Key.types.struct_datas.check_crop_info])
    #
    # plt.imshow(image_check)
    # plt.show()
    #
    # image_check.save("check-2.png")


    #
    # config = Config.Config_Json("json.json")
    # config_types = config.read(Config.Key.types.key)
    # # 讀取圖片
    # sensitive_pic = Image.open("05.TIF")
    # # sensitive_pic = sensitive_pic.crop(config_types[1][Config.Key.types.struct_datas.check_crop_info])
    # plt.imshow(sensitive_pic)
    # plt.show()
    # target_pic = Image.open("Type_2.TIF")
    #
    # # 比較圖片相似度
    # result = is_imgs_similar(target_pic, sensitive_pic)
    #
    # print(result)