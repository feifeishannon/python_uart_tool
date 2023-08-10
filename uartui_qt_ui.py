# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\me\Software\testpython\python_uart_tool\uartui_qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 732)
        MainWindow.setStyleSheet("")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(10, 53, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 275, 133, 20))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 85, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.comboBox.setPalette(palette)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.openUARTPortButton = QtWidgets.QPushButton(self.widget)
        self.openUARTPortButton.setObjectName("openUARTPortButton")
        self.horizontalLayout.addWidget(self.openUARTPortButton)
        self.horizontalLayout_13.addWidget(self.groupBox)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_13.addWidget(self.line)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.fan1_5 = QtWidgets.QFrame(self.groupBox_2)
        self.fan1_5.setGeometry(QtCore.QRect(13, 63, 68, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fan1_5.sizePolicy().hasHeightForWidth())
        self.fan1_5.setSizePolicy(sizePolicy)
        self.fan1_5.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan1_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan1_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan1_5.setObjectName("fan1_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.fan1_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.fan1_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.fan1_7 = QtWidgets.QFrame(self.groupBox_2)
        self.fan1_7.setEnabled(True)
        self.fan1_7.setGeometry(QtCore.QRect(13, 25, 68, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fan1_7.sizePolicy().hasHeightForWidth())
        self.fan1_7.setSizePolicy(sizePolicy)
        self.fan1_7.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan1_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan1_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan1_7.setObjectName("fan1_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fan1_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.fan1_7)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.fan1_9 = QtWidgets.QFrame(self.groupBox_2)
        self.fan1_9.setGeometry(QtCore.QRect(13, 101, 68, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fan1_9.sizePolicy().hasHeightForWidth())
        self.fan1_9.setSizePolicy(sizePolicy)
        self.fan1_9.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan1_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan1_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan1_9.setObjectName("fan1_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.fan1_9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.fan1_9)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(310, 20, 152, 119))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.horizontalLayout_6.addWidget(self.lcdNumber_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.horizontalLayout_7.addWidget(self.lcdNumber_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.groupBox_4)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.horizontalLayout_8.addWidget(self.lcdNumber_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(11, 150, 441, 144))
        self.groupBox_5.setObjectName("groupBox_5")
        self.fan6_3 = QtWidgets.QFrame(self.groupBox_5)
        self.fan6_3.setGeometry(QtCore.QRect(128, 22, 16, 112))
        self.fan6_3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan6_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan6_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan6_3.setObjectName("fan6_3")
        self.label_14 = QtWidgets.QLabel(self.fan6_3)
        self.label_14.setGeometry(QtCore.QRect(0, 10, 12, 92))
        self.label_14.setStyleSheet("")
        self.label_14.setTextFormat(QtCore.Qt.AutoText)
        self.label_14.setScaledContents(False)
        self.label_14.setWordWrap(False)
        self.label_14.setOpenExternalLinks(False)
        self.label_14.setObjectName("label_14")
        self.fan6_4 = QtWidgets.QFrame(self.groupBox_5)
        self.fan6_4.setGeometry(QtCore.QRect(144, 22, 16, 112))
        self.fan6_4.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan6_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan6_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan6_4.setObjectName("fan6_4")
        self.label_15 = QtWidgets.QLabel(self.fan6_4)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 12, 92))
        self.label_15.setStyleSheet("")
        self.label_15.setTextFormat(QtCore.Qt.AutoText)
        self.label_15.setScaledContents(False)
        self.label_15.setWordWrap(False)
        self.label_15.setOpenExternalLinks(False)
        self.label_15.setObjectName("label_15")
        self.fan2_3 = QtWidgets.QFrame(self.groupBox_5)
        self.fan2_3.setGeometry(QtCore.QRect(198, 22, 16, 112))
        self.fan2_3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan2_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan2_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan2_3.setObjectName("fan2_3")
        self.label_17 = QtWidgets.QLabel(self.fan2_3)
        self.label_17.setGeometry(QtCore.QRect(0, 10, 12, 92))
        self.label_17.setStyleSheet("")
        self.label_17.setTextFormat(QtCore.Qt.AutoText)
        self.label_17.setScaledContents(False)
        self.label_17.setWordWrap(False)
        self.label_17.setOpenExternalLinks(False)
        self.label_17.setObjectName("label_17")
        self.fan6_5 = QtWidgets.QFrame(self.groupBox_5)
        self.fan6_5.setGeometry(QtCore.QRect(420, 20, 16, 112))
        self.fan6_5.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan6_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan6_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan6_5.setObjectName("fan6_5")
        self.label_23 = QtWidgets.QLabel(self.fan6_5)
        self.label_23.setGeometry(QtCore.QRect(0, 10, 12, 92))
        self.label_23.setStyleSheet("")
        self.label_23.setTextFormat(QtCore.Qt.AutoText)
        self.label_23.setScaledContents(False)
        self.label_23.setWordWrap(False)
        self.label_23.setOpenExternalLinks(False)
        self.label_23.setObjectName("label_23")
        self.fan1_3 = QtWidgets.QFrame(self.groupBox_5)
        self.fan1_3.setGeometry(QtCore.QRect(160, 22, 32, 112))
        self.fan1_3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan1_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan1_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan1_3.setObjectName("fan1_3")
        self.label_16 = QtWidgets.QLabel(self.fan1_3)
        self.label_16.setGeometry(QtCore.QRect(10, 10, 12, 92))
        self.label_16.setStyleSheet("")
        self.label_16.setTextFormat(QtCore.Qt.AutoText)
        self.label_16.setScaledContents(False)
        self.label_16.setWordWrap(False)
        self.label_16.setOpenExternalLinks(False)
        self.label_16.setObjectName("label_16")
        self.fan4_3 = QtWidgets.QFrame(self.groupBox_5)
        self.fan4_3.setGeometry(QtCore.QRect(230, 22, 16, 112))
        self.fan4_3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan4_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan4_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan4_3.setObjectName("fan4_3")
        self.label_19 = QtWidgets.QLabel(self.fan4_3)
        self.label_19.setGeometry(QtCore.QRect(10, 10, 12, 92))
        self.label_19.setStyleSheet("")
        self.label_19.setTextFormat(QtCore.Qt.AutoText)
        self.label_19.setScaledContents(False)
        self.label_19.setWordWrap(False)
        self.label_19.setOpenExternalLinks(False)
        self.label_19.setObjectName("label_19")
        self.fan6_6 = QtWidgets.QFrame(self.groupBox_5)
        self.fan6_6.setGeometry(QtCore.QRect(400, 20, 16, 112))
        self.fan6_6.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan6_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan6_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan6_6.setObjectName("fan6_6")
        self.label_22 = QtWidgets.QLabel(self.fan6_6)
        self.label_22.setGeometry(QtCore.QRect(10, 10, 12, 92))
        self.label_22.setStyleSheet("")
        self.label_22.setTextFormat(QtCore.Qt.AutoText)
        self.label_22.setScaledContents(False)
        self.label_22.setWordWrap(False)
        self.label_22.setOpenExternalLinks(False)
        self.label_22.setObjectName("label_22")
        self.fan6_7 = QtWidgets.QFrame(self.groupBox_5)
        self.fan6_7.setGeometry(QtCore.QRect(370, 20, 16, 112))
        self.fan6_7.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan6_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan6_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan6_7.setObjectName("fan6_7")
        self.label_21 = QtWidgets.QLabel(self.fan6_7)
        self.label_21.setGeometry(QtCore.QRect(10, 10, 12, 92))
        self.label_21.setStyleSheet("")
        self.label_21.setTextFormat(QtCore.Qt.AutoText)
        self.label_21.setScaledContents(False)
        self.label_21.setWordWrap(False)
        self.label_21.setOpenExternalLinks(False)
        self.label_21.setObjectName("label_21")
        self.fan5_3 = QtWidgets.QFrame(self.groupBox_5)
        self.fan5_3.setGeometry(QtCore.QRect(246, 22, 16, 112))
        self.fan5_3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan5_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan5_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan5_3.setObjectName("fan5_3")
        self.label_20 = QtWidgets.QLabel(self.fan5_3)
        self.label_20.setGeometry(QtCore.QRect(10, 10, 12, 92))
        self.label_20.setStyleSheet("")
        self.label_20.setTextFormat(QtCore.Qt.AutoText)
        self.label_20.setScaledContents(False)
        self.label_20.setWordWrap(False)
        self.label_20.setOpenExternalLinks(False)
        self.label_20.setObjectName("label_20")
        self.fan3_3 = QtWidgets.QFrame(self.groupBox_5)
        self.fan3_3.setGeometry(QtCore.QRect(214, 22, 16, 112))
        self.fan3_3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan3_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan3_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan3_3.setObjectName("fan3_3")
        self.label_18 = QtWidgets.QLabel(self.fan3_3)
        self.label_18.setGeometry(QtCore.QRect(10, 10, 12, 92))
        self.label_18.setStyleSheet("")
        self.label_18.setTextFormat(QtCore.Qt.AutoText)
        self.label_18.setScaledContents(False)
        self.label_18.setWordWrap(False)
        self.label_18.setOpenExternalLinks(False)
        self.label_18.setObjectName("label_18")
        self.fan6_2 = QtWidgets.QFrame(self.groupBox_5)
        self.fan6_2.setGeometry(QtCore.QRect(112, 22, 16, 112))
        self.fan6_2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan6_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan6_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan6_2.setObjectName("fan6_2")
        self.label_13 = QtWidgets.QLabel(self.fan6_2)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 12, 92))
        self.label_13.setStyleSheet("")
        self.label_13.setTextFormat(QtCore.Qt.AutoText)
        self.label_13.setScaledContents(False)
        self.label_13.setWordWrap(False)
        self.label_13.setOpenExternalLinks(False)
        self.label_13.setObjectName("label_13")
        self.fan5_2 = QtWidgets.QFrame(self.groupBox_5)
        self.fan5_2.setGeometry(QtCore.QRect(96, 22, 16, 112))
        self.fan5_2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan5_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan5_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan5_2.setObjectName("fan5_2")
        self.label_12 = QtWidgets.QLabel(self.fan5_2)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 12, 92))
        self.label_12.setStyleSheet("")
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setScaledContents(False)
        self.label_12.setWordWrap(False)
        self.label_12.setOpenExternalLinks(False)
        self.label_12.setObjectName("label_12")
        self.fan4_2 = QtWidgets.QFrame(self.groupBox_5)
        self.fan4_2.setGeometry(QtCore.QRect(80, 22, 16, 112))
        self.fan4_2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan4_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan4_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan4_2.setObjectName("fan4_2")
        self.label_11 = QtWidgets.QLabel(self.fan4_2)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 12, 92))
        self.label_11.setStyleSheet("")
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setScaledContents(False)
        self.label_11.setWordWrap(False)
        self.label_11.setOpenExternalLinks(False)
        self.label_11.setObjectName("label_11")
        self.fan3_2 = QtWidgets.QFrame(self.groupBox_5)
        self.fan3_2.setGeometry(QtCore.QRect(64, 22, 16, 112))
        self.fan3_2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan3_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan3_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan3_2.setObjectName("fan3_2")
        self.label_10 = QtWidgets.QLabel(self.fan3_2)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 12, 92))
        self.label_10.setStyleSheet("")
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setScaledContents(False)
        self.label_10.setWordWrap(False)
        self.label_10.setOpenExternalLinks(False)
        self.label_10.setObjectName("label_10")
        self.fan2_2 = QtWidgets.QFrame(self.groupBox_5)
        self.fan2_2.setGeometry(QtCore.QRect(48, 22, 16, 112))
        self.fan2_2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan2_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan2_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan2_2.setObjectName("fan2_2")
        self.label_9 = QtWidgets.QLabel(self.fan2_2)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 12, 92))
        self.label_9.setStyleSheet("")
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setWordWrap(False)
        self.label_9.setOpenExternalLinks(False)
        self.label_9.setObjectName("label_9")
        self.fan1_2 = QtWidgets.QFrame(self.groupBox_5)
        self.fan1_2.setGeometry(QtCore.QRect(10, 22, 32, 112))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fan1_2.sizePolicy().hasHeightForWidth())
        self.fan1_2.setSizePolicy(sizePolicy)
        self.fan1_2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan1_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan1_2.setObjectName("fan1_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.fan1_2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.fan1_2)
        self.label_8.setStyleSheet("")
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setScaledContents(False)
        self.label_8.setWordWrap(False)
        self.label_8.setOpenExternalLinks(False)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(88, 22, 211, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName("gridLayout")
        self.fan1 = QtWidgets.QFrame(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fan1.sizePolicy().hasHeightForWidth())
        self.fan1.setSizePolicy(sizePolicy)
        self.fan1.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan1.setObjectName("fan1")
        self.gridLayout.addWidget(self.fan1, 0, 0, 1, 1)
        self.fan4 = QtWidgets.QFrame(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fan4.sizePolicy().hasHeightForWidth())
        self.fan4.setSizePolicy(sizePolicy)
        self.fan4.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan4.setObjectName("fan4")
        self.gridLayout.addWidget(self.fan4, 1, 0, 1, 1)
        self.fan5 = QtWidgets.QFrame(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fan5.sizePolicy().hasHeightForWidth())
        self.fan5.setSizePolicy(sizePolicy)
        self.fan5.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan5.setObjectName("fan5")
        self.gridLayout.addWidget(self.fan5, 1, 1, 1, 1)
        self.fan2 = QtWidgets.QFrame(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fan2.sizePolicy().hasHeightForWidth())
        self.fan2.setSizePolicy(sizePolicy)
        self.fan2.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan2.setObjectName("fan2")
        self.gridLayout.addWidget(self.fan2, 0, 1, 1, 1)
        self.fan3 = QtWidgets.QFrame(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fan3.sizePolicy().hasHeightForWidth())
        self.fan3.setSizePolicy(sizePolicy)
        self.fan3.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan3.setObjectName("fan3")
        self.gridLayout.addWidget(self.fan3, 0, 3, 1, 1)
        self.fan6 = QtWidgets.QFrame(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fan6.sizePolicy().hasHeightForWidth())
        self.fan6.setSizePolicy(sizePolicy)
        self.fan6.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.fan6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fan6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fan6.setObjectName("fan6")
        self.gridLayout.addWidget(self.fan6, 1, 3, 1, 1)
        self.horizontalLayout_13.addWidget(self.groupBox_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.graphicsView = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_5.addWidget(self.graphicsView)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "串口信息"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">test</p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "test"))
        self.label.setText(_translate("MainWindow", "串口："))
        self.openUARTPortButton.setText(_translate("MainWindow", "打开串口"))
        self.groupBox_2.setTitle(_translate("MainWindow", "状态显示"))
        self.label_3.setText(_translate("MainWindow", "风扇状态"))
        self.label_2.setText(_translate("MainWindow", "系统状态"))
        self.label_4.setText(_translate("MainWindow", "液泵状态"))
        self.groupBox_4.setTitle(_translate("MainWindow", "温度监控"))
        self.label_5.setText(_translate("MainWindow", "入口温度："))
        self.label_6.setText(_translate("MainWindow", "出口温度："))
        self.label_7.setText(_translate("MainWindow", "热端温度："))
        self.groupBox_5.setTitle(_translate("MainWindow", "PSW状态"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>系</p><p>统</p><p>状</p><p>态</p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "风扇状态"))
from pyqtgraph import PlotWidget
