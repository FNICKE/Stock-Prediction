from PyQt5 import QtCore, QtGui, QtWidgets
from PythonFinance import Finance

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
    
    def setupUi(self):
        self.setWindowTitle("Stock Genie")
        self.resize(800, 600)
        self.setStyleSheet("background-color: rgb(35, 3, 36);")
        
        # Central Widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        
        # Frame
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(180, 50, 440, 450))
        self.frame.setStyleSheet("background-color: rgb(27, 56, 49); border-radius: 15px;")
        
        # Title Label
        self.label = QtWidgets.QLabel("STOCK GENIE", self.frame)
        self.label.setGeometry(QtCore.QRect(90, 40, 281, 71))
        self.label.setFont(QtGui.QFont("Tw Cen MT", 36, QtGui.QFont.Bold))
        self.label.setStyleSheet("color: white;")
        
        # Input Field
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(80, 180, 261, 41))
        self.lineEdit.setFont(QtGui.QFont("Arial", 14))
        self.lineEdit.setStyleSheet("color: yellow; border-radius: 10px; padding: 5px;")
        self.lineEdit.setPlaceholderText("Enter Ticker Symbol")
        
        # Predict Button
        self.pushButton = QtWidgets.QPushButton("PREDICT", self.frame)
        self.pushButton.setGeometry(QtCore.QRect(150, 260, 140, 45))
        self.pushButton.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.pushButton.setStyleSheet("color: white; background-color: #0057B8; border-radius: 10px;")
        self.pushButton.clicked.connect(self.pressed)
        
        # Status Label
        self.statusLabel = QtWidgets.QLabel("", self.frame)
        self.statusLabel.setGeometry(QtCore.QRect(100, 330, 250, 40))
        self.statusLabel.setFont(QtGui.QFont("Arial", 12))
        self.statusLabel.setStyleSheet("color: white;")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        
    def pressed(self):
        ticker = self.lineEdit.text().strip().upper()
        
        if not ticker:
            self.statusLabel.setText("⚠️ Please enter a valid ticker symbol.")
            return
        
        try:
            finance = Finance()
            result = finance.get_moving_avg(ticker)
            self.statusLabel.setText(f"✅ Prediction complete for {ticker}.")
        except Exception as e:
            self.statusLabel.setText(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec_())
