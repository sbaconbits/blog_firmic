
import argparse
import numpy as np
import matplotlib.pyplot as plt

def plot_file(fn_list):

    fig, ax1 = plt.subplots()

    for fn in fn_list.split(" "):
        data = np.load(fn)
        ax1.plot(data[:,0], data[:,1:], "b-", alpha=0.2)

    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    parser = argparse.ArgumentParser(description='Plot npy file')
    parser.add_argument('--in', help='Input file', required=True)

    args = parser.parse_args()
    args_dict = vars(args)

    plot_file(args_dict['in'])


main()
