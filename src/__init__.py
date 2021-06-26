from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(550, 350)
        Form.setMinimumSize(QtCore.QSize(550, 350))
        Form.setMaximumSize(QtCore.QSize(550, 350))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #222, stop:0.45 #111);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.close = QtWidgets.QFrame(Form)
        self.close.setStyleSheet("")
        self.close.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.close.setFrameShadow(QtWidgets.QFrame.Raised)
        self.close.setObjectName("close")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.close)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.close)
        self.frame_2.setMinimumSize(QtCore.QSize(350, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(550, 16777215))
        self.frame_2.setStyleSheet("background: transparent;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(170, 120, 104, 16))
        self.label_2.setStyleSheet("color: #bbb")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(170, 60, 145, 16))
        self.label.setStyleSheet("color: #bbb")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(170, 80, 200, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 20))
        self.lineEdit.setStyleSheet("background:rgb(248, 248, 248) ;\n"
"border: 1px solid rgb(45, 45, 45);\n"
"border-radius: 4px")
        self.lineEdit.setObjectName("lineEdit")
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar.setGeometry(QtCore.QRect(140, 260, 251, 20))
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(210, 190, 111, 31))
        self.pushButton.setMaximumSize(QtCore.QSize(120, 40))
        self.pushButton.setStyleSheet("QPushButton {\n"
"color: #eee; \n"
"background: rgb(24, 104, 255); \n"
"border-radius: 4px;\n"
"}\n"
"   \n"
"QPushButton:hover\n"
"{\n"
"background: #000;\n"
"\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background: rgb(58, 59, 160);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 140, 200, 20))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(200, 20))
        self.lineEdit_2.setStyleSheet("background:rgb(248, 248, 248) ;\n"
"border: 1px solid rgb(45, 45, 45);\n"
"border-radius: 4px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(140, 240, 271, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Hebrew Scholar")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #666")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(10, 320, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Hebrew Scholar")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #444")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        
        
    def progressBar_Update(self, value):
            self.progressBar.setProperty("value", value)
            
            
            
    def get_url(self):
            url = self.lineEdit.text()
            print('url = ' + url)
            return url
    
    def get_name(self):
            name = self.lineEdit_2.text()
            return name
    
    

    
            
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Universidade Cruseiro do Sul PDF Downloader"))
        self.label_2.setText(_translate("Form", "Nome da Matéria"))
        self.label.setText(_translate("Form", "Link da do Primeiro PDF"))
        self.pushButton.setText(_translate("Form", "Download"))
        self.label_3.setText(_translate("Form", "Verificando quantidade de material"))
        self.label_4.setText(_translate("Form", "Desenvolvido por Marcio Shimizu"))


