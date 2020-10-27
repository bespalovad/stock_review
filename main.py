import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow, Ui_Form_Home, Ui_Form_Notifications, Ui_Form_Search, Ui_Form_Settings

class Company:
	def __init__ (self, name, link, color):
		super(Company, self).__init__()
		self.name = name
		self.link = link
		self.color = color
	
	def change_name (self, name):
		self.name = name
		
	def change_link (self, link):
		self.link = link
	
	def change_color (self, color):
		self.color = color
	
class Company_List:
	def __init__(self):
		super(Company_List, self).__init__()
		company_list = []
		self.company_list = company_list
		
	def add_company (self, name, link, color):
		new_company = Company (name, link, color)
		self.company_list.append(new_company)
	
	def return_company (self, index):
		return self.company_list[index]
		
	def remove_company (self, index):
		self.company_list.pop(index)
	
class Window (QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__ (self):
		super().__init__()
		self.setupUi(self)
		
		self.Home.clicked.connect( self.changeSceneToHome )
		self.Notifications.clicked.connect( self.changeSceneToNotifications )
		self.Search.clicked.connect( self.changeSceneToSearch )
		self.Settings.clicked.connect( self.changeSceneToSettings )
		
	def clearScene( self ):
		for i in reversed(range(self.MainMenuLayout.count())): 
			self.MainMenuLayout.itemAt(i).widget().setParent(None)

	def changeSceneToHome( self ):
		self.clearScene()
		self.changeModeToHome()
		self.MainMenuLayout.addWidget( Home() )

	def changeSceneToNotifications( self ):
		self.clearScene()
		self.changeModeToNotifications()
		self.MainMenuLayout.addWidget( Notifications() )
		
	def changeSceneToSearch( self ):
		self.clearScene()
		self.changeModeToSearch()
		self.MainMenuLayout.addWidget( Search() )

	def changeSceneToSettings( self ):
		self.clearScene()
		self.changeModeToSettings()
		self.MainMenuLayout.addWidget( Settings() )

class Home(QtWidgets.QWidget, Ui_Form_Home):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

class Notifications(QtWidgets.QWidget, Ui_Form_Notifications):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		
class Search(QtWidgets.QWidget, Ui_Form_Search):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

class Settings(QtWidgets.QWidget, Ui_Form_Settings):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

def main():
	app = QtWidgets.QApplication ([])
	win = Window()
	win.show()
	sys.exit(app.exec())

if __name__ == '__main__':
	main()

