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
        
    def callToAPI(self):
        try:
            response = requests.get() #Provide Currecny Exchange API link here.
            #print(response.json())
            self.data = response.json()
            print(self.data['rates']['AED'])
        except:
            print()
    
    def fillCurrencyCombo(self):
        self.from_currency_combo = self.findChild(QtWidgets.QComboBox, 'cb_from_currency')
        self.from_currency_combo.addItems(self.data['rates'].keys())

        self.to_currency_combo = self.findChild(QtWidgets.QComboBox, 'cb_to_currency')
        self.to_currency_combo.addItems(self.data['rates'].keys())
