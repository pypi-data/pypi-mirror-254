import requests
import json

class SmartThingsError(Exception):
    pass

class SmartThings:
    def __init__(self, personal_access_token):
        # include api_key in all requested url the session
        self.apiendpoint = "https://api.smartthings.com/v1"

        self._s = requests.Session()
        self._s.headers = {"Authorization": f"Bearer {personal_access_token}"}

    def _get(self, path):
        """
        Makes GET request, (auth is baked in to the session)
        Returns response as object
        """
        r = self._s.get(f"{self.apiendpoint}/{path}")

        if r.ok:
            return r.json()
        else:
            if r.status_code == 401:
                raise SmartThingsError("Unauthorized")

            # We got a bad error, raise it and wrapp the error msg for sending it up
            # this way we get a good error msg on every bad request
            try:
                r.raise_for_status()
            except requests.exceptions.HTTPError as error_msg:
                raise SmartThingsError(error_msg) from error_msg
            
            
    def _post(self, path, data):
        """
        Makes POST request, (auth is baked in to the session)
        Returns response as object
        """
        r = self._s.post(f"{self.apiendpoint}/{path}", data)
    
        if r.ok:
            return r.json()
        else:
            if r.status_code == 401:
                raise SmartThingsError("Unauthorized")
            if r.status_code == 403:
                raise SmartThingsError("Forbidden")

            # We got a bad error, raise it and wrapp the error msg for sending it up
            # this way we get a good error msg on every bad request
            try:
                r.raise_for_status()
            except requests.exceptions.HTTPError as error_msg:
                raise SmartThingsError(error_msg) from error_msg


    def capabilities(self):
        r = self._get("capabilities")
        return r["items"]

    def cap(self, cap_name, version=1):
        r = self._get(f"capabilities/{cap_name}/{version}")
        out = {
            "commands": [
                {
                    "component": "main",
                    "capability": cap_name,
                    "command": "setInputSource",
                    "arguments": ["HDMI1"],
                }
            ]
        }
        return out

    # def make_command():

    def devices(self):
        """Returns devices"""
        r = self._get("devices")
        return r["items"]

    def device(self, **kwargs):
        """Return first device to match key=value

        To get device with label "STV"
        >>> device(label="STV")
        """
        devices = self._get("devices")
        for device in devices["items"]:
            for match in kwargs:
                if device[match] == kwargs[match]:
                    return Device(device, self)
                    # return device
        return None
                    
class Device:
    def __init__(self, data, smartThings) -> None:
        self.label = data["label"]
        self.deviceId = data["deviceId"]
        self.component = data["components"][0]["id"]
        self.smartThings = smartThings


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.label})"
    
    def switch_on(self):
        commandData = {
            'commands': [
                {
                    'capability': "switch",
                    'command': "on",
                }
            ]
        }
        try:
            res = self.smartThings._post(f"devices/{self.deviceId}/commands", json.dumps(commandData))
            return res["results"][0]["status"] == "ACCEPTED"
        except:
            return False
    
    def switch_off(self):
        commandData = {
            'commands': [
                {
                    'capability': "switch",
                    'command': "off",
                }
            ]
        }
        try:
            res = self.smartThings._post(f"devices/{self.deviceId}/commands", json.dumps(commandData))
            return res["results"][0]["status"] == "ACCEPTED"
        except:
            return False
        
        # returns status of switch or exception
    def status(self):
        res = self.smartThings._get(f"devices/{self.deviceId}/status")
        try:
            main = res["components"]["main"]
            switch_status = main["switch"]["switch"]["value"]
            if switch_status == "on":
                return True
            elif switch_status == "off":
                return False
            elif switch_status == None:
                raise SmartThingsError("Unknown status : None")
            else:
                raise SmartThingsError(f"Unknown status : {switch_status}")
        except any as e:
            return e