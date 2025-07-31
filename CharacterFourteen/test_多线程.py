import threading
import time


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing, args=("我要唱歌 哈哈哈", ))

    dance_thread = threading.Thread(target=dance, kwargs={"msg": "我在跳舞哦 啦啦啦"})

    sing_thread.start()
    dance_thread.start()