# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 08:34:32 2023

@author: psar
"""
# Form implementation generated from reading ui file 'GSdetinit_.ui'


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QProcess
import glob

btn_stylesheet = ("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")

btn_in_out_font = QtGui.QFont("Calibri", 12, 50, False)
title_font = QtGui.QFont("Caladea", 14, 75, False)
btn_exit_stylesheet = ("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color: rgb(235, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(235, 0, 0, 150);\n"
"}")

btn_min_stylesheet = btn_exit_stylesheet.replace("(235, 0, 0", "(240, 135, 0")

results_btn_stylesheet = ("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 10), stop:1 rgba(255, 255, 255, 10));\n"
"}\n"
"\n"
"")

spinbox_stylesheet = ("QSpinBox"
                    "{"
                    "background-color : white;"
                    "}")
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 843)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_title_back= QtWidgets.QFrame(self.centralwidget)
        self.frame_title_back.setGeometry(QtCore.QRect(0, 0, 801, 31))
        self.frame_title_back.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(221, 231, 199, 255), stop:1 rgba(238, 248, 214, 255)); border-radius: 10px;")
        self.frame_title = QtWidgets.QFrame(self.centralwidget)
        self.frame_title.setGeometry(QtCore.QRect(0, 0, 801, 31))
        self.frame_title.setStyleSheet("background-color: rgba(1, 32, 15, 100)")
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.btn_min = QtWidgets.QPushButton(self.frame_title)
        self.btn_min.setGeometry(QtCore.QRect(740, 5, 20, 20))
        self.btn_min.setFont(QtGui.QFont("Calibri", 10, 75, True))
        self.btn_min.setStyleSheet(btn_min_stylesheet)
        self.btn_min.setObjectName("btn_min")
        self.btn_min.clicked.connect(self.minimize)        
        self.btn_exit = QtWidgets.QPushButton(self.frame_title)
        self.btn_exit.setGeometry(QtCore.QRect(770, 5, 20, 20))
        self.btn_exit.setFont(QtGui.QFont("Corbel", 10, 75, True))
        self.btn_exit.setStyleSheet(btn_exit_stylesheet)
        self.btn_exit.setObjectName("btn_exit")
        self.btn_exit.clicked.connect(self.on_closing)        
        self.title = QtWidgets.QLabel(self.frame_title)
        self.title.setGeometry(QtCore.QRect(11, -3, 381, 41))
        self.title.setFont(title_font)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.title.setObjectName("title")
        self.outer_frame = QtWidgets.QFrame(self.centralwidget)
        self.outer_frame.setGeometry(QtCore.QRect(0, 30, 801, 701))
        self.outer_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(221, 231, 199, 255), stop:1 rgba(238, 248, 214, 255)); border-radius: 10px;")
        self.outer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outer_frame.setObjectName("outer_frame")
        self.stackedWidget = QtWidgets.QStackedWidget(self.outer_frame)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 801, 701))
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setObjectName("stackedWidget")
        #%%Home page
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.home_frame = QtWidgets.QFrame(self.home_page)
        self.home_frame.setGeometry(QtCore.QRect(30, 60, 741, 611))
        self.home_frame.setStyleSheet("background-color: rgb(227, 227, 227);border-radius:10px;")
        self.home_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_frame.setObjectName("home_frame")
        self.files_processed_label = QtWidgets.QLabel(self.home_frame)
        self.files_processed_label.setGeometry(QtCore.QRect(20, 120, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.files_processed_label.setFont(font)
        self.files_processed_label.setObjectName("files_processed_label")
        self.include_sub = QtWidgets.QCheckBox(self.home_frame)
        self.include_sub.setGeometry(QtCore.QRect(630, 45, 91, 32))
        self.include_sub.setObjectName("include_sub")
        self.include_sub.setEnabled(False)
        self.btn_dir_in = QtWidgets.QPushButton(self.home_frame)
        self.btn_dir_in.setGeometry(QtCore.QRect(10, 20, 151, 81))
        self.btn_dir_in.setFont(btn_in_out_font)
        self.btn_dir_in.setStyleSheet(btn_stylesheet)
        self.btn_dir_in.setObjectName("btn_dir_in")
        self.wavs_to_scan = QtWidgets.QTextBrowser(self.home_frame)
        self.wavs_to_scan.setGeometry(QtCore.QRect(180, 120, 541, 121))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wavs_to_scan.setFont(font)        
        self.wavs_to_scan.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.wavs_to_scan.setObjectName("wavs_to_scan")
        self.pathIN = QtWidgets.QTextBrowser(self.home_frame)
        self.pathIN.setGeometry(QtCore.QRect(180, 30, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pathIN.setFont(font)
        self.pathIN.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pathIN.setObjectName("pathIN")
        self.dir_in_label = QtWidgets.QLabel(self.home_frame)
        self.dir_in_label.setGeometry(QtCore.QRect(180, 10, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.dir_in_label.setFont(font)
        self.dir_in_label.setObjectName("dir_in_label")
        self.btn_dir_out = QtWidgets.QPushButton(self.home_frame)
        self.btn_dir_out.setGeometry(QtCore.QRect(10, 260, 151, 81))
        self.btn_dir_out.setFont(btn_in_out_font)
        self.btn_dir_out.setStyleSheet(btn_stylesheet)
        self.btn_dir_out.setObjectName("btn_dir_out")
        self.pathOUT = QtWidgets.QTextBrowser(self.home_frame)
        self.pathOUT.setGeometry(QtCore.QRect(180, 270, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pathOUT.setFont(font)
        self.pathOUT.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pathOUT.setObjectName("pathOUT")
        self.adv_settings_label = QtWidgets.QLabel(self.home_frame)
        self.adv_settings_label.setGeometry(QtCore.QRect(20, 460, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.adv_settings_label.setFont(font)

        self.adv_settings_label.setObjectName("adv_settings_label")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.home_frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(180, 450, 431, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.adv_settings_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.adv_settings_layout.setContentsMargins(0, 0, 0, 0)
        self.adv_settings_layout.setObjectName("adv_settings_layout")
        self.cpus_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.cpus_label.setObjectName("cpus_label")
        self.adv_settings_layout.addWidget(self.cpus_label)
        self.cpus_spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.cpus_spinBox.setObjectName("cpus_spinBox")
        self.cpus_spinBox.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        self.cpus_spinBox.setStyleSheet(spinbox_stylesheet)
        self.cpus_spinBox.setAlignment(Qt.AlignCenter)
        self.adv_settings_layout.addWidget(self.cpus_spinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.adv_settings_layout.addItem(spacerItem)
        self.prob_th_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.prob_th_label.setObjectName("prob_th_label")
        self.adv_settings_layout.addWidget(self.prob_th_label)
        self.prob_th_spinBox = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_3)
        self.prob_th_spinBox.setObjectName("prob_th_spinBox")
        self.prob_th_spinBox.setSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        self.prob_th_spinBox.setStyleSheet(spinbox_stylesheet.replace("QSpinBox", "QDoubleSpinBox"))
        self.prob_th_spinBox.setAlignment(Qt.AlignCenter)

        self.adv_settings_layout.addWidget(self.prob_th_spinBox)
        self.btn_run = QtWidgets.QPushButton(self.home_frame)
        self.btn_run.setGeometry(QtCore.QRect(270, 530, 221, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_run.setFont(font)
        self.btn_run.setStyleSheet(f"{btn_stylesheet}"
"\n\n"
"QPushButton:disabled{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 10), stop:1 rgba(255, 255, 255, 10));\n"
"}\n"
"\n")
        self.btn_run.setObjectName("btn_run")
        self.btn_run.clicked.connect(self.run_main)  
              
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.home_frame)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(180, 370, 391, 61))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.settings_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.settings_layout.setContentsMargins(0, 0, 0, 0)
        self.settings_layout.setObjectName("settings_layout")
        self.extract_wavs_check = QtWidgets.QCheckBox(self.horizontalLayoutWidget_4)
        self.extract_wavs_check.setObjectName("extract_wavs_check")
        self.settings_layout.addWidget(self.extract_wavs_check)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.settings_layout.addItem(spacerItem1)
        self.sep_results_check = QtWidgets.QCheckBox(self.horizontalLayoutWidget_4)
        self.sep_results_check.setObjectName("sep_results_check")
        # self.sep_results_check.setEnabled(False)
        self.settings_layout.addWidget(self.sep_results_check)
        self.settings_label = QtWidgets.QLabel(self.home_frame)
        self.settings_label.setGeometry(QtCore.QRect(20, 380, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.settings_label.setFont(font)
        self.settings_label.setObjectName("settings_label")
        self.home_page_title = QtWidgets.QLabel(self.home_page)
        self.home_page_title.setGeometry(QtCore.QRect(30, 20, 161, 41))
        self.home_page_title.setFont(title_font)
        self.home_page_title.setAutoFillBackground(False)
        self.home_page_title.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.home_page_title.setObjectName("home_page_title")
        self.stackedWidget.addWidget(self.home_page)

        #%% Run page
        self.run_page = QtWidgets.QWidget()
        self.run_page.setObjectName("run_page")
        self.run_page_title = QtWidgets.QLabel(self.run_page)
        self.run_page_title.setGeometry(QtCore.QRect(30, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Caladea")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.run_page_title.setFont(font)
        self.run_page_title.setAutoFillBackground(False)
        self.run_page_title.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.run_page_title.setObjectName("run_page_title")
        self.run_frame = QtWidgets.QFrame(self.run_page)
        self.run_frame.setGeometry(QtCore.QRect(30, 60, 741, 611))
        self.run_frame.setStyleSheet("background-color: rgb(227, 227, 227);border-radius:10px;")
        self.run_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.run_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.run_frame.setObjectName("run_frame")
        self.run_console_log_text = QtWidgets.QTextEdit(self.run_frame)
        self.run_console_log_text.setGeometry(QtCore.QRect(20, 140, 701, 401))
        self.run_console_log_text.setObjectName("run_console_log_text")
        self.run_console_log_text.setReadOnly(True) 
        font = QtGui.QFont()
        font.setPointSize(9)
        self.run_console_log_text.setFont(font)
        self.run_console_log_text.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.run_files_processed_label = QtWidgets.QLabel(self.run_frame)
        self.run_files_processed_label.setGeometry(QtCore.QRect(20, 10, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Courier")
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.run_files_processed_label.setFont(font)
        self.run_files_processed_label.setStyleSheet("")
        self.run_files_processed_label.setObjectName("run_files_processed_label")
        self.run_progressBar = QtWidgets.QProgressBar(self.run_frame)
        self.run_progressBar.setGeometry(QtCore.QRect(20, 40, 601, 51))
        self.run_progressBar.setProperty("value", 24)
        self.run_progressBar.setObjectName("run_progressBar")
        self.run_progressBar.hide()
        self.run_console_log_label = QtWidgets.QLabel(self.run_frame)
        self.run_console_log_label.setGeometry(QtCore.QRect(30, 110, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.run_console_log_label.setFont(font)
        self.run_console_log_label.setStyleSheet("")
        self.run_console_log_label.setObjectName("run_console_log_label")
        self.run_btn_cancel = QtWidgets.QPushButton(self.run_frame)
        self.run_btn_cancel.setGeometry(QtCore.QRect(640, 40, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.run_btn_cancel.setFont(font)
        self.run_btn_cancel.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 0, 0, 10), stop:1 rgba(255, 0, 0, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 0, 0, 255), stop:1 rgba(150, 0, 0, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 0, 0, 10), stop:1 rgba(200, 0, 0, 10));\n"
"}\n"
"\n"
"")
        self.run_btn_cancel.setObjectName("run_btn_cancel")
        self.run_btn_cancel.clicked.connect(self.cancel)
        self.stackedWidget.addWidget(self.run_page)


        self.results_page = QtWidgets.QWidget()
        self.results_page.setObjectName("results_page")
        self.results_page_title = QtWidgets.QLabel(self.results_page)
        self.results_page_title.setGeometry(QtCore.QRect(30, 20, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Caladea")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.results_page_title.setFont(font)
        self.results_page_title.setAutoFillBackground(False)
        self.results_page_title.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.results_page_title.setObjectName("results_page_title")
        self.results_frame = QtWidgets.QFrame(self.results_page)
        self.results_frame.setGeometry(QtCore.QRect(30, 60, 741, 611))
        self.results_frame.setStyleSheet("background-color: rgb(227, 227, 227);border-radius:10px;")
        self.results_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.results_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.results_frame.setObjectName("results_frame")
        self.results_box = QtWidgets.QPlainTextEdit(self.results_frame)
        self.results_box.setGeometry(QtCore.QRect(20, 140, 701, 401))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.results_box.setFont(font)
        self.results_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.results_box.setReadOnly(True)
        self.results_box.setObjectName("results_box")
        self.files_processed_label_3 = QtWidgets.QLabel(self.results_frame)
        self.files_processed_label_3.setGeometry(QtCore.QRect(20, 10, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.files_processed_label_3.setFont(font)
        self.files_processed_label_3.setStyleSheet("")
        self.files_processed_label_3.setObjectName("files_processed_label_3")
        self.pathIN_2 = QtWidgets.QTextBrowser(self.results_frame)
        self.pathIN_2.setGeometry(QtCore.QRect(250, 10, 471, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pathIN_2.setFont(font)
        self.pathIN_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pathIN_2.setObjectName("pathIN_2")
        self.btn_save_xlsx = QtWidgets.QPushButton(self.results_frame)
        self.btn_save_xlsx.setGeometry(QtCore.QRect(440, 560, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_save_xlsx.setFont(font)
        self.btn_save_xlsx.setStyleSheet(results_btn_stylesheet)
        self.btn_save_xlsx.setObjectName("btn_save_xlsx")
        self.btn_save_txt = QtWidgets.QPushButton(self.results_frame)
        self.btn_save_txt.setGeometry(QtCore.QRect(130, 560, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_save_txt.setFont(font)
        self.btn_save_txt.setStyleSheet(results_btn_stylesheet)
        self.btn_save_txt.setObjectName("btn_save_txt")
        self.stackedWidget.addWidget(self.results_page)
        #%%
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(self.onFinished)

        # self.process.stateChanged.connect(self.process_state_changed)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_min.setText(_translate("MainWindow", "_"))
        self.btn_exit.setText(_translate("MainWindow", "X"))
        self.title.setText(_translate("MainWindow", "Gunshot Detector (v 0.1)"))
        self.files_processed_label.setText(_translate("MainWindow", "Files to be processed:"))
        self.include_sub.setText(_translate("MainWindow", "Include\nSubfolders"))
        self.btn_dir_in.setText(_translate("MainWindow", "Select\nInput\nDirectory"))
        self.dir_in_label.setText(_translate("MainWindow", "Directory with wav files:"))
        self.pathIN.setText(_translate("MainWindow", "[Please select a directory]"))
        self.wavs_to_scan.setText(_translate("MainWindow", "[No directory selected]"))

        self.btn_dir_out.setText(_translate("MainWindow", "Select\nOutput\nDirectory"))
        self.pathOUT.setText('[Please select a directory]')
        self.adv_settings_label.setText(_translate("MainWindow", "Advanced settings:"))
        self.cpus_label.setText(_translate("MainWindow", "Cores to use:\n(parallelization)"))
        self.prob_th_label.setText(_translate("MainWindow", "Probability\nthreshold:"))
        self.btn_run.setText(_translate("MainWindow", "Run"))
        self.run_btn_cancel.setText(_translate("MainWindow", "Cancel"))
        self.extract_wavs_check.setText(_translate("MainWindow", "Extract detected\nsegments"))
        self.sep_results_check.setText(_translate("MainWindow", "Separate raven .txt file\nfor each .wav"))
        self.settings_label.setText(_translate("MainWindow", "Settings:"))
        self.home_page_title.setText(_translate("MainWindow", "Initialization"))
        self.run_page_title.setText(_translate("MainWindow", "Run Page"))
        self.run_console_log_label.setText(_translate("MainWindow", "Log:"))
        self.files_processed_label_3.setText(_translate("MainWindow", "Directory with wav files processed:"))

        max_cpus = self.count_processors()
        self.btn_min.clicked.connect(self.minimize)       
        self.btn_exit.clicked.connect(self.on_closing)  
        self.btn_dir_in.clicked.connect(lambda func: self.select_dir(self.pathIN, self.btn_dir_in))                
        self.btn_dir_out.clicked.connect(lambda func: self.select_dir(self.pathOUT, self.btn_dir_out))                
        self.include_sub.stateChanged.connect(self.update_files)
        self.prob_th_spinBox.setMinimum(0.01)
        self.prob_th_spinBox.setMaximum(0.99)
        self.prob_th_spinBox.setValue(0.5)
        self.prob_th_spinBox.setSingleStep(0.01)
        self.cpus_spinBox.setMinimum(1)
        self.cpus_spinBox.setMaximum(max_cpus)
        self.cpus_spinBox.setValue(int(max_cpus*0.75))

        self.pathIN_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">[Please select a directory]</span></p></body></html>"))
        self.btn_save_xlsx.setText(_translate("MainWindow", "Save as .xlsx"))
        self.btn_save_txt.setText(_translate("MainWindow", "Save as .txt"))

        self.include_sub.hide()
        self.files=[]
        self.run_btn_enable()

    def count_processors(self):
        import multiprocessing
        import numpy as np
        nop=multiprocessing.cpu_count()
        # print(str(int(nop)) + ' cpus found')
        return nop  

    def run_btn_enable(self):
        cond1 = len(self.files)>0
        cond2 = self.pathOUT.toPlainText()!="[Please select a directory]"
        cond3 = self.pathIN.toPlainText()!="[Please select a directory]"
        if cond1 and cond2 and cond3:
            self.btn_run.setEnabled(True)
            self.btn_run.setText("Run")
        else:
            if not cond3:
                self.btn_run.setText("Run\n(Select an input dir)")
                self.btn_run.setEnabled(False)
            if not cond1:
                self.btn_run.setText("Run\n(Select a valid input dir)")
                self.btn_run.setEnabled(False)
            elif not cond2:
                self.btn_run.setText("Run\n(Select a valid output dir)")
                self.btn_run.setEnabled(False)


    def select_dir(self, text_widget, btn_widget):
        import glob
        folder = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        print(folder)
        if folder:
            text_widget.setText(folder)
        if text_widget==self.pathIN:
            self.include_sub.setEnabled(True)
            self.update_files()
            btn_widget.setText("Change\nInput\nDirectory")
        else:
            if text_widget.toPlainText()!="[Please select a directory]":
                btn_widget.setText("Change\nOutput\nDirectory")
            self.run_btn_enable()
                # self.btn_run.setEnabled(True)
                # self.btn_run.setText("Run")

    def update_files(self):
        timestamp_pattern = "[0-9][0-9]h[0-9][0-9]m[0-9][0-9]s"
        folder = self.pathIN.toPlainText()
        if not folder: return
        if self.include_sub.isChecked():
            files = glob.glob(f"{folder}/**/*.wav", recursive=True)
        else:
            files = glob.glob(f"{folder}/*.wav", recursive=False)

        if len(files)>0:
            files = "\n".join(files).replace("\\", "/").replace(folder, "./")
            self.files = files
            self.run_btn_enable()
            # self.btn_run.setEnabled(True)
            # self.btn_run.setText("Run")
        else:
            files = "No .wav files found in selected directory."
            # self.btn_run.setText("Run\n(Select a valid input dir)")
            # self.btn_run.setEnabled(False)
            self.files = []
            self.run_btn_enable()
        self.wavs_to_scan.setText(files)


    def minimize(self):
        self.showMinimized()


    def on_closing(self):
        import gc

        reply = QtWidgets.QMessageBox.question(self, 'Quit',
            "Are you sure to quit?", QtWidgets.QMessageBox.Yes | 
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            print('Thank you for using our tool!')
            QtCore.QCoreApplication.instance().quit()
            gc.collect()
            exit()
      


    def run_main(self):            
        self.stackedWidget.setCurrentIndex(1)
        print(f'Running batch processor with pathIN={self.pathIN.toPlainText()}, pathOUT={self.pathOUT.toPlainText()}, nopREQ={self.cpus_spinBox.value()}, probThresh={self.prob_th_spinBox.value()}, extract_wavs={self.extract_wavs_check.isChecked()}')
        msg = (f'Processing starting...\n-Arguments to use:\n'
               f'\tInput path = {self.pathIN.toPlainText()}\n'
               f'\tOutput path = {self.pathOUT.toPlainText()}\n'
               f'\tCPUs used = {self.cpus_spinBox.value()}\n'
               f'\tProbability Threshold = {self.prob_th_spinBox.value()}\n'
               f'\tExtract segments as wavs = {self.extract_wavs_check.isChecked()}\n'
               f'\tExport separated results for each input file = {self.sep_results_check.isChecked()}')
        self.run_console_log_text.append(msg)

        command = ['batch_processor.py', 
                    str(self.pathIN.toPlainText()),
                    '-o', str(self.pathOUT.toPlainText()),
                    '-p', str(self.cpus_spinBox.value()),
                    '-t', str(self.prob_th_spinBox.value())]
        if self.extract_wavs_check.isChecked():
            command.append('-ext_audio')
        if self.sep_results_check.isChecked():
            command.append('-sep_results')
        
        self.process.start('python', command)

    def load_results(self):
        import pandas as pd
        fname_xlsx_tmp = f"{self.pathOUT.toPlainText()}/results_raven_tmp.xlsx"
        try:
            df = pd.read_excel(fname_xlsx_tmp)
        except:
            df = pd.DataFrame()
        return df


    def initialize_files(self):
        import glob, os, pandas as pd, numpy as np
        pathIN = self.pathIN.toPlainText()
        self.pathIN_2.setText(pathIN)
        cwd = os.getcwd().replace("\\", "/")
        self.df = self.load_results()
        if len(glob.glob(f"{self.pathOUT.toPlainText()}/results_raven_tmp.xlsx"))<1:
            self.results_box.setPlainText("No instances found.")
            self.results_box.show()
            self.results_box.setReadOnly(True)
            self.btn_save_xlsx.hide()
            self.btn_save_txt.hide()
        else:
            self.results_box.setPlainText(self.df.to_markdown(index=False))#, tablefmt="grid"))
            model = pandasModel(self.df)
            self.view = QtWidgets.QTableView(parent = self.results_frame)
            self.view.setGeometry(QtCore.QRect(20, 130, 701, 301))
            self.view.setModel(model)
            self.results_box.hide()
            self.view.show()
            self.results_page_title.setText(f"Detections ({self.df.shape[0]})")
            self.results_page_title.adjustSize()
            self.btn_save_xlsx.hide()
            self.btn_save_txt.hide()
    
   

    def onFinished(self,  exitCode,  exitStatus):
        import time
        if exitCode==0:
            self.run_console_log_text.append("Process finished succesfully.")
            time.sleep(1)
            df = self.load_results()
            self.initialize_files()
            # print(df)
            self.stackedWidget.setCurrentIndex(2)
        else:
            self.run_console_log_text.append("An error occured, or user has cancelled the procedure. Process exited with exit code {exitCode}.")
            
    def handle_stdout(self):
        data = self.process.readAllStandardOutput().data().decode(encoding="latin-1")
        self.run_console_log_text.append(data)

    def handle_stderr(self):
        error = self.process.readAllStandardError().data().decode(encoding="latin-1")
        self.run_console_log_text.append(error)

    def cancel(self):
        import gc
        reply = QtWidgets.QMessageBox.question(self, 'Cancel',
            "Are you sure to cancel the procedure?", QtWidgets.QMessageBox.Yes | 
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:        
            self.process.kill()
            self.run_console_log_text.append("Procedure cancelled by user.\n")
            print("Procedure cancelled by user.")

            reply = QtWidgets.QMessageBox.question(self, 'Cancel',
                "Do you wish to return to initial page for another run?", QtWidgets.QMessageBox.Yes | 
                QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                self.run_console_log_text.clear()
                self.stackedWidget.setCurrentIndex(0)
            else:
                print('Thank you for using our tool!')
                QtCore.QCoreApplication.instance().quit()
                gc.collect()
                exit()
       

class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    #Stack over flow - draggable window
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        try:
            self.setWindowIcon(QtGui.QIcon('./lib/resources/forth_disk.png'))
        except:
            pass
    def mousePressEvent(self, event):                                 # +
        self.dragPos = event.globalPos()
        
    def mouseMoveEvent(self, event):                                  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()     


from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec())

