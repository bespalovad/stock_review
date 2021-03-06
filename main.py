import sys, requests, traceback
from PyQt5 import QtCore, QtGui, QtWidgets
from window import Ui_MainWindow, Ui_Form_Home, Ui_Form_Notifications, Ui_Form_Search, Ui_Form_Settings
from abc import ABC, abstractmethod

class Company:
  def __init__(self, price=None, valueChange=None, percentageChange=None, history=None):
    self.price = price
    self.valueChange = valueChange
    self.percentageChange = percentageChange
    self.history = history

  @property
  def price(self): return self._price
  @price.setter
  def price(self, value): self._price = value

  @property
  def valueChange(self): return self._valueChange
  @valueChange.setter
  def valueChange(self, value): self._valueChange = value

  @property
  def percentageChange(self): return self._percentageChange
  @percentageChange.setter
  def percentageChange(self, value): self._percentageChange = value

  @property
  def history(self): return self._history
  @history.setter
  def history(self, value): self._history = value

# INTERFACES
class IConfig(ABC):
  @abstractmethod
  def load(self): pass

  @abstractmethod
  def save(self): pass

  @abstractmethod
  def update(self, key, value): pass

  @abstractmethod
  def reset(self): pass

class IDataLoader(ABC):
  @abstractmethod
  def searchCompanyOrSymbol(self, searchText): pass

  @abstractmethod
  def getCompany(self, id): pass

# ABSTRACT CLASS
class WebDataLoader(IDataLoader):
  def __init__(self):
    self.searchURL = None
    self.companyURL = None

  @property
  def searchURL(self): return self._searchURL
  @searchURL.setter
  def searchURL(self, value): self._searchURL = value

  @property
  def companyURL(self): return self._companyURL
  @companyURL.setter
  def companyURL(self, value): self._companyURL = value

  @staticmethod
  def getRequestText(URL):
    return requests.get(URL).text

# ABSTRACT CLASS REALIZATION
class InvestopediaDotComWebDataLoader(WebDataLoader):
  def __init__(self):
    super().__init__()
    self.searchURL = 'https://www.investopedia.com/markets/suggestions?q='
    self.companyURL = 'https://www.investopedia.com/markets/quote?tvwidgetsymbol='

  def searchCompanyOrSymbol(self, searchText):
    suggestions = []
    html = self.getRequestText(self.searchURL + searchText)
    #... parsing process
    return suggestions

  def getCompany(self, symbol):
    company = Company()
    html = self.getRequestText(self.companyURL + searchText)
    #... parsing process
    return company

# WINDOW
class Window (QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__ (self):
		super().__init__()

		self.scenes = {

			'home': self.generateSceneFromForm(Ui_Form_Home),
			'notifications': self.generateSceneFromForm(Ui_Form_Notifications),
			'search': self.generateSceneFromForm(Ui_Form_Search),
			'settings': self.generateSceneFromForm(Ui_Form_Settings)

		}

		self.initialScene = 'home'
		self.currentScene = None

		self.setupUi(self)
		self.connectButtons()

		self.changeSceneTo( self.initialScene )

	@staticmethod
	def generateSceneFromForm( Form ):
		class Scene(QtWidgets.QWidget, Form):
			def __init__(self):
				super().__init__()
				self.setupUi(self)

		return Scene()

	def connectButtons(self):
		self.Home.clicked.connect( lambda: self.changeSceneTo( 'home' ) )
		self.Notifications.clicked.connect( lambda: self.changeSceneTo( 'notifications' ) )
		self.Search.clicked.connect( lambda: self.changeSceneTo( 'search' ) )
		self.Settings.clicked.connect( lambda: self.changeSceneTo( 'settings' ) )
		self.Exit.clicked.connect( lambda: sys.exit() )
		
	def clearScene( self ):
		for i in reversed(range(self.MainMenuLayout.count())): 
			self.MainMenuLayout.itemAt(i).widget().setParent(None)

	def changeSceneTo( self, sceneName ):
		self.clearScene()
		self.MainMenuLayout.addWidget( self.scenes[sceneName] )
		self.currentScene = sceneName

# MAIN
def main():
	app = QtWidgets.QApplication([])
	win = Window()
	win.show()
	sys.exit(app.exec())

if __name__ == '__main__':
	try:
		main()
	except Exception:
		f = open("log.txt", "w")
		f.write (traceback.format_exc())
		f.close()

