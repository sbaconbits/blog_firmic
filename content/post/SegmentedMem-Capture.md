+++
date = "2020-04-04T13:00:00+01:00"
draft = true
title = "O-Scope Segmented memory: Capture"
tags = ["keysight","oscope","1000-x-series","dsox1204"]
categories= ["oscope-segmented-memory"]
banner = "banners/oscope_segmented_banner.png"
+++

Segmented memory on an oscilloscope is really useful.

<!--more-->

# Intro
I've recent got a new oscolloscope which has a really useful feature called segmented memory. This allows for the capture of short-lived, triggered events in high detail. This works by effectively using the sample memory in the oscilloscope only for the data we care about and discarding the rest.

This video from keysight explains the feature in more detail:
{{< youtube GAM_CpxVYq8 >}}

# Setup
I setup a simple experiment by connecting a small speaker directly to the oscilloscope and triggering the scope by flicking the cone of the speaker. This is a short lived event that occurs with large time delays between events.

Once the trigger has been setup correctly, the number of segments need to be selected. The sample memory is split over this number of segments. Once the segments have been captured you can select between the segments as seen here:

![](/images/speaker_flick_capture.gif)

This gif image was created by saving a number of images over the scope's network connection.

The scope i'v been using is from the keysight 1000-x series, found here:


https://www.keysight.com/en/pcx-2759552/infiniivision-1000-x-series-oscilloscopes?nid=-32110.0&cc=GB&lc=eng

