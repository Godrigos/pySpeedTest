from zoneinfo import ZoneInfo
from datetime import datetime

def tz_converter(date: str, tz: str = 'UTC') -> datetime:
    """
    tz_converter converts returned UTC date to UTC-3

    Parameter
    ---------
    date : str 
        A UTC date with format %Y-%m-%dT%H:%M:%SZ.
    tz : str
        IANA zoneinfo code.
    """
    
    try:
        new_date = datetime.strptime(
            date, '%Y-%m-%dT%H:%M:%SZ').replace(
                tzinfo = ZoneInfo("UTC")).astimezone(
                    ZoneInfo(tz)
                    )
        return new_date
    except:
        exit(f'{datetime.now()} - Error converting dates.')