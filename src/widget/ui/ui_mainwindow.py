# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1028, 503)
        self.actionOpenFile = QAction(MainWindow)
        self.actionOpenFile.setObjectName(u"actionOpenFile")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"\u6a19\u6977\u9ad4"])
        font.setPointSize(14)
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_text_filename = QLabel(self.centralwidget)
        self.label_text_filename.setObjectName(u"label_text_filename")
        self.label_text_filename.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_text_filename)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox = QGroupBox(self.groupBox_4)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.text_name = QLabel(self.groupBox)
        self.text_name.setObjectName(u"text_name")
        self.text_name.setMinimumSize(QSize(40, 0))
        font1 = QFont()
        font1.setPointSize(12)
        self.text_name.setFont(font1)
        self.text_name.setLayoutDirection(Qt.LeftToRight)
        self.text_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.text_name, 0, 0, 1, 1)

        self.text_phone = QLabel(self.groupBox)
        self.text_phone.setObjectName(u"text_phone")
        self.text_phone.setFont(font1)
        self.text_phone.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.text_phone, 1, 0, 1, 1)

        self.label_image_name = QLabel(self.groupBox)
        self.label_image_name.setObjectName(u"label_image_name")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image_name.sizePolicy().hasHeightForWidth())
        self.label_image_name.setSizePolicy(sizePolicy)
        self.label_image_name.setMinimumSize(QSize(350, 60))

        self.gridLayout.addWidget(self.label_image_name, 0, 1, 1, 1)

        self.label_image_home = QLabel(self.groupBox)
        self.label_image_home.setObjectName(u"label_image_home")
        sizePolicy.setHeightForWidth(self.label_image_home.sizePolicy().hasHeightForWidth())
        self.label_image_home.setSizePolicy(sizePolicy)
        self.label_image_home.setMinimumSize(QSize(200, 60))
        self.label_image_home.setSizeIncrement(QSize(0, 0))

        self.gridLayout.addWidget(self.label_image_home, 2, 1, 1, 1)

        self.lineEdit_text_phone = QLineEdit(self.groupBox)
        self.lineEdit_text_phone.setObjectName(u"lineEdit_text_phone")
        self.lineEdit_text_phone.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamilies([u"\u6a19\u6977\u9ad4"])
        font2.setPointSize(12)
        self.lineEdit_text_phone.setFont(font2)

        self.gridLayout.addWidget(self.lineEdit_text_phone, 1, 2, 1, 1)

        self.lineEdit_text_home = QLineEdit(self.groupBox)
        self.lineEdit_text_home.setObjectName(u"lineEdit_text_home")
        self.lineEdit_text_home.setMinimumSize(QSize(0, 40))
        self.lineEdit_text_home.setFont(font2)

        self.gridLayout.addWidget(self.lineEdit_text_home, 2, 2, 1, 1)

        self.label_image_phone = QLabel(self.groupBox)
        self.label_image_phone.setObjectName(u"label_image_phone")
        sizePolicy.setHeightForWidth(self.label_image_phone.sizePolicy().hasHeightForWidth())
        self.label_image_phone.setSizePolicy(sizePolicy)
        self.label_image_phone.setMinimumSize(QSize(200, 60))

        self.gridLayout.addWidget(self.label_image_phone, 1, 1, 1, 1)

        self.text_home = QLabel(self.groupBox)
        self.text_home.setObjectName(u"text_home")
        self.text_home.setFont(font1)
        self.text_home.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.text_home, 2, 0, 1, 1)

        self.lineEdit_text_name = QLineEdit(self.groupBox)
        self.lineEdit_text_name.setObjectName(u"lineEdit_text_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_text_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_text_name.setSizePolicy(sizePolicy1)
        self.lineEdit_text_name.setMinimumSize(QSize(300, 40))
        self.lineEdit_text_name.setFont(font2)

        self.gridLayout.addWidget(self.lineEdit_text_name, 0, 2, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"\u6a19\u6977\u9ad4"])
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit_foldername = QLineEdit(self.groupBox_3)
        self.lineEdit_foldername.setObjectName(u"lineEdit_foldername")

        self.gridLayout_7.addWidget(self.lineEdit_foldername, 1, 1, 1, 1)

        self.checkBox_auto_write2excel = QCheckBox(self.groupBox_3)
        self.checkBox_auto_write2excel.setObjectName(u"checkBox_auto_write2excel")

        self.gridLayout_7.addWidget(self.checkBox_auto_write2excel, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_7, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_yes = QPushButton(self.groupBox_2)
        self.pushButton_yes.setObjectName(u"pushButton_yes")

        self.gridLayout_2.addWidget(self.pushButton_yes, 0, 0, 1, 1)

        self.pushButton_no = QPushButton(self.groupBox_2)
        self.pushButton_no.setObjectName(u"pushButton_no")

        self.gridLayout_2.addWidget(self.pushButton_no, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.pushButton_start = QPushButton(self.groupBox_2)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.gridLayout_4.addWidget(self.pushButton_start, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1028, 25))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionOpenFile)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6e2c\u8a66\u5de5\u5177", None))
        self.actionOpenFile.setText(QCoreApplication.translate("MainWindow", u"OpenFile", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6a94\u6848\u540d\u7a31\uff1a", None))
        self.label_text_filename.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.groupBox_4.setTitle("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8cc7\u6599\u8b58\u5225", None))
        self.text_name.setText(QCoreApplication.translate("MainWindow", u"\u540d\u5b57", None))
        self.text_phone.setText(QCoreApplication.translate("MainWindow", u"\u96fb\u8a71", None))
        self.label_image_name.setText("")
        self.label_image_home.setText("")
        self.label_image_phone.setText("")
        self.text_home.setText(QCoreApplication.translate("MainWindow", u"\u4f4f\u5740", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u624b\u52d5\u8cc7\u6599", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8cc7\u6599\u593e\u540d\u7a31\uff1a", None))
        self.checkBox_auto_write2excel.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u78ba\u6642\u81ea\u52d5\u8f38\u5165", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6309\u9215", None))
        self.pushButton_yes.setText(QCoreApplication.translate("MainWindow", u"\u8cc7\u6599\u6b63\u78ba", None))
        self.pushButton_no.setText(QCoreApplication.translate("MainWindow", u"\u8cc7\u6599\u932f\u8aa4", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u958b\u59cb\u8b58\u5225", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6a94\u6848", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

