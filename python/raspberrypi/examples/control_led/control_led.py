'''!
  @file control_led.py
  @brief 控制LED颜色值
  @n 实验现象：板载LED灯每秒钟切换一次颜色
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author      Alexander(ouki.wang@dfrobot.com)
  @version     V1.0.0
  @date        2017-10-9
  @url https://github.com/DFRobot/DFRobot_Sensor
'''

import time
from DFRobot_Sensor import *

sensor = DFRobot_Sensor_IIC(0,DFRobot_Sensor_IIC.eLowPower+DFRobot_Sensor_IIC.eHighSpeed)

def setup():
  while sensor.begin() != 0:
    print("初始化芯片失败，请确认芯片连接是否正确")

def loop():
  '''
    set_led函数用于点亮LED，可以直接指定颜色，如下参数都是可用的
    COLOR_RGB565_BLACK  COLOR_RGB565_NAVY  COLOR_RGB565_DGREEN  COLOR_RGB565_DCYAN   COLOR_RGB565_PURPLE
    COLOR_RGB565_MAROON COLOR_RGB565_OLIVE COLOR_RGB565_LGRAY   COLOR_RGB565_DGRAY   COLOR_RGB565_BLUE  
    COLOR_RGB565_GREEN  COLOR_RGB565_CYAN  COLOR_RGB565_RED     COLOR_RGB565_MAGENTA COLOR_RGB565_YELLOW      
    COLOR_RGB565_WHITE
  '''
  sensor.set_led(COLOR_RGB565_PURPLE)
  time.sleep(1000)
  sensor.set_led(COLOR_RGB565_YELLOW)
  time.sleep(1000)

  '''
    setLED函数用于点亮LED，可以通过配置RGB分量，显示特定颜色
      r g b 分量的范围都是0-255
  '''
  sensor.set_led(/*r=*/50, /*g=*/0,  /*b=*/0)
  time.sleep(1000)
  sensor.set_led(0,  50, 0)
  time.sleep(1000)
  sensor.set_led(0,  0,  50)
  time.sleep(1000)

if __name__ == "__main__":
  setup()
  while True:
    loop()
