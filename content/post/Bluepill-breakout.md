+++
date = "2019-02-10T13:00:00+01:00"
draft = true
title = "Bluepill breakout"
tags = ["stm32","bluepill","gerber"]
categories= ["bluepill"]
banner = "banners/bluepill_breakout_real.jpg"
+++

My handy breakout board for the [bluepill](https://wiki.stm32duino.com/index.php?title=Blue_Pill)

<!--more-->

My new favourite board for small projects is the [bluepill](https://wiki.stm32duino.com/index.php?title=Blue_Pill). I find bread boards and dupont hook up cables to be unreliable and I would prefer most of my project to be more permanent, so i've designed a handy breakout board to ease the creation of new designs. You can see the final board above.

This board has the following features:

* Breakout for every pin which is clearly labelled and can be easily cut if required.
* Top copper pour is connected to 3V3 and can be accessed close to each IO pin.
* Bottom copper pour is connected to ground and can be accessed close to each IO pin.
* USART1 has a separate connection at the bottom left to be connected to a [FTDI cable](https://www.ftdichip.com/Products/Cables/RPi.htm)
* Prototyping areas in each corner of the board.

Here is a photo of the board in use with the stlink programmer and a UART to USB cable connected.
![Bluepill breakout in use](/images/bluepill_breakout_use.jpg)

The board is 2-layer, here is a render of the top layer:
![Bluepill breakout render front](/images/bluepill_breakout_front.png)
And here is a render of the bottom layer:
![Bluepill breakout render back](/images/bluepill_breakout_back.png)

I had cheap boards made at [JLCPCB](https://jlcpcb.com/) using the files below and they work very well for my needs:

[Gerber files](/images/bluepill_breakout_gerbers.zip)

