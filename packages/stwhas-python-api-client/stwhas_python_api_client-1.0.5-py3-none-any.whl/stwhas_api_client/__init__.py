from datetime import datetime
from .stwhasinterval import StwhasInterval
from .stwhaseexdata import StwHasEexData
from .stwhassmartmeterdata import StwHasSmartMeterData
import requests

class StwHasApiClient:
    def __init__(self, username, password, endpoint= 'https://hassfurt.energy-assistant.de/api/') -> None:
        self.username = username
        self.password = password
        self.endpoint = endpoint
        self.token = None

    def login(self):
        loginData = {
            "email": self.username,
            "password": self.password
        }
        data = requests.post(self.endpoint + 'auth/v1/customer/login', json=loginData)
        if data.status_code == 200:
            self.token = data.json()["token"]
        return self.token

    def eexData(self, starttime:datetime, endtime:datetime, interval:StwhasInterval, token = None):
        url = "{endpoint}stockmarket/v1/mapped-values/startdate/{startdate}Z/enddate/{enddate}Z/interval/{interval}".format(
            endpoint=self.endpoint, 
            startdate=starttime.isoformat(), 
            enddate=endtime.isoformat(), 
            interval=interval.value)
        data = self.apiRequest(url, token).json()
        return StwHasEexData.fromJson(data)

    def smartMeterData(self, starttime:datetime, endtime:datetime, meternumber:str, interval:StwhasInterval, token = None):
        url = "{endpoint}meter/v1/meters/number/{meternumber}/mapped-values/startdate/{startdate}/enddate/{enddate}/interval/{interval}".format(
            endpoint=self.endpoint, 
            startdate=starttime.isoformat(), 
            enddate=endtime.isoformat(), 
            interval=interval.value,
            meternumber=meternumber)
        data = self.apiRequest(url, token).json()
        return StwHasSmartMeterData.fromJson(data)
        
    def apiRequest(self, url, token):
        if token is None and self.token != None:
            token = self.token
        if token == None:
            raise Exception("Please Login first or provide token")
        
        return requests.get(url, headers={
            "Authorization": "Bearer "+token
        })