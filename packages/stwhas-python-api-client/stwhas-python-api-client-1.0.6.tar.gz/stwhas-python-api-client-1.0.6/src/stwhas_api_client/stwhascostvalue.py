from datetime import datetime, timezone
from .stwhasinterval import StwhasInterval

class StwHasCostValue:
    time:datetime = None
    interval:StwhasInterval = StwhasInterval.Hour
    baseprice:float = 0.0
    workprice:float = 0.0
    delivery:float = 0.0
    sum:float = 0.0
    interpolated:bool = False

    def __init__(self, jsonData = None, interval:StwhasInterval = None):
        self.interval = interval
        if jsonData != None:
            self.parse(jsonData)

    def fromJson(data, interval:StwhasInterval):
        return StwHasCostValue(data, interval)
    
    def parse(self, jsonData):
        self.time = datetime.fromisoformat(jsonData['datetime'])
        self.time = self.time.replace(tzinfo=datetime.now(timezone.utc).astimezone().tzinfo)
        for v in [a for a in dir(self) if not a.startswith('__') and a != 'datetime' and a != 'time' and a != 'interval' and not callable(getattr(self, a))]:
            try:
                setattr(self, v, jsonData[v])
            except:
                pass