# We are going to develop a Currency Converter App :)
from PyQt5 import QtWidgets, uic
import sys
import requests
import json

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('CurrencyConverterGUI.ui', self)
        
        self.button = self.findChild(QtWidgets.QPushButton, 'pb_convert_currency') 
        self.button.clicked.connect(self.convertCurrency) 
        
        self.callToAPI()
        self.fillCurrencyCombo()

       
        
        self.show()
