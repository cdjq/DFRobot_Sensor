# DFRobot_Sensor

- [中文版](./README_CN.md)

数据手册上抄一下芯片的描述

这里写模块介绍，做到读完这段，就能对模块有初步了解，让客户懂的用这个模块能干什么（数据手册通常比较官方，这里你可以举例子，更场景化）<br>
这个模块的优点，告诉用户为什么要购买这个模块。一些关键术语，我们要在readme中有解释

这里需要显示拍照图片，可以一张图片，可以多张图片（不要用SVG图）

![产品效果图](../../resources/images/SEN0001.png)


## 产品链接（链接到中文商城）

    SKU：产品名称

## 目录

  * [概述](#概述)
  * [库安装](#库安装)
  * [方法](#方法)
  * [兼容性](#兼容性)
  * [历史](#历史)
  * [创作者](#创作者)

## 概述

这里填写当前Python软件库完成了基础功能，特色功能

## 库安装

要使用这个库，首先将库下载到Raspberry Pi，然后打开例程文件夹。要执行一个例程demox.py，请在命令行中输入python demox.py。例如，要执行control_led.py例程，你需要输入:

```python
python control_led.py
```



## 方法

```python
  '''!
    @brief   开始函数，探测传感器是否正常连接
    @return  初始化成功，返回ERR_OK，失败返回对应的错误码
  '''
  def begin(self):

  '''! 
    @brief   读取声音强度，单位为DB
    @return  声音强度，单位为DB
  '''
  def sound_strength_db(self):

  '''! 
    @brief   读取光线强度，单位为Lux
    @return  光线强度，单位为Lux
  '''
  def light_strength_lux(self):
  
  '''!
    @brief   切换模式
    @param mode 模式，参考模式枚举值
  '''
  def switch_mode(self, mode):

  '''!
    @brief   设置灯的颜色
    @param r 红色分量，范围0-255
    @param g 绿色分量，范围0-255
    @param b 蓝色分量，范围0-255
  '''
  def set_led(self, r, g, b):

  '''!
    @brief   设置灯的颜色
    @param color RGB565的值
  '''
  def set_led(self, color):
```

## 兼容性



| 主板         | 通过 | 未通过 | 未测试 | 备注 |
| ------------ | :--: | :----: | :----: | :--: |
| RaspberryPi2 |      |        |   √    |      |
| RaspberryPi3 |      |        |   √    |      |
| RaspberryPi4 |  √   |        |        |      |

* Python 版本

| Python  | 通过 | 未通过 | 未测试 | 备注 |
| ------- | :--: | :----: | :----: | ---- |
| Python2 |  √   |        |        |      |
| Python3 |  √   |        |        |      |

## 历史

- 2019/06/25 - 1.0.0 版本
- 2021/10/08 - 1.0.1 版本

## 创作者

Written by Alexander(ouki.wang@dfrobot.com), 2019. (Welcome to our [website](https://www.dfrobot.com/))
