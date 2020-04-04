+++
date = "2020-03-05T13:00:00+01:00"
draft = true
title = "Reflow LED Death"
tags = ["reflow","apa102"]
categories= ["reflow-problem"]
banner = "banners/led_dead_banner.png"
+++

I've killed many LED's in my reflow oven.

<!--more-->

# Problem
Before I had a reflow oven I used to solder these addressable LED's with a soldering iron and it never seemed to cause any troubles. I wasn't careful when handing these components.

When I started to reflow these same components many of them started to fail, about 1/4 of them.

Before I reflowed them they looked like this under the microscope.
![Happy LED](/images/led_death_before.jpg)

Once reflowed, some of them looked like this:
![Fresh death of LED](/images/led_death_clean.jpg)

To see the problem better I used a sharpie pen to highlight the crack:
![Highlighted death of LED](/images/led_death_highlight.jpg)

This image highlights the shear in the gel covering the LED die. It seemed to be caused due to the plastic package pulling in moisture, when the component was put in the reflow over it must have generated steam that pushed the die up from the substrate. 

## Others have seen the same problem
* https://wp.josh.com/2016/10/29/a-quick-test-for-crappy-ws2812b-neopixels/
* https://electronics.stackexchange.com/questions/99672/why-must-integrated-circuits-be-baked-in-the-oven-before-being-used-on-a-proto

# Solution
Once I found out what the problem was I put all of my LED's in a container of a "Tub Fine Pure White Silica Gel Desiccant Granules For Flower" from ebay for a week. After the LED's had fully dried out they all reflowed without a problem.



