# coding:utf-8
import cv2
import time

from utils import time_now_str

# capture = cv2.VideoCapture(0)
#
# print capture.isOpened()
#
# if capture.isOpened():
#     ret, img = capture.read()
#     cv2.imwrite(time_now_str()+'.jpg', img)
#     capture.release()


class Divineye(object):
    def __init__(self, img_save_path='/home/pi/what_i_see/', per_img_interval=5):
        self.capture = cv2.VideoCapture(0)
        self.img_save_path = img_save_path
        self.per_img_interval = per_img_interval    # 间隔时间, 单位为秒

    def save_img(self):
        ret, img = self.capture.read()
        cv2.imwrite(self.img_save_path + time_now_str()+'.jpg', img)
        self.capture.release()

# if __name__ == '__main__':
#     while True:
#         divineye = Divineye()
#         divineye.save_img()
#         time.sleep(PER_IMG_INTERVAL)