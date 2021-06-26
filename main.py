from src.pdfdownloader import pdfdownloader
from PyQt5 import QtWidgets
import sys
from src import *


app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)


ui.pushButton.clicked.connect(lambda:ui.get_url())
Form.show()
sys.exit(app.exec_())