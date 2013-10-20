import subprocess, os, sys, shutil, stat, time
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QSplashScreen, QPixmap, QApplication

class Form(QtGui.QWidget):
	def __init__(self, parent=None):
		src = "Y:\\SAVES\\007_LEGENDS\\%s\\007 Legends" % str(sys.argv[1])
		dst = "C:\\Users\\User\\Documents\\my games\\Activision\\007 Legends"
		splash = QSplashScreen(QPixmap("launching.jpg"))
		splash.show()
		if os.path.exists(src) == True:
			if os.path.exists(dst) == True:
				os.chmod(dst, stat.S_IWRITE)
				shutil.rmtree(dst)
				shutil.copytree(src, dst)
				time.sleep(1)
				splash.close()
			else:
				shutil.copytree(src, dst)
				time.sleep(1)
				splash.close()
		else:
			if os.path.exists(dst) == True:
				os.chmod(dst, stat.S_IWRITE)
				shutil.rmtree(dst)
				shutil.copytree(src, dst)
				time.sleep(1)
				splash.close()
			else:
				pass
		os.chdir("D:\\007 Legends")
		subprocess.call("Bond2012PC.exe")
		if os.path.exists(src) == True:
			os.chmod(dst, stat.S_IWRITE)
			os.chmod(src, stat.S_IWRITE)
			shutil.rmtree(src)
			shutil.move(dst, src)
			exit()
		else:
			os.chmod(dst, stat.S_IWRITE)
			shutil.move(dst, src)
			exit()
app = QtGui.QApplication(sys.argv)
form = Form()
app.exec_()