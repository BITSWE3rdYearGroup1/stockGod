from PyQt5.QtWidgets import QApplication, QMainWindow
from StockGod import Ui_MainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create an instance of the generated UI class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()

