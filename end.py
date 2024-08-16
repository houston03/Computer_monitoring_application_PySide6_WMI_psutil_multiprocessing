# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'end.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import (QFont, QIcon,
     QPixmap)
from PySide6.QtWidgets import (QCheckBox, QFrame, QLabel,
  QPushButton, QWidget)
import rec_rc
import cpuinfo
import wmi
from wmi import WMI
from windows_tools import product_key
import subprocess
import psutil
from platform import uname


controllers = wmi.WMI().Win32_VideoController()
gpu_data = list()
for controller in controllers:
   controller_info = {
        'Name': controller.wmi_property('Name').value,
        'HRes': controller.wmi_property('CurrentHorizontalResolution').value,
        'VRes': controller.wmi_property('CurrentVerticalResolution').value,
    }
   gpu_data.append(controller_info)


def correct_size(bts, ending='b'):
    size = 1024
    for item in ["", " K", " M", " G", " T", " P"]:
        if bts < size:
            return f"{bts:.2f}{item}{ending}"
        bts /= size
        if 'size' in item:  # Проверка наличия уже собранных данных
                return

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1120, 690)
        MainWindow.setMinimumSize(QSize(1120, 690))
        MainWindow.setMaximumSize(QSize(1120, 690))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(20,20,40), stop:1 rgba(10,10,20));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget_34 = QWidget(self.centralwidget)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setGeometry(QRect(20, -10, 1091, 61))
        self.widget_34.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,20), stop:1 rgba(205,200,250,50));\n"
"border-radius:7px;\n"
"\n"
"\n"
"border: none;")
        self.pushButton_10 = QPushButton(self.widget_34)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(1000, 20, 32, 32))
        self.pushButton_10.setMinimumSize(QSize(32, 32))
        self.pushButton_10.setMaximumSize(QSize(32, 32))
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        font.setPointSize(15)
        font.setBold(True)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,50), stop:1 rgba(205,200,250,50));\n"
"color: white;\n"
"\n"
"font-size: 15pt;\n"
"border: none;\n"
"border-radius: 5px;}\n"
"QPushButton:hover {background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,70), stop:1 rgba(205,200,250,70));\n"
"}\n"
"QPushButton:pressed {background-color:rgba(255,255,255,60);\n"
"}\n"
"")
        self.pushButton_11 = QPushButton(self.widget_34)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(1040, 20, 32, 32))
        self.pushButton_11.setMinimumSize(QSize(32, 32))
        self.pushButton_11.setMaximumSize(QSize(32, 32))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,50), stop:1 rgba(205,200,250,50));\n"
"color: white;\n"
"\n"
"font-size: 15pt;\n"
"border: none;\n"
"border-radius: 5px;}\n"
"QPushButton:hover {background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,70), stop:1 rgba(205,200,250,70));\n"
"}\n"
"QPushButton:pressed {background-color:rgba(255,255,255,60);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon)
        self.pushButton_11.setIconSize(QSize(28, 28))
        self.Gpu2_39 = QLabel(self.widget_34)
        self.Gpu2_39.setObjectName(u"Gpu2_39")
        self.Gpu2_39.setEnabled(False)
        self.Gpu2_39.setGeometry(QRect(70, 20, 32, 32))
        self.Gpu2_39.setMinimumSize(QSize(30, 30))
        self.Gpu2_39.setMaximumSize(QSize(500, 500))
        self.Gpu2_39.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 5pt;\n"
"border-radius:7px;")
        self.Gpu2_39.setLineWidth(0)
        self.Gpu2_39.setPixmap(QPixmap(u":/icons/image (10).png"))
        self.Gpu2_39.setScaledContents(True)
        self.Gpu2_20 = QLabel(self.widget_34)
        self.Gpu2_20.setObjectName(u"Gpu2_20")
        self.Gpu2_20.setEnabled(False)
        self.Gpu2_20.setGeometry(QRect(30, 20, 32, 32))
        self.Gpu2_20.setMinimumSize(QSize(30, 30))
        self.Gpu2_20.setMaximumSize(QSize(500, 500))
        self.Gpu2_20.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 5pt;\n"
"border-radius:7px;")
        self.Gpu2_20.setLineWidth(0)
        self.Gpu2_20.setPixmap(QPixmap(u":/icons/icons/pchel.png"))
        self.Gpu2_20.setScaledContents(True)
        self.line_12 = QFrame(self.widget_34)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(148, 21, 361, 3))
        self.line_12.setMaximumSize(QSize(10000, 3))
        self.line_12.setStyleSheet(u"color: white;\n"
"background-color:rgba(255,255,255,40);\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)
        self.Gpu2_40 = QLabel(self.widget_34)
        self.Gpu2_40.setObjectName(u"Gpu2_40")
        self.Gpu2_40.setEnabled(False)
        self.Gpu2_40.setGeometry(QRect(110, 20, 32, 32))
        self.Gpu2_40.setMinimumSize(QSize(30, 30))
        self.Gpu2_40.setMaximumSize(QSize(500, 500))
        self.Gpu2_40.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 5pt;\n"
"border-radius:7px;")
        self.Gpu2_40.setLineWidth(0)
        self.Gpu2_40.setPixmap(QPixmap(u":/icons/image (11).png"))
        self.Gpu2_40.setScaledContents(True)
        self.label_12 = QLabel(self.widget_34)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(518, -9, 31, 61))
        self.label_12.setMinimumSize(QSize(20, 20))
        self.label_12.setSizeIncrement(QSize(0, 0))
        self.label_12.setBaseSize(QSize(0, 0))
        self.label_12.setStyleSheet(u"color: black;\n"
"color: rgb(0, 0, 0);\n"
"background-color:none;\n"
"\n"
"font-weight:bold;\n"
"\n"
"border: none;\n"
"font-size: 16.5pt;\n"
"border-radius:7px;")
        self.label_12.setPixmap(QPixmap(u":/icons/icons/the.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.line_10 = QFrame(self.widget_34)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(148, 41, 381, 3))
        self.line_10.setMaximumSize(QSize(10000, 3))
        self.line_10.setStyleSheet(u"color: white;\n"
"background-color:rgba(25,255,255,40);\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)
        self.line_11 = QFrame(self.widget_34)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(148, 51, 381, 3))
        self.line_11.setMaximumSize(QSize(10000, 3))
        self.line_11.setStyleSheet(u"color: white;\n"
"background-color:rgba(255,5,25,40);\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.line_13 = QFrame(self.widget_34)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(8, 61, 521, 3))
        self.line_13.setMaximumSize(QSize(10000, 3))
        self.line_13.setStyleSheet(u"color: white;\n"
"background-color:rgba(255,5,25,40);\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)
        self.line_18 = QFrame(self.widget_34)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setGeometry(QRect(8, 21, 16, 3))
        self.line_18.setMaximumSize(QSize(10000, 3))
        self.line_18.setStyleSheet(u"color: white;\n"
"background-color:rgba(255,255,255,40);\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)
        self.line_6 = QFrame(self.widget_34)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(148, 31, 351, 3))
        self.line_6.setMaximumSize(QSize(10000, 3))
        self.line_6.setStyleSheet(u"color: white;\n"
"background-color:rgba(255,255,255,40);\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_16 = QFrame(self.widget_34)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setGeometry(QRect(8, 41, 16, 3))
        self.line_16.setMaximumSize(QSize(10000, 3))
        self.line_16.setStyleSheet(u"color: white;\n"
"background-color:rgba(25,255,255,40);\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)
        self.mem_4 = QLabel(self.widget_34)
        self.mem_4.setObjectName(u"mem_4")
        self.mem_4.setGeometry(QRect(558, 11, 181, 41))
        self.mem_4.setMinimumSize(QSize(0, 28))
        self.mem_4.setMaximumSize(QSize(500, 50))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI Light"])
        font1.setPointSize(7)
        font1.setBold(True)
        self.mem_4.setFont(font1)
        self.mem_4.setStyleSheet(u"font-weight:bold;\n"
"color:white;\n"
"background-color:none;\n"
"\n"
"\n"
"\n"
"border:none;\n"
"font-size: 7pt;\n"
"border-radius:7px;")
        self.mem_4.setLineWidth(0)
        self.label_48 = QLabel(self.widget_34)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(558, 21, 301, 41))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI Light"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_48.setFont(font2)
        self.label_48.setStyleSheet(u"color: white;\n"
"background-color:none;\n"
"\n"
"font-weight:bold;\n"
"\n"
"border: none;\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.line = QFrame(self.widget_34)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(548, 11, 2, 50))
        self.line.setStyleSheet(u"color:white;\n"
"background-color:rgba(255,255,255,150);\n"
"\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 20pt;\n"
"border-radius:7px;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_17 = QFrame(self.widget_34)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setGeometry(QRect(8, 31, 16, 3))
        self.line_17.setMaximumSize(QSize(10000, 3))
        self.line_17.setStyleSheet(u"color: white;\n"
"background-color:rgba(255,255,255,40);\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.widget_34)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(558, 29, 301, 41))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI Light"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"\n"
"border: none;\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.line_15 = QFrame(self.widget_34)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setGeometry(QRect(8, 51, 16, 3))
        self.line_15.setMaximumSize(QSize(10000, 3))
        self.line_15.setStyleSheet(u"color: white;\n"
"background-color:rgba(255,5,25,40);\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)
        self.Gpu2_32 = QLabel(self.widget_34)
        self.Gpu2_32.setObjectName(u"Gpu2_32")
        self.Gpu2_32.setGeometry(QRect(710, 20, 281, 32))
        self.Gpu2_32.setMinimumSize(QSize(50, 30))
        self.Gpu2_32.setMaximumSize(QSize(1000, 35))
        font4 = QFont()
        font4.setFamilies([u"Microsoft YaHei UI Light"])
        font4.setPointSize(10)
        self.Gpu2_32.setFont(font4)
        self.Gpu2_32.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_32.setLineWidth(0)
        self.widget_26 = QWidget(self.centralwidget)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setGeometry(QRect(490, 60, 351, 31))
        self.widget_26.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,20), stop:1 rgba(205,200,250,50));\n"
"border-radius:7px;\n"
"\n"
"\n"
"border: none;")
        self.label_36 = QLabel(self.widget_26)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(10, -3, 111, 35))
        self.label_36.setMinimumSize(QSize(35, 35))
        self.label_36.setMaximumSize(QSize(16777215, 35))
        font5 = QFont()
        font5.setFamilies([u"Microsoft YaHei Light"])
        font5.setPointSize(13)
        font5.setBold(False)
        self.label_36.setFont(font5)
        self.label_36.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: none;\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.widget_28 = QWidget(self.centralwidget)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setGeometry(QRect(490, 100, 621, 301))
        self.widget_28.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,30), stop:1 rgba(205,200,250,25));\n"
"border-radius:7px;\n"
"\n"
"\n"
"border: none;")
        self.label_25 = QLabel(self.widget_28)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(80, 10, 201, 30))
        self.label_25.setMinimumSize(QSize(35, 30))
        self.label_25.setMaximumSize(QSize(16777215, 35))
        font6 = QFont()
        font6.setFamilies([u"Microsoft YaHei UI Light"])
        font6.setPointSize(13)
        self.label_25.setFont(font6)
        self.label_25.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.label_26 = QLabel(self.widget_28)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(80, 200, 201, 30))
        self.label_26.setMinimumSize(QSize(35, 30))
        self.label_26.setMaximumSize(QSize(16777215, 35))
        self.label_26.setFont(font6)
        self.label_26.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.Gpu2_22 = QLabel(self.widget_28)
        self.Gpu2_22.setObjectName(u"Gpu2_22")
        self.Gpu2_22.setGeometry(QRect(290, 10, 321, 30))
        self.Gpu2_22.setMinimumSize(QSize(50, 30))
        self.Gpu2_22.setMaximumSize(QSize(1000, 35))
        self.Gpu2_22.setFont(font4)
        self.Gpu2_22.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_22.setLineWidth(0)
        self.Gpu2_23 = QLabel(self.widget_28)
        self.Gpu2_23.setObjectName(u"Gpu2_23")
        self.Gpu2_23.setGeometry(QRect(290, 200, 321, 30))
        self.Gpu2_23.setMinimumSize(QSize(50, 30))
        self.Gpu2_23.setMaximumSize(QSize(1000, 35))
        self.Gpu2_23.setFont(font4)
        self.Gpu2_23.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_23.setLineWidth(0)
        self.label_27 = QLabel(self.widget_28)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(170, 50, 111, 20))
        self.label_27.setMinimumSize(QSize(35, 20))
        self.label_27.setMaximumSize(QSize(16777215, 35))
        self.label_27.setFont(font4)
        self.label_27.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.label_28 = QLabel(self.widget_28)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(170, 80, 111, 20))
        self.label_28.setMinimumSize(QSize(35, 20))
        self.label_28.setMaximumSize(QSize(16777215, 35))
        self.label_28.setFont(font4)
        self.label_28.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.label_29 = QLabel(self.widget_28)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(170, 110, 111, 20))
        self.label_29.setMinimumSize(QSize(35, 20))
        self.label_29.setMaximumSize(QSize(16777215, 35))
        self.label_29.setFont(font4)
        self.label_29.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.label_30 = QLabel(self.widget_28)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(170, 170, 111, 20))
        self.label_30.setMinimumSize(QSize(35, 20))
        self.label_30.setMaximumSize(QSize(16777215, 35))
        self.label_30.setFont(font4)
        self.label_30.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.label_31 = QLabel(self.widget_28)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(100, 163, 71, 35))
        self.label_31.setMinimumSize(QSize(35, 35))
        self.label_31.setMaximumSize(QSize(16777215, 35))
        font7 = QFont()
        font7.setFamilies([u"Microsoft YaHei UI Light"])
        font7.setPointSize(8)
        self.label_31.setFont(font7)
        self.label_31.setStyleSheet(u"background-color:none;\n"
"color:rgba(250,250,250,150);\n"
"border: none;\n"
"font-size: 8pt;\n"
"border-radius:7px;")
        self.Gpu2_24 = QLabel(self.widget_28)
        self.Gpu2_24.setObjectName(u"Gpu2_24")
        self.Gpu2_24.setGeometry(QRect(290, 50, 321, 20))
        self.Gpu2_24.setMinimumSize(QSize(50, 20))
        self.Gpu2_24.setMaximumSize(QSize(1000, 35))
        self.Gpu2_24.setFont(font4)
        self.Gpu2_24.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_24.setLineWidth(0)
        self.Gpu2_25 = QLabel(self.widget_28)
        self.Gpu2_25.setObjectName(u"Gpu2_25")
        self.Gpu2_25.setGeometry(QRect(290, 80, 321, 20))
        self.Gpu2_25.setMinimumSize(QSize(50, 20))
        self.Gpu2_25.setMaximumSize(QSize(1000, 35))
        self.Gpu2_25.setFont(font4)
        self.Gpu2_25.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_25.setLineWidth(0)
        self.Gpu2_26 = QLabel(self.widget_28)
        self.Gpu2_26.setObjectName(u"Gpu2_26")
        self.Gpu2_26.setGeometry(QRect(290, 110, 321, 20))
        self.Gpu2_26.setMinimumSize(QSize(50, 20))
        self.Gpu2_26.setMaximumSize(QSize(1000, 35))
        self.Gpu2_26.setFont(font4)
        self.Gpu2_26.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_26.setLineWidth(0)
        self.Gpu2_27 = QLabel(self.widget_28)
        self.Gpu2_27.setObjectName(u"Gpu2_27")
        self.Gpu2_27.setGeometry(QRect(290, 170, 321, 20))
        self.Gpu2_27.setMinimumSize(QSize(50, 20))
        self.Gpu2_27.setMaximumSize(QSize(1000, 35))
        self.Gpu2_27.setFont(font4)
        self.Gpu2_27.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_27.setLineWidth(0)
        self.label_32 = QLabel(self.widget_28)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(170, 240, 111, 20))
        self.label_32.setMinimumSize(QSize(35, 20))
        self.label_32.setMaximumSize(QSize(16777215, 35))
        font8 = QFont()
        font8.setFamilies([u"Microsoft JhengHei UI Light"])
        font8.setPointSize(10)
        self.label_32.setFont(font8)
        self.label_32.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_28 = QLabel(self.widget_28)
        self.Gpu2_28.setObjectName(u"Gpu2_28")
        self.Gpu2_28.setGeometry(QRect(290, 240, 321, 20))
        self.Gpu2_28.setMinimumSize(QSize(50, 20))
        self.Gpu2_28.setMaximumSize(QSize(1000, 35))
        self.Gpu2_28.setFont(font4)
        self.Gpu2_28.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_28.setLineWidth(0)
        self.label_54 = QLabel(self.widget_28)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(170, 270, 111, 20))
        self.label_54.setMinimumSize(QSize(35, 20))
        self.label_54.setMaximumSize(QSize(16777215, 35))
        self.label_54.setFont(font8)
        self.label_54.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_41 = QLabel(self.widget_28)
        self.Gpu2_41.setObjectName(u"Gpu2_41")
        self.Gpu2_41.setGeometry(QRect(290, 270, 321, 20))
        self.Gpu2_41.setMinimumSize(QSize(50, 20))
        self.Gpu2_41.setMaximumSize(QSize(1000, 35))
        self.Gpu2_41.setFont(font4)
        self.Gpu2_41.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_41.setLineWidth(0)
        self.label_55 = QLabel(self.widget_28)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(170, 140, 111, 20))
        self.label_55.setMinimumSize(QSize(35, 20))
        self.label_55.setMaximumSize(QSize(16777215, 35))
        self.label_55.setFont(font4)
        self.label_55.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_42 = QLabel(self.widget_28)
        self.Gpu2_42.setObjectName(u"Gpu2_42")
        self.Gpu2_42.setGeometry(QRect(290, 140, 321, 20))
        self.Gpu2_42.setMinimumSize(QSize(50, 20))
        self.Gpu2_42.setMaximumSize(QSize(1000, 35))
        self.Gpu2_42.setFont(font4)
        self.Gpu2_42.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_42.setLineWidth(0)
        self.Gpu2_51 = QLabel(self.widget_28)
        self.Gpu2_51.setObjectName(u"Gpu2_51")
        self.Gpu2_51.setGeometry(QRect(40, 10, 30, 30))
        self.Gpu2_51.setMinimumSize(QSize(0, 0))
        self.Gpu2_51.setMaximumSize(QSize(180, 35))
        self.Gpu2_51.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_51.setLineWidth(0)
        self.Gpu2_51.setPixmap(QPixmap(u":/icons/1.png"))
        self.Gpu2_51.setScaledContents(True)
        self.Gpu2_52 = QLabel(self.widget_28)
        self.Gpu2_52.setObjectName(u"Gpu2_52")
        self.Gpu2_52.setGeometry(QRect(40, 200, 30, 30))
        self.Gpu2_52.setMinimumSize(QSize(0, 0))
        self.Gpu2_52.setMaximumSize(QSize(180, 35))
        self.Gpu2_52.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_52.setLineWidth(0)
        self.Gpu2_52.setPixmap(QPixmap(u":/icons/1.png"))
        self.Gpu2_52.setScaledContents(True)
        self.Gpu2_62 = QLabel(self.widget_28)
        self.Gpu2_62.setObjectName(u"Gpu2_62")
        self.Gpu2_62.setGeometry(QRect(10, 50, 151, 121))
        self.Gpu2_62.setMinimumSize(QSize(0, 0))
        self.Gpu2_62.setMaximumSize(QSize(200, 200))
        self.Gpu2_62.setStyleSheet(u"\n"
"color: white;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,20), stop:1 rgba(205,200,250,20));;\n"
"\n"
"\n"
"border: none;\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_62.setLineWidth(0)
        self.Gpu2_62.setScaledContents(True)
        self.Gpu2_96 = QLabel(self.widget_28)
        self.Gpu2_96.setObjectName(u"Gpu2_96")
        self.Gpu2_96.setGeometry(QRect(20, 50, 131, 30))
        self.Gpu2_96.setMinimumSize(QSize(50, 30))
        self.Gpu2_96.setMaximumSize(QSize(1000, 1000))
        font9 = QFont()
        font9.setPointSize(70)
        self.Gpu2_96.setFont(font9)
        self.Gpu2_96.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_96.setLineWidth(0)
        self.Gpu2_97 = QLabel(self.widget_28)
        self.Gpu2_97.setObjectName(u"Gpu2_97")
        self.Gpu2_97.setGeometry(QRect(30, 90, 131, 30))
        self.Gpu2_97.setMinimumSize(QSize(50, 30))
        self.Gpu2_97.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_97.setFont(font9)
        self.Gpu2_97.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_97.setLineWidth(0)
        self.Gpu2_98 = QLabel(self.widget_28)
        self.Gpu2_98.setObjectName(u"Gpu2_98")
        self.Gpu2_98.setGeometry(QRect(-20, 90, 50, 30))
        self.Gpu2_98.setMinimumSize(QSize(50, 30))
        self.Gpu2_98.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_98.setFont(font9)
        self.Gpu2_98.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_98.setLineWidth(0)
        self.Gpu2_99 = QLabel(self.widget_28)
        self.Gpu2_99.setObjectName(u"Gpu2_99")
        self.Gpu2_99.setGeometry(QRect(10, 130, 161, 30))
        self.Gpu2_99.setMinimumSize(QSize(50, 30))
        self.Gpu2_99.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_99.setFont(font9)
        self.Gpu2_99.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_99.setLineWidth(0)
        self.Gpu2_103 = QLabel(self.widget_28)
        self.Gpu2_103.setObjectName(u"Gpu2_103")
        self.Gpu2_103.setGeometry(QRect(10, 80, 50, 91))
        self.Gpu2_103.setMinimumSize(QSize(50, 30))
        self.Gpu2_103.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_103.setFont(font9)
        self.Gpu2_103.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_103.setLineWidth(0)
        self.Gpu2_104 = QLabel(self.widget_28)
        self.Gpu2_104.setObjectName(u"Gpu2_104")
        self.Gpu2_104.setGeometry(QRect(10, -10, 50, 91))
        self.Gpu2_104.setMinimumSize(QSize(50, 30))
        self.Gpu2_104.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_104.setFont(font9)
        self.Gpu2_104.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_104.setLineWidth(0)
        self.Gpu2_105 = QLabel(self.widget_28)
        self.Gpu2_105.setObjectName(u"Gpu2_105")
        self.Gpu2_105.setGeometry(QRect(130, 80, 50, 91))
        self.Gpu2_105.setMinimumSize(QSize(50, 30))
        self.Gpu2_105.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_105.setFont(font9)
        self.Gpu2_105.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_105.setLineWidth(0)
        self.Gpu2_106 = QLabel(self.widget_28)
        self.Gpu2_106.setObjectName(u"Gpu2_106")
        self.Gpu2_106.setGeometry(QRect(130, -10, 50, 91))
        self.Gpu2_106.setMinimumSize(QSize(50, 30))
        self.Gpu2_106.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_106.setFont(font9)
        self.Gpu2_106.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_106.setLineWidth(0)
        self.widget_29 = QWidget(self.centralwidget)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setGeometry(QRect(20, 100, 461, 171))
        self.widget_29.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,20), stop:1 rgba(205,200,250,20));\n"
"border-radius:7px;\n"
"\n"
"\n"
"border: none;")
        self.label_33 = QLabel(self.widget_29)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(50, 10, 111, 30))
        self.label_33.setMinimumSize(QSize(35, 30))
        self.label_33.setMaximumSize(QSize(16777215, 35))
        font10 = QFont()
        font10.setFamilies([u"Microsoft JhengHei UI Light"])
        font10.setPointSize(13)
        self.label_33.setFont(font10)
        self.label_33.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.label_34 = QLabel(self.widget_29)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(50, 50, 111, 30))
        self.label_34.setMinimumSize(QSize(35, 30))
        self.label_34.setMaximumSize(QSize(16777215, 35))
        self.label_34.setFont(font10)
        self.label_34.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.Gpu2_29 = QLabel(self.widget_29)
        self.Gpu2_29.setObjectName(u"Gpu2_29")
        self.Gpu2_29.setGeometry(QRect(170, 10, 281, 30))
        self.Gpu2_29.setMinimumSize(QSize(50, 30))
        self.Gpu2_29.setMaximumSize(QSize(1000, 35))
        self.Gpu2_29.setFont(font4)
        self.Gpu2_29.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_29.setLineWidth(0)
        self.Gpu2_30 = QLabel(self.widget_29)
        self.Gpu2_30.setObjectName(u"Gpu2_30")
        self.Gpu2_30.setGeometry(QRect(170, 50, 281, 30))
        self.Gpu2_30.setMinimumSize(QSize(50, 30))
        self.Gpu2_30.setMaximumSize(QSize(1000, 35))
        self.Gpu2_30.setFont(font4)
        self.Gpu2_30.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_30.setLineWidth(0)
        self.label_35 = QLabel(self.widget_29)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(50, 90, 111, 30))
        self.label_35.setMinimumSize(QSize(35, 30))
        self.label_35.setMaximumSize(QSize(16777215, 35))
        self.label_35.setFont(font10)
        self.label_35.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.Gpu2_31 = QLabel(self.widget_29)
        self.Gpu2_31.setObjectName(u"Gpu2_31")
        self.Gpu2_31.setGeometry(QRect(170, 90, 281, 30))
        self.Gpu2_31.setMinimumSize(QSize(50, 30))
        self.Gpu2_31.setMaximumSize(QSize(1000, 35))
        self.Gpu2_31.setFont(font4)
        self.Gpu2_31.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_31.setLineWidth(0)
        self.label_49 = QLabel(self.widget_29)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(50, 130, 111, 30))
        self.label_49.setMinimumSize(QSize(35, 30))
        self.label_49.setMaximumSize(QSize(16777215, 35))
        self.label_49.setFont(font10)
        self.label_49.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.Gpu2_35 = QLabel(self.widget_29)
        self.Gpu2_35.setObjectName(u"Gpu2_35")
        self.Gpu2_35.setGeometry(QRect(170, 130, 281, 30))
        self.Gpu2_35.setMinimumSize(QSize(50, 30))
        self.Gpu2_35.setMaximumSize(QSize(1000, 35))
        self.Gpu2_35.setFont(font4)
        self.Gpu2_35.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_35.setLineWidth(0)
        self.Gpu2_47 = QLabel(self.widget_29)
        self.Gpu2_47.setObjectName(u"Gpu2_47")
        self.Gpu2_47.setGeometry(QRect(10, 130, 30, 30))
        self.Gpu2_47.setMinimumSize(QSize(0, 0))
        self.Gpu2_47.setMaximumSize(QSize(180, 35))
        self.Gpu2_47.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_47.setLineWidth(0)
        self.Gpu2_47.setPixmap(QPixmap(u":/icons/image (5).png"))
        self.Gpu2_47.setScaledContents(True)
        self.Gpu2_47.setMargin(1)
        self.Gpu2_48 = QLabel(self.widget_29)
        self.Gpu2_48.setObjectName(u"Gpu2_48")
        self.Gpu2_48.setGeometry(QRect(10, 90, 30, 30))
        self.Gpu2_48.setMinimumSize(QSize(0, 0))
        self.Gpu2_48.setMaximumSize(QSize(180, 35))
        self.Gpu2_48.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_48.setLineWidth(0)
        self.Gpu2_48.setPixmap(QPixmap(u":/icons/image (8).png"))
        self.Gpu2_48.setScaledContents(True)
        self.Gpu2_48.setMargin(1)
        self.Gpu2_49 = QLabel(self.widget_29)
        self.Gpu2_49.setObjectName(u"Gpu2_49")
        self.Gpu2_49.setGeometry(QRect(10, 50, 30, 30))
        self.Gpu2_49.setMinimumSize(QSize(0, 0))
        self.Gpu2_49.setMaximumSize(QSize(180, 35))
        self.Gpu2_49.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_49.setLineWidth(0)
        self.Gpu2_49.setPixmap(QPixmap(u":/icons/1.png"))
        self.Gpu2_49.setScaledContents(True)
        self.Gpu2_50 = QLabel(self.widget_29)
        self.Gpu2_50.setObjectName(u"Gpu2_50")
        self.Gpu2_50.setGeometry(QRect(10, 10, 30, 30))
        self.Gpu2_50.setMinimumSize(QSize(0, 0))
        self.Gpu2_50.setMaximumSize(QSize(180, 35))
        self.Gpu2_50.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_50.setLineWidth(0)
        self.Gpu2_50.setPixmap(QPixmap(u":/icons/image 2).png"))
        self.Gpu2_50.setScaledContents(True)
        self.Gpu2_50.setMargin(1)
        self.widget_27 = QWidget(self.centralwidget)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setGeometry(QRect(140, 60, 341, 31))
        self.widget_27.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,20), stop:1 rgba(205,200,250,50));\n"
"border-radius:7px;\n"
"\n"
"\n"
"border: none;")
        self.label_37 = QLabel(self.widget_27)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, -3, 111, 35))
        self.label_37.setMinimumSize(QSize(35, 35))
        self.label_37.setMaximumSize(QSize(16777215, 35))
        self.label_37.setFont(font10)
        self.label_37.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: none;\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.widget_30 = QWidget(self.centralwidget)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setGeometry(QRect(141, 280, 371, 31))
        self.widget_30.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,20), stop:1 rgba(205,200,250,50));\n"
"border-radius:7px;\n"
"\n"
"\n"
"border: none;")
        self.label_38 = QLabel(self.widget_30)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, -3, 111, 35))
        self.label_38.setMinimumSize(QSize(35, 35))
        self.label_38.setMaximumSize(QSize(16777215, 35))
        self.label_38.setFont(font10)
        self.label_38.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: none;\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.widget_31 = QWidget(self.centralwidget)
        self.widget_31.setObjectName(u"widget_31")
        self.widget_31.setGeometry(QRect(20, 320, 171, 131))
        self.widget_31.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,20), stop:1 rgba(205,200,250,20));\n"
"border-radius:7px;\n"
"\n"
"\n"
"border: none;")
        self.label_39 = QLabel(self.widget_31)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(50, 10, 111, 30))
        self.label_39.setMinimumSize(QSize(35, 30))
        self.label_39.setMaximumSize(QSize(16777215, 35))
        self.label_39.setFont(font10)
        self.label_39.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.label_40 = QLabel(self.widget_31)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(50, 50, 111, 30))
        self.label_40.setMinimumSize(QSize(35, 30))
        self.label_40.setMaximumSize(QSize(16777215, 35))
        self.label_40.setFont(font10)
        self.label_40.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.label_41 = QLabel(self.widget_31)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(50, 90, 111, 30))
        self.label_41.setMinimumSize(QSize(35, 30))
        self.label_41.setMaximumSize(QSize(16777215, 35))
        self.label_41.setFont(font10)
        self.label_41.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.Gpu2_45 = QLabel(self.widget_31)
        self.Gpu2_45.setObjectName(u"Gpu2_45")
        self.Gpu2_45.setGeometry(QRect(10, 90, 30, 30))
        self.Gpu2_45.setMinimumSize(QSize(0, 0))
        self.Gpu2_45.setMaximumSize(QSize(180, 35))
        self.Gpu2_45.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_45.setLineWidth(0)
        self.Gpu2_45.setPixmap(QPixmap(u":/icons/image (14).png"))
        self.Gpu2_45.setScaledContents(True)
        self.Gpu2_44 = QLabel(self.widget_31)
        self.Gpu2_44.setObjectName(u"Gpu2_44")
        self.Gpu2_44.setGeometry(QRect(10, 10, 30, 30))
        self.Gpu2_44.setMinimumSize(QSize(0, 0))
        self.Gpu2_44.setMaximumSize(QSize(180, 35))
        self.Gpu2_44.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_44.setLineWidth(0)
        self.Gpu2_44.setPixmap(QPixmap(u":/icons/image (13).png"))
        self.Gpu2_44.setScaledContents(True)
        self.Gpu2_44.setMargin(1)
        self.Gpu2_46 = QLabel(self.widget_31)
        self.Gpu2_46.setObjectName(u"Gpu2_46")
        self.Gpu2_46.setGeometry(QRect(10, 50, 30, 30))
        self.Gpu2_46.setMinimumSize(QSize(0, 0))
        self.Gpu2_46.setMaximumSize(QSize(180, 35))
        self.Gpu2_46.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_46.setLineWidth(0)
        self.Gpu2_46.setPixmap(QPixmap(u":/icons/image (2).png"))
        self.Gpu2_46.setScaledContents(True)
        self.Gpu2_46.setMargin(2)
        self.Gpu2_46.setIndent(2)
        self.widget_32 = QWidget(self.centralwidget)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setGeometry(QRect(519, 410, 351, 31))
        self.widget_32.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,20), stop:1 rgba(205,200,250,50));\n"
"border-radius:7px;\n"
"\n"
"\n"
"border: none;")
        self.label_47 = QLabel(self.widget_32)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(10, -3, 211, 35))
        self.label_47.setMinimumSize(QSize(35, 35))
        self.label_47.setMaximumSize(QSize(16777215, 35))
        self.label_47.setFont(font10)
        self.label_47.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"border: none;\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.widget_33 = QWidget(self.centralwidget)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setGeometry(QRect(140, 460, 351, 31))
        self.widget_33.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,20), stop:1 rgba(205,200,250,50));\n"
"border-radius:7px;\n"
"\n"
"\n"
"border: none;")
        self.label_50 = QLabel(self.widget_33)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(10, -3, 111, 35))
        self.label_50.setMinimumSize(QSize(35, 35))
        self.label_50.setMaximumSize(QSize(16777215, 35))
        self.label_50.setFont(font10)
        self.label_50.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: none;\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.widget_35 = QWidget(self.centralwidget)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setGeometry(QRect(20, 500, 471, 131))
        self.widget_35.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,20), stop:1 rgba(205,200,250,20));\n"
"border-radius:7px;\n"
"\n"
"\n"
"border: none;")
        self.label_51 = QLabel(self.widget_35)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(50, 10, 111, 30))
        self.label_51.setMinimumSize(QSize(35, 30))
        self.label_51.setMaximumSize(QSize(16777215, 35))
        self.label_51.setFont(font10)
        self.label_51.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.label_52 = QLabel(self.widget_35)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(50, 50, 111, 30))
        self.label_52.setMinimumSize(QSize(35, 30))
        self.label_52.setMaximumSize(QSize(16777215, 35))
        self.label_52.setFont(font10)
        self.label_52.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.Gpu2_36 = QLabel(self.widget_35)
        self.Gpu2_36.setObjectName(u"Gpu2_36")
        self.Gpu2_36.setGeometry(QRect(170, 10, 291, 30))
        self.Gpu2_36.setMinimumSize(QSize(50, 30))
        self.Gpu2_36.setMaximumSize(QSize(1000, 35))
        self.Gpu2_36.setFont(font4)
        self.Gpu2_36.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_36.setLineWidth(0)
        self.Gpu2_37 = QLabel(self.widget_35)
        self.Gpu2_37.setObjectName(u"Gpu2_37")
        self.Gpu2_37.setGeometry(QRect(170, 50, 291, 30))
        self.Gpu2_37.setMinimumSize(QSize(50, 30))
        self.Gpu2_37.setMaximumSize(QSize(1000, 35))
        self.Gpu2_37.setFont(font4)
        self.Gpu2_37.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_37.setLineWidth(0)
        self.label_53 = QLabel(self.widget_35)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(50, 90, 111, 30))
        self.label_53.setMinimumSize(QSize(35, 30))
        self.label_53.setMaximumSize(QSize(16777215, 35))
        self.label_53.setFont(font10)
        self.label_53.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.Gpu2_38 = QLabel(self.widget_35)
        self.Gpu2_38.setObjectName(u"Gpu2_38")
        self.Gpu2_38.setGeometry(QRect(170, 90, 291, 30))
        self.Gpu2_38.setMinimumSize(QSize(50, 30))
        self.Gpu2_38.setMaximumSize(QSize(1000, 35))
        self.Gpu2_38.setFont(font4)
        self.Gpu2_38.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_38.setLineWidth(0)
        self.Gpu2_53 = QLabel(self.widget_35)
        self.Gpu2_53.setObjectName(u"Gpu2_53")
        self.Gpu2_53.setGeometry(QRect(10, 10, 30, 30))
        self.Gpu2_53.setMinimumSize(QSize(0, 0))
        self.Gpu2_53.setMaximumSize(QSize(180, 35))
        self.Gpu2_53.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_53.setLineWidth(0)
        self.Gpu2_53.setPixmap(QPixmap(u":/icons/image (7).png"))
        self.Gpu2_53.setScaledContents(True)
        self.Gpu2_53.setMargin(2)
        self.Gpu2_54 = QLabel(self.widget_35)
        self.Gpu2_54.setObjectName(u"Gpu2_54")
        self.Gpu2_54.setGeometry(QRect(10, 50, 30, 30))
        self.Gpu2_54.setMinimumSize(QSize(0, 0))
        self.Gpu2_54.setMaximumSize(QSize(180, 35))
        self.Gpu2_54.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_54.setLineWidth(0)
        self.Gpu2_54.setPixmap(QPixmap(u":/icons/image (4).png"))
        self.Gpu2_54.setScaledContents(True)
        self.Gpu2_54.setMargin(2)
        self.Gpu2_55 = QLabel(self.widget_35)
        self.Gpu2_55.setObjectName(u"Gpu2_55")
        self.Gpu2_55.setGeometry(QRect(10, 90, 30, 30))
        self.Gpu2_55.setMinimumSize(QSize(0, 0))
        self.Gpu2_55.setMaximumSize(QSize(180, 35))
        self.Gpu2_55.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_55.setLineWidth(0)
        self.Gpu2_55.setPixmap(QPixmap(u":/icons/image 1).png"))
        self.Gpu2_55.setScaledContents(True)
        self.Gpu2_55.setMargin(2)
        self.line_14 = QFrame(self.centralwidget)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(870, 420, 360, 3))
        self.line_14.setMaximumSize(QSize(10000, 3))
        self.line_14.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,50), stop:1 rgba(205,200,250,50));\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)
        self.line_19 = QFrame(self.centralwidget)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setGeometry(QRect(841, 70, 361, 3))
        self.line_19.setMaximumSize(QSize(10000, 3))
        self.line_19.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,50), stop:1 rgba(205,200,250,50));\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)
        self.line_20 = QFrame(self.centralwidget)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setGeometry(QRect(-221, 70, 361, 3))
        self.line_20.setMaximumSize(QSize(10000, 3))
        self.line_20.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,50), stop:1 rgba(205,200,250,50));\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)
        self.line_21 = QFrame(self.centralwidget)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setGeometry(QRect(-220, 290, 361, 3))
        self.line_21.setMaximumSize(QSize(10000, 3))
        self.line_21.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,50), stop:1 rgba(205,200,250,50));\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)
        self.line_26 = QFrame(self.centralwidget)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setGeometry(QRect(-221, 470, 361, 3))
        self.line_26.setMaximumSize(QSize(10000, 3))
        self.line_26.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,50), stop:1 rgba(205,200,250,50));\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)
        self.widget_36 = QWidget(self.centralwidget)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setGeometry(QRect(20, 650, 1091, 61))
        self.widget_36.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(205,200,250,50), stop:1 rgba(35,30,60,20));\n"
"border-radius:7px;\n"
"\n"
"\n"
"border: none;")
        self.line_30 = QFrame(self.widget_36)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setGeometry(QRect(8, 61, 521, 3))
        self.line_30.setMaximumSize(QSize(10000, 3))
        self.line_30.setStyleSheet(u"color: white;\n"
"background-color:rgba(255,5,25,40);\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_30.setFrameShape(QFrame.HLine)
        self.line_30.setFrameShadow(QFrame.Sunken)
        self.line_8 = QFrame(self.widget_36)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(0, 10, 1091, 3))
        self.line_8.setMaximumSize(QSize(10000, 3))
        self.line_8.setStyleSheet(u"color: white;\n"
"background-color:rgba(255,5,25,40);\n"
"\n"
"font-weight:bold;\n"
"\n"
"\n"
"font-size: 1pt;\n"
"border-radius:0px;")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.checkBox_9 = QCheckBox(self.widget_36)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setGeometry(QRect(1060, 10, 21, 31))
        self.checkBox_9.setStyleSheet(u"QCheckBox{\n"
"background-color:none;\n"
"    spacing: 5px;\n"
"}\n"
"QCheckBox::indicator {\n"
"	width: 15px;\n"
"	height: 15px;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/newPrefix/image (16).png);\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    image: url(:/newPrefix/image (22).png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/newPrefix/image (33).png);\n"
"}\n"
"\n"
"\n"
"")
        self.checkBox_9.setIconSize(QSize(40, 40))
        self.Gpu2_56 = QLabel(self.widget_36)
        self.Gpu2_56.setObjectName(u"Gpu2_56")
        self.Gpu2_56.setGeometry(QRect(360, 15, 701, 20))
        self.Gpu2_56.setMinimumSize(QSize(50, 20))
        self.Gpu2_56.setMaximumSize(QSize(1000, 35))
        self.Gpu2_56.setFont(font4)
        self.Gpu2_56.setStyleSheet(u"\n"
"color:rgba(250,250,250,150);\n"
"background-color:none;\n"
"\n"
"\n"
"border: none;\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_56.setLineWidth(0)
        self.widget_37 = QWidget(self.centralwidget)
        self.widget_37.setObjectName(u"widget_37")
        self.widget_37.setGeometry(QRect(200, 320, 311, 131))
        self.widget_37.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,20), stop:1 rgba(205,200,250,20));\n"
"border-radius:7px;\n"
"\n"
"\n"
"border: none;")
        self.Gpu2_58 = QLabel(self.widget_37)
        self.Gpu2_58.setObjectName(u"Gpu2_58")
        self.Gpu2_58.setGeometry(QRect(10, 10, 291, 30))
        self.Gpu2_58.setMinimumSize(QSize(50, 30))
        self.Gpu2_58.setMaximumSize(QSize(1000, 35))
        self.Gpu2_58.setFont(font4)
        self.Gpu2_58.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_58.setLineWidth(0)
        self.Gpu2_59 = QLabel(self.widget_37)
        self.Gpu2_59.setObjectName(u"Gpu2_59")
        self.Gpu2_59.setGeometry(QRect(10, 50, 291, 30))
        self.Gpu2_59.setMinimumSize(QSize(50, 30))
        self.Gpu2_59.setMaximumSize(QSize(1000, 35))
        self.Gpu2_59.setFont(font4)
        self.Gpu2_59.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_59.setLineWidth(0)
        self.Gpu2_60 = QLabel(self.widget_37)
        self.Gpu2_60.setObjectName(u"Gpu2_60")
        self.Gpu2_60.setGeometry(QRect(10, 90, 291, 30))
        self.Gpu2_60.setMinimumSize(QSize(50, 30))
        self.Gpu2_60.setMaximumSize(QSize(1000, 35))
        self.Gpu2_60.setFont(font4)
        self.Gpu2_60.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_60.setLineWidth(0)
        self.Gpu2_61 = QLabel(self.centralwidget)
        self.Gpu2_61.setObjectName(u"Gpu2_61")
        self.Gpu2_61.setGeometry(QRect(530, 340, 121, 81))
        self.Gpu2_61.setMinimumSize(QSize(0, 0))
        self.Gpu2_61.setMaximumSize(QSize(200, 200))
        self.Gpu2_61.setStyleSheet(u"\n"
"color: white;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,20), stop:1 rgba(205,200,250,20));;\n"
"\n"
"\n"
"border: none;\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_61.setLineWidth(0)
        self.Gpu2_61.setScaledContents(True)
        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(20, 640, 41, 41))
        self.pushButton_12.setMinimumSize(QSize(32, 32))
        self.pushButton_12.setMaximumSize(QSize(60, 60))
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,50), stop:1 rgba(205,200,250,50));\n"
"color: white;\n"
"\n"
"font-size: 15pt;\n"
"border: none;\n"
"border-radius: 5px;}\n"
"QPushButton:hover {background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,70), stop:1 rgba(205,200,250,70));\n"
"}\n"
"QPushButton:pressed {background-color:rgba(255,255,255,60);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-vk-96 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon1)
        self.pushButton_12.setIconSize(QSize(50, 40))
        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(70, 640, 41, 41))
        self.pushButton_15.setMinimumSize(QSize(32, 32))
        self.pushButton_15.setMaximumSize(QSize(60, 60))
        self.pushButton_15.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,50), stop:1 rgba(205,200,250,50));\n"
"color: white;\n"
"\n"
"font-size: 15pt;\n"
"border: none;\n"
"border-radius: 5px;}\n"
"QPushButton:hover {background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,70), stop:1 rgba(205,200,250,70));\n"
"}\n"
"QPushButton:pressed {background-color:rgba(255,255,255,60);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-\u043f\u043e\u0447\u0442\u0430-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon2)
        self.pushButton_15.setIconSize(QSize(40, 40))
        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(120, 640, 41, 41))
        self.pushButton_14.setMinimumSize(QSize(32, 32))
        self.pushButton_14.setMaximumSize(QSize(60, 60))
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,50), stop:1 rgba(205,200,250,50));\n"
"color: white;\n"
"\n"
"font-size: 15pt;\n"
"border: none;\n"
"border-radius: 5px;}\n"
"QPushButton:hover {background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,70), stop:1 rgba(205,200,250,70));\n"
"}\n"
"QPushButton:pressed {background-color:rgba(255,255,255,60);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-\u043d\u043e\u0432\u044b\u0439-\u043b\u043e\u0433\u043e\u0442\u0438\u043f-discord-new-logo-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon3)
        self.pushButton_14.setIconSize(QSize(40, 40))
        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(170, 640, 41, 41))
        self.pushButton_13.setMinimumSize(QSize(32, 32))
        self.pushButton_13.setMaximumSize(QSize(60, 60))
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,50), stop:1 rgba(205,200,250,50));\n"
"color: white;\n"
"\n"
"font-size: 15pt;\n"
"border: none;\n"
"border-radius: 5px;}\n"
"QPushButton:hover {background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,70), stop:1 rgba(205,200,250,70));\n"
"}\n"
"QPushButton:pressed {background-color:rgba(255,255,255,60);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons8-youtube-96 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon4)
        self.pushButton_13.setIconSize(QSize(40, 40))
        self.Gpu2_71 = QLabel(self.centralwidget)
        self.Gpu2_71.setObjectName(u"Gpu2_71")
        self.Gpu2_71.setGeometry(QRect(220, 640, 41, 41))
        self.Gpu2_71.setMinimumSize(QSize(0, 0))
        self.Gpu2_71.setMaximumSize(QSize(200, 200))
        self.Gpu2_71.setStyleSheet(u"\n"
"color: white;\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,20), stop:1 rgba(205,200,250,20));;\n"
"\n"
"\n"
"border: none;\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_71.setLineWidth(0)
        self.Gpu2_71.setPixmap(QPixmap(u":/icons/icons8-\u043f\u0438\u0442\u043e\u043d-96.png"))
        self.Gpu2_71.setScaledContents(True)
        self.widget_38 = QWidget(self.centralwidget)
        self.widget_38.setObjectName(u"widget_38")
        self.widget_38.setGeometry(QRect(500, 450, 171, 211))
        self.widget_38.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,20), stop:1 rgba(205,200,250,20));\n"
"border-radius:7px;\n"
"\n"
"\n"
"border: none;")
        self.label_42 = QLabel(self.widget_38)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(50, 10, 111, 30))
        self.label_42.setMinimumSize(QSize(35, 30))
        self.label_42.setMaximumSize(QSize(16777215, 35))
        self.label_42.setFont(font10)
        self.label_42.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.label_43 = QLabel(self.widget_38)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(50, 50, 111, 30))
        self.label_43.setMinimumSize(QSize(35, 30))
        self.label_43.setMaximumSize(QSize(16777215, 35))
        self.label_43.setFont(font10)
        self.label_43.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.label_44 = QLabel(self.widget_38)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(50, 90, 111, 30))
        self.label_44.setMinimumSize(QSize(35, 30))
        self.label_44.setMaximumSize(QSize(16777215, 35))
        self.label_44.setFont(font10)
        self.label_44.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.Gpu2_63 = QLabel(self.widget_38)
        self.Gpu2_63.setObjectName(u"Gpu2_63")
        self.Gpu2_63.setGeometry(QRect(10, 90, 30, 30))
        self.Gpu2_63.setMinimumSize(QSize(0, 0))
        self.Gpu2_63.setMaximumSize(QSize(180, 35))
        self.Gpu2_63.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_63.setLineWidth(0)
        self.Gpu2_63.setPixmap(QPixmap(u":/icons/imagec (1).png"))
        self.Gpu2_63.setScaledContents(True)
        self.Gpu2_63.setMargin(1)
        self.Gpu2_72 = QLabel(self.widget_38)
        self.Gpu2_72.setObjectName(u"Gpu2_72")
        self.Gpu2_72.setGeometry(QRect(10, 10, 30, 30))
        self.Gpu2_72.setMinimumSize(QSize(0, 0))
        self.Gpu2_72.setMaximumSize(QSize(180, 35))
        self.Gpu2_72.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_72.setLineWidth(0)
        self.Gpu2_72.setPixmap(QPixmap(u":/icons/imagge (1).png"))
        self.Gpu2_72.setScaledContents(True)
        self.Gpu2_72.setMargin(1)
        self.Gpu2_73 = QLabel(self.widget_38)
        self.Gpu2_73.setObjectName(u"Gpu2_73")
        self.Gpu2_73.setGeometry(QRect(10, 50, 30, 30))
        self.Gpu2_73.setMinimumSize(QSize(0, 0))
        self.Gpu2_73.setMaximumSize(QSize(180, 35))
        self.Gpu2_73.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_73.setLineWidth(0)
        self.Gpu2_73.setPixmap(QPixmap(u":/icons/imaget (1).png"))
        self.Gpu2_73.setScaledContents(True)
        self.Gpu2_73.setMargin(3)
        self.Gpu2_73.setIndent(2)
        self.label_45 = QLabel(self.widget_38)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(50, 130, 111, 30))
        self.label_45.setMinimumSize(QSize(35, 30))
        self.label_45.setMaximumSize(QSize(16777215, 35))
        self.label_45.setFont(font10)
        self.label_45.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.Gpu2_78 = QLabel(self.widget_38)
        self.Gpu2_78.setObjectName(u"Gpu2_78")
        self.Gpu2_78.setGeometry(QRect(10, 130, 30, 30))
        self.Gpu2_78.setMinimumSize(QSize(0, 0))
        self.Gpu2_78.setMaximumSize(QSize(180, 35))
        self.Gpu2_78.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_78.setLineWidth(0)
        self.Gpu2_78.setPixmap(QPixmap(u":/icons/image (9).png"))
        self.Gpu2_78.setScaledContents(True)
        self.label_46 = QLabel(self.widget_38)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(50, 170, 111, 30))
        self.label_46.setMinimumSize(QSize(35, 30))
        self.label_46.setMaximumSize(QSize(16777215, 35))
        self.label_46.setFont(font10)
        self.label_46.setStyleSheet(u"background-color:none;\n"
"color: white;\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 13pt;\n"
"border-radius:7px;")
        self.Gpu2_108 = QLabel(self.widget_38)
        self.Gpu2_108.setObjectName(u"Gpu2_108")
        self.Gpu2_108.setGeometry(QRect(10, 170, 30, 30))
        self.Gpu2_108.setMinimumSize(QSize(0, 0))
        self.Gpu2_108.setMaximumSize(QSize(180, 35))
        self.Gpu2_108.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_108.setLineWidth(0)
        self.Gpu2_108.setPixmap(QPixmap(u":/icons/image (12).png"))
        self.Gpu2_108.setScaledContents(True)
        self.Gpu2_108.setMargin(2)
        self.widget_39 = QWidget(self.centralwidget)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setGeometry(QRect(680, 450, 431, 211))
        self.widget_39.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:2, x1:0, y2:0, stop:0\n"
"rgba(55,250,55), stop:0.4274 rgba(35,30,60,20), stop:1 rgba(205,200,250,20));\n"
"border-radius:7px;\n"
"\n"
"\n"
"border: none;")
        self.Gpu2_74 = QLabel(self.widget_39)
        self.Gpu2_74.setObjectName(u"Gpu2_74")
        self.Gpu2_74.setGeometry(QRect(10, 10, 411, 30))
        self.Gpu2_74.setMinimumSize(QSize(50, 30))
        self.Gpu2_74.setMaximumSize(QSize(1000, 35))
        self.Gpu2_74.setFont(font4)
        self.Gpu2_74.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_74.setLineWidth(0)
        self.Gpu2_75 = QLabel(self.widget_39)
        self.Gpu2_75.setObjectName(u"Gpu2_75")
        self.Gpu2_75.setGeometry(QRect(10, 50, 411, 30))
        self.Gpu2_75.setMinimumSize(QSize(50, 30))
        self.Gpu2_75.setMaximumSize(QSize(1000, 35))
        self.Gpu2_75.setFont(font4)
        self.Gpu2_75.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_75.setLineWidth(0)
        self.Gpu2_76 = QLabel(self.widget_39)
        self.Gpu2_76.setObjectName(u"Gpu2_76")
        self.Gpu2_76.setGeometry(QRect(10, 90, 411, 30))
        self.Gpu2_76.setMinimumSize(QSize(50, 30))
        self.Gpu2_76.setMaximumSize(QSize(1000, 35))
        self.Gpu2_76.setFont(font4)
        self.Gpu2_76.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_76.setLineWidth(0)
        self.Gpu2_77 = QLabel(self.widget_39)
        self.Gpu2_77.setObjectName(u"Gpu2_77")
        self.Gpu2_77.setGeometry(QRect(10, 130, 411, 30))
        self.Gpu2_77.setMinimumSize(QSize(50, 30))
        self.Gpu2_77.setMaximumSize(QSize(1000, 35))
        self.Gpu2_77.setFont(font4)
        self.Gpu2_77.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_77.setLineWidth(0)
        self.Gpu2_100 = QLabel(self.widget_39)
        self.Gpu2_100.setObjectName(u"Gpu2_100")
        self.Gpu2_100.setGeometry(QRect(10, 170, 411, 30))
        self.Gpu2_100.setMinimumSize(QSize(50, 30))
        self.Gpu2_100.setMaximumSize(QSize(1000, 35))
        self.Gpu2_100.setFont(font4)
        self.Gpu2_100.setStyleSheet(u"\n"
"color: white;\n"
"background-color:none;\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"font-size: 10pt;\n"
"border-radius:7px;")
        self.Gpu2_100.setLineWidth(0)
        self.Gpu2_70 = QLabel(self.centralwidget)
        self.Gpu2_70.setObjectName(u"Gpu2_70")
        self.Gpu2_70.setGeometry(QRect(880, 440, 161, 30))
        self.Gpu2_70.setMinimumSize(QSize(50, 30))
        self.Gpu2_70.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_70.setFont(font9)
        self.Gpu2_70.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_70.setLineWidth(0)
        self.Gpu2_79 = QLabel(self.centralwidget)
        self.Gpu2_79.setObjectName(u"Gpu2_79")
        self.Gpu2_79.setGeometry(QRect(850, 60, 161, 30))
        self.Gpu2_79.setMinimumSize(QSize(50, 30))
        self.Gpu2_79.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_79.setFont(font9)
        self.Gpu2_79.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_79.setLineWidth(0)
        self.Gpu2_80 = QLabel(self.centralwidget)
        self.Gpu2_80.setObjectName(u"Gpu2_80")
        self.Gpu2_80.setGeometry(QRect(1010, 60, 161, 30))
        self.Gpu2_80.setMinimumSize(QSize(50, 30))
        self.Gpu2_80.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_80.setFont(font9)
        self.Gpu2_80.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_80.setLineWidth(0)
        self.Gpu2_81 = QLabel(self.centralwidget)
        self.Gpu2_81.setObjectName(u"Gpu2_81")
        self.Gpu2_81.setGeometry(QRect(1040, 440, 161, 30))
        self.Gpu2_81.setMinimumSize(QSize(50, 30))
        self.Gpu2_81.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_81.setFont(font9)
        self.Gpu2_81.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_81.setLineWidth(0)
        self.Gpu2_82 = QLabel(self.centralwidget)
        self.Gpu2_82.setObjectName(u"Gpu2_82")
        self.Gpu2_82.setGeometry(QRect(-30, 460, 161, 30))
        self.Gpu2_82.setMinimumSize(QSize(50, 30))
        self.Gpu2_82.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_82.setFont(font9)
        self.Gpu2_82.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_82.setLineWidth(0)
        self.Gpu2_83 = QLabel(self.centralwidget)
        self.Gpu2_83.setObjectName(u"Gpu2_83")
        self.Gpu2_83.setGeometry(QRect(-30, 280, 161, 30))
        self.Gpu2_83.setMinimumSize(QSize(50, 30))
        self.Gpu2_83.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_83.setFont(font9)
        self.Gpu2_83.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_83.setLineWidth(0)
        self.Gpu2_84 = QLabel(self.centralwidget)
        self.Gpu2_84.setObjectName(u"Gpu2_84")
        self.Gpu2_84.setGeometry(QRect(-20, 60, 161, 30))
        self.Gpu2_84.setMinimumSize(QSize(50, 30))
        self.Gpu2_84.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_84.setFont(font9)
        self.Gpu2_84.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_84.setLineWidth(0)
        self.Gpu2_85 = QLabel(self.centralwidget)
        self.Gpu2_85.setObjectName(u"Gpu2_85")
        self.Gpu2_85.setGeometry(QRect(980, 480, 161, 30))
        self.Gpu2_85.setMinimumSize(QSize(50, 30))
        self.Gpu2_85.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_85.setFont(font9)
        self.Gpu2_85.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_85.setLineWidth(0)
        self.Gpu2_86 = QLabel(self.centralwidget)
        self.Gpu2_86.setObjectName(u"Gpu2_86")
        self.Gpu2_86.setGeometry(QRect(1040, 520, 161, 30))
        self.Gpu2_86.setMinimumSize(QSize(50, 30))
        self.Gpu2_86.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_86.setFont(font9)
        self.Gpu2_86.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_86.setLineWidth(0)
        self.Gpu2_87 = QLabel(self.centralwidget)
        self.Gpu2_87.setObjectName(u"Gpu2_87")
        self.Gpu2_87.setGeometry(QRect(1080, 560, 161, 30))
        self.Gpu2_87.setMinimumSize(QSize(50, 30))
        self.Gpu2_87.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_87.setFont(font9)
        self.Gpu2_87.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_87.setLineWidth(0)
        self.Gpu2_88 = QLabel(self.centralwidget)
        self.Gpu2_88.setObjectName(u"Gpu2_88")
        self.Gpu2_88.setGeometry(QRect(990, 100, 161, 30))
        self.Gpu2_88.setMinimumSize(QSize(50, 30))
        self.Gpu2_88.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_88.setFont(font9)
        self.Gpu2_88.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_88.setLineWidth(0)
        self.Gpu2_89 = QLabel(self.centralwidget)
        self.Gpu2_89.setObjectName(u"Gpu2_89")
        self.Gpu2_89.setGeometry(QRect(1020, 140, 161, 30))
        self.Gpu2_89.setMinimumSize(QSize(50, 30))
        self.Gpu2_89.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_89.setFont(font9)
        self.Gpu2_89.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_89.setLineWidth(0)
        self.Gpu2_90 = QLabel(self.centralwidget)
        self.Gpu2_90.setObjectName(u"Gpu2_90")
        self.Gpu2_90.setGeometry(QRect(1060, 180, 161, 30))
        self.Gpu2_90.setMinimumSize(QSize(50, 30))
        self.Gpu2_90.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_90.setFont(font9)
        self.Gpu2_90.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_90.setLineWidth(0)
        self.Gpu2_91 = QLabel(self.centralwidget)
        self.Gpu2_91.setObjectName(u"Gpu2_91")
        self.Gpu2_91.setGeometry(QRect(-70, 320, 161, 30))
        self.Gpu2_91.setMinimumSize(QSize(50, 30))
        self.Gpu2_91.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_91.setFont(font9)
        self.Gpu2_91.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_91.setLineWidth(0)
        self.Gpu2_92 = QLabel(self.centralwidget)
        self.Gpu2_92.setObjectName(u"Gpu2_92")
        self.Gpu2_92.setGeometry(QRect(-100, 360, 161, 30))
        self.Gpu2_92.setMinimumSize(QSize(50, 30))
        self.Gpu2_92.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_92.setFont(font9)
        self.Gpu2_92.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_92.setLineWidth(0)
        self.Gpu2_93 = QLabel(self.centralwidget)
        self.Gpu2_93.setObjectName(u"Gpu2_93")
        self.Gpu2_93.setGeometry(QRect(-70, 399, 161, 51))
        self.Gpu2_93.setMinimumSize(QSize(50, 30))
        self.Gpu2_93.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_93.setFont(font9)
        self.Gpu2_93.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_93.setLineWidth(0)
        self.Gpu2_94 = QLabel(self.centralwidget)
        self.Gpu2_94.setObjectName(u"Gpu2_94")
        self.Gpu2_94.setGeometry(QRect(-50, 20, 161, 30))
        self.Gpu2_94.setMinimumSize(QSize(50, 30))
        self.Gpu2_94.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_94.setFont(font9)
        self.Gpu2_94.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_94.setLineWidth(0)
        self.Gpu2_95 = QLabel(self.centralwidget)
        self.Gpu2_95.setObjectName(u"Gpu2_95")
        self.Gpu2_95.setGeometry(QRect(-70, -20, 161, 30))
        self.Gpu2_95.setMinimumSize(QSize(50, 30))
        self.Gpu2_95.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_95.setFont(font9)
        self.Gpu2_95.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_95.setLineWidth(0)
        self.Gpu2_101 = QLabel(self.centralwidget)
        self.Gpu2_101.setObjectName(u"Gpu2_101")
        self.Gpu2_101.setGeometry(QRect(530, 340, 121, 41))
        self.Gpu2_101.setMinimumSize(QSize(50, 30))
        self.Gpu2_101.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_101.setFont(font9)
        self.Gpu2_101.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_101.setLineWidth(0)
        self.Gpu2_102 = QLabel(self.centralwidget)
        self.Gpu2_102.setObjectName(u"Gpu2_102")
        self.Gpu2_102.setGeometry(QRect(560, 390, 91, 31))
        self.Gpu2_102.setMinimumSize(QSize(50, 20))
        self.Gpu2_102.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_102.setFont(font9)
        self.Gpu2_102.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_102.setLineWidth(0)
        self.Gpu2_107 = QLabel(self.centralwidget)
        self.Gpu2_107.setObjectName(u"Gpu2_107")
        self.Gpu2_107.setGeometry(QRect(710, 400, 441, 31))
        self.Gpu2_107.setMinimumSize(QSize(50, 20))
        self.Gpu2_107.setMaximumSize(QSize(1000, 1000))
        self.Gpu2_107.setFont(font9)
        self.Gpu2_107.setStyleSheet(u"\n"
"color:rgba(250,250,250,20);\n"
"background-color:none;\n"
"\n"
"\n"
"border:none;\n"
"font-size: 70pt;\n"
"border-radius:7px;")
        self.Gpu2_107.setLineWidth(0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.pushButton_11.setText("")
        self.Gpu2_39.setText("")
        self.Gpu2_20.setText("")
        self.Gpu2_40.setText("")
        self.label_12.setText("")
        self.mem_4.setText(QCoreApplication.translate("MainWindow", u"Testing version 0.0.3 ", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"THETL", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"project", None))
        a = wmi.WMI()
        os_info = a.Win32_OperatingSystem()[0]
        self.Gpu2_32.setText(QCoreApplication.translate("MainWindow", (f"{os_info.RegisteredUser} | {a.Win32_Processor()[0].SystemName}")))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Processors", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"GPU | Drivers", None))
        self.Gpu2_22.setText(QCoreApplication.translate("MainWindow", ((f"{cpuinfo.get_cpu_info()['brand_raw']}  "))))

        self.Gpu2_23.setText(
                QCoreApplication.translate("MainWindow", ((f"{controller.wmi_property('Name').value} | {controller.wmi_property('DriverVersion').value}"))))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Cores", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Total cores", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"CPU id", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Condition", None))
        a = wmi.WMI()
        self.label_31.setText(QCoreApplication.translate("MainWindow", f"{a.Win32_Processor()[0].SocketDesignation}", None))
        self.Gpu2_24.setText(QCoreApplication.translate("MainWindow", ((f"{psutil.cpu_count(logical=False)}"))))
        self.Gpu2_25.setText(QCoreApplication.translate("MainWindow", ((f"{psutil.cpu_count(logical=True)}"))))
        proc_id_com = 'WMIC CPU GET ProcessorId /VALUE'.split()
        processor_id = str(subprocess.check_output(proc_id_com, shell=True)).split("\\n")[2].split("\\r")[0].split("=")[1]
        self.Gpu2_26.setText(QCoreApplication.translate("MainWindow", (f"{processor_id} ")))
        a = wmi.WMI()
        w = a.Win32_Processor()[0].Availability
        if w==1:
                w = 'Not defined ⚠️'
        if w==2:
                w = 'Not defined ⚠️'
        if w==3:
                w = 'Full power, good 👍'
        if w==4:
                w = 'Warning ❗'
        if w==5:
                w = 'Being tested ⭕'
        if w==6:
                w = 'Not applicable ⚠️'
        if w==7:
                w = 'The power is off ⚠️'
        if w==8:
                w = 'Autonomous operation 👌'
        if w==9:
                w = 'Does not serve ⚠️️'
        if w==10:
                w = 'Degradation ‼️'
        if w==11:
                w = 'Not installed ⚠️'
        if w==12:
                w = 'Installation error ❗'
        if w==13 or w==14 or w==15:
                w = 'Energy saving ❓'
        if w==16:
                w = 'Power supply cycle ⚠️'
        if w==17:
                w = 'Warning ❗'
        self.Gpu2_27.setText(QCoreApplication.translate("MainWindow", (f"{w}")))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Condition", None))

        b = wmi.WMI().Win32_VideoController()[0].Availability
        if b==1:
                b = 'Not defined ⚠️'
        if b==2:
                b = 'Not defined ⚠️'
        if b==3:
                b = 'Full power, good 👍'
        if b==4:
                b = 'Warning ❗'
        if b==5:
                b = 'Being tested ⭕'
        if b==6:
                b = 'Not applicable ⚠️'
        if b==7:
                b = 'The power is off ⚠️'
        if b==8:
                b = 'Autonomous operation 👌'
        if b==9:
                b = 'Does not serve ⚠️'
        if b==10:
                b = 'Degradation ‼️'
        if b==11:
                b = 'Not installed ⚠️'
        if b==12:
                b = 'Installation error ❗'
        if b==13 or b==14 or b==15:
                b = 'Energy saving ❓'
        if b==16:
                b = 'Power supply cycle ⚠️'
        if b==17:
                b = 'Warning ❗'
        self.Gpu2_28.setText(QCoreApplication.translate("MainWindow", ((f"{b}"))))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        a = wmi.WMI()
        m = a.Win32_VideoController()[0].VideoArchitecture
        if m == 1:
                m = 'Another type'
        if m == 2:
                m = 'Unknown'
        if m == 3:
                m = 'CGA'
        if m == 4:
                m = 'EGA'
        if m == 5:
                m = 'VGA'
        if m == 6:
                m = 'SVGA'
        if m == 7:
                m = 'MDA'
        if m == 8:
                m = 'HGC'
        if m == 9:
                m = 'MCGA'
        if m == 10:
                m = '8514A'
        if m == 11:
                m = 'XGA'
        if m == 12:
                m = 'Linear Frame Buffer'
        if m == 160:
                m = 'PC-98'
        self.Gpu2_41.setText(QCoreApplication.translate("MainWindow", ((f"h - {controller.wmi_property('CurrentHorizontalResolution').value} | v - {controller.wmi_property('CurrentVerticalResolution').value} | Architecture - {m}"))))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Manufacturer", None))
        collect_info_dict = dict()
        collect_info_dict['system_info'] = {
                        'processor': {'name': uname().processor}}
        self.Gpu2_42.setText(QCoreApplication.translate("MainWindow", (f"{uname().processor}")))
        self.Gpu2_51.setText("")
        self.Gpu2_52.setText("")
        self.Gpu2_62.setText("")
        self.Gpu2_96.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.Gpu2_97.setText(QCoreApplication.translate("MainWindow", u"H|J", None))
        self.Gpu2_98.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.Gpu2_99.setText(QCoreApplication.translate("MainWindow", u"THE", None))
        self.Gpu2_103.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.Gpu2_104.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.Gpu2_105.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.Gpu2_106.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Manufacturer", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        motherboard = dict()
        c = WMI().Win32_BaseBoard()[0]
        motherboard.update({'Manufacturer': c.Manufacturer})
        self.Gpu2_29.setText(QCoreApplication.translate("MainWindow", ((f"{c.Manufacturer} "))))
        a = wmi.WMI()
        self.Gpu2_30.setText(
                        QCoreApplication.translate("MainWindow", ((f"{a.Win32_ComputerSystem()[0].Description} | {a.Win32_ComputerSystem()[0].SystemType}"))))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Chipset", None))
        cpu_info = dict()
        cpu_info.update({'Product': c.Product})
        self.Gpu2_31.setText(QCoreApplication.translate("MainWindow", ((f"{c.Product}"))))

        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Version bios", None))
        verb_com = 'WMIC BIOS GET Version /VALUE'.split()
        self.Gpu2_35.setText(
                QCoreApplication.translate("MainWindow", ((
                        f"{str(subprocess.check_output(verb_com, shell=True)).split("\\n")[2].split("\\r")[0].split("=")[1]}"))))
        self.Gpu2_47.setText("")
        self.Gpu2_48.setText("")
        self.Gpu2_49.setText("")
        self.Gpu2_50.setText("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Motherboard", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Memory", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Memory", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Part number", None))
        self.Gpu2_45.setText("")
        self.Gpu2_44.setText("")
        self.Gpu2_46.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Additional information", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Info system", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Architecture", None))
        computer = wmi.WMI()
        os_info = computer.Win32_OperatingSystem()[0]
        self.Gpu2_36.setText(QCoreApplication.translate("MainWindow", (f"{os_info.caption}")))
        collect_info_dict = dict()
        collect_info_dict['system_info'] = {'system': {'comp_name': uname().node,
                                                                       'os_name': f"{uname().system} {uname().release}",
                                                                       'version': uname().version,
                                                                       'machine': uname().machine}, }
        computer = wmi.WMI()
        os_info = computer.Win32_OperatingSystem()[0]
        self.Gpu2_37.setText(QCoreApplication.translate("MainWindow", (f"{uname().machine} | {os_info.OSArchitecture}")))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Assembling", None))
        self.Gpu2_38.setText(QCoreApplication.translate("MainWindow", (f"{uname().version}")))
        self.Gpu2_53.setText("")
        self.Gpu2_54.setText("")
        self.Gpu2_55.setText("")
        self.checkBox_9.setText("")
        self.Gpu2_56.setText(QCoreApplication.translate("MainWindow", u"Thank you for downloading this application, an application for displaying real-time information will be released soon", None))
        collect_info_dict = dict()
        collect_info_dict['system_info'] = {'ram': {'volume': correct_size(psutil.virtual_memory().total)}}
        ram_man_com = 'WMIC MEMORYCHIP GET Manufacturer /value'.split()
        ram_manufacturer = str(subprocess.check_output(ram_man_com, shell=True)).strip().split("\\n")
        for num, ram_m in enumerate(ram_manufacturer):
                if 'Manufacturer=' in ram_m:
                        self.Gpu2_58.setText(QCoreApplication.translate("MainWindow", ((
                                f"{ram_m.split("\\r")[0].split("=")[1].strip()} | Total {correct_size(psutil.virtual_memory().total)}"))))
        ram_spf_com = 'WMIC MEMORYCHIP GET Speed /value'.split()
        ram_speed_frequency = str(subprocess.check_output(ram_spf_com, shell=True)).strip().split("\\n")
        for num, rsf in enumerate(ram_speed_frequency):
                if 'Speed=' in rsf:
                        self.Gpu2_59.setText(
                                QCoreApplication.translate("MainWindow",
                                                           ((f"{rsf.split("\\r")[0].split("=")[1].strip()} MHz"))))
        ram_pn_com = 'WMIC MEMORYCHIP GET PartNumber /value'.split()
        ram_part_number = str(subprocess.check_output(ram_pn_com, shell=True)).strip().split("\\n")
        for num, rpn in enumerate(ram_part_number):
            if 'PartNumber=' in rpn:
                self.Gpu2_60.setText(QCoreApplication.translate("MainWindow", ((
                    f"{rpn.split("\\r")[0].split("=")[1].strip()}"))))
        self.Gpu2_61.setText("")
        self.pushButton_12.setText("")
        self.pushButton_15.setText("")
        self.pushButton_14.setText("")
        self.pushButton_13.setText("")
        self.Gpu2_71.setText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"UUid system", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Key activate", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"OS serial", None))
        self.Gpu2_63.setText("")
        self.Gpu2_72.setText("")
        self.Gpu2_73.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"win_Test", None))
        self.Gpu2_78.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"SystemDirect", None))
        self.Gpu2_108.setText("")
        uuid_sys_com = 'WMIC CSPRODUCT GET UUID /VALUE'.split()
        uuid_system = str(subprocess.check_output(uuid_sys_com, shell=True)).split("\\n")[2].split("\\r")[0].split("=")[1]
        self.Gpu2_74.setText(QCoreApplication.translate("MainWindow", (f"{uuid_system} ")))
        win_info = dict()
        if pkey := product_key.get_windows_product_key_from_reg():
                win_info.update({"ActivateKey": pkey})
        elif pkey := product_key.get_windows_product_key_from_wmi():
                win_info.update({"ActivateKey": pkey})
        else:
                win_info.update({"ActivateKey": "No Key"})
        self.Gpu2_75.setText(QCoreApplication.translate("MainWindow", (f"{pkey}")))
        os_sn_com = 'WMIC OS get SerialNumber /value'.split()
        os_serial_number = str(subprocess.check_output(os_sn_com, shell=True)).strip().split("\\n")[2].split("\\r")[0].split("=")[1]
        self.Gpu2_76.setText(QCoreApplication.translate("MainWindow", (f"{os_serial_number} ")))
        self.Gpu2_77.setText(QCoreApplication.translate("MainWindow", f'MtBoard - {a.Win32_BaseBoard()[0].Status} | CPU - {a.Win32_Processor()[0].Status} | GPU - {wmi.WMI().Win32_VideoController()[0].Status} | NTFS - {os_info.Status} | Mem - {a.Win32_ComputerSystem()[0].Status}'))
        computer = wmi.WMI()
        os_info = computer.Win32_OperatingSystem()[0]
        self.Gpu2_100.setText(QCoreApplication.translate("MainWindow", (f"{os_info.SystemDirectory} | NTFS")))
        self.Gpu2_70.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.Gpu2_79.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.Gpu2_80.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.Gpu2_81.setText(QCoreApplication.translate("MainWindow", u"X/C", None))
        self.Gpu2_82.setText(QCoreApplication.translate("MainWindow", u"N/D", None))
        self.Gpu2_83.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.Gpu2_84.setText(QCoreApplication.translate("MainWindow", u"Q/\"A", None))
        self.Gpu2_85.setText(QCoreApplication.translate("MainWindow", u"ZVB", None))
        self.Gpu2_86.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.Gpu2_87.setText(QCoreApplication.translate("MainWindow", u"|Q", None))
        self.Gpu2_88.setText(QCoreApplication.translate("MainWindow", u"K|P", None))
        self.Gpu2_89.setText(QCoreApplication.translate("MainWindow", u"WW", None))
        self.Gpu2_90.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.Gpu2_91.setText(QCoreApplication.translate("MainWindow", u"N/??", None))
        self.Gpu2_92.setText(QCoreApplication.translate("MainWindow", u"N/Y", None))
        self.Gpu2_93.setText(QCoreApplication.translate("MainWindow", u"N/R", None))
        self.Gpu2_94.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.Gpu2_95.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.Gpu2_101.setText(QCoreApplication.translate("MainWindow", u"G''E", None))
        self.Gpu2_102.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.Gpu2_107.setText(QCoreApplication.translate("MainWindow", u"u/?   Tr Bu      f", None))

    # retranslateUi

