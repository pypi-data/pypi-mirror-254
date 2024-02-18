from .stwhascostvalue import StwHasCostValue
from .stwhasunit import StwhasUnit
from .stwhasinterval import StwhasInterval
import os, time, datetime
from datetime import datetime, timezone

class StwHasConsumptionCost:
    data:list[StwHasCostValue] = []
    unit:StwhasUnit = None

    def __init__(self, jsonData = None, unit:StwhasUnit = None, interval:StwhasInterval = None):
        self.unit = unit
        if jsonData != None:
            self.parse(jsonData, interval)
        pass

    def fromJson(data, unit:StwhasUnit, interval:StwhasInterval):
        # the response data is in timezone Europe/Berlin and incorrectly marked as UTC
        oldtz = datetime.now(timezone.utc).astimezone().tzinfo
        os.environ['TZ'] = 'Europe/Berlin'
        time.tzset()

        data = StwHasConsumptionCost(data, unit, interval)

        # reset timezone to te previous zone
        os.environ['TZ'] = str(oldtz)
        time.tzset()

        return data
    
    def parse(self, jsonData, interval:StwhasInterval):
        if jsonData["values"] is None:
            raise Exception("Invalid data")
        for value in jsonData["values"]:
            data = StwHasCostValue.fromJson(value, interval)
            self.data.append(data)