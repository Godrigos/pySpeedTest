import json
from os.path import exists
from settings import directory
from datetime import datetime
from src.tz_converter import tz_converter

def results_to_tsv(filepath: str) -> None:
    """
    results_to_csv creates a tab separated value file to append
    the speedtest results to.

    Paramenters
    -----------
    filepath : str
        A valid file path to save the file to. You must have write
        permission to such path.
    """
    
    try:
        with open(f'{directory}/data/results.json', mode = 'rt') as file:
            data = json.load(file)
        file.close()
    except:
        exit(f'{datetime.now()} - Error reading file results.json')
    else:
        try:
            if not exists(filepath):
                with open(filepath, mode = 'w+') as file:
                    file.write(
                        'Date'
                        '\tISP'
                        '\tIP'
                        '\tServer'
                        '\tLocation'
                        '\tLatency (ms)'
                        '\tDownload Speed (Mbps)'
                        '\tDownload Size (MB)'
                        '\tDownload Latency (ms)'
                        '\tUpload Speed (Mbps)'
                        '\tUpload Size (MB)'
                        '\tUpload Latency (ms)'
                        '\tPacket Loss (%)'
                        '\tId'
                        '\n')
                file.close()
        except:
            exit(f'{datetime.now()} - Error creating file {filepath}')

        try:
            with open(filepath, mode = 'at') as file:
                file.write(
                    f"{tz_converter(data['timestamp'], 'America/Sao_Paulo')}"
                    f"\t{data['isp']}"
                    f"\t{data['interface']['externalIp']}"
                    f"\t{data['server']['name']}"
                    f"\t{data['server']['location']}"
                    f"\t{data['ping']['latency']}"
                    f"\t{data['download']['bandwidth']/125000}"
                    f"\t{data['download']['bytes']/1000000}"
                    f"\t{data['download']['latency']['iqm']}"
                    f"\t{data['upload']['bandwidth']/125000}"
                    f"\t{data['upload']['bytes']/1000000}"
                    f"\t{data['upload']['latency']['iqm']}"
                    f"\t{data['packetLoss']}"
                    f"\t{data['result']['id']}"
                    "\n")
            file.close()
        except:
            exit(f'{datetime.now()} - Error writing data to {filepath}')