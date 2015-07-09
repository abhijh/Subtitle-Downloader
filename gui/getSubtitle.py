#!/usr/bin/python
import sys, time, utilities
from PyQt4 import QtGui, QtCore


class App(QtGui.QWidget):
    
    def __init__(self):
        super(App, self).__init__()
        self.initUI()
        
    def initUI(self):      
        self.status = QtGui.QLabel('Generating Hash', self)
        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.timer = QtCore.QBasicTimer()
        self.step = 0
        self.final = 20
        self.timer.start(20,self)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Subtitle Downloader')
        self.show()

        self.final = 100        
        process = utilities.utilities(sys.argv[1])
        self.responce = process.get_hash()
        if self.responce == 1:
            self.status.setText('IO error') 
            self.timer.start(20,self)
        else:
            self.responce = process.get_subtitle()
            if self.responce == 2:
                self.status.setText('Not found')
                self.timer.start(20,self)
            else:
                self.responce = process.write_subtitle()
                if self.responce == 0:
                    self.status.setText('Done')
                    self.timer.start(0,self)
                else:
                    self.timer.start(20,self)
                    self.status.setText('Permission Err')

        
    def timerEvent(self, e):
      
        if self.step >= self.final:
            self.timer.stop()
            #self.status.setText('Done!')   
            if self.final == 100:
                time.sleep(.5)
                QtCore.QCoreApplication.instance().quit()
            return
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    