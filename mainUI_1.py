# -*- coding: utf-8 -*-
#import Gender_prediction
#import Gender_wise_words
#import Geo_tweets_trump
import sentiment


# Form implementation generated from reading ui file 'tweeteranaylsisui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import pandas
from PyQt5 import *
import numpy as np
import matplotlib.pyplot as plt
#import sklearn
#from mpl_toolkits.basemap import Basemap
import sys
import os
import tweepy
from tweepy import *
from textblob import TextBlob
import re
import PyQt5.uic as uic

   
class Ui_Dialog(object):
    def __init__(self):
        super().__init__()
        #self.initGUI()

    def SentimentAnalysis(self, Dialog):
        print("Inside SentimentAnalysis method")
        print(self.plainTextEdit_2.toPlainText())
        print(self.plainTextEdit_3.toPlainText())
        if(self.radioButton.isChecked()):
            print("sentimentwise radio")
            sentiment.run_sentiment(self.plainTextEdit_2.toPlainText(),int(self.plainTextEdit_3.toPlainText()))

        elif(self.radioButton_3.isChecked()):
            print("Gender wise radio")
            import Gender_wise_words
        elif(self.radioButton_4.isChecked()):
            print("Geolocation wise radio")
            #Geo_tweets_trump.run_geolocation(self.plainTextEdit_2.toPlainText(),int(self.plainTextEdit_3.toPlainText()))

        else:
            print("Nothing is selected")

    def openFileNamesDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)


    """def showDialog(SentimentAnalysis):

        fname = QFileDialog.getOpenFileName(self, 'Open file', 'C:/Python36/sentiment.py')

        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)"""  
    
                
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(555, 463)

        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(209, 50, 311, 121))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")

        
        #gen
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(354, 202, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")

        #Dip
        #self.Genderwise(Dialog)
        #self.radioButton_3.clicked.connect(self.Genderwise)

        
        
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(204, 202, 121, 17))
        self.radioButton_4.setObjectName("radioButton_4")

        #Dip
        #self.Geolocationwise(Dialog)
        #self.radioButton_4.clicked.connect(self.Geolocationwise)

        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(203, 20, 361, 20))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 141, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(43, 172, 111, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(240, 335, 231, 31))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(242, 389, 231, 31))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(241, 413, 231, 31))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(241, 363, 231, 31))
        self.label_7.setObjectName("label_7")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 292, 251, 41))
        self.pushButton.setObjectName("search_btn")

        
        self.pushButton.clicked.connect(self.SentimentAnalysis)
        #self.connect(self.pushButton, Qt.SIGNAL("clicked()"), self.SentimentAnalysis)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 300, 91, 23))
        self.pushButton_2.setObjectName("clear_btn")

        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(50, 250, 68, 19))
        self.label_8.setObjectName("label_8")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(220, 250, 281, 21))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")

        #sentiment
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(270, 180, 121, 21))
        self.radioButton.setObjectName("radioButton")
        
        #self.SentimentAnalysis(Dialog)
        #self.radioButton.clicked.connect(self.SentimentAnalysis)
        #self.radioButton.toggled.connect(self.SentimentAnalysis)"""
        #radioButton = self.sender()
     #   w.addAction.triggered.connect(SentimentAnalysis)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #Dip
        #self.SentimentAnalysis(Dialog)
        #self.radioButton.clicked.connect(self.SentimentAnalysis)
        #self.radioButton_4.clicked.connect(self.SentimentAnalysis)
        
        
        
    """def browse_folder(self):
        self.listWidget.clear()
        directory = QtGui.QFileDialog.getExistingDirectory(self,"C:/Users/Deep Ankur/Desktop/Student/adittwitter/11/geograpgh/sentiment.py")
        for file_name in os.listdir(directory): 
                self.listWidget.addItem(file_name)
                print("filepath")"""

        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioButton.setText(_translate("Dialog", "Sentiment Analysis"))
        self.radioButton_3.setText(_translate("Dialog", "Genderwise "))
        self.radioButton_4.setText(_translate("Dialog", "   Geolocationwise"))
        self.label.setText(_translate("Dialog", "Sentimental Analysics of Twitter"))
        self.label_2.setText(_translate("Dialog", "Keywords forTweets Scan"))
        self.label_3.setText(_translate("Dialog", "Select Filter"))
        self.label_4.setText(_translate("Dialog", "Designed by ADIT Students"))
        self.label_5.setText(_translate("Dialog", "Margish 140010116042"))
        self.label_6.setText(_translate("Dialog", "Saurin 140010116062"))
        self.label_7.setText(_translate("Dialog", "Digesh 140010116013 "))
        self.pushButton.setText(_translate("Dialog", "Start searching and Analysis"))
        
        self.pushButton_2.setText(_translate("Dialog", "Clear all"))
        self.label_8.setText(_translate("Dialog", "Counts "))
        self.radioButton_4.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.radioButton.setChecked(False)

class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.openFileNameDialog()
        self.openFileNamesDialog()
        self.saveFileDialog()
 
        self.show()
 
    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
 
    def openFileNamesDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        
        if files:
            print(files)
        self.SentimentAnalysis(Dialog)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    #app = QApplication(sys.argv)
    #ex = App()
    sys.exit(app.exec_())
