#INSTALL PyQt5 WITH:
# 1. ANACONDA:
# conda install -c anaconda pyqt
# 2. PIP:
# pip install PyQt5
#3. LINUX:
# sudo apt-get install python3-pyqt5

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *

#define size & color of the window
app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("TEMPNAME - PyQT")
window.setFixedWidth(1920)
window.setFixedHeight(1080)
window.setStyleSheet("background-color: #20bebe;")

#define the grid layout

grid=QGridLayout()
#logo
image=QPixmap("./tutorial/logo.png")
logo=QLabel()
logo.setPixmap(image)
grid.addWidget(logo, 0,0)

window=QLayout(grid)

#setup gui
window.show()
sys.exit(app.exec())
