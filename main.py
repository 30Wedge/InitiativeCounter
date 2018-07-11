###
### main.py 
###

#Launches the main intiative counter window
# contains mouse click events and ticker logic.
#Simple AF

###
### Core features
###

#Left-click: Tick up by one
#Right-click: Reset to 0
#Double Right-Click is an undo. Go back to the last non-zero number.
#And that's all I can think of for now.
#We can add functionality to a Double Left-Click, 
#Could also use the scroll wheel.
# Could use Up and Down Keys if we want a PC to manage it etc.
# And yeah


###
### Bonus features
###

#I wonder what it'd be like if we rolled for initative once per encounter.
#If we had a way to send that info into this program, so it skips to who is up
#You can see along the right or left side who is up when in relation to who
#That's maybe too much, but brainstorming is important
#Stick to this basic one for now, and we'll be good

from PyQt5 import QtCore, QtGui, QtWidgets
from gen import Ui_MainWindow

class MwWithClickSlots(Ui_MainWindow):
  """ Extends the auto-generated code to add methods to manipulate members"""
  def increment_me(self):
    self.lcdNumber.setProperty("value", self.lcdNumber.value() + 1)

  def reset_me(self):
    self.lcdNumber.setProperty("value", 0.0)


class IncrementorWindow(QtWidgets.QMainWindow):
  """ Extends Main Window with mouse tracking events """
  def __init__(self, ui_handle):
    """ Initialize the main window with a handle to the rest of the widgets.
    Lets you use MainWindow events to manipulate other widgets"""
    super().__init__()
    self.ui_handle = ui_handle

  def mouseReleaseEvent(self, QMouseEvent):
    if QMouseEvent.button() == QtCore.Qt.RightButton:
      self.ui_handle.reset_me()
    elif QMouseEvent.button() == QtCore.Qt.LeftButton:
      self.ui_handle.increment_me()



#Main function
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    ui = MwWithClickSlots()
    MainWindow = IncrementorWindow(ui)
    #make it frameless
    #MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint or QtCore.Qt.CustomizeWindowHint) #idk if that second flag is needed
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint )
    ui.setupUi(MainWindow)
    # (V) show it full screen
    MainWindow.showFullScreen()
    sys.exit(app.exec_())