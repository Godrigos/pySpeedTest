from zoneinfo import ZoneInfo
from datetime import datetime

def tz_converter(date: str) -> datetime:
    """
    tz_converter converts returned UTC date to UTC-3

    Parameter
    ---------
    date : str 
        A UTC date with format %Y-%m-%dT%H:%M:%SZ.
    """
    
    new_date = datetime.strptime(
        date, '%Y-%m-%dT%H:%M:%SZ').replace(
            tzinfo = ZoneInfo("UTC")).astimezone(
                ZoneInfo('America/Sao_Paulo')
                )
    return new_date
