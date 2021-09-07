# DFRobot_Sensor
- [English](./README_.md)

Copy the relevant description about the chip from datasheet. 

Write the module introduction here, including the basic functions (Use examples or application scenes to explain what users can do with this product), the advantages of the module (What makes this product worthy buying) and some key terms. 


Product images (SVG is not recommended here) 

![Product Image](https://github.com/cdjq/DFRobot_Sensor/raw/master/resources/images/SEN0245svg1.png)


## Product Link (Link to DFRobot store)
    SKU: 

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
   * @brief Init function
   * @return Return 0 if init successful, return non-zero when failed
   */
  int begin(void);
  
  /**
   * @brief Get sound intensity 
   * @return Return sound intensity, unit DB
   */
  uint16_t getSoundStrength(void);

  /**
   * @brief Get light intensity 
   * @return Return light intensity, unit lm 
   */
  uint16_t getLightStrength(void);
  
    /**
   * @brief Switch mode 
   * @return Return 0 if successful, return non-zero when failed
   */

  uint8_t switchMode(uint8_t mode);
  /**
   * @brief Set LED color 
     @note  The color setup takes effect after 0.2s 
   * @param r Red channel color value, range 0-255
   * @param g Green channel color value, range 0-255
   * @param b Blue channel color value, range 0-255
   */
   void setLED(uint8_t r, uint8_t g, uint8_t b);

   /**
   * @brief Set LED Color
     @note  The color setup takes effect after 0.2s 
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

- Data 2019-6-25
- Version V0.1


## Credits

Written by Alexander(ouki.wang@dfrobot.com), 2019. (Welcome to our [website](https://www.dfrobot.com/))





