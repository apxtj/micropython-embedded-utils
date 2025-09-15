import network
import time

class WiFiManager:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.wifi = network.WLAN(network.STA_IF)
        self.wifi.active(True)

    def connect(self, timeout=10):
        if self.wifi.isconnected():
            return True
        self.wifi.disconnect()
        self.wifi.connect(self.ssid, self.password)
        start = time.time()
        while not self.wifi.isconnected():
            if time.time() - start > timeout:
                return False
            time.sleep(0.5)
        return True

    def status(self):
        return 'connected' if self.wifi.isconnected() else 'disconnected'

    def ip_address(self):
        return self.wifi.ifconfig()[0]
