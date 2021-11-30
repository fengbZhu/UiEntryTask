import base64
import os
import random

import cv2

from conf.setting import WEBPICTUREPATH


class Tool(object):
    def __init__(self):
        self.filelist = os.listdir(WEBPICTUREPATH)

    def error_picture(self):
        picture = []
        for item in self.filelist:
            if item.endswith('.jpg'):
                picture.append((item,))
        return picture

    def clear_picture(self):
        list(map(os.remove, map(lambda file: WEBPICTUREPATH + file, self.filelist)))

    def save_picture(self, src, name):
        res_img_data = src.strip("data:image/jpeg;base64")
        img_data = base64.urlsafe_b64decode(res_img_data + '=' * (4 - len(res_img_data) % 4))
        abs_img = WEBPICTUREPATH + os.path.sep + name
        f = open(abs_img, "wb")  # 保存图片
        f.write(img_data)
        f.close()

    def findpic(self, target='background.png', template='slider.png'):
        """
        :param target: 背景图路径
        :param template: 滑块图片路径
        :return:
        """
        target_rgb = cv2.imread(target)
        target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
        template_rgb = cv2.imread(template, 0)
        res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)  # 模板匹配，在大图中找小图
        value = cv2.minMaxLoc(res)
        a, b, c, d = value
        if abs(1 + a) >= abs(b):
            distance = c[0]
        else:
            distance = d[0]
        # print(value)
        # print(distance)
        return int(distance)

    def get_tracks(self, distance):
        """
        :param distance: 缺口距离
        :return: 轨迹
        """
        # 分割加减速路径的阀值
        value = round(random.uniform(0.55, 0.75), 2)
        # 划过缺口 20 px
        distance += 20
        # 初始速度，初始计算周期， 累计滑动总距
        v, t, sum = 0, 0.3, 0
        # 轨迹记录
        plus = []
        # 将滑动记录分段，一段加速度，一段减速度
        mid = distance * value
        while sum < distance:
            if sum < mid:
                # 指定范围随机产生一个加速度
                a = round(random.uniform(2.5, 3.5), 1)
            else:
                # 指定范围随机产生一个减速的加速度
                a = -round(random.uniform(2.0, 3.0), 1)
            s = v * t + 0.5 * a * (t ** 2)
            v = v + a * t
            sum += s
            plus.append(round(s))

        # end_s = sum - distance
        # plus.append(round(-end_s))

        # 手动制造回滑的轨迹累积20px
        # reduce = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1]
        reduce = [-6, -4, -6, -4]
        return {'plus': plus, 'reduce': reduce}

tool = Tool()

if __name__ == '__main__':
    tool = Tool()
    src = 'data:image/jpeg;base64,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'
    tool.save_picture(src=src, name='aaa.jpg')
