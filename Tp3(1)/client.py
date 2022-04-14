import requests
from PyQt5.QtWidgets import QMessageBox

class Main():
    def query(self, hostname,api_key,ip):
        url = "http://%s" % (hostname)
        
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":

    main = Main()
    hostname = "127.0.0.1:8000"
    api_key="C9NgykpMuBucuOf7kn0Qd8C4FrSfsGFf"
    ip="149.62.158.57"
    res = main.query(hostname,api_key,ip)
    if res:
        print(res)