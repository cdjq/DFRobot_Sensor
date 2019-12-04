""" file read_light.py
  # @brief 读取环境光线强度，单位是勒克斯(Lux)
  # @n 实验现象：每秒读取一次环境光线强度，并打印到串口，给传感器以不同的光照强度，可以得到不同的采集结果
  # @n 由于只有4 bits存放光照强度，最低分辨率1000，所以能采集的范围是 0Lux-150000Lux
  #
  # @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  # @licence     The MIT License (MIT)
  # @author      Alexander(ouki.wang@dfrobot.com)
  # version  V1.0
  # date  2017-10-9
  # @get from https://www.dfrobot.com
  # @url https://github.com/DFRobot/DFRobot_Sensor
"""

import time
from DFRobot_Sensor import *

sensor = DFRobot_Sensor_IIC(0,DFRobot_Sensor_IIC.eLowPower)
 
def setup():
  while sensor.begin() != 0:
    print("初始化芯片失败，请确认芯片连接是否正确")

def loop():
  light_strength = sensor.light_strength_lux()
  print("Light Strength=%d Lux"%(light_strength))
  time.sleep(1)

if __name__ == "__main__":
  setup()
  while True:
    loop()
