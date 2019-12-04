""" file switch_mode.py
  # @brief 各种模式切换
  # @n 实验现象：演示各种模式切换，保证板子正常工作
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
  ret=0
  #为了完成xxx任务，先切换到正常功耗模式, 
  if((ret = sensor.switch_mode(sensor.eNormalPower)) != 0):
    print("切换到eNormalPower失败 ret=%d"%(ret))

  #为了完成xxx任务，切换到高速度模式
  if((ret = sensor.switchMode(sensor.eHighSpeed)) != 0):
    print("切换到eNormalPower失败 ret=%d"%(ret))
  
  #为了完成xxx任务，切换到正常速度模式
  if((ret = sensor.switchMode(sensor.eNormalSpeed)) != 0):
    print("切换到eNormalPower失败 ret=%d"%(ret))
  
  #为了完成xxx任务，切换到低功耗模式
  if((ret = sensor.switchMode(sensor.eLowPower)) != 0):
    print("切换到eNormalPower失败 ret=%d"%(ret))

  #为了完成xxx任务，切换到eNormalPower+eHighSpeed模式
  if((ret = sensor.switchMode(sensor.eNormalPower+sensor.eHighSpeed)) != 0):
    print("切换到eNormalPower失败 ret=%d"%(ret))

  #为了完成xxx任务，切换到eHighPrecision+eNormalSpeed模式
  if((ret = sensor.switchMode(sensor.eHighPrecision+sensor.eNormalSpeed)) != 0):
    print("切换到eNormalPower失败 ret=%d"%(ret))

  v = sensor.sound_strength_db()
  print("sound strength= %ddB"%(v))
  time.sleep(1)


if __name__ == "__main__":
  setup()
  while True:
    loop()
