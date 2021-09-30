# DFRobot_Sensor
- [中文版](./README_CN.md)

Copy the relevant description of the chip from the datasheet. 

Write the module introduction here, including the basic functions (Use examples or application scenes to explain what users can do with this product), the advantages of the module (What makes this product worthy buying) and some key terms. 


Product images (SVG is not recommended here) 

![Product Image](./resources/images/SEN0245svg1.png)


## Product Link (Link to DFRobot store)
    SKU: XXXX

## Table of Contents

* [Summary](#summary)
* [Installation](#installation)
* [Methods](#methods)
* [Compatibility](#compatibility)
* [History](#history)
* [Credits](#credits)

## Summary

Introduce the basic and special functions of this Arduino Library. 

## Installation

To use this library, first download the library file, paste it into the \Arduino\libraries directory, then open the examples folder and run the demo in the folder.

## Methods

```C++
  /**
   * @fn begin
   * @brief Init function
   * @return Return 0 if init successful, return non-zero when failed
   */
  int begin(void);
  
  /**
   * @fn getSoundStrength
   * @brief Get sound intensity 
   * @return Return sound intensity, unit DB
   */
  uint16_t getSoundStrength(void);

  /**
   * @fn getLightStrength
   * @brief Get light intensity 
   * @return Return light intensity, unit lm 
   */
  uint16_t getLightStrength(void);
  
  /**
   * @fn switchMode
   * @brief Switch mode 
   * @return Return 0 if successful, return non-zero when failed
   */

  uint8_t switchMode(uint8_t mode);
  /**
   * @fn setLED
   * @brief Set LED color 
   * @note  The color setup takes effect after 0.2s 
   * @param r Red channel color value, range 0-255
   * @param g Green channel color value, range 0-255
   * @param b Blue channel color value, range 0-255
   */
   void setLED(uint8_t r, uint8_t g, uint8_t b);

  /**
   * @fn setLED
   * @brief Set LED Color
   * @note  The color setup takes effect after 0.2s 
   * @param Color value in rgb565 format 
   */
   void setLED(uint16_t color);
```

## Compatibility

MCU                | Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | -----
Arduino uno        |      √       |              |             | 
Mega2560        |      √       |              |             | 
Leonardo        |      √       |              |             | 
ESP32           |      √       |              |             | 
micro:bit        |      √       |              |             | 


## History

- 2019/06/25 - Version 1.0.0 released.
- 2021/09/30 - Version 1.0.1 released.

## Credits

Written by Alexander(ouki.wang@dfrobot.com), 2019. (Welcome to our [website](https://www.dfrobot.com/))





