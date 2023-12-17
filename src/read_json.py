import json
from os.path import exists
from settings import directory

def results_to_tsv(filepath: str) -> None:
    """
    results_to_csv creates a tab separated value file to append
    the speedtest results to.

    Paramenters
    -----------
    filepath : str
        A valid file path to save the file to. You must have write
        access to such path.
    """
    
    try:
        with open(f'{directory}/data/results.json', mode = 'rt') as file:
            data = json.load(file)
    except:
        exit('Error reading file results.json')
    else:

        if not exists(filepath):
            with open(filepath, mode = 'w+') as file:
                file.write('Date\tISP\tIP\tServer\tLocation	Latency (ms)\tDownload Speed (Mbps)\tDownload Latency (ms)\tUpload Speed (Mbps)\tUpload Latency (ms)\tPacket Loss (%)\tId\n')

        try:
            with open(filepath, mode = 'at') as file:
                file.write(f"{data['timestamp']}\t{data['isp']}\t{data['interface']['externalIp']}\t{data['server']['name']}\t{data['server']['location']}\t{data['ping']['latency']}\t{data['download']['bandwidth']/125000}\t{data['download']['latency']['iqm']}\t{data['upload']['bandwidth']/125000}\t{data['upload']['latency']['iqm']}\t{data['packetLoss']}\t{data['result']['id']}\n")
        except:
            exit(f'Error writing data to {filepath}')