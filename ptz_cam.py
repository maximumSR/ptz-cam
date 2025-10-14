import time

import requests
from requests.auth import HTTPBasicAuth

class PTZCamera:
    def __init__(self, ip, username, password, timeout=5):
        self.ip = ip
        self.auth = HTTPBasicAuth(username, password)
        self.timeout = timeout
        self.base_url = f"http://{ip}/web/cgi-bin/hi3510/ptzctrl.cgi"

    def _send(self, params):
        try:
            response = requests.get(self.base_url, params=params, auth=self.auth, timeout=self.timeout)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print("Request failed:", e)
            return None

    def move(self, direction, speed=45, step=0):
        """
        direction: one of 'left', 'right', 'up', 'down', 'zoomin', 'zoomout'
        """
        valid_dirs = ['left', 'right', 'up', 'down', 'zoomin', 'zoomout']
        if direction not in valid_dirs:
            raise ValueError(f"Invalid direction: {direction}")
        return self._send({'-step': step, '-act': direction, '-speed': speed})

    def stop(self):
        """Stop current movement"""
        return self._send({'-step': 0, '-act': 'stop', '-speed': 45})

# Example usage
if __name__ == "__main__":
    cam = PTZCamera("192.168.1.250", "SR-SV3C", "silent")

    print("Moving camera right...")
    cam.move("right", speed=45)
    
    time.sleep(2)
    
    print("Stopping...")
    cam.stop()
