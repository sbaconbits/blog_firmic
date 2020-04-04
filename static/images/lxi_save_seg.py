# Use in venv3
import vxi11
import time
import requests
import numpy as np
import os

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


def main():
    do_save_segs("speaker_flick", 10)

main()
