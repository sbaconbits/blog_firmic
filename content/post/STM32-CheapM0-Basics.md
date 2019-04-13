+++
date = "2019-04-13T13:00:00+01:00"
draft = true
title = ""
tags = ["stm32","cortex-m0","stm32f030","STM32F030F4P6","stlink"]
categories= ["Cortex-M0"]
banner = "banners/stm32_m0_board.png"
+++

My first look at this really cheap Cortex-M0 development board.

<!--more-->

# Introduction
I was looking for a new cheap and low-ish power microcontroller and I found this [Aliexpress dev board](https://www.aliexpress.com/item/STM32F030F4P6-Small-Systems-Development-Board-CORTEX-M0-Core-32bit-Mini-System-Development-Panels-48-MHz/32742017601.html). It's current only £0.98 per board, that's pretty cheap and it has a Arm Cortex-M0 in it, it's also available in packages that are quite easy to solder. The same chip is also available at farnell, so it shouldn't be too hard to source them:
[Available at Farnell](https://uk.farnell.com/stmicroelectronics/stm32f030f4p6/mcu-32bit-cortex-m0-48mhz-tssop/dp/2393635).

# Source code
I like to start projects with the absolute minimum amount of code, I also prefer not to use IDE's as I find them mostly just get in the way. I started this project by getting basic register definitions file from ST, creating a simple Makefile and from there created a program to exercise GPIO's and the UART (print debug).

My code is available [here](https://github.com/sbaconbits/STM32F030_dev_board)

## Start up code
The startup code consists of the following and mainly came from STM32Cube:

* Register definitions files.
* linker script.
* Startup assembler to configure the 'C' environment.

### STM32Cube
I hand picked the required files from a file called 'STM32Cube_FW_F0_V1.9.0' from ST, available for download here [STM32Cube](https://www.st.com/en/embedded-software/stm32cubef0.html).

## Clock configuration
In the file 'main.c' (function init()) I configure the MCU clock to use the external 8MHz crystal and PLL to multiply it to 48MHz for the core.

## Toolchain
The toolchain i'm using is GCC from [Arm](https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads), i'm using this version gcc-arm-none-eabi-8-2018-q4-major-linux.tar.bz2.

## My make file
My Make file requires two environment variables to be set:

* STLINK: This should point to a pre-built stlink tool (mentioned below).
* TOOL_BASE_GENERIC : The tool chain mentioned above.

This Makefile can be used to build the entire image and flash it to the target board. This makefile also has a couple of targets for disassembling the built binaries which is useful when debugging or if there are initial startup issues.

# Programming
This board is very easy to program when you have the correct programmer and doesn't require an extra bootloader stage.
## Hardware configuration
The hardware is setup as in the photo above, a ST-Link V2 programmer is connected to the SWD lines and an FTDI UART to USB cable it plugged in to see debug prints on the PC.
## stlink
The programmer used is a ST-link V2, it also powers the board. To find this programmer search for "ST-Link V2 programmer" [Aliexpress link](https://www.aliexpress.com/item/1PCS-ST-LINK-Stlink-ST-Link-V2-Mini-STM8-STM32-Simulator-Download-Programmer-Programming-With-Cover/32792513237.html)
It's worth pointing out that I have several of these programmers and the pinout changes between models, so make sure you check the pinout before powering up.

This programmer requires some software on the PC to run, I use this [Stlink tool](https://github.com/texane/stlink), it works really well and I haven't had any trouble with it.

# Debugging
Even though this chip is really cheap it's also possible to debug it using the hardware mentioned above and GDB running on the PC.

The connection to the device is created using stlink in one terminal as follows:
{{< highlight bash>}}
$> $STLINK/src/gdbserver/st-util
{{< /highlight >}}
NOTE: kill this program before trying to re-program the chip.

And the GDB session is started using the following command:
{{< highlight bash>}}
$> $TOOL_BASE_GENERIC/bin/arm-none-eabi-gdb -x ./gdbinit build/first.elf 
{{< /highlight >}}


# Conclusion
This chip has all of the peripheral you would expect in a modern microcontroller, it's really cheap, easy to source, is easy to debug, available in easy to solder packages and did I mention it's **really cheap**.
