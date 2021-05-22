from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from random import randint
from time import sleep

class Ui_MainWindow(object):

    def pushButtons(self):
        proxy_ip_port = self.proxytext.text()
        proxy = Proxy()
        proxy.proxy_type = ProxyType.MANUAL
        proxy.http_proxy = proxy_ip_port
        proxy.ssl_proxy = proxy_ip_port
        capabilities = webdriver.DesiredCapabilities.CHROME
        proxy.add_to_capabilities(capabilities)
        driver = webdriver.Chrome(desired_capabilities=capabilities)
        driver.get(self.videotext.text())
        sleep(randint(self.timeone.text(), self.timetwo.text()))
        driver.quit

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.viewbutton = QtWidgets.QPushButton(self.centralwidget)
        self.viewbutton.setGeometry(QtCore.QRect(10, 110, 301, 121))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.viewbutton.setFont(font)
        self.viewbutton.setObjectName("viewbutton")
        self.viewbutton.clicked.connect(self.pushButtons)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 49, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 49, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 49, 16))
        self.label_3.setObjectName("label_3")
        self.proxytext = QtWidgets.QLineEdit(self.centralwidget)
        self.proxytext.setGeometry(QtCore.QRect(70, 20, 231, 21))
        self.proxytext.setObjectName("proxytext")
        self.videotext = QtWidgets.QLineEdit(self.centralwidget)
        self.videotext.setGeometry(QtCore.QRect(70, 50, 231, 21))
        self.videotext.setObjectName("videotext")
        self.timeone = QtWidgets.QLineEdit(self.centralwidget)
        self.timeone.setGeometry(QtCore.QRect(70, 80, 113, 21))
        self.timeone.setObjectName("timeone")
        self.timetwo = QtWidgets.QLineEdit(self.centralwidget)
        self.timetwo.setGeometry(QtCore.QRect(190, 80, 113, 21))
        self.timetwo.setObjectName("timetwo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube View Bot Mr. Smart"))
        self.viewbutton.setText(_translate("MainWindow", "View"))
        self.label.setText(_translate("MainWindow", "Proxy"))
        self.label_2.setText(_translate("MainWindow", "Video"))
        self.label_3.setText(_translate("MainWindow", "Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())