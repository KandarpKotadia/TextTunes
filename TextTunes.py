# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextTunes.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 836)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(40, 30, 991, 721))
        self.stackedWidget.setStyleSheet("#page{\n"
"    background-image: url(:/images/resources/background-texttunes.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
# "    background-size: cover;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setAutoFillBackground(False)
        self.page.setStyleSheet("background-color: rgb(111, 158, 209);")
        self.page.setObjectName("page")
        self.fileinput = QtWidgets.QLineEdit(self.page)
        self.fileinput.setGeometry(QtCore.QRect(30, 121, 781, 31))
        self.fileinput.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.fileinput.setObjectName("fileinput")
        self.inputBrowse = QtWidgets.QPushButton(self.page)
        self.inputBrowse.setGeometry(QtCore.QRect(850, 120, 93, 31))
        self.inputBrowse.setStyleSheet("\n"
"\n"
"/* CSS */\n"
"#inputBrowse {\n"
"  background-color: #0095ff;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 3px;\n"
# "  box-shadow: rgba(255, 255, 255, .4) 0 1px 0 0 inset;\n"
# "  box-sizing: border-box;\n"
"  color: #fff;\n"
# "  cursor: pointer;\n"
# "  display: inline-block;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",\"Liberation Sans\",sans-serif;\n"
"  font-size: 13px;\n"
"  font-weight: 400;\n"
"  line-height: 1.15385;\n"
"  margin: 0;\n"
"  outline: none;\n"
"  padding: 8px .8em;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
# "  user-select: none;\n"
# "  -webkit-user-select: none;\n"
# "  touch-action: manipulation;\n"
"  vertical-align: baseline;\n"
"  white-space: nowrap;\n"
"}\n"
"\n"
"#inputBrowse:hover,\n"
"#inputBrowse:focus {\n"
"  background-color: #07c;\n"
"}\n"
"\n"
"#inputBrowse:focus {\n"
# "  box-shadow: 0 0 0 4px rgba(0, 149, 255, .15);\n"
"}\n"
"\n"
"#inputBrowse:active {\n"
"  background-color: #0064bd;\n"
# "  box-shadow: none;\n"
"}")
        self.inputBrowse.setObjectName("inputBrowse")
        self.title2_2 = QtWidgets.QLabel(self.page)
        self.title2_2.setGeometry(QtCore.QRect(370, 30, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title2_2.setFont(font)
        self.title2_2.setAutoFillBackground(False)
        self.title2_2.setStyleSheet("#title2_2 {\n"
"    background-color: transparent;\n"
"}")
        self.title2_2.setObjectName("title2_2")
        self.execute1 = QtWidgets.QPushButton(self.page)
        self.execute1.setGeometry(QtCore.QRect(420, 330, 101, 28))
        font = QtGui.QFont()
        font.setFamily("-apple-system,system-ui,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.execute1.setFont(font)
        self.execute1.setStyleSheet("\n"
"\n"
"#execute1 {\n"
# "  appearance: none;\n"
"  background-color: #2ea44f;\n"
"  border: 1px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
# "  box-shadow: rgba(27, 31, 35, .1) 0 1px 0;\n"
# "  box-sizing: border-box;\n"
"  color: #fff;\n"
# "  cursor: pointer;\n"
# "  display: inline-block;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Helvetica,Arial,sans-serif,\"Apple Color Emoji\",\"Segoe UI Emoji\";\n"
"  font-size: 14px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 6px 16px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
# "  user-select: none;\n"
# "  -webkit-user-select: none;\n"
# "  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  white-space: nowrap;\n"
"}\n"
"\n"
"\n"
"#execute1:hover {\n"
"  background-color: #2c974b;\n"
"}\n"
"\n"
"#execute1:focus {\n"
# "  box-shadow: rgba(46, 164, 79, .4) 0 0 0 3px;\n"
"  outline: none;\n"
"}\n"
"\n"
"#execute1:disabled {\n"
"  background-color: #94d3a2;\n"
"  border-color: rgba(27, 31, 35, .1);\n"
"  color: rgba(255, 255, 255, .8);\n"
# "  cursor: default;\n"
"}\n"
"\n"
"#execute1:active {\n"
"  background-color: #298e46;\n"
# "  box-shadow: rgba(20, 70, 32, .2) 0 1px 0 inset;\n"
"}")
        self.execute1.setObjectName("execute1")
        self.fileoutput = QtWidgets.QLineEdit(self.page)
        self.fileoutput.setGeometry(QtCore.QRect(30, 181, 781, 31))
        self.fileoutput.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.fileoutput.setObjectName("fileoutput")
        self.outputBrowse = QtWidgets.QPushButton(self.page)
        self.outputBrowse.setGeometry(QtCore.QRect(850, 180, 93, 31))
        self.outputBrowse.setStyleSheet("\n"
"\n"
"/* CSS */\n"
"#outputBrowse {\n"
"  background-color: #0095ff;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 3px;\n"
# "  box-shadow: rgba(255, 255, 255, .4) 0 1px 0 0 inset;\n"
# "  box-sizing: border-box;\n"
"  color: #fff;\n"
# "  cursor: pointer;\n"
# "  display: inline-block;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",\"Liberation Sans\",sans-serif;\n"
"  font-size: 13px;\n"
"  font-weight: 400;\n"
"  line-height: 1.15385;\n"
"  margin: 0;\n"
"  outline: none;\n"
"  padding: 8px .8em;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
# "  user-select: none;\n"
# "  -webkit-user-select: none;\n"
# "  touch-action: manipulation;\n"
"  vertical-align: baseline;\n"
"  white-space: nowrap;\n"
"}\n"
"\n"
"#outputBrowse:hover,\n"
"#outputBrowse:focus {\n"
"  background-color: #07c;\n"
"}\n"
"\n"
"#outputBrowse:focus {\n"
# "  box-shadow: 0 0 0 4px rgba(0, 149, 255, .15);\n"
"}\n"
"\n"
"#outputBrowse:active {\n"
"  background-color: #0064bd;\n"
# "  box-shadow: none;\n"
"}")
        self.outputBrowse.setObjectName("outputBrowse")
        self.output = QtWidgets.QTextEdit(self.page)
        self.output.setGeometry(QtCore.QRect(43, 386, 821, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output.setFont(font)
        self.output.setStyleSheet("\n"
"background-color: rgb(238, 238, 238);\n"
"color: rgb(0, 0, 0);")
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.dynamicfile2 = QtWidgets.QLineEdit(self.page)
        self.dynamicfile2.setGeometry(QtCore.QRect(30, 250, 781, 61))
        self.dynamicfile2.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.dynamicfile2.setObjectName("dynamicfile2")
        self.dynamicmapBrow2 = QtWidgets.QPushButton(self.page)
        self.dynamicmapBrow2.setGeometry(QtCore.QRect(850, 250, 93, 61))
        self.dynamicmapBrow2.setStyleSheet("\n"
"\n"
"/* dynamicmapBrow2 */\n"
"\n"
"\n"
"\n"
"/* CSS */\n"
"#dynamicmapBrow2 {\n"
"  background-color: #0095ff;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 3px;\n"
# "  box-shadow: rgba(255, 255, 255, .4) 0 1px 0 0 inset;\n"
# "  box-sizing: border-box;\n"
"  color: #fff;\n"
# "  cursor: pointer;\n"
# "  display: inline-block;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",\"Liberation Sans\",sans-serif;\n"
"  font-size: 13px;\n"
"  font-weight: 400;\n"
"  line-height: 1.15385;\n"
"  margin: 0;\n"
"  outline: none;\n"
"  padding: 8px .8em;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
# "  user-select: none;\n"
# "  -webkit-user-select: none;\n"
# "  touch-action: manipulation;\n"
"  vertical-align: baseline;\n"
"  white-space: nowrap;\n"
"}\n"
"\n"
"#dynamicmapBrow2:hover,\n"
"#dynamicmapBrow2:focus {\n"
"  background-color: #07c;\n"
"}\n"
"\n"
"#dynamicmapBrow2:focus {\n"
# "  box-shadow: 0 0 0 4px rgba(0, 149, 255, .15);\n"
"}\n"
"\n"
"#dynamicmapBrow2:active {\n"
"  background-color: #0064bd;\n"
# "  box-shadow: none;\n"
"}")
        self.dynamicmapBrow2.setObjectName("dynamicmapBrow2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setStyleSheet("#page_2 {\n"
"    background-image: url(:/images/resources/background-texttunes.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
# "    background-size: cover;\n"
"}")
        self.page_2.setObjectName("page_2")
        self.textInput = QtWidgets.QLineEdit(self.page_2)
        self.textInput.setGeometry(QtCore.QRect(110, 130, 801, 61))
        self.textInput.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.textInput.setObjectName("textInput")
        self.execute2 = QtWidgets.QPushButton(self.page_2)
        self.execute2.setGeometry(QtCore.QRect(440, 360, 101, 31))
        font = QtGui.QFont()
        font.setFamily("-apple-system,system-ui,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.execute2.setFont(font)
        self.execute2.setStyleSheet("\n"
"\n"
"#execute2 {\n"
# "  appearance: none;\n"
"  background-color: #2ea44f;\n"
"  border: 1px solid rgba(27, 31, 35, .15);\n"
"  border-radius: 6px;\n"
# "  box-shadow: rgba(27, 31, 35, .1) 0 1px 0;\n"
# "  box-sizing: border-box;\n"
"  color: #fff;\n"
# "  cursor: pointer;\n"
# "  display: inline-block;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",Helvetica,Arial,sans-serif,\"Apple Color Emoji\",\"Segoe UI Emoji\";\n"
"  font-size: 14px;\n"
"  font-weight: 600;\n"
"  line-height: 20px;\n"
"  padding: 6px 16px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
# "  user-select: none;\n"
# "  -webkit-user-select: none;\n"
# "  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  white-space: nowrap;\n"
"}\n"
"\n"
"\n"
"#execute2:hover {\n"
"  background-color: #2c974b;\n"
"}\n"
"\n"
"#execute2:focus {\n"
# "  box-shadow: rgba(46, 164, 79, .4) 0 0 0 3px;\n"
"  outline: none;\n"
"}\n"
"\n"
"#execute2:disabled {\n"
"  background-color: #94d3a2;\n"
"  border-color: rgba(27, 31, 35, .1);\n"
"  color: rgba(255, 255, 255, .8);\n"
# "  cursor: default;\n"
"}\n"
"\n"
"#execute2:active {\n"
"  background-color: #298e46;\n"
# "  box-shadow: rgba(20, 70, 32, .2) 0 1px 0 inset;\n"
"}")
        self.execute2.setObjectName("execute2")
        self.title2 = QtWidgets.QLabel(self.page_2)
        self.title2.setGeometry(QtCore.QRect(400, 40, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title2.setFont(font)
        self.title2.setObjectName("title2")
        self.widget_2 = QtWidgets.QWidget(self.page_2)
        self.widget_2.setGeometry(QtCore.QRect(80, 420, 841, 211))
        self.widget_2.setObjectName("widget_2")
        self.play_btn = QtWidgets.QPushButton(self.page_2)
        self.play_btn.setGeometry(QtCore.QRect(620, 660, 93, 28))
        self.play_btn.setStyleSheet("background-color: rgb(255, 248, 250);")
        self.play_btn.setObjectName("play_btn")
        self.fileoutput_2 = QtWidgets.QLineEdit(self.page_2)
        self.fileoutput_2.setGeometry(QtCore.QRect(110, 210, 671, 31))
        self.fileoutput_2.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.fileoutput_2.setObjectName("fileoutput_2")
        self.outputBrowse_2 = QtWidgets.QPushButton(self.page_2)
        self.outputBrowse_2.setGeometry(QtCore.QRect(810, 210, 93, 31))
        self.outputBrowse_2.setStyleSheet("\n"
"\n"
"/* dynamicmapBrow2 */\n"
"\n"
"\n"
"\n"
"/* CSS */\n"
"#outputBrowse_2 {\n"
"  background-color: #0095ff;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 3px;\n"
# "  box-shadow: rgba(255, 255, 255, .4) 0 1px 0 0 inset;\n"
# "  box-sizing: border-box;\n"
"  color: #fff;\n"
# "  cursor: pointer;\n"
# "  display: inline-block;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",\"Liberation Sans\",sans-serif;\n"
"  font-size: 13px;\n"
"  font-weight: 400;\n"
"  line-height: 1.15385;\n"
"  margin: 0;\n"
"  outline: none;\n"
"  padding: 8px .8em;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
# "  user-select: none;\n"
# "  -webkit-user-select: none;\n"
# "  touch-action: manipulation;\n"
"  vertical-align: baseline;\n"
"  white-space: nowrap;\n"
"}\n"
"\n"
"#outputBrowse_2:hover,\n"
"#outputBrowse_2:focus {\n"
"  background-color: #07c;\n"
"}\n"
"\n"
"#outputBrowse_2:focus {\n"
# "  box-shadow: 0 0 0 4px rgba(0, 149, 255, .15);\n"
"}\n"
"\n"
"#outputBrowse_2:active {\n"
"  background-color: #0064bd;\n"
# "  box-shadow: none;\n"
"}")
        self.outputBrowse_2.setObjectName("outputBrowse_2")
        self.progressBar = QtWidgets.QProgressBar(self.page_2)
        self.progressBar.setGeometry(QtCore.QRect(750, 660, 201, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.dynamicfile1 = QtWidgets.QLineEdit(self.page_2)
        self.dynamicfile1.setGeometry(QtCore.QRect(110, 250, 671, 61))
        self.dynamicfile1.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.dynamicfile1.setObjectName("dynamicfile1")
        self.dynamicmapBrow1 = QtWidgets.QPushButton(self.page_2)
        self.dynamicmapBrow1.setGeometry(QtCore.QRect(810, 250, 93, 61))
        self.dynamicmapBrow1.setStyleSheet("\n"
"\n"
"/* dynamicmapBrow2 */\n"
"\n"
"\n"
"\n"
"/* CSS */\n"
"#dynamicmapBrow1 {\n"
"  background-color: #0095ff;\n"
"  border: 1px solid transparent;\n"
"  border-radius: 3px;\n"
# "  box-shadow: rgba(255, 255, 255, .4) 0 1px 0 0 inset;\n"
# "  box-sizing: border-box;\n"
"  color: #fff;\n"
# "  cursor: pointer;\n"
# "  display: inline-block;\n"
"  font-family: -apple-system,system-ui,\"Segoe UI\",\"Liberation Sans\",sans-serif;\n"
"  font-size: 13px;\n"
"  font-weight: 400;\n"
"  line-height: 1.15385;\n"
"  margin: 0;\n"
"  outline: none;\n"
"  padding: 8px .8em;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
# "  user-select: none;\n"
# "  -webkit-user-select: none;\n"
# "  touch-action: manipulation;\n"
"  vertical-align: baseline;\n"
"  white-space: nowrap;\n"
"}\n"
"\n"
"#dynamicmapBrow1:hover,\n"
"#dynamicmapBrow1:focus {\n"
"  background-color: #07c;\n"
"}\n"
"\n"
"#dynamicmapBrow1:focus {\n"
# "  box-shadow: 0 0 0 4px rgba(0, 149, 255, .15);\n"
"}\n"
"\n"
"#dynamicmapBrow1:active {\n"
"  background-color: #0064bd;\n"
# "  box-shadow: none;\n"
"}")
        self.dynamicmapBrow1.setObjectName("dynamicmapBrow1")
        self.stackedWidget.addWidget(self.page_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 780, 471, 31))
        self.pushButton_4.setStyleSheet("\n"
"\n"
"/* CSS */\n"
"#pushButton_4{\n"
"  background-color: #EA4C89;\n"
"  border-radius: 8px;\n"
"  border-style: none;\n"
# "  box-sizing: border-box;\n"
"  color: #FFFFFF;\n"
# "  cursor: pointer;\n"
# "  display: inline-block;\n"
"  font-family: \"Haas Grot Text R Web\", \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n"
"  font-size: 14px;\n"
"  font-weight: 500;\n"
"  height: 40px;\n"
"  line-height: 20px;\n"
"  list-style: none;\n"
"  margin: 0;\n"
"  outline: none;\n"
"  padding: 10px 16px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
# "  transition: color 100ms;\n"
"  vertical-align: baseline;\n"
# "  user-select: none;\n"
# "  -webkit-user-select: none;\n"
# "  touch-action: manipulation;\n"
"}\n"
"\n"
"\n"
"#pushButton_4:hover,\n"
"#pushButton_4:focus {\n"
"  background-color: #F082AC;\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 780, 461, 31))
        self.pushButton_5.setStyleSheet("\n"
"\n"
"/* CSS */\n"
"#pushButton_5 {\n"
"  background-color: #EA4C89;\n"
"  border-radius: 8px;\n"
"  border-style: none;\n"
# "  box-sizing: border-box;\n"
"  color: #FFFFFF;\n"
# "  cursor: pointer;\n"
# "  display: inline-block;\n"
"  font-family: \"Haas Grot Text R Web\", \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n"
"  font-size: 14px;\n"
"  font-weight: 500;\n"
"  height: 40px;\n"
"  line-height: 20px;\n"
"  list-style: none;\n"
"  margin: 0;\n"
"  outline: none;\n"
"  padding: 10px 16px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
# "  transition: color 100ms;\n"
"  vertical-align: baseline;\n"
# "  user-select: none;\n"
# "  -webkit-user-select: none;\n"
# "  touch-action: manipulation;\n"
"}\n"
"\n"
"#pushButton_5:hover,\n"
"#pushButton_5:focus {\n"
"  background-color: #F082AC;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fileinput.setPlaceholderText(_translate("MainWindow", "Enter Your Input File Path Here"))
        self.inputBrowse.setText(_translate("MainWindow", "Browse"))
        self.title2_2.setText(_translate("MainWindow", "Music To Text"))
        self.execute1.setText(_translate("MainWindow", "Execute"))
        self.fileoutput.setPlaceholderText(_translate("MainWindow", "Enter Your Output File Path Here"))
        self.outputBrowse.setText(_translate("MainWindow", "Browse"))
        self.dynamicfile2.setPlaceholderText(_translate("MainWindow", "Enter you mapping file here ( Like  a C4 1 then b C4 1 in new line )"))
        self.dynamicmapBrow2.setText(_translate("MainWindow", "Browse"))
        self.textInput.setPlaceholderText(_translate("MainWindow", "Enter Your Input Text Here"))
        self.execute2.setText(_translate("MainWindow", "Execute"))
        self.title2.setText(_translate("MainWindow", "Text To Music"))
        self.play_btn.setText(_translate("MainWindow", "Play"))
        self.fileoutput_2.setPlaceholderText(_translate("MainWindow", "Enter Your Output File Path Here"))
        self.outputBrowse_2.setText(_translate("MainWindow", "Browse"))
        self.dynamicfile1.setPlaceholderText(_translate("MainWindow", "Enter you mapping file here ( Like  a C4 1 then b C4 1 in new line )"))
        self.dynamicmapBrow1.setText(_translate("MainWindow", "Browse"))
        self.pushButton_4.setText(_translate("MainWindow", "Music To Text"))
        self.pushButton_5.setText(_translate("MainWindow", "Text To Music"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())