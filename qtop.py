#!bin/bash 
import os
import psutil
import time
from tqdm import tqdm

def main():
    percents = [
            ('Main Memory',     psutil.virtual_memory()[2]),
            ('CPU',             psutil.cpu_percent(interval=1)),
            ('DISK',            psutil.disk_usage('/')[3])
            ]


    max_value = max(count for _, count in percents)
    increment = max_value / 25

    longest_label_length = max(len(label) for label, _ in percents)

    for label, count in percents:

        bar_chunks, remainder = divmod(int(count * 8 / increment), 8)

        bar = '█' * bar_chunks
        if remainder > 0:
            bar += chr(ord('█') + (8 - remainder))

        bar = bar or  '▏'
        print(f'{label.ljust(longest_label_length + 5)} ▏ {count:0.02f}% |{bar}', '\n')
    time.sleep(3)
    os.system('clear')
    main()


main()
