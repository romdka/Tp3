import webbrowser
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 250)
        
        self.labelIP = QLabel("Enter your host IP:", self)
        self.textIP = QLineEdit(self)
        self.textIP.move(10, 30)

        self.labelIpWeb= QLabel("Enter the IP of the desired website :", self)
        self.labelIpWeb.move(10, 70)
        self.textIpWeb = QLineEdit(self)
        self.textIpWeb.move(10, 90)

        self.labelAPI= QLabel("Enter your Api key :",self)
        self.labelAPI.move(10, 120)
        self.textAPI = QLineEdit(self)
        self.textAPI.move(10, 140)

        self.label = QLabel("Answer:", self)
        self.label.move(10, 170)
        self.button = QPushButton("Send", self)
        self.button.move(10, 200)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()
        
    def on_click(self):
        hostname = self.textIP.text()
        api_key = self.textAPI.text()
        ip = self.textIpWeb.text()

        if hostname == "" or api_key=="" or ip=="":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname,ip,api_key)
            if res or res and type(res)==dict:
                latitude=str(res["latitude"])
                longitude=str(res["longitude"])
                self.label.setText("Answer%s" % (res["Organization"]+"\n latitude :"+latitude+"\n longitude :"+longitude))
                self.label.adjustSize()
                self.show()
                webbrowser.open( url = "https://www.openstreetmap.org/?mlat="+latitude+"&mlon="+longitude+"#map=12",new =0 )

    def __query(self, hostname,ip,api_key):
        ##ping esiea : 149.62.158.51
        ##ip hostname : 127.0.0.1:8000
        ##api key : C9NgykpMuBucuOf7kn0Qd8C4FrSfsGFf
        ##url = "http://%s/ip/%s?key=%s" % (hostname) % (ip) % (api_key)
        
        url = "http://"+hostname+"/ip/"+ip+"?key="+api_key

        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()