'''!
  @file switch_mode.py
  @brief 各种模式切换
  @n 实验现象：演示各种模式切换，保证板子正常工作
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author      Alexander(ouki.wang@dfrobot.com)
  @version     V1.0.0
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
  ret=0
  #为了完成xxx任务，先切换到正常功耗模式, 
  if((ret = sensor.switch_mode(sensor.NORMAL_POWER)) != 0):
    print("切换到NORMAL_POWER失败 ret=%d"%(ret))

  #为了完成xxx任务，切换到高速度模式
  if((ret = sensor.switchMode(sensor.HIGH_SPEED)) != 0):
    print("切换到HIGH_SPEED失败 ret=%d"%(ret))
  
  #为了完成xxx任务，切换到正常速度模式
  if((ret = sensor.switchMode(sensor.NORMAL_SPEED)) != 0):
    print("切换到NORMAL_SPEED失败 ret=%d"%(ret))
  
  #为了完成xxx任务，切换到低功耗模式
  if((ret = sensor.switchMode(sensor.LOW_POWER)) != 0):
    print("切换到LOW_POWER失败 ret=%d"%(ret))

  #为了完成xxx任务，切换到NORMAL_POWER+HIGH_SPEED模式
  if((ret = sensor.switchMode(sensor.NORMAL_POWER | sensor.HIGH_SPEED)) != 0):
    print("切换到NORMAL_POWER+HIGH_SPEED失败 ret=%d"%(ret))

  #为了完成xxx任务，切换到HIGH_PRECISION+NORMAL_SPEED模式
  if((ret = sensor.switchMode(sensor.HIGH_PRECISION | sensor.NORMAL_SPEED)) != 0):
    print("切换到HIGH_PRECISION+NORMAL_SPEED失败 ret=%d"%(ret))

  v = sensor.sound_strength_db()
  print("sound strength= %ddB"%(v))
  time.sleep(1)


if __name__ == "__main__":
  setup()
  while True:
    loop()
