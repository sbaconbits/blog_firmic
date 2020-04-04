+++
date = "2020-04-04T14:00:00+01:00"
draft = true
title = "O-Scope Segmented memory: Automation"
tags = ["keysight","oscope","1000-x-series","dsox1204"]
categories= ["oscope-segmented-memory"]
banner = "banners/oscope_segmented_banner.png"
+++

Save segmented memory on an oscilloscope automatically via a network.

<!--more-->

# Intro
In my previous blog post I mentioned how useful segmented memory is.

In the most recent version of firmware for my oscilloscope, Keysight have added extra functionality to this range of scopes. The scope can now be controlled via [SCPI](https://en.wikipedia.org/wiki/Standard_Commands_for_Programmable_Instruments) commands. It is now possible to save scope data over the network.

I was trying to "save" multiple segments at full resolution as CSV files via a script for some signal analysis that i've been doing. This was causing trouble as the combined file was so large the connection kept timing out, but I knew with the ability to control the scope using SCPI I had other options.

# Automating multi-segment CSV download

My goal was to be able to programmatically download multiple segments as csv files, one at a time. By doing this I could do something similar to the plot below which overlays each segment into one plot which is very useful to visualise a repeating pattern in a signal.

![](/images/speaker_flick_plot.png)

The following python code uses the [LXI](https://en.wikipedia.org/wiki/LAN_eXtensions_for_Instrumentation) interface on the scope to perform the above operations. The code executes as follows:

* Enumerates LXI devices on the network (I only have one)
* Send a few SCPI commands to configure the scope for the correct type of download ("Save").
* Select the segment index via SCPI.
* Downloads the CSV file via the HTTP interface (this may also be possible via SCPI).
* Convert the files to npy formation for efficiency reasons.
* Delete the csv file.

{{< highlight python>}}
def do_save_segs(run_name, seg_count):
    # Search for oscope
    device_list = vxi11.list_devices()
    print("List devices:")
    print(device_list)
    # Will throw exception if none exist
    instr = vxi11.Instrument(device_list[0])

    def send_scpi(cmd, delay=0.5):
        time.sleep(delay)
        print("Sending command: " + cmd)
        instr.write(cmd)

    def save_seg(folder, name):
        ip_addr = str(device_list[0])
        save_url = "http://" + ip_addr + "/infiniivision/SaveDownload.php"
        # Download a single segment at max length
        save_params = {'filename' : name,
                       'p1': "8",   # CSV file format
                       'p2': "-1",  # Maximum length
                       'command' : "save_execute"}
        full_name = folder + name
        print("GET filename " + full_name)
        r = requests.get(url=save_url, params=save_params)
        with open(full_name, "wb") as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
        print("Save result:" + str(r))

    # Configure oscope
    send_scpi(":save:waveform:format csv")
    send_scpi(":save:waveform:segmented current")

    for s in range(1, seg_count+1):
        # Select segment
        send_scpi(":acquire:segmented:index {}".format(s))

        # Get Segment data over HTTP
        fn = run_name + "_seg_{:02d}.csv".format(s)
        folder = "/tmp/"
        save_seg(folder, fn)

        # Convert to npy
        data = np.genfromtxt(folder + fn, delimiter=',', skip_header=1)
        npy_fn = fn.replace(".csv", ".npy")
        np.save(folder + npy_fn, data)

        # Delete the CSV file
        os.remove(folder + fn)

{{< /highlight >}}
![lxi_save_seg.py](/images/lxi_save_seg.py)

Here is a very simple script to plot a number of npy files on the same axis:

{{< highlight python>}}
def plot_file(fn_list):

    fig, ax1 = plt.subplots()

    for fn in fn_list.split(" "):
        data = np.load(fn)
        ax1.plot(data[:,0], data[:,1:], "b-", alpha=0.2)

    plt.legend()
    plt.grid(True)
    plt.show()
{{< /highlight >}}
![plot_npy.py](/images/plot_npy.py)

# Conclusion
There are probably a number of ways to achieve the above results, but this method has proven to be successful so I'm happy with it.

I think having support for these SCPI commands and the ability to save raw data over a network connection make this oscilloscope incredibly useful.


