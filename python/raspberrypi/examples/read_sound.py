'''!
  @file read_sound.py
  @brief 读取环境声音强度，单位DB
  @n 实验现象：每秒读取一次环境光线强度，并打印到串口
  @n 给传感器以不同的光照强度，可以得到不同的采集结果
  @n 由于只有4 bits存放声音强度，最低分辨率8dB，所以测量范围是 0dB-120dB
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author      Alexander(ouki.wang@dfrobot.com)
  @version     V1.0
  @date        2017-10-9
  @url https://github.com/DFRobot/DFRobot_Sensor
'''

import time
from DFRobot_Sensor import *

sensor = DFRobot_Sensor_IIC(0,DFRobot_Sensor_IIC.LOW_POWER)

def setup():
  while sensor.begin() != 0:
    print("初始化芯片失败，请确认芯片连接是否正确")


def loop():
  #读取声音强度
  sound_strength = sensor.sound_strength_db()
  Serial.print("sound strength= %ddB"%(sound_strength))
  time.sleep(1)

if __name__ == "__main__":
  setup()
  while True:
    loop()