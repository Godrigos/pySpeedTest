#!/usr/bin/env python3

from src.speedtest import speedtest
from src.read_json import results_to_tsv
from settings import directory
import argparse

parser = argparse.ArgumentParser(
    prog = 'SpeedTest',
    description = 'Internet connection speed test.',
    epilog = 'Source executable by Ookla, LLC.'
)
parser.add_argument(
    '-o', '--output',
    help = 'Full path to file where data will be saved. Defaults to '
    f'{directory}/data/results.csv',
    type = str,
    nargs = 1,
    metavar = 'filepath',
    default = f'{directory}/data/results.csv'
    )
args = parser.parse_args()

def main() -> None:
    speedtest()
    results_to_tsv(args.output)

if __name__ == "__main__":
    main()