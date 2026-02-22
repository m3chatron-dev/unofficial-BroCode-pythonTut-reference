# PyQt5 QLabels
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #292929; "
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")

        # label.setAlignment(Qt.AlignmentFlag.AlignTop) #VERTICALLY TOP
        # label.setAlignment(Qt.AlignmentFlag.AlignBottom) # VERTICALLY BOTTOM
        # label.setAlignment(Qt.AlignmentFlag.AlignVCenter)  # VERTICALLY CENTER

        # label.setAlignment(Qt.AlignmentFlag.AlignRight)  # HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter)  # HORIZONTALLY CENTER
        # label.setAlignment(Qt.AlignmentFlag.AlignLeft)  # HORIZONTALLY LEFT

        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop) # CENTER & TOP
        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom) # CENTER & BOTTOM
        # label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) # CENTER & CENTER
        label.setAlignment(Qt.AlignmentFlag.AlignCenter) # CENTER & CENTER

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()