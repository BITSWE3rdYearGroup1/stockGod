

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QDoubleSpinBox, QLineEdit, \
    QTextEdit, QPushButton, QGraphicsView, QFileDialog, QGraphicsScene
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from sklearn.linear_model import LinearRegression
import pickle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 980)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(33, 47, 63);\n"
                                 "color:#FFF;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 550, 41, 21))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(
            parent=self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(250, 550, 221, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(
            parent=self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(250, 650, 221, 22))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(
            parent=self.centralwidget)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(250, 750, 221, 22))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")

        self.doubleSpinBox.setRange(0, 9999999.99)
        self.doubleSpinBox.setSingleStep(0.000001)

        self.doubleSpinBox_2.setRange(0, 9999999.99)
        self.doubleSpinBox_2.setSingleStep(0.000001)

        self.doubleSpinBox_3.setRange(0, 9999999999.99)
        self.doubleSpinBox_3.setSingleStep(0.00001)

        self.doubleSpinBox.setDecimals(8)
        self.doubleSpinBox_2.setDecimals(8)
        self.doubleSpinBox_3.setDecimals(8)

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 650, 51, 21))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 750, 81, 21))
        self.label_3.setStyleSheet("color:#FFF;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 850, 51, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 850, 211, 22))
        self.lineEdit.setStyleSheet("border:none;")
        self.lineEdit.setObjectName("lineEdit")
        self.graphicsView_3 = QtWidgets.QGraphicsView(
            parent=self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(830, 20, 400, 500))
        self.graphicsView_3.setStyleSheet("background-color:#fff;\n"
                                          "color:#212f3f;")
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(850, 550, 121, 31))
        self.pushButton.setStyleSheet("background-color:#fff;\n"
                                      "color:#212f3f;\n"
                                      "border-radius:10px;")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(770, 650, 300, 31))
        self.textEdit.setStyleSheet("border:none;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(770, 750, 300, 31))
        self.textEdit_2.setStyleSheet("border:none;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 850, 110, 28))
        self.pushButton_2.setStyleSheet("background-color:#FFF;\n"
                                        "color:#212f3f;\n"
                                        "border-radius: 10px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView_4 = QtWidgets.QGraphicsView(
            parent=self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(420, 20, 400, 500))
        self.graphicsView_4.setStyleSheet("background-color:#fff;\n"
                                          "color:#212f3f;")
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.graphicsView_5 = QtWidgets.QGraphicsView(
            parent=self.centralwidget)
        self.graphicsView_5.setGeometry(QtCore.QRect(10, 20, 400, 500))
        self.graphicsView_5.setStyleSheet("background-color:#FFF;\n"
                                          "color:#212f3f;")
        self.graphicsView_5.setObjectName("graphicsView_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "High"))
        self.label_2.setText(_translate("MainWindow", "Low"))
        self.label_3.setText(_translate("MainWindow", "Volume"))
        self.label_4.setText(_translate("MainWindow", "Close"))
        self.pushButton.setText(_translate("MainWindow", "Predict"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">MSE( Mean Squared Error): 34.8334296</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">R</span><span style=\" font-size:8pt; vertical-align:super;\">2 </span><span style=\" font-size:8pt;\">Score( R-Squared Score): 0.99989</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "File Upload"))
        self.pushButton_2.clicked.connect(self.handle_file_upload)
        self.pushButton.clicked.connect(self.predictClicked)

    def handle_file_upload(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            None, "Upload CSV File", ".", "CSV Files (*.csv)")

        if file_path:
            # Read the CSV file using pandas
            df = pd.read_csv(file_path)
            model = LinearRegression()

            with open('trained_model.pkl', 'rb') as file:
                model = pickle.load(file)
            try:  
                # Extract the required columns
                high = df['High']
                low = df['Low']
                volume = df['Volume']
                close = model.predict(df)

                # Plot High vs Close
                figure1 = plt.figure()
                plt.plot(high, close, 'r.')
                plt.xlabel('High')
                plt.ylabel('Close')

                # Plot Low vs Close
                figure2 = plt.figure()
                plt.plot(low, close, 'g.')
                plt.ylabel('Close')
                plt.xlabel('Low')

                # Plot Volume vs Close
                figure3 = plt.figure()
                plt.plot(volume, close, 'b.')
                plt.ylabel('Close')
                plt.xlabel('Volume')

                canvas1 = FigureCanvas(figure1)
                canvas2 = FigureCanvas(figure2)
                canvas3 = FigureCanvas(figure3)

                # Create QGraphicsScene objects
                scene1 = QGraphicsScene()
                scene2 = QGraphicsScene()
                scene3 = QGraphicsScene()

                # Add the FigureCanvas objects to the QGraphicsScene objects
                scene1.addWidget(canvas1)
                scene2.addWidget(canvas2)
                scene3.addWidget(canvas3)

                # Set the QGraphicsScene objects as the scene for the respective QGraphicsView widgets
                self.graphicsView_3.setScene(scene1)
                self.graphicsView_4.setScene(scene2)
                self.graphicsView_5.setScene(scene3)
            except ValueError:
                self.lineEdit.setText("Invalid File format")


    def predictClicked(self):
        # Get the values from the spin boxes
        high = self.doubleSpinBox.value()
        low = self.doubleSpinBox_2.value()
        volume = self.doubleSpinBox_3.value()
        model = LinearRegression()

        with open('trained_model.pkl', 'rb') as file:
            model = pickle.load(file)
        # Create a DataFrame with the input values
        data = {'High': [high], 'Low': [low], 'Volume': [volume]}
        df = pd.DataFrame(data)
        close = model.predict(df)
        data = {'High': [high], 'Low': [low],
                'Volume': [volume], 'Close': [close]}
        df = pd.DataFrame(data)
        self.lineEdit.setText(str(close[0]))
        # Plot the graphs
        figure1 = plt.figure()
        plt.plot(high, close, 'r.')
        plt.ylabel('Close')
        plt.xlabel('High')

        # Plot Low vs Close
        figure2 = plt.figure()
        plt.plot(low, close, 'g.')
        plt.ylabel('Close')
        plt.xlabel('Low')

        # Plot Volume vs Close
        figure3 = plt.figure()
        plt.plot(volume, close, 'b.')
        plt.ylabel('Close')
        plt.xlabel('Volume')

        canvas1 = FigureCanvas(figure1)
        canvas2 = FigureCanvas(figure2)
        canvas3 = FigureCanvas(figure3)

        # Create QGraphicsScene objects
        scene1 = QGraphicsScene()
        scene2 = QGraphicsScene()
        scene3 = QGraphicsScene()

        # Add the FigureCanvas objects to the QGraphicsScene objects
        scene1.addWidget(canvas1)
        scene2.addWidget(canvas2)
        scene3.addWidget(canvas3)

        # Set the QGraphicsScene objects as the scene for the respective QGraphicsView widgets
        self.graphicsView_3.setScene(scene1)
        self.graphicsView_4.setScene(scene2)
        self.graphicsView_5.setScene(scene3)
