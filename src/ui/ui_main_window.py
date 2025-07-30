# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowCSyBQT.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 490)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(15)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(20, 20, 20, 20)
        self.inputGroup = QGroupBox(self.centralwidget)
        self.inputGroup.setObjectName(u"inputGroup")
        self.inputLayout = QHBoxLayout(self.inputGroup)
        self.inputLayout.setSpacing(20)
        self.inputLayout.setObjectName(u"inputLayout")
        self.fileSection = QVBoxLayout()
        self.fileSection.setSpacing(12)
        self.fileSection.setObjectName(u"fileSection")
        self.TV2Path = QLineEdit(self.inputGroup)
        self.TV2Path.setObjectName(u"TV2Path")
        self.TV2Path.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.TV2Path.setReadOnly(True)

        self.fileSection.addWidget(self.TV2Path)

        self.BleR5Path = QLineEdit(self.inputGroup)
        self.BleR5Path.setObjectName(u"BleR5Path")
        self.BleR5Path.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.BleR5Path.setReadOnly(True)

        self.fileSection.addWidget(self.BleR5Path)

        self.carVariantCombo = QComboBox(self.inputGroup)
        self.carVariantCombo.setObjectName(u"carVariantCombo")

        self.fileSection.addWidget(self.carVariantCombo)


        self.inputLayout.addLayout(self.fileSection)

        self.processButton = QPushButton(self.inputGroup)
        self.processButton.setObjectName(u"processButton")
        self.processButton.setMinimumSize(QSize(120, 120))
        self.processButton.setMaximumSize(QSize(120, 120))

        self.inputLayout.addWidget(self.processButton)


        self.mainLayout.addWidget(self.inputGroup)

        self.logGroup = QGroupBox(self.centralwidget)
        self.logGroup.setObjectName(u"logGroup")
        self.logLayout = QVBoxLayout(self.logGroup)
        self.logLayout.setSpacing(12)
        self.logLayout.setObjectName(u"logLayout")
        self.progressLayout = QHBoxLayout()
        self.progressLayout.setObjectName(u"progressLayout")
        self.progressBar = QProgressBar(self.logGroup)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setTextVisible(True)

        self.progressLayout.addWidget(self.progressBar)

        self.openOutputFolder = QPushButton(self.logGroup)
        self.openOutputFolder.setObjectName(u"openOutputFolder")

        self.progressLayout.addWidget(self.openOutputFolder)


        self.logLayout.addLayout(self.progressLayout)

        self.logText = QTextEdit(self.logGroup)
        self.logText.setObjectName(u"logText")
        self.logText.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
        self.logText.setReadOnly(True)

        self.logLayout.addWidget(self.logText)

        self.outputPathLayout = QHBoxLayout()
        self.outputPathLayout.setObjectName(u"outputPathLayout")
        self.outputPathLabel = QLabel(self.logGroup)
        self.outputPathLabel.setObjectName(u"outputPathLabel")

        self.outputPathLayout.addWidget(self.outputPathLabel)

        self.outputPath = QLineEdit(self.logGroup)
        self.outputPath.setObjectName(u"outputPath")
        self.outputPath.setReadOnly(True)

        self.outputPathLayout.addWidget(self.outputPath)


        self.logLayout.addLayout(self.outputPathLayout)


        self.mainLayout.addWidget(self.logGroup)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FlashMate - Firmware Extraction Tool", None))
        MainWindow.setStyleSheet(QCoreApplication.translate("MainWindow", u"QMainWindow {\n"
"    background-color: #f8fafc;\n"
"}\n"
"QGroupBox {\n"
"    border: 1px solid #e2e8f0;\n"
"    border-radius: 8px;\n"
"    margin-top: 6px;\n"
"    padding-top: 6px;\n"
"    font-weight: 600;\n"
"    color: #334155;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 8px;\n"
"    padding: 0 6px 0 6px;\n"
"    background-color: #f8fafc;\n"
"}\n"
"QPushButton {\n"
"    background-color: #3b82f6;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 8px 16px;\n"
"    font-weight: 500;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2563eb;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1d4ed8;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #cbd5e1;\n"
"    color: #64748b;\n"
"}\n"
"QLineEdit {\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    background-color: white;\n"
"}\n"
"QLineEdit:focus {\n"
"    border-color: #3b82f6;\n"
"}\n"
"QComboBox {\n"
"    borde"
                        "r: 1px solid #cbd5e1;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    background-color: white;\n"
"}\n"
"QComboBox:focus {\n"
"    border-color: #3b82f6;\n"
"}\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 5px solid #64748b;\n"
"}\n"
"QTextEdit {\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"}\n"
"QProgressBar {\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 6px;\n"
"    text-align: center;\n"
"    background-color: #f1f5f9;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #3b82f6;\n"
"    border-radius: 4px;\n"
"}\n"
"QTableWidget {\n"
"    border: 1px solid #cbd5e1;\n"
"    border-radius: 6px;\n"
"    background-color: white;\n"
"    gridline-color: #f1f5f9;\n"
"}\n"
"QTableWidget::item {\n"
"    padding: 8px;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    back"
                        "ground-color: #dbeafe;\n"
"    color: #334155;\n"
"}\n"
"QLabel {\n"
"    color: #475569;\n"
"}", None))
        self.inputGroup.setTitle(QCoreApplication.translate("MainWindow", u"Input", None))
        self.TV2Path.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #f8fafc; border: 2px dashed #cbd5e1;", None))
        self.TV2Path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Click to add TV2 Zip file here...", None))
        self.BleR5Path.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #f8fafc; border: 2px dashed #cbd5e1;", None))
        self.BleR5Path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Click to add BLE/R5 Zip file here...", None))
        self.carVariantCombo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Car Variant", None))
        self.processButton.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-size: 16px; font-weight: bold; background-color: #3b82f6; text-align: center; padding: 15px; line-height: 1.3; letter-spacing: 1px;", None))
        self.processButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.logGroup.setTitle(QCoreApplication.translate("MainWindow", u"Progress & Log", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.openOutputFolder.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #3b82f6;", None))
        self.openOutputFolder.setText(QCoreApplication.translate("MainWindow", u"Open Output", None))
        self.logText.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-family: Consolas, Monaco, monospace; font-size: 11px; background-color: #f8f9fa;", None))
        self.outputPathLabel.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-weight: bold;", None))
        self.outputPathLabel.setText(QCoreApplication.translate("MainWindow", u"Output Path:", None))
        self.outputPath.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: #fafafa; font-family: monospace;", None))
    # retranslateUi

