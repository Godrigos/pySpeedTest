#!/usr/bin/env python3

from src.speedtest import speedtest
from src.read_json import results_to_tsv
from settings import directory
import argparse

parser = argparse.ArgumentParser(
    prog = 'pySpeedTest',
    description = 'Internet connection speed test.',
    epilog = 'Source executable by Ookla, LLC.'
)
parser.add_argument(
    '-o', '--output',
    help = 'Full path to file where data will be saved. '
    'You must have write permission to such path. '
    f'Defaults to {directory}/data/results.csv',
    type = str,
    metavar = 'filepath',
    default = f'{directory}/data/results.csv'
    )
args = parser.parse_args()

def main() -> None:
    speedtest()
    results_to_tsv(args.output)

if __name__ == "__main__":
    main()