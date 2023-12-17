import subprocess
from settings import directory

def speedtest() -> None:
    """
    speedtest calls the connection speed test and saves the result
    temporarily to a json file in data folder. This file preserves
    only the last test result.
    """
    
    try:
        result = subprocess.run(
            [f'{directory}/vendor/speedtest', '-f', 'json'],
            capture_output=True,
            check=True
            )
    except subprocess.CalledProcessError as e:
        exit('Error testing internet connection.')
    else:
        try:
            with open(f'{directory}/data/results.json', mode = 'wt') as file: 
                file.write(result.stdout.decode('utf-8'))
        except:
            exit('Error saving data.')
